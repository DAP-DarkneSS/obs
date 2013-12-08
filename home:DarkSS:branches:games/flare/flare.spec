#
# spec file for package flare
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define pack_desc Flare (Free Libre Action Roleplaying Engine) \
is a simple game engine built to handle a very specific kind of \
game: single-player 2D action RPGs. Flare is not a \
reimplementation of an existing game or engine. It is a tribute \
to and exploration of the action RPG genre. \
\
Rather than building a very abstract, robust game engine, the \
goal of this project is to build several real games and harvest \
an engine from the common, reusable code. The first game, in \
progress, is a fantasy dungeon crawl. \
\
Flare uses simple file formats (INI style config files) for most \
of the game data, allowing anyone to easily modify game contents. \
Open formats are preferred (png, ogg). The game code is C++.

Name:           flare
Version:        0.19
Release:        0
Summary:        Free Libre Action Roleplaying Engine: binary file
License:        GPL-3.0+
Group:          Amusements/Games/RPG

Url:            http://flarerpg.org/
Source0:        http://netcologne.dl.sourceforge.net/project/flare-game/Linux/flare.%{version}.tar.gz

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
Requires:       %{name}-game
Recommends:     python

%description
%{pack_desc}

%package data
Summary:        Flare: art and other architecture independent data
License:        CC-BY-SA-3.0
Group:          Amusements/Games/RPG
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%{pack_desc}

%package game
Summary:        Flare: default game mode
License:        CC-BY-SA-3.0
Group:          Amusements/Games/RPG
Requires:       %{name}
BuildArch:      noarch

%description game
%{pack_desc}

%prep
%setup -q -n %{name}.%{version}
find mods/ -name "*DS_Store" -exec rm {} \;

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
make V=1 %{?_smp_mflags}

%install
cd build
make V=1 install DESTDIR=%{buildroot}
chmod +x %{buildroot}%{_datadir}/games/%{name}/default/mods/*/languages/readme.txt
chmod +x %{buildroot}%{_datadir}/games/%{name}/default/mods/*/languages/xgettext.py
chmod +x %{buildroot}%{_datadir}/games/%{name}/default/mods/*/languages/regenerate_po.sh
# %%suse_update_desktop_file -i %{name}
%fdupes -s %{buildroot}%{_datadir}/games/%{name}

%files
%defattr(-,root,root)
%doc COPYING README* CREDITS.txt Codingstyle.txt RELEASE_NOTES.txt
%{_bindir}/%{name}

%files data
%defattr(-,root,root)
# %%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/default
%dir %{_datadir}/games/%{name}/default/mods
%{_datadir}/games/%{name}/default/mods/default
# %%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc %{_mandir}/man*/flare.*.gz

%files game
%defattr(-,root,root)
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/default
%dir %{_datadir}/games/%{name}/default/mods
%{_datadir}/games/%{name}/default/mods/*
%exclude %{_datadir}/games/%{name}/default/mods/default

%changelog
