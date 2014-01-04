#
# spec file for package monsterz
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


Name:           monsterz
Version:        0.7.1
Release:        0
Summary:        A little addictive puzzle game
License:        SUSE-WTFPL-2.0
Group:          Amusements/Games/Board/Puzzle
Url:            http://sam.zoy.org/projects/monsterz

Source:         http://sam.zoy.org/monsterz/monsterz-%{version}.tar.gz
#gw Debian man page
Source1:        monsterz.1
# PATCH-FIX-OPENSUSE really from original Mageia package.
Patch0:         monsterz-fix-crash-x86_64.patch
# PATCH-FIX-OPENSUSE also from original Mageia package.
#gw from Debian, fix crash on start (bug #49431)
Patch1:         020_fix_blit_crash.diff

BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
# libmikmod might be installed to prevent runtime startup error.
Requires:       libmikmod
Requires:       python-pygame
BuildArch:      noarch


%description
Monsterz is a little puzzle game, similar to the famous Bejeweled or Zookeeper.

The goal of the game is to create rows of similar monsters, either horizontally
or vertically. The only allowed move is the swap of two adjacent monsters, on
the condition that it creates a row of three or more. When alignments are
cleared, pieces fall from the top of the screen to fill the board again. Chain
reactions earn you even more points.

This game is mostly about luck, but it remains highly addictive. You have been
warned.


%prep
%setup -q
%patch0
%patch1 -p1


%build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -R monsterz.py graphics/ sound/ %{buildroot}/%{_datadir}/%{name}

mkdir -p %{buildroot}/%{_bindir}/

cat > %{buildroot}/%{_bindir}/%{name} <<EOF
#!/bin/bash
exec python %{_datadir}/%{name}/monsterz.py
EOF

chmod 755 %{buildroot}/%{_bindir}/%{name}

install -D graphics/logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name} %{name} "A little addictive puzzle game" %{name} %{name} "Game;BlocksGame;"

install -D %{SOURCE1} %{buildroot}%{_mandir}/man6/%{name}.6

%fdupes -s %{buildroot}%{_datadir}


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README TODO
%{_datadir}/%{name}/
%{_bindir}/%{name}
%doc %attr(644,root,root) %{_mandir}/man6/%{name}.6*
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.png

%changelog
