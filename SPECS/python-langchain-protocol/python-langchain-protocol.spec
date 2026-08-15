# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langchain-protocol
%global pypi_name langchain_protocol

Name:           python-%{srcname}
Version:        0.0.18
Release:        %autorelease
Summary:        Python bindings for the LangChain agent streaming protocol
License:        MIT
URL:            https://github.com/langchain-ai/agent-protocol
VCS:            git:https://github.com/langchain-ai/agent-protocol.git
#!RemoteAsset:  sha256:ec3e11782f1ed0c9db38e5a9ed01b0e7a0d3fba406faa8aef6594b73c56a63e6
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
langchain-protocol provides generated Python typing primitives for the
LangChain agent streaming protocol.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
