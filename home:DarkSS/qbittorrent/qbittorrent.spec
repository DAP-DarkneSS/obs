#
# spec file for package qbittorrent
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Mariusz Fik <fisiu@opensuse.org>.
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


Name:           qbittorrent
Version:        3.0.6
Release:        1
Summary:        A Bittorrent Client built with C++ / Qt4
License:        GPL-2.0+
Group:          Productivity/Networking/File-Sharing
Url:            http://sourceforge.net/projects/qbittorrent
Source:         http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  boost-devel >= 1.35
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(QtCore) >= 4.6
BuildRequires:  pkgconfig(QtDBus) >= 4.6
BuildRequires:  pkgconfig(QtGui) >= 4.6
BuildRequires:  pkgconfig(QtNetwork) >= 4.6
BuildRequires:  pkgconfig(QtXml) >= 4.6
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 0.14.4
Requires:       GeoIP
Requires:       python
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A Bittorrent client using C++ / libtorrent and a Qt4 Graphical User Interface.
It aims to be as fast as possible and to provide multi-OS, unicode support.

%package nox

Summary:        A Bittorrent Client built with C++, console version
Group:          Productivity/Networking/File-Sharing

%description nox
A Bittorrent client using C++ / libtorrent, console version.
It aims to be as fast as possible and to provide multi-OS, unicode support.

%prep
%setup -q
# apply patches
# none atm

%build
echo -e "\n# openSUSE way optflags\nQMAKE_CFLAGS += %{optflags}\nQMAKE_CXXFLAGS += %{optflags}" >> unixconf.pri
# build nox first
mkdir nox && cd nox
../configure --prefix=%{_prefix} --disable-gui
cp conf.pri ../
make %{?_smp_mflags}
cd ../

# build gui version
mkdir gui && cd gui
../configure --prefix=%{_prefix}
cp conf.pri ../
make %{?_smp_mflags}

%install
# install nox version
cd nox && cp conf.pri ../ && cp conf.log ../ && cp Makefile ../ && sed -i '/STRIP/d' src/Makefile
make INSTALL_ROOT=%{buildroot} install
cd ../

#install gui version
cd gui && cp conf.pri ../ && cp conf.log ../ && cp Makefile ../ && sed -i '/STRIP/d' src/Makefile
make INSTALL_ROOT=%{buildroot} install

# update .desktop file
%suse_update_desktop_file -r qBittorrent Network P2P

# duplicate files warning resolving
%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%doc AUTHORS Changelog COPYING NEWS README TODO
%doc %{_mandir}/man1/qbittorrent.1.gz
%{_bindir}/qbittorrent
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/qBittorrent.desktop
%{_datadir}/pixmaps/qbittorrent.png

%files nox
%defattr(-,root,root)
%doc AUTHORS Changelog COPYING NEWS README TODO
%doc %{_mandir}/man1/qbittorrent-nox.1.gz
%{_bindir}/qbittorrent-nox

%changelog
