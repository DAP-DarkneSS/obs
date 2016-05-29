#
# spec file for package flare
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


Name:           flare
Version:        0.19
Release:        0
Summary:        Free Libre Action Roleplaying Engine: binary file
License:        GPL-3.0
Group:          Amusements/Games/RPG
Url:            http://flarerpg.org/
Source0:        http://downloads.sourceforge.net/project/flare-game/Linux/%{name}.%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_ttf-devel
BuildRequires:  update-desktop-files
Requires:       %{name}-data = %{version}
Recommends:     python

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
License:        CC-BY-SA-3.0
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
%setup -q -n %{name}.%{version}

%build
%cmake \
       -DBINDIR="bin"
make %{?_smp_mflags}

%install
%cmake_install
chmod +x %{buildroot}%{_datadir}/games/%{name}/default/mods/*/languages/xgettext.py

# Might not be needed with next bump, verify!
find %{buildroot} -name ".DS_Store" -type f -delete
find %{buildroot} -name "._.DS_Store" -type f -delete
find %{buildroot} -name "._xp_table.txt" -type f -delete

%fdupes -s %{buildroot}%{_datadir}/games/%{name}/

%files
%defattr(-,root,root)
%doc COPYING CREDITS.txt README* RELEASE_NOTES.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%files data
%defattr(-,root,root)
%{_datadir}/games/%{name}/

%changelog
