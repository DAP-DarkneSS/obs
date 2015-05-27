#
# spec file for package monster-rpg-2
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define tarballver  20150519
%define topleveldir monster-rpg-2_src-%{tarballver}
%define allegrover  5.1.10

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
Version:        2.1+%{tarballver}
Release:        0
Summary:        An Old School Japanese Style RPG
License:        Zlib
Group:          Amusements/Games/RPG
Url:            http://nooskewl.ca/monster-rpg-2
Source0:        http://nooskewl.ca/monster-rpg-2/code/%{topleveldir}.zip
# PATCH-FIX-OPENSUSE to prevent static linking.
Patch0:         monster-rpg-2-dynamic-linking.diff
# PATCH-FIX-OPENSUSE to use {_datadir} at runtime.
Patch1:         monster-rpg-2-datadir.diff

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libphysfs-devel
BuildRequires:  sed
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  zip
BuildRequires:  pkgconfig(allegro_acodec-5)     >= %{allegrover}
BuildRequires:  pkgconfig(allegro_audio-5)      >= %{allegrover}
BuildRequires:  pkgconfig(allegro_color-5)      >= %{allegrover}
BuildRequires:  pkgconfig(allegro_dialog-5)     >= %{allegrover}
BuildRequires:  pkgconfig(allegro_font-5)       >= %{allegrover}
BuildRequires:  pkgconfig(allegro_image-5)      >= %{allegrover}
BuildRequires:  pkgconfig(allegro_memfile-5)    >= %{allegrover}
BuildRequires:  pkgconfig(allegro_physfs-5)     >= %{allegrover}
BuildRequires:  pkgconfig(allegro_primitives-5) >= %{allegrover}
BuildRequires:  pkgconfig(allegro_ttf-5)        >= %{allegrover}
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
BuildRequires:  pkgconfig(xi)
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
%setup -q -n %{topleveldir}
%patch0
%patch1
chmod -x data/*.*
chmod -x data/*/*.*

# sed patching lua5.2 includes to lua
sed "s/include <lua5.2\//include </" \
    -i include/monster2.hpp

sed "s/lua5.2/lua/" \
    -i CMakeLists.txt

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
zip -r %{buildroot}%{_datadir}/%{name}/data.zip data

# Create a desktop entry
for i in 57 72 114 144; do install -Dm644 "xcode/Monster 2/icon$i".png %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps/%{name}.png; done
%suse_update_desktop_file -c %{name} %{name} "An Old School Japanese Style RPG" %{name} %{name} "Game;RolePlaying;"

%fdupes -s %{buildroot}%{_datadir}

# NOTE: prevents runtime issue because of packaging
# scheme major change (2.1: data/ → 2.1+2015*: data.zip)
%pre
rm -rf %{_datadir}/%{name}/data
echo "WARNING: 2.1' configuration ( ~/.config/Nooskewl )"
echo "is incompatible with any later version."

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc %attr(644,root,root) SourceLicense.txt ubuntu/changelog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/57x57
%dir %{_datadir}/icons/hicolor/57x57/apps
%dir %{_datadir}/icons/hicolor/114x114
%dir %{_datadir}/icons/hicolor/114x114/apps
%dir %{_datadir}/icons/hicolor/144x144
%dir %{_datadir}/icons/hicolor/144x144/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files data
%defattr(-,root,root)
%{_datadir}/%{name}

%changelog
