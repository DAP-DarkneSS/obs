#
# spec file for package flare
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


Name:           flare
Version:        0.20
Release:        0
Summary:        Free Libre Action Roleplaying Engine
License:        GPL-3.0+ and (CC-BY-SA-3.0 or CC-BY-SA-4.0)
Group:          Amusements/Games/RPG
Url:            http://flarerpg.org
Source0:        https://github.com/clintbellanger/flare-engine/archive/v%{version}.tar.gz#/%{name}-engine-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
Requires:       %{name}-game = %{version}
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Recommends:     python
Provides:       %{name}-engine = %{version}

%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine built
to handle a very specific kind of game: single-player 2D action RPGs.
Flare is not a reimplementation of an existing game or engine. It is a
tribute to and exploration of the action RPG genre.

Rather than building a very abstract, robust game engine, the goal of this
project is to build several real games and harvest an engine from the common,
reusable code. The first game, in progress, is a fantasy dungeon crawl.

Flare uses simple file formats (INI style config files) for most of the
game data, allowing anyone to easily modify game contents. Open formats
are preferred (png, ogg). The game code is C++.

%prep
%setup -q -n %{name}-engine-%{version}
# W: desktopfile-without-binary flare.desktop /usr/bin/flare
sed -i 's/@FLARE_EXECUTABLE_PATH@/%{name}/g' distribution/flare.desktop.in

%build
%cmake \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DBINDIR="bin"
make V=1 %{?_smp_mflags}

%install
%cmake_install

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
# Vs. error about wrong permissions.
%doc %attr(644,root,root) COPYING CREDITS.txt README* RELEASE_NOTES.txt
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.*
%{_datadir}/games/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
