#
# spec file for package kdeneur
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define tarballver 0.18.0+git6

Name:           kdeneur
Version:        0.18.0
Release:        0
Summary:        KDE Front-end for XNeur
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://www.xneur.ru
Source0:        https://launchpad.net/~andrew-crew-kuznetsov/+archive/xneur-stable/+files/kdeneur_%{tarballver}.orig.tar.gz
# PATCH-FIX-OPENSUSE to fix Qt4 binaries names.
Patch0:         kdeneur-qt4-bin.patch

BuildRequires:  hicolor-icon-theme
BuildRequires:  libkde4-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(xnconfig) = %{version}
BuildRequires:  pkgconfig(xneur) = %{version}
Requires:       xneur = %{version}
Provides:       xneur-gui
%{kde4_runtime_requires}

%description
KDE frontend for xneur keyboard layout switcher
kdeneur runs in system tray and shows XNeur's state.
It also allows to configure XNeur via GUI dialog.

%prep
%setup -q
%patch0

%build
%configure
make %{?_smp_mflags}
%suse_update_desktop_file -r %{name} 'Utility;DesktopUtility;Qt;'

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/%{name}/
%{_mandir}/man?/%{name}*

%changelog
