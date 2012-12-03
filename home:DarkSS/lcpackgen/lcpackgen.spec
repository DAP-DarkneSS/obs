#
# spec file for package lcpackgen
#
# Copyright (c) 2010-2012 Rudoy Georg aka 0xd34df00d (source),
# (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# https://github.com/0xd34df00d/lcpackgen/issues
#

Name:           lcpackgen
Version:        1.1.git
Release:        1
Summary:        Package description file generator for LeechCraft repos

License:        BSD-2-Clause
Url:            https://github.com/0xd34df00d/lcpackgen
Group:          Development/Tools/Other
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  libQtWebKit-devel
BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files

Recommends:     leechcraft-lackman

Provides:       leechcraft-%{name} = %{version}
Obsoletes:      leechcraft-%{name} < %{version}

%description
Package description file generator for packages for LeechCraft repos:
script plugins, iconsets, additional data and other similar packages.

%prep
%setup -q

%build
cd ./src/
export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS
cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} ./src/lcpackgen %{buildroot}%{_bindir}
%suse_update_desktop_file -c lcpackgen lcpackgen "LeechCraft packages generator" lcpackgen "" "Development;Design;"

%files
%defattr(-,root,root)
%{_bindir}/lcpackgen
%{_datadir}/applications/lcpackgen.desktop

%changelog
