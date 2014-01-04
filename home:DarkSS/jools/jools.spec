#
# spec file for package jools
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


Name:           jools
Version:        0.20
Release:        0
Summary:        A graphical addictive puzzle game
License:        GPL-2.0+
Group:          Amusements/Games/Board/Puzzle
Url:            http://www.pygame.org/projects/21/72/

Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-sys.patch
Patch1:         %{name}-%{version}-sharegames.patch

BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
Requires:       python-pygame
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch


%description
Jools is a graphical puzzle game in the tradition of Tetris.
In a nutshell, the goal is to swap adjacent jools (jewels) within a grid,
in order to create rows of three or more of a kind.
These jools will then disappear, and more will fall to fill their places.
Jools features nifty 3D rendered graphics.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
dos2unix doc/detonate.txt


%build
python \
       setup.py \
       build

%install
python \
       setup.py \
       install \
       -O1 \
       --skip-build \
       --root=%{buildroot} \
       --prefix=%{_prefix}

rm -rf %{buildroot}%{_datadir}/doc
find %{buildroot} -name '.arch-ids' -o -name '.placeholder' -o -name '.id' | xargs rm -rf

install -D jools/images/emerald/0001.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name} %{name} "A graphical addictive puzzle game" %{name} %{name} "Game;BlocksGame;"

%fdupes -s %{buildroot}
chmod +x %{buildroot}%{python_sitelib}/%{name}/__init__.py


%files
%defattr(-,root,root,755)
%doc COPYING ChangeLog README doc/*
%{_bindir}/%{name}
%{python_sitelib}/%{name}-*.egg-info
%{python_sitelib}/%{name}
%{_datadir}/games/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
