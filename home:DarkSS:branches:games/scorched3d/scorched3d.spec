#
# spec file for package scorched3d
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           scorched3d
Version:        43.3d
Release:        0
Summary:        Game based loosely on the classic DOS game Scorched Earth
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://www.scorched3d.co.uk/
# this is
# http://downloads.sourceforge.net/%{name}/Scorched3D-%{version}-src.tar.gz
# with the included glew removed as that contains files under the non free
# SGI Free license B. Instead the system version is used, which has the
# troublesome glew parts replaced
Source0:        Scorched3D-%{version}-src.tar.gz
Source1:        %{name}.desktop
Source2:        openal-config
# PATCH-FIX-OPENSUSE patch to use system libglew
Patch0:         %{name}-systemglew.patch
# PATCH-FIX-UPSTREAM scorched3d-gcc47.patch
Patch1:         %{name}-gcc47.patch
# PATCH-FIX-UPSTREAM scorched3d-libpng15.patch
Patch2:         %{name}-libpng15.patch
BuildRequires:  SDL_net-devel
BuildRequires:  fftw3-devel
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1140
BuildRequires:  wxWidgets-devel
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
%else
BuildRequires:  wxGTK-devel
%endif
%if 0%{?suse_version} > 0
BuildRequires:  libexpat-devel
%else
BuildRequires:  expat-devel
%endif
BuildRequires:  fastjar
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
%if 0%{?suse_version} > 0
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  automake
Requires:       opengl-games-utils
# Upstream naming compatibility
Provides:       Scorched3D = %{version}

%description
Scorched 3D is a game based on the classic DOS game Scorched Earth
"The Mother Of All Games".  Scorched 3D adds amongst other new
features a 3D island environment and LAN and internet play.  At its
lowest level, Scorched 3D is just an artillery game with two+ tanks
taking turns to destroy opponents in an arena.  Choose the angle,
direction and power of each shot, launch your weapon, and try to blow
up other tanks.  But Scorched 3D can be a lot more complex than that,
if you want it to be.  You can earn money from successful battles and
use it to invest in additional weapons and accessories.  You can play
with up to twenty four other players at a time, mixing computer
players with humans.  There's a variety of changing environmental
conditions and terrains to be dealt with.

%prep
%setup -q -n scorched
%patch0
%patch1 -p1
%patch2 -p1
sed -i 's/\r$//' COPYING README CHANGELOG
chmod +x %{SOURCE2}

%build
export OPENAL_CONFIG=%{SOURCE2}
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CPPFLAGS="$CFLAGS"
export CXXFLAGS="$CFLAGS"
aclocal
%configure --disable-dependency-tracking --datadir=%{_datadir}/%{name} \
  --with-docdir=%{_docdir}/%{name}-%{version}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
ln -s opengl-game-wrapper.sh "%{buildroot}%{_bindir}/%{name}-wrapper"
rm -r "%{buildroot}%{_docdir}/%{name}-%{version}"
%if 0%{?suse_version} > 0
# below is the desktop file and icon stuff.
%suse_update_desktop_file -i %{name} Game ArcadeGame
%endif
install -D -m 644 data/images/tank2.png "%{buildroot}%{_datadir}/pixmaps/%{name}.png"
%if 0%{?suse_version} > 0
%fdupes %{buildroot}
%endif

%files
%defattr(-,root,root,-)
%doc COPYING README CHANGELOG
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
