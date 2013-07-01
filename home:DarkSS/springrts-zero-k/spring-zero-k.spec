%define		oname	zk

Name:		spring-zero-k
Version:	1.0.10.8
Release:	2
Summary:	Spring engine based game focused on a streamlined economy & advanced interface
Group:		Games/Strategy
License:	GPL
URL:		http://zero-k.info/
Source0:	http://packages.springrts.com/builds/%{oname}-v%{version}.sdz
Source1:	http://api.springfiles.com/files/maps/tabula-v5b.sd7
Source2:	http://api.springfiles.com/files/maps/folsomdamdeluxev4.sd7
Source3:	http://api.springfiles.com/files/maps/worldv2.sd7
Requires:	spring
Provides:	zero-k = %{version}
Suggests:	%{name}-maps
Buildarch:	noarch

%description
Zero-K is a fast, competitive game with a focus on a streamlined economy
and advanced interface that takes the focus off tedious tasks and back on
the action. A huge roster of interesting, unique units and a variety of unit
abilities provides tremendous tactical and strategic depth to the game.

Uses Spring engine to run.

%package maps
Summary:	Maps designed specially for Zero-K game
Requires:	spring

%description maps
Maps designed specially for Zero-K game.
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

%files
%{_gamesdatadir}/spring/mods/*

%files maps
%{_gamesdatadir}/spring/maps/*

