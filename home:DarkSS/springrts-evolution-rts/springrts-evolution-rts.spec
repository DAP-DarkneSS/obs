#
# spec file for package springrts-evolution-rts
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


Name:           springrts-evolution-rts
Version:        6.42
Release:        1
License:        SUSE-Freeware or CC-BY-NC-ND-3.0
Summary:        Evolution RTS is a Spring engine based Real Time Strategy game
Url:            http://www.evolutionrts.info/
Group:          Amusements/Games/Strategy/Real Time

Source0:        http://packages.springrts.com/builds/evo-v%{version}.sdz
Source1:        http://springfiles.com/sites/default/files/downloads/spring/spring-maps/evorts-altored_divide-v12.sd7
Source2:        http://spring1.admin-box.com/maps/evorts_-_delta_siege_-_v12.sd7
Source3:        http://spring1.admin-box.com/maps/evorts_-_division_-_v12.sd7
Source4:        http://springfiles.com/sites/default/files/downloads/spring/spring-maps/evorts-eye_of_horus-v12.sd7
Source5:        http://spring1.admin-box.com/maps/evorts_-_glacier_pass_-_v12.sd7
Source6:        http://spring1.admin-box.com/maps/evorts_-_new_iammas_-_v12.sd7
Source7:        http://springfiles.com/sites/default/files/downloads/spring/spring-maps/evorts-pockmark_valley-v12.sd7
Source8:        http://spring1.admin-box.com/maps/evorts_-_proving_grounds_-_v12.sd7
Source9:        http://spring1.admin-box.com/maps/evorts_-_riverglade_-_v12.sd7

Requires:       springrts
Requires:       springrts-features
Requires:       %{name}-maps
Provides:       evolution-rts = %{version}
BuildArch:      noarch

%description
A new war is brewing. A violent conflict, between the Six Colonies,
each one convinced that it was in the right, each one sure of its
own ability to defeat its enemies. But they need Generals.
They need soldiers. They need you.

Uses Spring engine to run.

%package maps
Summary:        Maps designed specially for Evolution RTS game
Requires:       %{name}

%description maps
Maps designed specially for Evolution RTS game.
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
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/games/spring/maps/
install -m 644 %{SOURCE5} %{buildroot}%{_datadir}/games/spring/maps/
install -m 644 %{SOURCE6} %{buildroot}%{_datadir}/games/spring/maps/
install -m 644 %{SOURCE7} %{buildroot}%{_datadir}/games/spring/maps/
install -m 644 %{SOURCE8} %{buildroot}%{_datadir}/games/spring/maps/
install -m 644 %{SOURCE9} %{buildroot}%{_datadir}/games/spring/maps/

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
