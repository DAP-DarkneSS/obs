#
# spec file for package andy-super-great-park
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


%define pack_summ 2D platform game

%define pack_desc Andy's Super Great Park is an original game with an \
inventive and easy to learn gameplay, where every action can be simply \
done with a mouse. Challenge your reflexes and your dexterity in this \
adventure of 25 to 43 levels, punctuated by amazing boss fights. \
\
Through 25 main levels, you will have to retrieve a minimum number of \
balloons using your plunger gun while avoiding collisions with the \
obstacles dropped on the path (explosive zeppelins, crates, TNT…). \
Try to get the best scores and unlock up to 18 extra levels! \
\
Grabbing balloons with a plunger gun, shooting birds with a cannon and \
exploding everything else, all while riding a roller coaster: this is \
Andy's Super Great Park!

Name:           andy-super-great-park
Version:        1.0.8
Release:        0
Summary:        %{pack_summ} — binary files
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://www.stuff-o-matic.com/asgp/
Source0:        http://www.stuff-o-matic.com/asgp/download/download.php?platform=source#/%{name}-%{version}.tar.gz
Source5:        bend-image.6
Source6:        bf-animation-editor.6
Source7:        bf-level-editor.6
Source8:        bf-model-editor.6
Source9:        andy-super-great-park.6
# PATCH-FIX-UPSTREAM vs. build failure via gcc6, see more at bottom of
# https://github.com/j-jorge/bear/commit/52f9f4f6816e8dbb7c959167678eb
Patch0:         andy-super-great-park-1.0.8-gcc6-c++11.diff

BuildRequires:  boost-devel
BuildRequires:  chrpath
BuildRequires:  cmake >= 3
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libxslt-tools
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(gl)
Requires:       %{name}-data = %{version}
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
# Cmake suggests it but "parser error" will be got.
BuildConflicts: docbook2x

%description
%{pack_desc}

%package        -n bear-factory
Summary:        Editors for Plee the Bear & Andy's Super Great Park
License:        GPL-2.0+ and CC-BY-SA-3.0
Group:          Amusements/Games/Action/Arcade

%description    -n bear-factory
This package includes the level editor, animation editor and model editor
of the Bear Engine for Plee the Bear & Andy's Super Great Park.


%package        data
Summary:        %{pack_summ} — art and other architecture independent data
License:        CC-BY-SA-3.0
Group:          Amusements/Games/Action/Arcade
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%{pack_desc}

%prep
%setup -q
%patch0 -p1

%build
mkdir build && cd build
# WARNING: %%cmake breaks linking (undefined reference to boost).
cmake .. \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_NO_BUILTIN_CHRPATH=ON \
        -DCMAKE_C_FLAGS="-DNDEBUG %{optflags}" \
        -DCMAKE_CXX_FLAGS="-DNDEBUG %{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DRP_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib}/%{name} \
        -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib}/%{name} \
        -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib} \
        -DBEAR_USES_FREEDESKTOP=1
make V=1 %{?_smp_mflags}

%install
%cmake_install

# Translations
%find_lang super-great-park
%find_lang bear-engine
cat bear-engine.lang >>super-great-park.lang
%find_lang bear-factory

# Menu entries
%suse_update_desktop_file -r bf-animation-editor 'Game;ArcadeGame;'
%suse_update_desktop_file -r bf-level-editor     'Game;ArcadeGame;'
%suse_update_desktop_file -r bf-model-editor     'Game;ArcadeGame;'
%suse_update_desktop_file -r desc2img            'Game;ArcadeGame;'

chrpath --delete %{buildroot}%{_bindir}/bend-image

%fdupes -s %{buildroot}%{_datadir}/super-great-park
%fdupes -s %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{_mandir}/man6
cd %{_sourcedir}
for MANPAGE in *.?; do
cp $MANPAGE %{buildroot}%{_mandir}/man`echo "$MANPAGE" | grep -o '[0-9]*'`
done

%post
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post

%postun
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun

%post -n bear-factory -p /sbin/ldconfig

%postun -n bear-factory -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.*
%{_libdir}/%{name}
%doc asgp/LICENSE asgp/license/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/asgp.png
%{_datadir}/pixmaps/asgp.*

%files data -f super-great-park.lang
%defattr(-,root,root)
%{_datadir}/super-great-park
%dir %{_datadir}/bear-factory
%{_datadir}/bear-factory/super-great-park

%files -n bear-factory -f bear-factory.lang
%defattr(-,root,root)
%{_libdir}/libbear-editor.so
%{_bindir}/b*
%{_mandir}/man6/b*.6.*
%dir %{_datadir}/bear-factory
%{_datadir}/bear-factory/images
%{_datadir}/bear-factory/item-description
%{_datadir}/applications/bf*editor.desktop
%{_datadir}/applications/desc2img.desktop
%{_datadir}/icons/hicolor/*/apps/bear-factory.png
%{_datadir}/pixmaps/bear-factory*
%doc bear/LICENSE bear/license/* bear/README.md

%changelog
