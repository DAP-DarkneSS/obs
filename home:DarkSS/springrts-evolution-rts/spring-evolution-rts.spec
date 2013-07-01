#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           spring-evolution-rts
Version:        4.9
Release:        1
License:        CC-BY-NC-ND
Summary:        Evolution RTS is a Spring engine based Real Time Strategy game
Url:            http://www.evolutionrts.info/
Group:          Games/Strategy
Source0:        http://packages.springrts.com/builds/evo-v%{version}.sdz
# Maps are here: http://springfiles.com/spring/spring-maps
Source1:        evorts-altored_divide-v12.sd7
Source2:        evorts_-_delta_siege_-_v12.sd7
Source3:        evorts_-_division_-_v12.sd7
Source4:        evorts-eye_of_horus-v12.sd7
Source5:        evorts_-_glacier_pass_-_v12.sd7
Source6:        evorts_-_new_iammas_-_v12.sd7
Source7:        evorts-pockmark_valley-v12.sd7
Source8:        evorts_-_proving_grounds_-_v12.sd7
Source9:        evorts_-_riverglade_-_v12.sd7
Requires:       spring
Requires:       spring-features
Suggests:       %{name}-maps
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
Requires:       spring

%description maps
Maps designed specially for Evolution RTS game.
But you can try to use them with other Spring based games.

%prep
%setup -q -T -c %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/spring/mods
install -m 644 %{SOURCE0} %{buildroot}%{_gamesdatadir}/spring/mods/

mkdir -p %{buildroot}%{_gamesdatadir}/spring/maps
install -m 644 %{SOURCE1} %{buildroot}%{_gamesdatadir}/spring/maps/
install -m 644 %{SOURCE2} %{buildroot}%{_gamesdatadir}/spring/maps/
install -m 644 %{SOURCE3} %{buildroot}%{_gamesdatadir}/spring/maps/
install -m 644 %{SOURCE4} %{buildroot}%{_gamesdatadir}/spring/maps/
install -m 644 %{SOURCE5} %{buildroot}%{_gamesdatadir}/spring/maps/
install -m 644 %{SOURCE6} %{buildroot}%{_gamesdatadir}/spring/maps/
install -m 644 %{SOURCE7} %{buildroot}%{_gamesdatadir}/spring/maps/
install -m 644 %{SOURCE8} %{buildroot}%{_gamesdatadir}/spring/maps/
install -m 644 %{SOURCE9} %{buildroot}%{_gamesdatadir}/spring/maps/

%files
%{_gamesdatadir}/spring/mods/*

%files maps
%{_gamesdatadir}/spring/maps/*
