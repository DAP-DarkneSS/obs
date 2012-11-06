#
# spec file for package rexloader
#
# Copyright (c) 2011-2012 Sarvaritdinov Ravil (source),
# (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via http://code.google.com/p/rexloader/issues/list
#

Name:           rexloader
Version:        0.1a.rev
Release:        1
Summary:        An advanced Qt download manager over http

Group:          Productivity/Networking/Other
License:        GPL-3.0
URL:            http://code.google.com/p/rexloader/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files

%description
An advanced Qt download manager over http with configurable multithreaded
downloading, proxy support, logging and nice notifications.

%prep
%setup -q

%build
cd Httploader
qmake HttpLoader.pro QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}
cd ../NoticeWindow
qmake NoticeWindow.pro QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}
cd ../REXLoader
qmake REXLoader.pro QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} ./usr/bin/REXLoader %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}/plugins
%{__install} ./usr/lib/%{name}/plugins/* %{buildroot}%{_libdir}/%{name}/plugins
%{__install} ./NoticeWindow/NoticeWindow %{buildroot}%{_libdir}/%{name}/plugins/libNoticeWindow.so
mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} ./REXLoader/images/RExLoader_64x64.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications/
%{__install} ./REXLoader/%{name}.desktop %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/%{name}/locales
%{__install} ./usr/share/%{name}/locales/* %{buildroot}%{_datadir}/%{name}/locales
%suse_update_desktop_file %{name}

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
%{_libdir}/%{name}/plugins/*.so
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Wed Nov 06 2012 DA <dap.darkness@gmail.com> - 20121106-1
- Revision 252 with url import from files.

* Thu Oct 07 2012 DA <dap.darkness@gmail.com> - 20121007-1
- Revision #249 with rpm optflags, locales and actions after downloading.

* Thu Jun 07 2012 DA <dap.darkness@gmail.com> - 20120607-1
- Revision #234 with desktop file.

* Sun Jun 03 2012 DA <dap.darkness@gmail.com> - 20120603-1
- Revision #233 with logging.

* Wed Mar 21 2012 DA <dap.darkness@gmail.com> - 20120321-1
- Revision #214 with Mandriva patch.

* Fri Feb 17 2012 DA <dap.darkness@gmail.com> - 20120217-1
- Revision #205 with patches for rpm and x64.

* Fri Jan 13 2012 DA <dap.darkness@gmail.com> - 20120113-1
- Revision #201 with proxy support.

* Sat Jan 07 2012 DA <dap.darkness@gmail.com> - 20120107-1
- Revision #199 with http and notice plugins.
