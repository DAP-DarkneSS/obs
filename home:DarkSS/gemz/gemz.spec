#
# spec file for package gemz
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


Name:           gemz
Version:        0.97.0
Release:        0
Summary:        Another addictive puzzle game
License:        GPL-2.0
Group:          Amusements/Games/Board/Puzzle
Url:            http://sourceforge.net/projects/gemz/
Source0:        http://heanet.dl.sourceforge.net/project/gemz/gemz/Source/gemz-%{version}.tgz
# PATCH-FIX-OPENSUSE to prevent linking issue.
Patch0:         Makefile-LFLAGS.diff

BuildRequires:  fdupes
BuildRequires:  libSDL_image-devel
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%description
Gemz is an SDL implementation
of the popular puzzle game «Bejeweled.»


%prep
%setup -q
%patch0


%build
make V=1 %{?_smp_mflags} CFLAGS="%{optflags} `sdl-config --cflags`"

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a fonts gfx tilesets %{buildroot}%{_datadir}/%{name}

install -D %{name} %{buildroot}%{_bindir}/%{name}-bin

cat > %{buildroot}/%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec %{_bindir}/%{name}-bin
EOF

install -D gfx/jewel3.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name} %{name} "Another addictive puzzle game" %{name} %{name} "Game;BlocksGame;"

%fdupes -s %{buildroot}


%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
