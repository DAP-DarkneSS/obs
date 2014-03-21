#
# spec file for package sumwars
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Asterios Dramis <asterios.dramis@gmail.com>.
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


Name:           sumwars
Version:        0.5.7+hg.2014.03.17
Release:        0
Summary:        Summoning Wars Role-Playing Game
License:        GPL-3.0+
Group:          Amusements/Games/RPG
Url:            http://www.sumwars.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2

BuildRequires:  boost-devel
BuildRequires:  cmake
%if 0%{?suse_version} > 1210
BuildRequires:  dejavu-fonts
%else
BuildRequires:  dejavu
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  freealut-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libOIS-devel
BuildRequires:  libOgreMain-plugins
BuildRequires:  libcegui-devel
BuildRequires:  libenet-devel
BuildRequires:  libogg-devel
BuildRequires:  libphysfs-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  pkg-config
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(OGRE)
BuildRequires:  pkgconfig(OGRE-Paging)
BuildRequires:  pkgconfig(OGRE-Property)
BuildRequires:  pkgconfig(OGRE-RTShaderSystem)
BuildRequires:  pkgconfig(OGRE-Terrain)
BuildRequires:  pkgconfig(lua) < 5.2
BuildRequires:  pkgconfig(lua) >= 5.1
BuildRequires:  pkgconfig(xrandr)
Requires:       %{name}-data = %{version}
Requires:       libOgreMain-plugins
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Summoning Wars is an open source role-playing game, featuring both a
single-player and a multiplayer mode for about 2 to 8 players.

%package data
Summary:        Summoning Wars Role-Playing Game
License:        CC-BY-SA-3.0
Group:          Amusements/Games/RPG
Requires:       %{name} = %{version}
%if 0%{?suse_version} > 1210
Requires:       dejavu-fonts
%else
Requires:       dejavu
%endif
BuildArch:      noarch

%description data
Summoning Wars is an open source role-playing game, featuring both a
single-player and a multiplayer mode for about 2 to 8 players.

%prep
%setup -q

# Make sure bundled libraries are not used
rm -rf src/enet/
rm -rf src/tinyxml/

%build
mkdir build
cd build
cmake ../ \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DSUMWARS_DOC_DIR=%{_docdir}/%{name} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_CXX_FLAGS="%{optflags} -fno-strict-aliasing" \
    -DSUMWARS_NO_TINYXML=ON \
    -DSUMWARS_NO_ENET=ON \
    -DSUMWARS_BUILD_TOOLS=OFF
make %{?_smp_mflags} VERBOSE=1
cd ..

%install
cd build
%make_install
cd ..

# Use system-wide dejavu sans and serif fonts
rm -f %{buildroot}/%{_datadir}/%{name}/resources/gui/fonts/DejaVuSans.ttf
ln -s %{_datadir}/fonts/truetype/DejaVuSans.ttf %{buildroot}/%{_datadir}/%{name}/resources/gui/fonts
rm -f %{buildroot}/%{_datadir}/%{name}/resources/gui/fonts/DejaVuSerif.ttf
ln -s %{_datadir}/fonts/truetype/DejaVuSerif.ttf %{buildroot}/%{_datadir}/%{name}/resources/gui/fonts

# Install additional docs
install -pm 0644 Changelog.txt %{buildroot}/%{_docdir}/%{name}/

# Install icons
for i in 16 24 32 48 64 128; do
  install -D "share/icon/SumWarsIcon_${i}x${i}.png" \
  "%{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png"
done

# Fix and install desktop file
%if 0%{?suse_version} > 1210
desktop-file-edit --set-key=TryExec --set-value=sumwars --set-key=Exec --set-value=sumwars --set-icon=sumwars packaging/sumwars.desktop
desktop-file-install packaging/sumwars.desktop
%else
sed -i "s/Exec=\/usr\/games\/sumwars/Exec=sumwars/" packaging/sumwars.desktop
sed -i "s/Icon=\/usr\/share\/icons\/hicolor\/128x128\/sumwars.png/Icon=sumwars/" packaging/sumwars.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications packaging/sumwars.desktop
%endif

%fdupes -s %{buildroot}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%dir %{_datadir}/%{name}/translation/
%lang(de) %{_datadir}/%{name}/translation/de/
%lang(en) %{_datadir}/%{name}/translation/en/
%lang(es) %{_datadir}/%{name}/translation/es/
%lang(it) %{_datadir}/%{name}/translation/it/
%lang(pl) %{_datadir}/%{name}/translation/pl/
%lang(pt) %{_datadir}/%{name}/translation/pt/
%lang(ru) %{_datadir}/%{name}/translation/ru/
%lang(uk) %{_datadir}/%{name}/translation/uk/
%doc %{_docdir}/%{name}/

%files data
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/data/
%{_datadir}/%{name}/resources/

%changelog
