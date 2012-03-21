#
# spec file for package rexloader
#
# Copyright (c) 2011-2012 Sarvaritdinov Ravil (source), (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via http://code.google.com/p/rexloader/issues/list
#

Name:           rexloader
Version:        0.1a.rev
Release:        0
Summary:        An advanced Qt download manager over http

Group:          Productivity/Networking/Other
License:        GPL-3.0
URL:            http://code.google.com/p/rexloader/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  qt4-devel
BuildRequires:  zlib-devel

%description
An advanced Qt download manager over http with configurable multithreaded downloading.

%prep
%setup -q

%build
cd Httploader
qmake HttpLoader.pro
make
cd ../NoticeWindow
qmake NoticeWindow.pro
make
cd ../REXLoader
qmake REXLoader.pro
make

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} ./usr/bin/REXLoader %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}/plugins
%{__install} ./usr/lib/%{name}/plugins/* %{buildroot}%{_libdir}/%{name}/plugins
%{__install} ./NoticeWindow/NoticeWindow %{buildroot}%{_libdir}/%{name}/plugins/libNoticeWindow.so
mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} ./REXLoader/images/RExLoader_64x64.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications/
touch %{buildroot}%{_datadir}/applications/%{name}.desktop
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=REXLoader
Comment=Download manager
Comment[ru]=Менеджер закачек
Exec=%{name}
Icon=%{name}.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Network;FileTransfer;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}
%{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Wed Mar 21 2012 DA <dap.darkness@gmail.com> - 20120321-1
- Revision #214 with bug fixes and enhancements.
- Mandriva build doesn't require lz linking patch.

* Fri Mar 09 2012 DA <dap.darkness@gmail.com> - 20120309-1
- Revision #213 with optimization and bug fixes.

* Sat Mar 03 2012 DA <dap.darkness@gmail.com> - 20120303-2
- Revision #212 with bug fixes.

* Sat Mar 03 2012 DA <dap.darkness@gmail.com> - 20120303-1
- Revision #211 with enhancements.

* Tue Feb 28 2012 DA <dap.darkness@gmail.com> - 20120218-3
- Revision #210 with bug fixes.

* Tue Feb 28 2012 DA <dap.darkness@gmail.com> - 20120218-2
- Revision #209 with critical bug fixes.

* Tue Feb 28 2012 DA <dap.darkness@gmail.com> - 20120218-1
- Revision #208 with optimization and bug fixes.

* Sat Feb 18 2012 DA <dap.darkness@gmail.com> - 20120218-2
- Revision #207 with optimization.

* Sat Feb 18 2012 DA <dap.darkness@gmail.com> - 20120218-1
- Revision #206 with enhancements and bug fixes.

* Fri Feb 17 2012 DA <dap.darkness@gmail.com> - 20120217-1
- Revision #205 with patches for SUSE x64.

* Sun Feb 12 2012 DA <dap.darkness@gmail.com> - 20120212-3
- Revision #204 with enhancement of downloads management.

* Sun Feb 12 2012 DA <dap.darkness@gmail.com> - 20120212-2
- Revision #203 with enhancement of visual features.

* Sun Feb 12 2012 DA <dap.darkness@gmail.com> - 20120212-1
- Revision #202 with enhancement of visual style.

* Fri Jan 13 2012 DA <dap.darkness@gmail.com> - 20120113-1
- Revision #201 with proxy support.

* Wed Jan 11 2012 DA <dap.darkness@gmail.com> - 20120111-1
- Revision #200 with some fixes and improvements.

* Sat Jan 07 2012 DA <dap.darkness@gmail.com> - 20120107-1
- Revision #199 with http and notice plugins.
