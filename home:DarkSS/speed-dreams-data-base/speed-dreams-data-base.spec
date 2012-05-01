%define oname speed-dreams-2

Name:		speed-dreams-data-base
Version:	2.0.0
Release:	%mkrel 1
Summary:	Data base for Speed Dreams 2.0
License:	GPLv2
Group:		Games/Arcade
Source0:	%{name}-2.0.0-svn4687.tar.xz
URL:		http://www.speed-dreams.org
BuildArch:	noarch
Requires:	speed-dreams = %{version}

%description
Base data for Speed Dreams
A Torcs's fork
include track Espie - cars SC
Textures - sounds - menu - config

%prep
%setup -q -n %{name}-2.0

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_gamesdatadir}/%{oname}
cp -a %{_topdir}/BUILD/%{name}-2.0/* %{buildroot}/%{_gamesdatadir}/%{oname}

%files
%{_gamesdatadir}/%{oname}/tracks/circuit/espie/*.*
%{_gamesdatadir}/%{oname}/cars/sc-boxer-96/*.*
%{_gamesdatadir}/%{oname}/cars/sc-cavallo-360/*.*
%{_gamesdatadir}/%{oname}/cars/sc-fmc-gt4/*.*
%{_gamesdatadir}/%{oname}/cars/sc-lynx-220/*.*
%{_gamesdatadir}/%{oname}/cars/sc-murasama-nsx/*.*
%{_gamesdatadir}/%{oname}/cars/sc-spirit-300/*.*
%{_gamesdatadir}/%{oname}/categories/*.*
%{_gamesdatadir}/%{oname}/data/fonts/*.*
%{_gamesdatadir}/%{oname}/data/img/*.*
%{_gamesdatadir}/%{oname}/data/menu/*.*
%{_gamesdatadir}/%{oname}/data/objects/*.*
%{_gamesdatadir}/%{oname}/data/sound/*.*
%{_gamesdatadir}/%{oname}/data/textures/*.*
%{_gamesdatadir}/%{oname}/data/tracks/*.*
%{_gamesdatadir}/%{oname}/config
%{_gamesdatadir}/%{oname}/drivers/human
%{_gamesdatadir}/%{oname}/drivers/simplix_sc
%{_gamesdatadir}/%{oname}/drivers/usr_sc



%changelog

* Mon Apr 09 2012 shadow95 <shadow95> 2.0.0-1.mga2
+ Revision: 229838
- update to Release
- Update to RC2

* Tue Feb 28 2012 shadow95 <shadow95> 2.0.0-0.1.rc1_r4527.1.mga2
+ Revision: 215923
- remove version in description
- remove buildroot
- update to RC1
- Update data base to svn 4414 (RC1)
- add Requires: speed-dreams
- imported package speed-dreams-data-base

