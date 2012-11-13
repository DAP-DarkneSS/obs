#
# spec file for package kdeneur
#
# Copyright (c) 2012, Sergei Chistyakov <brestows@gmail.com> (source),
# (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via http://forum.ubuntu.ru/index.php?topic=165332
#

Name:           kdeneur
Version:        0.16.0
Release:        1
Summary:        KDE Front-end for XNeur

License:        GPL-2.0+
Group:          System/X11/Utilities
URL:            http://forum.ubuntu.ru/index.php?topic=165332
Source0:        %{name}-%{version}.tar.gz
Patch1:         unistd_h_include.patch

BuildRequires:  libkde4-devel
BuildRequires:  libxneur-devel
BuildRequires:  update-desktop-files
Requires:       xneur >= %{version}
%kde4_runtime_requires

%description
KDE frontend for xneur keyboard layout switcher
kdeneur runs in system tray and shows XNeur's state.
It also allows to configure XNeur via GUI dialog.

%prep
%setup -q -n src
%patch1

%build
qmake QMAKE_CXXFLAGS+="%{optflags}" PREFIX=/usr
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
%suse_update_desktop_file -r %{name} 'Utility;DesktopUtility;Qt;'

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/%{name}*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/??.png

%changelog
