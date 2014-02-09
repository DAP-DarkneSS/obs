#
# spec file for package tennix
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


Name:           tennix
Version:        1.1
Release:        0
Summary:        Tennis Game
License:        GPL-2.0+
Group:          Amusements/Games/Action/Other
Url:            http://icculus.org/tennix/
# http://icculus.org/tennix/downloads/tennix-%{version}.tar.gz
Source:         tennix-%{version}.tar.bz2
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         tennix-optflags.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch2:         tennix-archive-initialize-realloc.patch
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tennix is a 2D bird's-eye-view tennis game with single-player and multiplayer
modes. Its features include different weather conditions, day/night play at
several locations around the Earth and realistic physics, with the option to
write your own opponents in Python.

%prep
%setup -q
%patch1
%patch2 -p1

%build
make %{?_smp_mflags} \
    CC="g++" \
    PREFIX="%{_prefix}" \
    OPTFLAGS="%{optflags}" \
    USE_PYTHON=1 \
    DELUXE=1

%install
make \
    CC="g++" \
    PREFIX="%{_prefix}" \
    OPTFLAGS="%{optflags}" \
    USE_PYTHON=1 \
    DELUXE=1 \
    DESTDIR=%{buildroot} \
    install
%suse_update_desktop_file -r "%{name}" Game SportsGame

%files
%defattr(-,root,root)
%doc ChangeLog COPYING HACKING README TODO
%{_bindir}/tennix
%{_datadir}/games/tennix
%{_datadir}/icons/*
%{_datadir}/applications/tennix.desktop
%{_datadir}/pixmaps/tennix.png
%doc %{_mandir}/man6/tennix.6%{ext_man}

%changelog
