#
# spec file for package monster-rpg-2
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


%define pack_desc Monster RPG 2 is a fantasy quest that spans \
continents and worlds and lets you take a simple villager and \
develop her into a hero with the power to save her world. The \
next instalment in the classic Monster RPG series, Monster RPG 2 \
is a turn-based role-playing game with enough variety, plot \
twists, secrets, and scenery to keep even the old school players \
coming back for more. If you loved the 16 bit classics on old \
console systems, you'll love this game. If you've never heard of \
those games, you're in for a real treat! 

Name:           monster-rpg-2
Version:        2.1
Release:        0
Summary:        An Old School Japanese Style RPG
License:        GiYOL
Group:          Amusements/Games/RPG
# http://www.nooskewl.com/content/official-license-post
Url:            http://www.monster-rpg.com/
Source0:        http://www.monster-rpg.com/stuff/downloads/monster-rpg-2-src-20130605-2.tar.bz2

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libphysfs-devel
BuildRequires:  sed
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(allegro_acodec-5)     >= 5.1
BuildRequires:  pkgconfig(allegro_audio-5)      >= 5.1
BuildRequires:  pkgconfig(allegro_color-5)      >= 5.1
BuildRequires:  pkgconfig(allegro_dialog-5)     >= 5.1
BuildRequires:  pkgconfig(allegro_font-5)       >= 5.1
BuildRequires:  pkgconfig(allegro_image-5)      >= 5.1
BuildRequires:  pkgconfig(allegro_memfile-5)    >= 5.1
BuildRequires:  pkgconfig(allegro_physfs-5)     >= 5.1
BuildRequires:  pkgconfig(allegro_primitives-5) >= 5.1
BuildRequires:  pkgconfig(allegro_ttf-5)        >= 5.1
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}

%description
%{pack_desc}

%package data
Summary:        Monster RPG 2: art and other architecture independent data
Group:          Amusements/Games/RPG
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%{pack_desc}

%prep
%setup -q -n monster-rpg-2-src-20130605-2
chmod -x data/*.*
chmod -x data/*/*.*

# sed patching lua5.2 includes to lua
sed "s/include <lua5.2\//include </" \
    -i include/monster2.hpp

sed "s/lua5.2/lua/" \
    -i CMakeLists.txt

# sed patching data directory to /usr/share/monster-rpg-2
sed "s/sprintf(result,\ \"%s\/data\/\", tmp)/\
    sprintf(result,\ \"\/usr\/share\/monster-rpg-2\/data\/\", tmp)/" \
    -i src/util.cpp

%build
mkdir -p build && cd build

cmake .. \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DUSER_INCLUDE_PATH="%{_includedir}" \
      -DUSER_LIBRARY_PATH="%{_libdir}" \
      -DKCM_AUDIO=on

make V=1 %{?_smp_mflags}

%install
install -D -m755 build/monster2 %{buildroot}%{_bindir}/%{name}

# Install game files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r data %{buildroot}%{_datadir}/%{name}

# Create a desktop entry
for i in 72 512 1024; do install -Dm644 icon"$i".png %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps/%{name}.png; done
%suse_update_desktop_file -c %{name} %{name} "An Old School Japanese Style RPG" %{name} %{name} "Game;RolePlaying;"

%fdupes -s %{buildroot}%{_datadir}

%post   data
%{icon_theme_cache_post}

%postun data
%{icon_theme_cache_postun}

%files
%defattr(-,root,root)
%doc %attr(644,root,root) LICENSE.txt README.txt Prologue.rtf ubuntu/changelog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files data
%defattr(-,root,root)
%{_datadir}/%{name}

%changelog
