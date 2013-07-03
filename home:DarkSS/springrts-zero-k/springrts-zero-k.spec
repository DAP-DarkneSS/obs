#
# spec file for package springrts-zero-k
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

#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           springrts-zero-k
Version:        1.2.2.4
Release:        1
License:        SUSE-Freeware or GPL-2.0+
Summary:        Spring engine based game focused on a streamlined economy & advanced interface
Url:            http://zero-k.info/
Group:          Amusements/Games/Strategy/Real Time

Source0:        http://packages.springrts.com/builds/zk-v%{version}.sdz
Source1:        http://api.springfiles.com/files/maps/tabula-v5b.sd7
Source2:        http://api.springfiles.com/files/maps/folsomdamdeluxev4.sd7
Source3:        http://api.springfiles.com/files/maps/worldv2.sd7

Requires:       %{name}-maps
Requires:       springrts
Provides:       zero-k = %{version}
BuildArch:      noarch

%description
Zero-K is a fast, competitive game with a focus on a streamlined economy
and advanced interface that takes the focus off tedious tasks and back on
the action. A huge roster of interesting, unique units and a variety of unit
abilities provides tremendous tactical and strategic depth to the game.

Uses Spring engine to run.

%package maps
Summary:        Maps designed specially for Zero-K game
Requires:       springrts

%description maps
Maps designed specially for Zero-K game.
But you can try to use them with other Spring based games.

%prep
%setup -q -T -c %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/games/spring/mods
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/games/spring/mods/

mkdir -p %{buildroot}%{_datadir}/games/spring/maps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/games/spring/maps/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/games/spring/maps/
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/games/spring/maps/

%files
%defattr(-,root,root)
%dir %{_datadir}/games/spring
%dir %{_datadir}/games/spring/mods
%{_datadir}/games/spring/mods/*.sdz

%files maps
%defattr(-,root,root)
%dir %{_datadir}/games/spring
%dir %{_datadir}/games/spring/maps
%{_datadir}/games/spring/maps/*.sd7

