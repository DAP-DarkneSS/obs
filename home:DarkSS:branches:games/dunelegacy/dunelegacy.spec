#
# spec file for package dunelegacy
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Summary:        A modern Dune II reimplementation
License:        GPL-2.0+
Group:          Amusements/Games/Strategy/Real Time
Name:           dunelegacy
Version:        0.96.3
Release:        0
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2
Source9:        %{name}.6
# PATCH-FIX-UPSTREAM mostly no prevent build failure via gcc6.
Patch0:         dunelegacy-0.96.3-configure-CXXFLAGS.diff
Url:            http://dunelegacy.sourceforge.net/
BuildRequires:  cppunit-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Lead one of three interplanetary houses, Atreides, Harkonnen or Ordos,
in an attempt to harvest the largest amount of spice from the sand
dunes. Exchange your spice stockpiles for credits through refinement
and build an army capable of thwarting attempts of the other houses to
stop your harvesting!

Dune Legacy is an effort by a handful of developers to revitalize the
first-ever real-time strategy game. The original game was the basis
for the hugely successful Command and Conquer series, and the gameplay
has been replicated an extended to a wide variety of storylines and
series.

NOTE: Original Dune 2 game files are needed.

%prep
%setup -q
dos2unix ToDo.txt
%patch0 -p0

%build
%configure
make %{?_smp_mflags}

%check
make distclean
./runUnitTests.sh

%install
%suse_update_desktop_file -i %{name}
install -D -p -m 0644 %{name}-128x128.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%make_install

mkdir -p %{buildroot}%{_mandir}/man6
cp %{SOURCE9} %{buildroot}%{_mandir}/man6

%files
%defattr(644,root,root,755)
%doc README ToDo.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/%{name}.?.*
%{_datadir}/%{name}/
%attr(755,root,root) %{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
