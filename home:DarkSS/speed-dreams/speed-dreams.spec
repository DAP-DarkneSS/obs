#
# spec file for package speed-dreams
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2008-2012 Jean-Philippe Meuret aka pouillot
# & Bertaux Xavier aka torcs-ng (GPLv2 & GPLv3)
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


Name:           speed-dreams
Version:        2.0.0
Release:        0
Summary:        Speed Dreams: binary files
License:        GPL-2.0+
Group:          Amusements/Games/3D/Race
Url:            http://speed-dreams.org/
Source2:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-base-%{version}-r4687.tar.xz
Source3:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-hq-cars-and-tracks-%{version}-r4687.tar.xz
Source4:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-more-hq-cars-and-tracks-%{version}-r4687.tar.xz
Source5:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-wip-cars-and-tracks-%{version}-r4687.tar.xz
Source6:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-src-unmaintained-%{version}-r4687.tar.xz
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXi6-devel
BuildRequires:  libenet-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  plib-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libXmu-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}

%description
Speed Dreams: binary files.

A fork of the open racing car simulator Torcs,
aiming to implement exciting new features, cars, tracks and
AI opponents to make a more enjoyable game for the player,
as well as constantly improving visual and physics realism.

%package data
Summary:        Speed Dreams: architecture independent data
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
Summary:        Speed Dreams Development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description    devel
Includes files for development robots for Speed Dreams.

%prep
tar -xf %{SOURCE2}
tar -xf %{SOURCE3}
tar -xf %{SOURCE4}
tar -xf %{SOURCE5}
tar -xf %{SOURCE6}
chmod -x *.txt

%build
mkdir -p build
cd build
cmake .. \
       -DOPTION_OFFICIAL_ONLY:BOOL=ON \
       -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=FALSE \
       -DSD_BINDIR:PATH=bin \
       -DCMAKE_INSTALL_PREFIX:PATH=/usr
make %{?_smp_mflags} BINDIR=%{_bindir}

%install
cd build
make DESTDIR=%{buildroot} install
%suse_update_desktop_file -c %{name} "Speed Dreams" "Racing car simulator" "%{name}-2" %{name} "Game;Simulation;"
mkdir -p %{buildroot}%{_datadir}/pixmaps
install ../data/data/icons/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_mandir}/man6
install -m644 ../doc/man/sd2-accc.6 %{buildroot}%{_mandir}/man6/sd2-accc.6
install -m644 ../doc/man/sd2-nfs2ac.6 %{buildroot}%{_mandir}/man6/sd2-nfs2ac.6
install -m644 ../doc/man/sd2-nfsperf.6 %{buildroot}%{_mandir}/man6/sd2-nfsperf.6
install -m644 ../doc/man/sd2-trackgen.6 %{buildroot}%{_mandir}/man6/sd2-trackgen.6
install -m644 ../doc/man/speed-dreams-2.6 %{buildroot}%{_mandir}/man6/speed-dreams-2.6
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt COPYING.txt INSTALL.txt README.txt TODO.txt
%{_mandir}/man6/*
%attr(755,root,root) %{_bindir}/sd2*
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_datadir}/pixmaps/%{name}.png
%dir %{_libdir}/games
%{_libdir}/games/%{name}-2/

%files data
%defattr(-,root,root)
%{_datadir}/games/%{name}-2/

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}-2/

%changelog
