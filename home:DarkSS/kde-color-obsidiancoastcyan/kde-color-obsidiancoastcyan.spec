#
# spec file for package kde-color-obsidiancoastcyan
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           kde-color-obsidiancoastcyan
Version:        0
Release:        1
Summary:        KDE colour theme — Obsidian Coast Cyan

License:        GPL-2.0+
Url:            http://dap-darkness.livejournal.com/tag/kde
Group:          System/GUI/KDE
Source0:        obsidiancoastcyan.colors

BuildRequires:  kde4-filesystem
Requires:       kdebase4-workspace
BuildArch:      noarch

%description
This package contains a colour theme for KDE4 Obsidian Coast Cyan.

%prep

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/color-schemes/
%{__install} %{SOURCE0} %{buildroot}%{_kde4_appsdir}/color-schemes/

%files
%defattr(-,root,root)
%attr(644,root,root) %{_kde4_appsdir}/color-schemes/obsidiancoastcyan.colors

%changelog
