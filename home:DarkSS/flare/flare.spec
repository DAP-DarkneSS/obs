#
# spec file for package flare
#
# Copyright (c) 2010-2012 Clint Bellanger except where otherwise noted
# (source [GPL-3.0] and art [CC-BY-SA 3.0]), (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via https://github.com/clintbellanger/flare/issues
#

Name:           flare
Version:        0.16
Release:        1
Summary:        Free Libre Action Roleplaying Engine: binary file

License:        GPL-3.0
URL:            http://clintbellanger.net/rpg/
Source0:        https://github.com/clintbellanger/%{name}/tarball/v%{version}
Group:          Amusements/Games/RPG

BuildRequires:  make cmake
BuildRequires:  update-desktop-files fdupes
BuildRequires:  gcc gcc-c++
BuildRequires:  libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel
Requires:       %{name}-data = %{version}
Requires:       python

%description
Free Libre Action Roleplaying Engine: binary file.

Flare (Free Libre Action Roleplaying Engine) is a simple game engine built to handle a
very specific kind of game: single-player 2D action RPGs. Flare is not a reimplementation
of an existing game or engine. It is a tribute to and exploration of the action RPG genre. 

Rather than building a very abstract, robust game engine, the goal of this project is to build several real games
and harvest an engine from the common, reusable code. The first game, in progress, is a fantasy dungeon crawl. 

Flare uses simple file formats (INI style config files) for most of the game data, allowing anyone
to easily modify game contents. Open formats are preferred (png, ogg). The game code is C++.

%package data
Summary:        Flare: art and other architecture independent data
License:        CC-BY-SA 3.0
Group:          Amusements/Games/RPG
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Free Libre Action Roleplaying Engine: art and other architecture independent data.

Flare (Free Libre Action Roleplaying Engine) is a simple game engine built to handle a
very specific kind of game: single-player 2D action RPGs. Flare is not a reimplementation
of an existing game or engine. It is a tribute to and exploration of the action RPG genre. 

Rather than building a very abstract, robust game engine, the goal of this project is to build several real games
and harvest an engine from the common, reusable code. The first game, in progress, is a fantasy dungeon crawl. 

Flare uses simple file formats (INI style config files) for most of the game data, allowing anyone
to easily modify game contents. Open formats are preferred (png, ogg). The game code is C++.

%prep
%setup -q -n clintbellanger-%{name}-347ecb6

%build
mkdir -p build
cd build
export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS
cmake .. \
       -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_PREFIX:PATH=/usr \
       -DBINDIR="bin"
make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}
chmod +x %{buildroot}%{_datadir}/games/%{name}/mods/fantasycore/languages/xgettext.py
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_datadir}/games/%{name}/mods/fantasycore/soundfx/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{name}

%files data
%defattr(-,root,root)
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
