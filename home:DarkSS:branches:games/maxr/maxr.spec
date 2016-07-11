#
# spec file for package maxr
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009 oc2pus
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


Name:           maxr
Version:        0.2.9
Release:        0
Summary:        M.A.X.R. (Mechanized Assault and eXploration Reloaded)
License:        GPL-2.0+ and CC-BY-SA-3.0
Group:          Amusements/Games/Strategy/Turn Based
Url:            http://www.maxr.org/
Source0:        http://www.maxr.org/downloads/%{name}-%{version}.tar.gz
Source2:        http://www.maxr.org/downloads/manual.pdf
Source9:        %{name}.6
# PATCH-FIX-OPENSUSE vs. W: file-contains-date-and-time /usr/bin/maxr
Patch0:         maxr-date-time.diff

BuildRequires:  cmake >= 3
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(sdl2)
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
M.A.X.R. (Mechanized Assault and eXploration Reloaded) is a
fanmade strategy game by the community of maxr.org. MAXR is
OpenSource and a remake of the old M.A.X.by Interplay from 1996
featuring network games based on TCP/IP (e.g. over the internet).

The game can be played in a turn-based mode (with or without time
limit), or simultaneous mode (all the players take their turns at
the same time), and features combat in air, land, and sea. Three
resources are present on the maps - Raw Materials, which are
needed to manufacture units, structures and ammunition, Fuel,
which power generators need to function, and Gold, which is
used to purchase upgrades. This game is a mix of realtime and
turnbased strategy with battle chess character.

%prep
%setup -q -n%{name}-%{version}
%patch0
find -name '.empty' -delete -print
dos2unix data/AUTHORS data/CHANGELOG data/MANUAL
install -m 644 %{SOURCE2} .

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
make V=1 %{?_smp_mflags}

%install
%cmake_install
# icon
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 data/%{name}.png %{buildroot}%{_datadir}/pixmaps
# menu
install -dm 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
#Encoding=UTF-8
Type=Application
Exec=%{name}
Icon=%{name}
Terminal=false
Name=M.A.X.R. (Mechanized Assault and eXploration Reloaded)
GenericName=M.A.X.R. (Mechanized Assault and eXploration Reloaded)
Comment=M.A.X.R. (Mechanized Assault and eXploration Reloaded)
EOF
%suse_update_desktop_file %{name} Game StrategyGame
%fdupes -s %{buildroot}
# man
mkdir -p %{buildroot}%{_mandir}/man6
cp %{SOURCE9} %{buildroot}%{_mandir}/man6
# Let's use %%doc macro for:
cd %{buildroot}/%{_datadir}/%{name}
rm ABOUT AUTHORS CHANGELOG COPYING* MANUAL

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root,-)
%doc README.md manual.pdf data/ABOUT data/AUTHORS
%doc data/CHANGELOG data/COPYING* data/MANUAL
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.6.*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
