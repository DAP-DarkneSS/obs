#
# spec file for package plee-the-bear
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


%define pack_summ 2D platform game

%define pack_desc Plee the Bear is a 2D platform game like those we found \
on consoles in the beginning of the 90's. The basis of the scenario fit in \
few lines: \
\
4 PM or so, Plee wakes up, tired. He has dreamed again about that awesome \
period when he went across the entire world together with his belle. He \
puts his leg in the honey pot... empty! Moreover every single honey pot in \
the house is empty. "One more trick of that kid", he thinks. "I'm going to \
give him such a wallop of which he sure will remember". \
\
Following honey drops on the ground, Plee reaches the edge of the forest. \
Beginning of the game. \
\
The game is led by Julien Jorge and Sebastien Angibaud. Nevertheless, the \
game counts several contributions from external people.

Name:           plee-the-bear
Version:        0.7.0
Release:        0
Summary:        %{pack_summ} — binary files
License:        GPL-2.0+
Group:          Amusements/Games/Other
Url:            http://www.stuff-o-matic.com/ptb/
Source0:        plee-the-bear-%{version}.tar.gz
# http://www.stuff-o-matic.com/plee-the-bear/download/file.php?platform=source

BuildRequires:  SDL_mixer-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libxslt-tools
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(SDL2_mixer)
# Cmake suggests it but "parser error" will be got.
BuildConflicts: docbook2x

%description
%{pack_desc}

%package        data
Summary:        %{pack_summ} — art and other architecture independent data
License:        CC-BY-SA-3.0
Group:          Amusements/Games/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%{pack_desc}

%prep
%setup -q -n %{name}-%{version}-light

%build
cmake  . \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_NO_BUILTIN_CHRPATH=ON \
        -DCMAKE_C_FLAGS="-DNDEBUG %{optflags}" \
        -DCMAKE_CXX_FLAGS="-DNDEBUG %{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib}/%{name} \
        -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib}/%{name} \
        -DBEAR_EDITORS_ENABLED=False
make V=1 %{?_smp_mflags}

%install
make V=1 install DESTDIR=%{buildroot} INSTALL="install -p"

# Translations
%find_lang %{name}
%find_lang bear-engine
cat bear-engine.lang >>%{name}.lang

%suse_update_desktop_file -r plee-the-bear 'Game;PlatformGame;'

# W: non-executable-script
chmod +x %{buildroot}%{_datadir}/%{name}/gfx/title_screen/mk.sh
chmod +x %{buildroot}%{_datadir}/%{name}/gfx/forest/bk/*/mk.sh

%fdupes -s %{buildroot}%{_datadir}

%post
/sbin/ldconfig
%if 0%{?suse_version} >= 1140
%icon_theme_cache_post
%desktop_database_post
%else
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :
%endif

%postun
/sbin/ldconfig
%if 0%{?suse_version} >= 1140
%icon_theme_cache_postun
%desktop_database_postun
%else
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :
%endif

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}
%doc %{name}/LICENSE %{name}/README.md %{name}/license/*
%{_datadir}/applications/%{name}.desktop

%files data -f %{name}.lang
%defattr(-,root,root)
%{_datadir}/%{name}
%dir %{_datadir}/bear-factory
%{_datadir}/bear-factory/%{name}
%{_datadir}/icons/hicolor/*/apps/ptb.png
%{_datadir}/pixmaps/ptb.*
%{_datadir}/cmake/bear-engine

%changelog
