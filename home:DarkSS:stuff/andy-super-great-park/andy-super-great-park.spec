#
# spec file for package andy-super-great-park
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
Version:        1.0.7
Release:        0
License:        GPL-2.0+
Summary:        %{pack_summ} — binary files
Url:            http://www.stuff-o-matic.com/asgp/
Group:          Amusements/Games/Other

Source0:        %{name}-%{version}.tar.gz
# FEATURE-OPENSUSE to prevent warnings: string list key "MimeType" in group
# "Desktop Entry" does not have a semicolon (';') as trailing character.
Patch1:         desktop-mimetype-semicolon.patch
# FIX-UPSREAM vs. black window.
Patch2:         fix-window-size.patch

BuildRequires:  Mesa-libGL-devel
BuildRequires:  boost-devel <= 1.49.0
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libxslt-tools
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
Requires:       %{name}-data = %{version}
# Cmake suggests it but "parser error" will be got.
BuildConflicts: docbook2x

%description
%{pack_desc}


%package        -n bear-factory
License:        GPL-2.0+ and CC-BY-SA-3.0
Summary:        Editors for Plee the Bear & Andy's Super Great Park

%description    -n bear-factory
This package includes the level editor, animation editor and model editor
of the Bear Engine for Plee the Bear & Andy's Super Great Park.


%package        data
License:        CC-BY-SA-3.0
Summary:        %{pack_summ} — art and other architecture independent data
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%{pack_desc}


%prep
%setup -q
%patch1
%patch2


%build
cmake  . \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_NO_BUILTIN_CHRPATH=ON \
        -DCMAKE_C_FLAGS="-DNDEBUG %{optflags}" \
        -DCMAKE_CXX_FLAGS="-DNDEBUG %{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DRP_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib}/%{name} \
        -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib}/%{name} \
        -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib} \
        -DBEAR_USES_FREEDESKTOP=1
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

# Translations
%find_lang super-great-park
%find_lang bear-engine
cat bear-engine.lang >>super-great-park.lang
%find_lang bear-factory

# Menu entries
%suse_update_desktop_file -r bf-animation-editor 'Game;PlatformGame;'
%suse_update_desktop_file -r bf-level-editor     'Game;PlatformGame;'
%suse_update_desktop_file -r bf-model-editor     'Game;PlatformGame;'
%suse_update_desktop_file -r desc2img            'Game;PlatformGame;'

chrpath --delete %{buildroot}%{_bindir}/bend-image

# Removing obsoleted and forgotten binary file.
rm %{buildroot}%{_bindir}/running-bear

%fdupes -s %{buildroot}%{_datadir}/super-great-park
%fdupes -s %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps


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


%post -n bear-factory -p /sbin/ldconfig

%postun -n bear-factory -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}
%doc asgp/LICENSE asgp/license/*

%files data -f super-great-park.lang
%defattr(-,root,root)
%{_datadir}/super-great-park
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/asgp.png
%{_datadir}/pixmaps/asgp.*
%dir %{_datadir}/bear-factory
%{_datadir}/bear-factory/super-great-park

%files -n bear-factory -f bear-factory.lang
%defattr(-,root,root)
%{_libdir}/libbear-editor.so
%{_bindir}/bend-image
%{_bindir}/bf*editor
%dir %{_datadir}/bear-factory
%{_datadir}/bear-factory/images
%{_datadir}/bear-factory/item-description
%{_datadir}/applications/bf*editor.desktop
%{_datadir}/applications/desc2img.desktop
%{_datadir}/icons/hicolor/*/apps/bear-factory.png
%{_datadir}/pixmaps/bear-factory*
%doc bear/LICENSE bear/license/* bear/README.md


%changelog
