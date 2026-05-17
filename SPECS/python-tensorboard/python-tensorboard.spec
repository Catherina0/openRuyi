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
# PyPI does not publish an sdist for 2.20.0, so use the upstream wheel.
#!RemoteAsset:  sha256:9dc9f978cb84c0723acf9a345d96c184f0293d18f166bb8d59ee098e6cfaaba6
Source0:        https://files.pythonhosted.org/packages/9c/d9/a5db55f88f258ac669a92858b70a714bbbd5acd993820b41ec4a96a4d77f/%{srcname}-%{version}-py3-none-any.whl
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
TensorBoard is a suite of web applications for inspecting and understanding
your TensorFlow runs and graphs.

%prep

%build
mkdir -p dist
cp %{SOURCE0} dist/

%install
%py3_install_wheel %{srcname}-%{version}-py3-none-any.whl

%files
%license %{python3_sitelib}/%{srcname}-%{version}.dist-info/licenses/LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
%autochangelog
