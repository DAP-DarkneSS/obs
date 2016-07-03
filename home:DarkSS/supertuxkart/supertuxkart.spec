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
Version:        0.9.2
Release:        0
Summary:        A 3D kart racing game
License:        GPL-2.0+ and GPL-3.0+ and CC-BY-SA-3.0
Group:          Amusements/Games/3D/Race
Url:            http://supertuxkart.sourceforge.net/
Source:         http://sourceforge.net/projects/supertuxkart/files/SuperTuxKart/%{version}/%{name}-%{version}-src.tar.xz
# Geeko kart add-on (CC-BY 3.0)
Source1:        http://stkaddons.net/dl/14e6ba25b17f0d.zip
Source9:        supertuxkart.6

BuildRequires:  cmake >= 3
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xrandr)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Requires:       %{name}-data = %{version}
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
%setup -q
find -name '*~' -delete -print
find -name '.git*' -delete -print

%build
mkdir build && cd build
# NOTE that %%cmake macro breaks linking.
cmake .. \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_C_FLAGS="%{optflags} -fno-strict-aliasing" \
        -DCMAKE_CXX_FLAGS="%{optflags} -fno-strict-aliasing" \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo
make V=1 %{?_smp_mflags}

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/supertuxkart/data/karts/geeko/
cd %{buildroot}%{_datadir}/supertuxkart/data/karts/geeko/
unzip %{SOURCE1}
# WARNING non-executable-script:
rm %{buildroot}%{_datadir}/supertuxkart/data/run_me.sh
rm %{buildroot}%{_datadir}/supertuxkart/data/po/update_po_authors.py
rm %{buildroot}%{_datadir}/supertuxkart/data/po/pull_from_transifex.sh
rm %{buildroot}%{_datadir}/supertuxkart/data/optimize_data.sh
%fdupes  %{buildroot}%{_datadir}
%suse_update_desktop_file supertuxkart
# Man page:
mkdir -p %{buildroot}%{_mandir}/man6
cp %{SOURCE9} %{buildroot}%{_mandir}/man6

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.md TODO.md CHANGELOG.md
%{_bindir}/supertuxkart
%{_mandir}/man?/%{name}.?.*
%dir %{_datadir}/appdata
%{_datadir}/appdata/supertuxkart.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_*.png
%{_datadir}/icons/hicolor/

%files data
%defattr(-,root,root)
%{_datadir}/supertuxkart/

%changelog
