#
# spec file for packages openarena-data-extra & openarena-citymod
#
# [spec] Copyright (c) 2012 Perlow Dmitriy A.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           openarena-data-extra
Version:        0
Release:        1
Summary:        Extra data files for Open Arena
License:        GPL-2.0+
Group:          Amusements/Games/Action/Shoot
Url:            http://openarena.ws/
# Extra data:
Source0:        drasticcity.pk3
Source1:        houseby.pk3
Source2:        osiedle.pk3
Source3:        penthouse.pk3
# City mod:
Source10:       z-gpl-q3a2oa-textures-v5.pk3
Source11:       z-proskins2.pk3
Source12:       zz-proskins2.pk3
Requires:       openarena
BuildArch:      noarch

%description
OpenArena is an open-source content package for Quake III Arena 
licensed under the GPL, effectively creating a free stand-alone game.

This package contain only platform independent data files
(maps, player models, weapon models, etc. )

%package -n openarena-citymod
Summary:        City mod for Open Arena
Requires:       openarena

%description -n openarena-citymod
This package contains an Open Arena City mod independent data files
(maps, player models, weapon models, etc. )

%prep

%build

%install
mkdir -p %{buildroot}/%{_datadir}/games/openarena/baseoa
%{__install} %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_datadir}/games/openarena/baseoa

mkdir -p %{buildroot}/%{_datadir}/games/openarena/city
%{__install} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{buildroot}%{_datadir}/games/openarena/city

%files
%defattr(-,root,root)
%dir %{_datadir}/games/openarena
%dir %{_datadir}/games/openarena/baseoa
%attr(644,root,root) %{_datadir}/games/openarena/baseoa/*

%files -n openarena-citymod
%defattr(-,root,root)
%dir %{_datadir}/games/openarena
%dir %{_datadir}/games/openarena/city
%attr(644,root,root) %{_datadir}/games/openarena/city/*

%changelog
