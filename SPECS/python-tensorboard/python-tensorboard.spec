# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tensorboard

Name:           python-%{srcname}
Version:        2.20.0
Release:        %autorelease
Summary:        TensorBoard lets you watch Tensors Flow
License:        Apache-2.0
URL:            https://github.com/tensorflow/tensorboard
#!RemoteAsset:  sha256:7a3b3bb111a9734fd051bd34e763ae90b0a76a2549e74ec75ebcba752ba5a21a
Source0:        https://github.com/tensorflow/tensorboard/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  bazel
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Requires:       python3dist(absl-py) >= 0.4
Requires:       python3dist(grpcio) >= 1.48.2
Requires:       python3dist(markdown) >= 2.6.8
Requires:       python3dist(numpy) >= 1.12.0
Requires:       python3dist(packaging)
Requires:       python3dist(pillow)
Requires:       python3dist(protobuf) >= 3.19.6
Requires:       python3dist(setuptools) >= 41.0.0
Requires:       python3dist(tensorboard-data-server) >= 0.7.0
Requires:       python3dist(werkzeug) >= 1.0.1

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
TensorBoard is a suite of web applications for inspecting and understanding
your TensorFlow runs and graphs.

%prep
%autosetup -n %{srcname}-%{version}

%build
bazel build //tensorboard/pip_package:build_pip_package

RUNFILES=bazel-bin/tensorboard/pip_package/build_pip_package.runfiles
rm -rf pip-src
mkdir -p pip-src

cp -LR "${RUNFILES}/org_tensorflow_tensorboard/tensorboard" pip-src/
mv -f pip-src/tensorboard/pip_package/LICENSE pip-src/
mv -f pip-src/tensorboard/pip_package/MANIFEST.in pip-src/
mv -f pip-src/tensorboard/pip_package/README.rst pip-src/
mv -f pip-src/tensorboard/pip_package/requirements.txt pip-src/
mv -f pip-src/tensorboard/pip_package/setup.cfg pip-src/
mv -f pip-src/tensorboard/pip_package/setup.py pip-src/
rm -rf pip-src/tensorboard/pip_package
rm -f pip-src/tensorboard/tensorboard

chmod -x pip-src/LICENSE
find pip-src -name __init__.py -exec chmod -x {} +

mkdir -p pip-src/tensorboard/_vendor
touch pip-src/tensorboard/_vendor/__init__.py
cp -LR "${RUNFILES}/org_mozilla_bleach/bleach" pip-src/tensorboard/_vendor/
cp -LR "${RUNFILES}/org_pythonhosted_webencodings/webencodings" pip-src/tensorboard/_vendor/

chmod -R u+w,go+r pip-src
find pip-src/tensorboard -name '*.py' -exec perl -pi -e '
    s/^import bleach$/from tensorboard._vendor import bleach/;
    s/^from bleach/from tensorboard._vendor.bleach/;
    s/^import webencodings$/from tensorboard._vendor import webencodings/;
    s/^from webencodings/from tensorboard._vendor.webencodings/;
  ' {} +

pushd pip-src
%{python3} -m pip wheel --no-build-isolation --no-deps -w dist .
popd

%install
pushd pip-src
%{python3} -m pip install --no-build-isolation --no-deps \
    --root %{buildroot} --prefix %{_prefix} \
    dist/*.whl
popd

%files
%license pip-src/LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
%autochangelog
