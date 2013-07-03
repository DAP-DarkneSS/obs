#
# spec file for package springrts-features
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

Name:           springrts-features
Version:        1.0
Release:        1
License:        SUSE-Freeware
Summary:        All of the features made for Spring engine to date
Url:            http://springfiles.com/spring/tools/spring-features
Group:          Amusements/Games/Strategy/Real Time
Source0:        http://springfiles.com/sites/default/files/downloads/spring/tools/spring_features-v01.sdz
Requires:       springrts
BuildArch:      noarch

%description
Games/mods can add this archive as a dependency and map authors can then use
featureplacer in Gundam RTS/Evolution RTS/Other to place features. Mapconv
already has support for featureplacer configs.

Adding this archive as a dependency also enables that game/mod to use maps
that were previously limited to specific games. For example, many of the
EvoRTS maps. (I.E. General Caiaphas' Revenge - Attached screenshot)

This also allows for map sizes to be smaller as there is no longer any need
to include the textures with the map.

Additionally, maps may also call this archive as a dependency. Maps can also
include the featuredef files if necessary so that reclaim and blocking
values can be changed. The featuredefs included are simply fallbacks so that
the features will show up, and most reclaim values are really low (like 10
energy, 10 metal, etc).

Basically, the point is that mappers can change the features up however they
like with this archive..

%prep
%setup -q -T -c %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/games/spring/mods
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/games/spring/mods/

%files
%defattr(-,root,root)
%dir %{_datadir}/games/spring
%dir %{_datadir}/games/spring/mods
%{_datadir}/games/spring/mods/*.sdz

