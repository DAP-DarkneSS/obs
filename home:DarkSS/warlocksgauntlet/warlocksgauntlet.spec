#
# spec file for package warlocksgauntlet
#
# Copyright (c) 2010-2012 Warlock's Gauntlet team:
# see more at http://www.assembla.com/spaces/gdpl/wiki/Kontakty
# (the code is open source and the assets are licensed CC),
# (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via http://www.assembla.com/spaces/gdpl/tickets
#

%define rev 5234a6147bac

Name:           warlocksgauntlet
Version:        1.3
Release:        3
Summary:        Warlock's Gauntlet: binary files

License:        Open Source
URL:            http://www.assembla.com/wiki/show/gdpl
Source0:        https://bitbucket.org/toxic/wg/get/%{version}.tar.bz2
Group:          Amusements/Games/Action/Other
# PATCH-FIX-UPSTREAM Error while building bleeding edge version is fixed.
# Patch1:         tomat.patch
# PATCH-FIX-UPSTREAM Error while building bleeding edge version is fixed.
# Patch2:         include.patch
# PATCH-FIX-UPSTREAM Building error is fixed.
Patch3:         include2.patch
# PATCH-FIX-OPENSUSE Makefile for x32 is fixed in order to unify the binary
# file name, exclude built-in libraries and resolve linking error.
Patch4:         link64.patch
# PATCH-FIX-OPENSUSE Makefile for x64 is fixed in order to unify the binary
# file name, exclude built-in libraries and resolve linking error.
Patch5:         link32.patch
# PATCH-FIX-UPSTREAM Crash on startup is fixed.
Patch6:         toxic.patch
# See patch discussion with the game developer at
# http://www.assembla.com/spaces/gdpl/tickets/1282-make--***-%5Bwarlocksgauntlet-bin64%5D-error-1-in-opensuse-12-1

BuildRequires:  make
BuildRequires:  update-desktop-files fdupes
BuildRequires:  gcc-c++
BuildRequires:  Mesa-devel libglue-devel openal-soft-devel libsndfile-devel sfml-devel
BuildRequires:  glew-devel zlib-devel
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
License:        CC
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
# %%patch1
# %%patch2
%patch3
%patch4
%patch5
%patch6
# rm ./libs32/libopenal*
# rm ./libs64/libopenal*
# rm ./libs32/libsndfile*
# rm ./libs64/libsndfile*

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
# mkdir -p %%{buildroot}%%{_libdir}
# %%ifarch %%{ix86}
# %%{__install} ./libs32/libsfml* %%{buildroot}%%{_libdir}
# %%endif
# %%ifarch x86_64
# %%{__install} ./libs64/libsfml* %%{buildroot}%%{_libdir}
# %%endif
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r ./data/ %{buildroot}%{_datadir}/%{name}
%{__install} ./data.vfs %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
%{__install} ./%{name} %{buildroot}%{_bindir}/%{name}-bin
echo -e '#!/bin/sh'"\n\ncd %{_datadir}/%{name}\n%{name}-bin" > %{buildroot}%{_bindir}/%{name}
# The binary file must be run from the game data directory.
chmod +x %{buildroot}%{_bindir}/%{name}
cp -r ./tools/deb_image/usr/share/icons/ %{buildroot}%{_datadir}
%suse_update_desktop_file -c %{name} "Warlock's Gauntlet" "Dynamic, top-down spell-caster game" %{name} WarlocksGauntlet "Game;ActionGame;"
%fdupes -s %{buildroot}%{_datadir}/%{name}/data/

# %%post -n %%{name} -p /sbin/ldconfig
# 
# %%postun -n %%{name} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}-bin
%attr(755,root,root) %{_bindir}/%{name}
# %%{_libdir}/libsfml*

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
