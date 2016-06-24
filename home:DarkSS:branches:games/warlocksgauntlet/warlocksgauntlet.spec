#
# spec file for package warlocksgauntlet
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2010-2012 Warlock's Gauntlet team:
# see more at http://www.assembla.com/spaces/gdpl/wiki/Kontakty
# (the code is open source and the assets are licensed CC),
# (c) 2012 Perlow Dmitriy A. (spec file)
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


%define rev 5234a6147bac

Name:           warlocksgauntlet
Version:        1.3
Release:        0
Summary:        Warlock's Gauntlet: binary files
License:        CC-BY-3.0
Group:          Amusements/Games/Action/Other
Url:            http://www.assembla.com/wiki/show/gdpl
Source0:        https://bitbucket.org/toxic/wg/get/%{version}.tar.bz2
# PATCH-FIX-UPSTREAM Building error is fixed.
Patch1:         include2.patch
# PATCH-FIX-OPENSUSE Makefile for x32 is fixed in order to unify the binary
# file name, exclude built-in libraries and resolve linking error.
Patch2:         link64.patch
# PATCH-FIX-OPENSUSE Makefile for x64 is fixed in order to unify the binary
# file name, exclude built-in libraries and resolve linking error.
Patch3:         link32.patch
# PATCH-FIX-UPSTREAM Crash on startup is fixed.
Patch4:         toxic.patch
# See patch discussion with the game developer at
# http://www.assembla.com/spaces/gdpl/tickets/1282-make--***-%5Bwarlocksgauntlet-bin64%5D-error-1-in-opensuse-12-1
# PATCH-FIX-UPSTREAM warlocksgauntlet-gcc47.patch
Patch5:         warlocksgauntlet-gcc47.patch
BuildRequires:  Mesa-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
%if 0%{?suse_version} > 1220
BuildRequires:  glu-devel
%endif
BuildRequires:  libglue-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  openal-soft-devel
BuildRequires:  sfml-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
Requires:       %{name}-data = %{version}

%description
Warlock's Gauntlet: binary file.

Warlock's Gauntlet is a dynamic, top-down shooter (well, spell-caster) game,
placing you - the player - in the role of a battlemage.

The hero travels through maps filled with monsters, gaining experience and
learning new spells. The game is similar to titles like Gauntlet or Diablo.
The game features 25 random-generated levels which should amount to about
three hours of gameplay; the player character can find over 60 distinct
spells. There is no networked multiplayer, but the game includes a hot-seat
two-player mode. The game available entirely for free.

%package data
Summary:        Warlock's Gauntlet: assets and other architecture independent data
Group:          Amusements/Games/Action/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Warlock's Gauntlet: assets and other architecture independent data.

Warlock's Gauntlet is a dynamic, top-down shooter (well, spell-caster) game,
placing you - the player - in the role of a battlemage.

The hero travels through maps filled with monsters, gaining experience and
learning new spells. The game is similar to titles like Gauntlet or Diablo.
The game features 25 random-generated levels which should amount to about
three hours of gameplay; the player character can find over 60 distinct
spells. There is no networked multiplayer, but the game includes a hot-seat
two-player mode. The game available entirely for free.

%prep
tar -xf %{SOURCE0} -C ./
cd toxic-wg-%{rev}
%patch1
%patch2
%patch3
%patch4
%patch5 -p1

%build
cd toxic-wg-%{rev}
%ifarch %{ix86}
make
%endif
%ifarch x86_64
make -f Makefile.x86_64
%endif

%install
cd toxic-wg-%{rev}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r ./data/ %{buildroot}%{_datadir}/%{name}
install ./data.vfs %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
install ./%{name} %{buildroot}%{_bindir}/%{name}.bin
echo -e '#!/bin/sh'"\n\ncd %{_datadir}/%{name}\n%{name}.bin" > %{buildroot}%{_bindir}/%{name}
# The binary file must be run from the game data directory.
chmod +x %{buildroot}%{_bindir}/%{name}
cp -r ./tools/deb_image/usr/share/icons/ %{buildroot}%{_datadir}
%suse_update_desktop_file -c %{name} "Warlock's Gauntlet" "Dynamic, top-down spell-caster game" %{name} WarlocksGauntlet "Game;ActionGame;"
%fdupes -s %{buildroot}%{_datadir}/%{name}/data/

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}.bin
%attr(755,root,root) %{_bindir}/%{name}

%files data
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%dir %{_datadir}/icons/hicolor
%{_datadir}/%{name}/data/*
%{_datadir}/%{name}/data.vfs
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/%{name}.desktop

%changelog
