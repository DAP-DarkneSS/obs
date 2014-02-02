#
# spec file for package rexloader
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
# http://code.google.com/p/rexloader/issues/list
#


Name:           rexloader
Version:        0.1a.svn
Release:        0
Summary:        An advanced Qt download manager over http or ftp
License:        GPL-3.0
Group:          Productivity/Networking/Other
Url:            http://code.google.com/p/rexloader/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         ftploader-enable.diff

BuildRequires:  libQtWebKit-devel
BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files
Requires:       %{name}-loader
Requires:       libqt4-sql-sqlite
Recommends:     %{name}-ftploader
Recommends:     %{name}-hashcalculator
Recommends:     %{name}-httploader
Recommends:     %{name}-notifications
Suggests:       %{name}-httploader
Suggests:       %{name}-nixnotify

%description
An advanced Qt download manager over http or ftp with configurable multi-threaded
downloading, proxy support, logging, hash calculating and nice notifications.


%package ftploader
Summary:        Rexloader Ftp Support
Group:          Productivity/Networking/Ftp/Clients
Provides:       %{name}-loader
Requires:       %{name} = %{version}

%description ftploader
This package provides a Ftp Loader plugin for Rexloader.

It allows to download files over ftp protocol.


%package httploader
Summary:        Rexloader Http Support
Group:          Productivity/Networking/Other
Provides:       %{name}-loader
Requires:       %{name} = %{version}

%description httploader
This package provides a Http Loader plugin for Rexloader.

It allows to download files over http protocol.


%package hashcalculator
Summary:        Rexloader Hash Calculator
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description hashcalculator
This package provides a Hash Calculator plugin for Rexloader.

It allows to calculate downloaded files hash sums.


%package nixnotify
Summary:        Rexloader D-Bus Notifications
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-notifications

%description nixnotify
This package provides a D-Bus implementation plugin for Rexloader.

It allows to show notifications via implementations supporting FreeDesktop's
notifications standard, like KDE 4.4 (or higher), Gnome, XFCE and others.


%package noticewindow
Summary:        Rexloader Qt Notifications
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-notifications

%description noticewindow
This package provides a simple Qt Notifications plugin for Rexloader.


%prep
%setup -q
%patch0
mkdir build


%build
cd build

qmake \
QMAKE_STRIP="" \
PREFIX=%{_prefix} \
../REXLoader.pro \
QMAKE_CXXFLAGS+="%{optflags}"

make %{?_smp_mflags}

cd ../plugins/NoticeWindow

qmake \
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

%if 0%{?suse_version} >= 1140
   %suse_update_desktop_file -i %{name}
%else
   mkdir -p %{buildroot}%{_datadir}/applications/
   %{__install} ../REXLoader/%{name}.desktop %{buildroot}%{_datadir}/applications
%endif


%files
%defattr(-,root,root)
%doc COPYING
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locales
%{_datadir}/%{name}/locales/*.qm
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%attr(755,root,root) %{_bindir}/%{name}


%files ftploader
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libFtpLoader.so


%files httploader
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libHttpLoader.so


%files hashcalculator
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libhashcalculator.so


%files nixnotify
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libNixNotifyPlugin.so


%files noticewindow
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libNoticeWindow.so

%changelog
