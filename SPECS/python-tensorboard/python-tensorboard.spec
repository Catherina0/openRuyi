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
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
TensorBoard is a suite of web applications for inspecting and understanding
your TensorFlow runs and graphs.

%prep
%autosetup -n %{srcname}-%{version}

perl -pi \
  -e 's/virtualenv -q -p python3 venv/virtualenv -q --system-site-packages -p python3 venv/;' \
  -e 's/^[ \t]*pip\s+install\s+.*/  python -c "import setuptools, wheel"/;' \
  tensorboard/pip_package/build_pip_package.sh

%build
mkdir -p dist
bazel build //tensorboard/pip_package:pip_package
tar -xzf bazel-bin/tensorboard/pip_package/pip_packages.tar.gz -C dist

%install
%py3_install_wheel %{srcname}-%{version}-py3-none-any.whl

%files
%license %{python3_sitelib}/%{srcname}-%{version}.dist-info/licenses/LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
%autochangelog
