Name:		spring-features
Version:	1.0
Release:	1
Summary:	Spring Features contains all of the features made for Spring engine to date
Group:		Games/Strategy
# Some kind of "Free" as stated in upstream. Nobody seems to really care?
License:	Freeware
URL:		http://springfiles.com/spring/tools/spring-features
Source0:	spring_features-v01.sdz
Requires:	spring
Buildarch:	noarch

%description
Spring Features contains all of the features made for Spring engine to date.

Required by some Spring engine-based games.

%prep
%setup -q -T -c %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/spring/mods
install -m 644 %{SOURCE0} %{buildroot}%{_gamesdatadir}/spring/mods/

%files
%{_gamesdatadir}/spring/mods/*

