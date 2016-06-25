#
# spec file for package torcs
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


Name:           torcs
Summary:        The Open Racing Car Simulator
License:        GPL-2.0+
Group:          Amusements/Games/3D/Race
Version:        1.3.7
Release:        0
Url:            http://torcs.sourceforge.net
Source:         http://downloads.sourceforge.net/%{name}/all-in-one/%{version}/%{name}-%{version}.tar.bz2
Source4:        accc.1
Source5:        nfs2ac.1
Source6:        nfsperf.1
Source7:        texmapper.1
Source8:        torcs.1
Source9:        trackgen.1
# PATCH-FIX-OPENSUSE to prevent error: 'isnan' was not declared in this scope.
Patch0:         torcs-1.3.7-isnan.patch

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  plib-devel
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(vorbis)
Requires:       %{name}-data = %{version}

%description
A 3D racing car simulator using OpenGL, which includes highly trained,
computer programmed driver opponents.

%package data
Summary:        Data files for TORCS
Group:          Amusements/Games/Action/Race
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Architecture independent data files for The Open Racing Car Simulator.

%prep
%setup -q
%patch0 -p1

%build
export SUSE_ASNEEDED=0
%configure
# WARNING: don't use parallel build because of compiling fatal errors.
make V=1

%install
make V=1 install DESTDIR=%{buildroot}
make V=1 datainstall DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications/
cp torcs.desktop %{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp torcs.xpm %{buildroot}%{_datadir}/pixmaps/
cp icon.png %{buildroot}%{_datadir}/pixmaps/torcs.png

desktop-file-edit %{buildroot}%{_datadir}/applications/%{name}.desktop --remove-category=Application --add-category=Simulation --set-icon=torcs

chmod +x %{buildroot}%{_datadir}/games/torcs/telemetry/telemetry.sh

%fdupes %{buildroot}%{_datadir}

find %{buildroot}%{_prefix} -exec chmod go-w {} \;

rm -rf %{buildroot}/%{_datadir}/games/%{name}/COPYING

mkdir -p %{buildroot}%{_mandir}/man1
cd %{_sourcedir}
for MANPAGE in *.1; do
gzip -c9 $MANPAGE | tee -a %{buildroot}%{_mandir}/man1/$MANPAGE.gz
done

%files
%defattr(-, root, root)
%doc COPYING README
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%files data
%defattr(-, root, root)
%{_datadir}/games/%{name}

%changelog
