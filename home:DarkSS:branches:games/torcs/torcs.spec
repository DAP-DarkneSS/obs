#
# spec file for package torcs
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           torcs
Summary:        The Open Racing Car Simulator
License:        GPL-2.0+
Group:          Amusements/Games/3D/Race
Version:        1.3.5
Release:        0
Url:            http://torcs.sourceforge.net
Source:         http://downloads.sourceforge.net/%{name}/all-in-one/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  plib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(vorbis)

%description
A 3D racing car simulator using OpenGL, which includes highly trained,
computer programmed driver opponents.

%prep
%setup -q

%build
export SUSE_ASNEEDED=0
%configure
# don't use parallel build
make

%install
make install DESTDIR=%{buildroot}
make datainstall DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications/
cp torcs.desktop %{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp torcs.xpm %{buildroot}%{_datadir}/pixmaps/
cp icon.png %{buildroot}%{_datadir}/pixmaps/torcs.png

desktop-file-edit %{buildroot}%{_datadir}/applications/%{name}.desktop --remove-category=Application --add-category=Simulation --set-icon=torcs

chmod +x %{buildroot}%{_datadir}/games/torcs/telemetry/telemetry.sh

%fdupes %{buildroot}%{_datadir}

find %{buildroot}%{_prefix} -exec chmod go-w {} \;

%files
%defattr(-, root, root)
%doc README
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/games/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
