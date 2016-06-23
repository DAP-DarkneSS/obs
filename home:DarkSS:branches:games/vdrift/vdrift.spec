#
# spec file for package vdrift
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


#
%define _year   2014
%define _month  10
%define _day    20

Name:           vdrift
Version:        %{_year}%{_month}%{_day}
Release:        0
Summary:        A cross-platform, open source driving simulation
License:        GPL-3.0
Group:          Amusements/Games/3D/Race
Url:            http://vdrift.net/
# See also: https://github.com/VDrift/vdrift
Source:         https://downloads.sourceforge.net/project/vdrift/vdrift/vdrift-%{_year}-%{_month}-%{_day}/vdrift-%{_year}-%{_month}-%{_day}.tar.bz2
# PATCH-FIX-UPSTREAM fix-desktop-and-appdata.patch -- https://github.com/VDrift/vdrift/pull/147
Patch0:         fix-desktop-and-appdata.patch
# PATCH-FIX-OPENSUSE to prevent build issue via gcc6.
Patch1:         vdrift-20141020-gcc6.patch
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  scons
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(bullet)
BuildRequires:  pkgconfig(libcurl) >= 7.21.6
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis) >= 1.2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       %{name}-data = %{version}

%description
VDrift is a cross-platform, open source driving simulation made
with drift racing in mind. It's powered by the excellent Vamos
physics engine.

%package data
Summary:        Data files for VDrift
Group:          Amusements/Games/3D/Race
Requires:       %{name} = %{version}
Requires:       %{name}-data-cars = %{version}
Requires:       %{name}-data-tracks = %{version}
Obsoletes:      %{name}-data-drivers < %{version}
Obsoletes:      %{name}-data-sounds < %{version}
BuildArch:      noarch

%description data
Common data files for VDrift.

%package data-cars
Summary:        Cars for VDrift
Group:          Amusements/Games/3D/Race
Requires:       %{name}-data = %{version}
BuildArch:      noarch

%description data-cars
Cars for package VDrift.

Included cars: 360, CO, CS, F1-02, G4, M7, MC, MI, T73, TC6, TL2, XS...

%package data-tracks
Summary:        Tracks for VDrift
Group:          Amusements/Games/3D/Race
Requires:       %{name}-data = %{version}
BuildArch:      noarch

%description data-tracks
Tracks for package VDrift.

Included tracks: Bahrain, Estoril88, Hungaro Ring, Jerez, Monaco,
Monza, Paul Ricard, Vir, ...

%lang_package

%prep
%setup -q -n vdrift
%patch0 -p1
%if 0%{?suse_version} > 1320
%patch1 -p0
%endif

find . -name "*.bak" -delete

%build
scons revision="exported" \
  prefix=%{_prefix} \
  release=1 \
  verbose=1 \
  minimal=0 \
  use_binreloc=0 \
  NLS=1 \
  datadir=share/vdrift/data \
  localedir=share/locale

%install
scons install prefix=%{_prefix} destdir=%{buildroot} bindir=bin

install -Dm644 vdrift.desktop %{buildroot}%{_datadir}/applications/vdrift.desktop

install -Dm644 data/textures/icons/vdrift-16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/vdrift.png
install -Dm644 data/textures/icons/vdrift-32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/vdrift.png
install -Dm644 data/textures/icons/vdrift-64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/vdrift.png

install -Dm644 vdrift.appdata.xml %{buildroot}%{_datadir}/appdata/vdrift.appdata.xml
%suse_update_desktop_file %{name}

%find_lang %{name}
%fdupes %{buildroot}%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(0644, root, root, 0755)
%doc LICENSE README.md
%attr(0755,-,-) %{_bindir}/%{name}
%dir %{_datadir}/vdrift
%dir %{_datadir}/vdrift/data/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/vdrift.png
%dir %{_datadir}/appdata/
%{_datadir}/appdata/vdrift.appdata.xml

%files data
%defattr(0644, root, root, 0755)
%{_datadir}/vdrift/data/*
%exclude %{_datadir}/vdrift/data/car*
%exclude %{_datadir}/vdrift/data/track*

%files data-cars
%defattr(0644, root, root, 0755)
%{_datadir}/vdrift/data/cars/
%{_datadir}/vdrift/data/carparts/

%files data-tracks
%defattr(0644, root, root, 0755)
%{_datadir}/vdrift/data/tracks/
%{_datadir}/vdrift/data/trackparts/

%files lang -f %{name}.lang

%changelog
