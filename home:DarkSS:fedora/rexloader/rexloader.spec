#
# spec file for package rexloader
#
# Copyright (c) 2015 rexloader team.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via
# https://github.com/DAP-DarkneSS/rexloader/issues
#

Name:           rexloader
Version:        0.1a.svn
Release:        1
Summary:        An advanced Qt download manager over http

License:        GPL-3.0
Url:            https://github.com/DAP-DarkneSS/rexloader
Group:          Productivity/Networking/Other
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  qt-devel

Requires:       %{name}-hashcalculator
Requires:       %{name}-notifications

%description
An advanced Qt download manager over http with configurable multithreaded
downloading, proxy support, logging, hash calculating and nice notifications.

%package hashcalculator
Summary:        Rexloader Hash Calculator
Requires:       %{name} = %{version}

%description hashcalculator
This package provides a Hash Calculator plugin for Rexloader.

It allows to calculate downloaded files hash sums.

%package nixnotify
Summary:        Rexloader D-Bus Notifications
Requires:       %{name} = %{version}
Provides:       %{name}-notifications

%description nixnotify
This package provides a D-Bus implementation plugin for Rexloader.

It allows to show notifications via implementations supporting FreeDesktop's
notifications standard, like KDE 4.4 (or higher), Gnome, XFCE and others.

%package noticewindow
Summary:        Rexloader Qt Notifications
Requires:       %{name} = %{version}
Provides:       %{name}-notifications

%description noticewindow
This package provides a simple Qt Notifications plugin for Rexloader.

%prep
%setup -q
mkdir build

%build
cd build
qmake-qt4 \
QMAKE_STRIP="" \
PREFIX=%{_prefix} \
../REXLoader.pro \
QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

cd ../plugins/NoticeWindow
qmake-qt4 \
QMAKE_STRIP="" \
NoticeWindow.pro \
QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
cd build
mkdir -p %{buildroot}%{_bindir}
%{__install} ./usr/bin/%{name} %{buildroot}%{_bindir}
cp -R ./usr/share %{buildroot}/usr

mkdir -p %{buildroot}%{_libdir}
cp -R ./usr/lib/%{name} %{buildroot}%{_libdir}

%{__install} ../plugins/NoticeWindow/NoticeWindow %{buildroot}%{_libdir}/%{name}/plugins/libNoticeWindow.so

mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} ../REXLoader/images/RExLoader_64x64.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications/
%{__install} ../REXLoader/%{name}.desktop %{buildroot}%{_datadir}/applications

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locales
%{_datadir}/%{name}/locales/*.qm
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libHttpLoader.so
%attr(755,root,root) %{_bindir}/%{name}

%files hashcalculator
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/libhashcalculator.so

%files nixnotify
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/libNixNotifyPlugin.so

%files noticewindow
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/libNoticeWindow.so

%changelog
