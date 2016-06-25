#
# spec file for package stuntrally
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           stuntrally
Version:        2.4
Release:        0
Summary:        Rally game with stunt elements
License:        GPL-3.0
Group:          Amusements/Games/Action/Race
Url:            http://code.google.com/p/vdrift-ogre/
Source0:        stuntrally-%{version}.tar.xz
Source1:        tracks-%{version}.tar.xz
Patch0:         strcmp.diff
# PATCH-FIX-OPENSUSE marguerite@opensuse.org - because our boost 1.49 contains a fix that coming in 1.50+
# so upstream fix the same thing...(rename Boost::TIME_UTC to Boost::TIME_UTC_)
Patch1:         stuntrally-2.0-boost-fix.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  xz
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(MYGUI)
BuildRequires:  pkgconfig(OGRE)
BuildRequires:  pkgconfig(OGRE-Overlay)
BuildRequires:  pkgconfig(OGRE-Paging)
BuildRequires:  pkgconfig(OGRE-Property)
BuildRequires:  pkgconfig(OGRE-RTShaderSystem)
BuildRequires:  pkgconfig(OGRE-Terrain)
BuildRequires:  pkgconfig(OIS)
BuildRequires:  pkgconfig(libenet)
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
Data files for Stunt Rally.

%prep
%setup -q -a1
%patch0
mv tracks-%{version} data/tracks
%if 0%{?suse_version} == 1230
%patch1 -p1
%endif

%build
mkdir build
cd build
export CFLAGS='%{optflags} -fno-strict-aliasing'
export CXXFLAGS='%{optflags} -fno-strict-aliasing'
cmake -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DSHARE_INSTALL=share/stuntrally \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      ..
#no parallel build to avoid out of memory exception
make

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%fdupes %{buildroot}%{_datadir}

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
%{_datadir}/applications/sr-editor.desktop
%{_datadir}/applications/stuntrally.desktop
%{_datadir}/icons/hicolor/*/apps/
%dir %{_datadir}/stuntrally/
%{_datadir}/stuntrally/config/

%files data
%defattr(-,root,root,-)
%{_datadir}/stuntrally/
%exclude %{_datadir}/stuntrally/config/

%changelog
