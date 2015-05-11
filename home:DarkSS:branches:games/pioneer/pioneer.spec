#
# spec file for package pioneer
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pioneer
Version:        20150509
Release:        0
Summary:        A game of lonely space adventure
License:        GPL-3.0
Group:          Amusements/Games/3D/Simulation
Url:            http://pioneerspacesim.net/
Source:         https://github.com/pioneerspacesim/%{name}/archive/%{version}.tar.gz
Source1:        pioneer.png
Source2:        pioneer.desktop
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(assimp) >= 3.0
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sigc++-1.2)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  hicolor-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       %{name}-data = %{version}

%description
Pioneer is a space adventure game set in our galaxy at the turn of the 31st century.

The game is open-ended, and you are free to eke out whatever kind of space-faring
existence you can think of. Look for fame or fortune by exploring the millions of
star systems. Turn to a life of crime as a pirate, smuggler or bounty hunter. Forge
and break alliances with the various factions fighting for power, freedom or self-
determination. The universe is whatever you make of it.

%package data
Summary:        Pioneer: art and other architecture independent data
Group:          Amusements/Games/3D/Simulation
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Pioneer is a space adventure game set in our galaxy at the turn of the 31st century.

%prep
%setup -q

%build
./bootstrap
%configure PIONEER_DATA_DIR=%{_datadir}/%{name}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -m0644 %{SOURCE1} "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/"

mkdir -p %{buildroot}%{_datadir}/applications
install -m0644 %{SOURCE2} "%{buildroot}%{_datadir}/applications"

find "%{buildroot}%{_datadir}/%{name}" -type f -name ".gitignore" -exec rm {} \;

%fdupes %{buildroot}%{_datadir}/%{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files data
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
