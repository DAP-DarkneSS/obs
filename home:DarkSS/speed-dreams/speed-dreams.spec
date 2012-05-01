#
# spec file for package speed-dreams
#
# Copyright (c) 2008-2012 Jean-Philippe Meuret aka pouillot
# & Bertaux Xavier aka torcs-ng (GPLv2 & GPLv3)
#
# Please submit bugfixes or comments via 
# http://sourceforge.net/apps/trac/speed-dreams/report
#

Summary:        Speed Dreams: binary files
Name:           speed-dreams
Version:        2.0.0
Release:        1
Source2:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-base-%{version}-r4687.tar.xz
Source3:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-hq-cars-and-tracks-%{version}-r4687.tar.xz
Source4:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-more-hq-cars-and-tracks-%{version}-r4687.tar.xz
Source5:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-wip-cars-and-tracks-%{version}-r4687.tar.xz
Source6:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-unmaintained-%{version}-r4687.tar.xz
URL:            http://speed-dreams.org/
Group:          Amusements/Games/3D/Race
License:        GPL-2.0+
Patch1:         bin.patch

BuildRequires:  update-desktop-files xz fdupes
BuildRequires:  gcc gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  freealut-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(openal)
BuildRequires:  libpng14-compat-devel
BuildRequires:  libenet-devel
BuildRequires:  Mesa-devel
BuildRequires:  plib-devel 
BuildRequires:  freeglut-devel
BuildRequires:  libXi6-devel
BuildRequires:  xorg-x11-libXmu-devel
BuildRequires:  libjpeg8-devel
Requires:       libSDL >= 1.2.13
Requires:       %{name}-data = %{version}

%description
Speed Dreams: binary files.

A fork of the open racing car simulator Torcs, 
aiming to implement exciting new features, cars, tracks and 
AI opponents to make a more enjoyable game for the player, 
as well as constantly improving visual and physics realism.

%package data
Summary:        Speed Dreams: architecture independent data
License:        GPL-2.0+
Group:          Amusements/Games/3D/Race
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Speed Dreams: architecture independent data.

A fork of the open racing car simulator Torcs, 
aiming to implement exciting new features, cars, tracks and 
AI opponents to make a more enjoyable game for the player, 
as well as constantly improving visual and physics realism.

%package        devel
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Summary:        Speed Dreams Development files

%description    devel
Includes files for development robots for Speed Dreams.

%prep 
tar -xf %{SOURCE2} -C ./
tar -xf %{SOURCE3} -C ./
tar -xf %{SOURCE4} -C ./
tar -xf %{SOURCE5} -C ./
tar -xf %{SOURCE6} -C ./
%patch1

%build
mkdir -p build
cd build
cmake -DOPTION_OFFICIAL_ONLY:BOOL=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
make

%install
cd build
make install DESTDIR=%{buildroot}

%suse_update_desktop_file -c %{name} "Speed Dreams" "Racing car simulator" "%{name}-2" %{name} "Game;ArcadeGame;"

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
%{__install} ../data/data/icons/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

mkdir -p %{buildroot}%{_mandir}/man6
install -m644 ../doc/man/sd2-accc.6 %{buildroot}%{_mandir}/man6/sd2-accc.6
install -m644 ../doc/man/sd2-nfs2ac.6 %{buildroot}%{_mandir}/man6/sd2-nfs2ac.6
install -m644 ../doc/man/sd2-nfsperf.6 %{buildroot}%{_mandir}/man6/sd2-nfsperf.6
install -m644 ../doc/man/sd2-trackgen.6 %{buildroot}%{_mandir}/man6/sd2-trackgen.6
install -m644 ../doc/man/speed-dreams-2.6 %{buildroot}%{_mandir}/man6/speed-dreams-2.6

%fdupes -s %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt COPYING.txt INSTALL.txt README.txt TODO.txt
%{_mandir}/man6/*
%attr(755,root,root) %{_bindir}/sd2*
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%attr(644,root,root) %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_libdir}/games
%dir %{_libdir}/games/%{name}-2
%{_libdir}/games/%{name}-2/*

%files data
%defattr(-,root,root)
%dir %{_datadir}/games/%{name}-2
%{_datadir}/games/%{name}-2/*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}-2
%{_includedir}/%{name}-2/*

%changelog
