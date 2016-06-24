#
# spec file for package warlocksgauntlet
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


%define rev 5234a6147bac

Name:           warlocksgauntlet
Version:        1.3
Release:        0
Summary:        Warlock's Gauntlet: binary files
License:        CC-BY-3.0
Group:          Amusements/Games/Action/Other
Url:            http://www.assembla.com/wiki/show/gdpl
Source0:        https://bitbucket.org/toxic/wg/get/%{version}.tar.bz2

# PATCH-FIX-OPENSUSE to 1) unify the binary file name 2) exclude built-in
# libraries 3) prevent linking error 4) prevent build error via gcc6.
Patch0:         warlocksgauntlet-makefiles.diff
# PATCH-FIX-OPENSUSE to prevent build error.
Patch1:         include2.patch
# PATCH-FIX-OPENSUSE to prevent crash on start-up.
Patch4:         toxic.patch
# PATCH-FIX-OPENSUSE to prevent build error via gcc≥47.
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
%setup -q -n toxic-wg-%{rev}
%patch0 -p0
%patch1
%patch4
%patch5 -p1

%build
%ifarch x86_64
make V=1 %{?_smp_mflags} -f Makefile.x86_64
%else
make V=1 %{?_smp_mflags}
%endif

%install
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
