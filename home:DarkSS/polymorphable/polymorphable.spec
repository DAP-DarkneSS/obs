#
# spec file for package polymorphable
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           polymorphable
Version:        0.18
Release:        0
License:        CC-BY-SA-3.0
Summary:        A total conversion, orthographic game based on Clint Bellanger's FLARE
Url:            http://polymorphable.sf.net/
Group:          Amusements/Games/RPG
Source0:        https://github.com/makrohn/polymorphable/archive/flare%{version}_mod_only.tar.gz

BuildRequires:  fdupes
BuildRequires:  flare-data
BuildRequires:  update-desktop-files
Requires:       flare >= %{version}
Requires:       flare-data >= %{version}
# Requires:       flare-engine >= %%{version}
# Provides:       flare-game = %%{version}
BuildArch:      noarch

%description
Originally created for the 2012 Liberated Pixel Cup, this game is based upon
Clint Bellanger's FLARE engine. Our goal is to create a game which draws upon
several different classics in the genre, with a heavy emphasis on
polymorphable main character. Laurelia's Polymorphable Citizen (or just
Polymorphable for short) is an action-rpg based on the Flare engine. We're
aiming a little more towards an 8-bit adventure classic feel, only with more
RPG aspects (ie. attribute choices on level up!) The core mechanic in
Polymorphable is using different talismans to polymorph into different forms
so you can reach different areas. Imagine being blocked by a pit, so you
transform into a bat to fly across. Or perhaps there's a wall of fire in
front of you, so you turn into ghost form to phase right through.

%prep
%setup -q -n polymorphable-flare0.18_mod_only
rm mods/%{name}/*/*~

%build

%install
mkdir -p %{buildroot}/%{_datadir}/games/%{name}
cp -R mods %{buildroot}/%{_datadir}/games/%{name}

mkdir -p %{buildroot}%{_bindir}
echo -e '#!/bin/sh'"\n\nflare --game_data=%{_datadir}/games/%{name} --game=%{name}" > %{buildroot}%{_bindir}/%{name}

%suse_update_desktop_file -c %{name} "Polymorphable" "Laurelia-s Polymorphable Citizen" %{name} "%{_datadir}/games/%{name}/mods/%{name}/images/portraits/female01.png" "Game;RolePlaying;"

%fdupes -s %{buildroot}%{_datadir}/games/%{name}/mods

ln -s %{_datadir}/games/flare/mods/default %{buildroot}%{_datadir}/games/%{name}/mods/default

%files
%defattr(-,root,root)
%doc AUTHORS.txt cc-by-sa-3.0.txt README.md
%{_datadir}/games/%{name}
%{_datadir}/applications/%{name}.desktop
%attr(755,root,root) %{_bindir}/%{name}

%changelog
