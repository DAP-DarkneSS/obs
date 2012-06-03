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
Source1:        %{name}.desktop

BuildRequires:  qt4-devel zlib-devel
BuildConflicts: libpulseaudio0 lib64pulseaudio0 libalsa-plugins-pulseaudio lib64alsa-plugins-pulseaudio

%description
An advanced Qt download manager over http with configurable multithreaded
downloading and nice notifications.

%prep
%setup -q

%build
cd Httploader
qmake HttpLoader.pro
make %{?_smp_mflags}
cd ../NoticeWindow
qmake NoticeWindow.pro
make %{?_smp_mflags}
cd ../REXLoader
qmake REXLoader.pro
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
%{__install} %{SOURCE1} %{buildroot}%{_datadir}/applications

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pixmaps/%{name}.png
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*.so
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Sun Jun 03 2012 DA <dap.darkness@gmail.com> - 20120603-1
- Revision #233.

* Sun May 27 2012 DA <dap.darkness@gmail.com> - 20120527-1
- Revision #232.

* Sat May 26 2012 DA <dap.darkness@gmail.com> - 20120526-1
- Revision #230.

* Fri May 25 2012 DA <dap.darkness@gmail.com> - 20120525-1
- Revision #227.

* Sun May 20 2012 DA <dap.darkness@gmail.com> - 20120520-1
- Revision #225.

* Sat May 19 2012 DA <dap.darkness@gmail.com> - 20120519-1
- Revision #224.

* Fri May 18 2012 DA <dap.darkness@gmail.com> - 20120518-1
- Revision #223.

* Sat May 12 2012 DA <dap.darkness@gmail.com> - 20120512-1
- Revision #222.

* Wed May 09 2012 DA <dap.darkness@gmail.com> - 20120509-1
- Revision #221.

* Sun Apr 29 2012 DA <dap.darkness@gmail.com> - 20120429-1
- Revision #220.

* Sat Apr 28 2012 DA <dap.darkness@gmail.com> - 20120428-1
- Revision #219.

* Wed Mar 21 2012 DA <dap.darkness@gmail.com> - 20120321-1
- Revision #214 with with Mandriva patch.

* Fri Feb 17 2012 DA <dap.darkness@gmail.com> - 20120217-1
- Revision #205 with patches for rpm and x64.

* Fri Jan 13 2012 DA <dap.darkness@gmail.com> - 20120113-1
- Revision #201 with proxy support.

* Sat Jan 07 2012 DA <dap.darkness@gmail.com> - 20120107-1
- Revision #199 with http and notice plugins.
