#
# spec file for package stuntrally
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


Name:           stuntrally
Version:        2.6
Release:        0
Summary:        Rally game with stunt elements
License:        GPL-3.0
Group:          Amusements/Games/Action/Race
Url:            http://code.google.com/p/vdrift-ogre/
Source0:        https://github.com/stuntrally/stuntrally/archive/%{version}.tar.gz#/stuntrally-%{version}.tar.gz
Source1:        https://github.com/stuntrally/tracks/archive/%{version}.tar.gz#/tracks-%{version}.tar.gz
Source8:        sr-editor.1
Source9:        stuntrally.1
Patch0:         strcmp.diff

BuildRequires:  boost-devel >= 1.54
BuildRequires:  cmake >= 3
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(MYGUI)
BuildRequires:  pkgconfig(OGRE)
BuildRequires:  pkgconfig(OGRE-Overlay)
BuildRequires:  pkgconfig(OGRE-Paging)
BuildRequires:  pkgconfig(OGRE-Property)
BuildRequires:  pkgconfig(OGRE-RTShaderSystem)
BuildRequires:  pkgconfig(OGRE-Terrain)
BuildRequires:  pkgconfig(OIS)
BuildRequires:  pkgconfig(bullet) >= 2.83
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
Requires:       %{name}-data = %{version}
Requires:       %( echo libOgreMain$(pkg-config --modversion OGRE)-plugin-Cg | sed 's/\./_/g' )

%description
Stunt Rally is a car simulation using VDrift and libbullet.
Rendering is achieved by OGRE. Trees/grass by PagedGeometry,
user interface by MyGUI, materials are managed by shiny.
The Road is based on a 3D spline and is fully customizable
in editor the track editor.

The game focuses on closed rally tracks with possible stunt
elements (jumps, loops, pipes).

%package data
Summary:        Data files for Stunt Rally
Group:          Amusements/Games/Action/Race
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Architecture independent data files for Stunt Rally.

%package devel
Summary:        Development files for Stunt Rally
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
This package contain all that is needed to developer or compile
appliancation with the Stunt Rally.

%prep
%setup -q -a1
%patch0
mv tracks-%{version} data/tracks

%build
mkdir build
cd build
# WARNING: %%cmake breaks game linking (undefined reference to boost).
cmake -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
      -DCMAKE_C_FLAGS="%{optflags} -std=gnu++98 -fno-strict-aliasing -Wno-narrowing" \
      -DCMAKE_CXX_FLAGS="%{optflags} -std=gnu++98 -fno-strict-aliasing -Wno-narrowing" \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DSHARE_INSTALL=share/stuntrally \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      ..
# WARNING: don't use parallel build because of compiling fatal errors.
make V=1

%install
%cmake_install
%fdupes %{buildroot}/%{_datadir}/stuntrally
rm %{buildroot}/%{_prefix}/lib/OGRE/libshiny.OgrePlatform.a
rm %{buildroot}/%{_prefix}/lib/libshiny.a

mkdir -p %{buildroot}%{_mandir}/man1
cd %{_sourcedir}
for MANPAGE in *.1; do
gzip -c9 $MANPAGE | tee -a %{buildroot}%{_mandir}/man1/$MANPAGE.gz
done

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root,-)
%{_bindir}/sr-editor
%{_bindir}/stuntrally
%{_mandir}/man1/s*.1.gz
%{_datadir}/applications/sr-editor.desktop
%{_datadir}/applications/stuntrally.desktop
%{_datadir}/icons/hicolor/*/apps/
%dir %{_datadir}/stuntrally/
%{_datadir}/stuntrally/config/

%files data
%defattr(-,root,root,-)
%{_datadir}/stuntrally/
%exclude %{_datadir}/stuntrally/config/

%files devel
%defattr(-,root,root,-)
%{_includedir}/shiny

%changelog
