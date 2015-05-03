#
# spec file for package commandergenius
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


%define dotlessver 1811

Name:           commandergenius
Version:        1.8.1.1
Release:        0
Summary:        An open clone of the Commander Keen engines
License:        GPL-2.0
Group:          Amusements/Games/Action/Arcade
Url:            http://clonekeenplus.sf.net/

Source:         https://github.com/gerstrong/Commander-Genius/archive/v%{dotlessver}release.tar.gz
# PATCH-FIX-OPENSUSE to prevent useless rebuilds.
Patch0:         commandergenius-nocurrentdate.diff

BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image) >= 2.0.0
BuildRequires:  pkgconfig(vorbis)

%description
Clonekeen is a nearly complete reimplementation of the id Software
game "Commander Keen", with new features and enhancements, such as
2-player support, a built-in level editor and alternate game modes.

%prep
%setup -qn Commander-Genius-%{dotlessver}release
%patch0

%build
cmake . \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DAPPDIR=%{_bindir}
make V=1 %{?_smp_mflags}

%install
make V=1 install DESTDIR=%{buildroot}
install -D CGLogo.png %{buildroot}/%{_datadir}/pixmaps/CGLogo.png
# Let's use %%doc macro.
rm -rf %{buildroot}/%{_datadir}/games

%files
%defattr(-,root,root)
%attr(644,root,root) %doc COPYRIGHT README changelog.txt
%{_bindir}/CGeniusExe
%{_datadir}/applications/cgenius.desktop
%{_datadir}/pixmaps/CGLogo.png

%changelog
