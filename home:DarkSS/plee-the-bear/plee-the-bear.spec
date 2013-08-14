#
# spec file for package plee-the-bear
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
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           plee-the-bear
Version:        0.6.0
Release:        0
# Code and artwork respectively
License:        GPL-2.0+ and CC-BY-SA-3.0
Summary:        2D platform game
Url:            http://www.stuff-o-matic.com/ptb/
Group:          Amusements/Games/Other
Source0:        http://downloads.sourceforge.net/project/plee-the-bear/Plee%20the%20Bear/0.6/%{name}-%{version}.tar.gz

# There is probably a more appropriate C++ fix instead of using -fpermissive, but I don't know it.
Patch1:         plee-the-bear-0.6.0-fpermissive.patch
# Disable stupid & broken SVN revision checking
Patch2:         plee-the-bear-0.6.0-svnclawfix.patch
# Initial work taken from Debian, thanks to Konstantinos Margaritis <markos@genesi-usa.com>
Patch3:         plee-the-bear-boost-1.50-patch

BuildRequires:  -post-build-checks
BuildRequires:  SDL_mixer-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel

%description
Plee the Bear is a 2D platform game like those we found on consoles in the
beginning of the 90's. The basis of the scenario fit in few lines:

4 PM or so, Plee wakes up, tired. He has dreamed again about that awesome
period when he went across the entire world together with his belle. He
puts his leg in the honey pot... empty! Moreover every single honey pot in
the house is empty. "One more trick of that kid", he thinks. "I'm going to
give him such a wallop of which he sure will remember".

Following honey drops on the ground, Plee reaches the edge of the forest.
Beginning of the game.

The game is led by Julien Jorge and Sebastien Angibaud. Nevertheless, the
game counts several contributions from external people.


%prep
%setup -q
%patch1 -p1 -b .fpermissive
# %patch2 -p1 -b .svnclawfix
%patch3 -p1 -b .boost150

%build
cmake  . \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=FALSE \
        -DCMAKE_SKIP_RPATH=ON \
        -DCMAKE_C_FLAGS="-fpermissive %{optflags}" \
        -DCMAKE_CXX_FLAGS="-fpermissive %{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib} \
        -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} \
        -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib}
make %{?_smp_mflags} VERBOSE=1


%install
make install DESTDIR=%{buildroot} VERBOSE=1 INSTALL="install -p"

# Translations
%find_lang %{name}
%find_lang bear-factory
cat bear-factory.lang >>%{name}.lang
%find_lang bear-engine
cat bear-engine.lang >>%{name}.lang

%suse_update_desktop_file -r bf-animation-editor 'Game;PlatformGame;'
%suse_update_desktop_file -r bf-level-editor     'Game;PlatformGame;'
%suse_update_desktop_file -r bf-model-editor     'Game;PlatformGame;'
%suse_update_desktop_file -r plee-the-bear       'Game;PlatformGame;'

%fdupes -s %{buildroot}%{_datadir}/plee-the-bear
%fdupes -s %{buildroot}%{_datadir}/bear-factory

%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
/sbin/ldconfig
[ $1 = 0 ] || exit 0
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/*.so
%{_bindir}/*
%{_datadir}/plee-the-bear
%{_datadir}/bear-factory
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*
%doc CCPL COPYING GPL


%changelog
