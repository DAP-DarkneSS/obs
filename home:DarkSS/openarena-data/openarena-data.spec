#
# spec file for package openarena-data
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           openarena-data
Version:        0.8.8
Release:        0
Summary:        Data files for Open Arena
License:        GPL-2.0+
Group:          Amusements/Games/Action/Shoot
Url:            http://openarena.ws/
Source:         http://openarena.ws/request.php?4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  unzip
Requires:       openarena = %{version}
BuildArch:      noarch
NoSource:       0

%description
OpenArena is an open-source content package for Quake III Arena 
licensed under the GPL, effectively creating a free stand-alone game.

This package contain only platform independent data files (maps, player models, weapon models, etc. )

Authors:
--------
Aardappel       - Maps (Converted with permission)
leileilol       - Leads, gfx, models, anim, sound
                                     and textures
Multiplex       - Models, textures
crayon          - Skins, models
JK Makowka      - Models, skins
Democritus      - Textures
jzero           - Models, textures, 2D
Mancubus        - The Announcer
mewse           - Engine compiling, tools, textures
                                       and testing
div0            - Engine compiling, fixing
dmn_clown       - Botfiles code
MilesTeg        - 2D art and textures
evillair        - Textures (nicked from Nexuiz)
Shadowdragon    - Models
mightypea       - Models
Morphed         - Skins
toddd           - Sound
DarkThief       - Skins
slyus           - Skins
SavageX         - Maps
Kaz             - Skins
pixie           - Voices (Kyonshi, Major)
Vondur          - Map (kaos)
Tyrann          - Map (Aggressor)
Ed              - Map (Conversion of ce1m7)

%package -n openarena-doc
Summary:        Documentation for Open Arena
Group:          System/Libraries  
%if 0%{?suse_version} > 1000
Recommends:     openarena
%endif

%description -n openarena-doc
This package contains documentation and license for Open Arena.

%prep
%setup -q -n openarena-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/games/openarena/baseoa
%{__install} baseoa/* %{buildroot}%{_datadir}/games/openarena/baseoa
mkdir -p %{buildroot}/%{_datadir}/games/openarena/missionpack
%{__install} missionpack/* %{buildroot}%{_datadir}/games/openarena/missionpack
mkdir -p %{buildroot}/%{_docdir}/games/openarena
%{__install} LINUX* C* README readme* WENEED %{buildroot}/%{_docdir}/games/openarena

%files
%defattr(-,root,root)
%dir %{_datadir}/games/openarena
%dir %{_datadir}/games/openarena/baseoa
%attr(644,root,root) %{_datadir}/games/openarena/baseoa/*
%dir %{_datadir}/games/openarena/missionpack
%attr(644,root,root) %{_datadir}/games/openarena/missionpack/*

%files -n openarena-doc
%defattr(-,root,root)
%dir %{_docdir}/games
%dir %{_docdir}/games/openarena
%attr(644,root,root) %{_docdir}/games/openarena/*

%changelog
