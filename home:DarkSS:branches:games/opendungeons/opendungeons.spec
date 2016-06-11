Name:           opendungeons
Version:        0.7.0
Release:        %mkrel 0
Summary:        RTS game in dark, damp and dangerous dungeons
Group:          Games/Strategy
License:        GPLv3+
URL:            http://opendungeons.github.io
Source0:        http://download.tuxfamily.org/opendungeons/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  pkgconfig(CEGUI-0)
BuildRequires:  pkgconfig(OGRE)
BuildRequires:  pkgconfig(OIS)
BuildRequires:  pkgconfig(sfml-audio)
BuildRequires:  pkgconfig(sfml-network)
BuildRequires:  pkgconfig(sfml-system)
Requires:       %{name}-data >= %{version}-%{release}

%description
OpenDungeons is an open source, real time strategy game sharing game
elements with the Dungeon Keeper series and Evil Genius. Players build
an underground dungeon which is inhabited by creatures. Players fight
each other for control of the underground by indirectly commanding their
minions, directly casting spells in combat, and luring enemies
into sinister traps.

%files
%doc AUTHORS CREDITS LICENSE.md README.md RELEASE-NOTES.md
%{_gamesbindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man6/%{name}.6*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/plugins.cfg

#----------------------------------------------------------------------

%package        data
Summary:        Data files for OpenDungeons
License:        GPLv3+ and CC-BY-SA and CC-BY and CC0 and MIT
BuildArch:      noarch

%description    data
This package contains arch-independent data files for OpenDungeons.
It is meant to be used with the "opendungeons" binary package.

%files          data
%{_gamesdatadir}/%{name}/

#----------------------------------------------------------------------

%prep
%autosetup

%build
%cmake
%make

%install
%make_install -C build


%changelog
