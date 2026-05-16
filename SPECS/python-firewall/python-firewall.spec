# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname firewall

Name:           python-%{srcname}
Version:        2.4.1
Release:        %autorelease
Summary:        A firewall daemon with D-Bus interface
License:        GPL-2.0
URL:            https://github.com/firewalld/firewalld
VCS:            git:https://github.com/firewalld/firewalld.git
#!RemoteAsset:  sha256:453230c49b961853144dd7614d59e82fafbcc52c314c39ec66d1316274a33001
Source0:        https://github.com/firewalld/firewalld/releases/download/v%{version}/firewalld-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils

Requires:       python3-dbus
Requires:       python3-gobject

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package contains the Python libraries used by firewalld, including
the firewall Python module for interacting with firewalld.

%install -a

%files
%doc README.md
%license COPYING
%{python3_sitelib}/firewall/

%changelog
%autochangelog
