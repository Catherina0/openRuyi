# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langchain

Name:           python-%{srcname}
Version:        1.3.15
Release:        %autorelease
Summary:        Building applications with LLMs through composability
License:        MIT
URL:            https://github.com/langchain-ai/langchain
VCS:            git:https://github.com/langchain-ai/langchain.git
#!RemoteAsset:  sha256:ab4b775b9703f7e37babe0b325dbbaef25573bda60ecf79f7850bc875f252795
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(langchain-core)
BuildRequires:  python3dist(langgraph)
BuildRequires:  python3dist(pydantic)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
LangChain is a framework for building composable applications with LLMs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
