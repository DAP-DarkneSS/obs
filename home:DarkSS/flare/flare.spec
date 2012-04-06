#
# spec file for package flare
#
# Copyright (c) 2010-2012 Clint Bellanger except where otherwise noted
# (source [GPL-3.0] and art [CC-BY-SA 3.0]), (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via https://github.com/clintbellanger/flare/issues
#

Name:           flare
Version:        v0.14-541-gc545832
Release:        0
Summary:        Free Libre Action Roleplaying Engine: binary file

License:        GPL-3.0
URL:            http://clintbellanger.net/rpg/
Source0:        %{name}-%{version}.tar.bz2
Patch1:         bin.patch
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
%setup -q
%patch1

%build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX:STRING="/usr" ..
make

%install
cd build
make install DESTDIR=%{buildroot}
chmod +x %{buildroot}%{_datadir}/games/flare/mods/fantasycore/languages/xgettext.py
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/flare

%files data
%defattr(-,root,root)
%{_datadir}/applications/flare.desktop
%dir %{_datadir}/games/flare
%{_datadir}/games/flare/*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/flare.svg

%changelog
