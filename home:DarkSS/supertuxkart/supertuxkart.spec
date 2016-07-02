#
# spec file for package supertuxkart
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


Name:           supertuxkart
Version:        0.9.2~rc1
Release:        0
Summary:        A 3D kart racing game
License:        GPL-2.0+ and GPL-3.0+ and CC-BY-SA-3.0
Group:          Amusements/Games/3D/Race
Url:            http://supertuxkart.sourceforge.net/
Source:         http://sourceforge.net/projects/supertuxkart/files/SuperTuxKart/0.9.2/%{name}-0.9.2-rc1-src.tar.xz
# Geeko kart add-on (CC-BY 3.0)
Source1:        http://stkaddons.net/dl/14e6ba25b17f0d.zip
BuildRequires:  bluez-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  glu-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libXrandr-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
%if 0%{?suse_version} <= 1220
BuildRequires:  libopenal1
%endif
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
Requires:       %{name}-data = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64

%description
SuperTuxKart is a Free 3d kart racing game.

The focus of the game is more to be fun than it is to be realistic.
You can play with up to 4 friends on one PC, racing against each other or just try to beat the computer.

See the great lighthouse or drive through the sand and visit the pyramids. Race underground or in space,
watching the stars passing by. Have some rest under the palms on the beach (watching the other karts
overtaking you :) ). But don't eat the bananas! Watch for bowling balls, plungers, bubble gum and cakes thrown by opponents.

You can do a single race against other karts, compete in one of several Grand Prix, try to beat the high score in time trials
on your own, play battle mode against your friends, and more!

%package data
Summary:        Data files for SuperTuxKart
Group:          Amusements/Games/3D/Race
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Data files for SuperTuxKart a Free 3d kart racing game.

%prep
%setup -q -n %{name}-0.9.2-rc1
find -name '*~' -delete -print

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
   mkdir cmake_build
   cd cmake_build
   cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}

%install
cd cmake_build
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_datadir}/supertuxkart/data/karts/geeko/
cd %{buildroot}%{_datadir}/supertuxkart/data/karts/geeko/
unzip %{SOURCE1}
%fdupes  %{buildroot}%{_datadir}
%suse_update_desktop_file supertuxkart

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.md TODO.md CHANGELOG.md
%{_bindir}/supertuxkart
%dir %{_datadir}/appdata
%{_datadir}/appdata/supertuxkart.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_*.png
%{_datadir}/icons/hicolor/

%files data
%defattr(-,root,root)
%{_datadir}/supertuxkart/

%changelog
