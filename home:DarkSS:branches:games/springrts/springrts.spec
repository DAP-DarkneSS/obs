#
# spec file for package springrts
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

%define relto() $(realpath --relative-to %{_prefix} %{1})
%define libunitsyncSONAME 1
%define _version 103.0
Name:           springrts
Version:        0.%{_version}
Release:        0
Summary:        A full 3D open source RTS game engine
License:        GPL-2.0+
Group:          Amusements/Games/Strategy/Real Time
Url:            http://springrts.com
Source:         https://springrts.com/dl/buildbot/default/master/%{_version}/source/spring_%{_version}_src.tar.lzma
# PATCH-FIX-UPSTREAM fix-cmake.patch -- https://springrts.com/mantis/view.php?id=5329
Patch0:         fix-cmake.patch
# PATCH-FIX-OPENSUSE fix-random-return.patch -- https://springrts.com/mantis/view.php?id=5328
Patch1:         fix-random-return.patch
BuildRequires:  asciidoc
## we choose the gold linker for build
BuildRequires:  binutils-gold
BuildRequires:  boost-devel >= 1.52
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  p7zip
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-engine = %{version}
Requires:       libunitsync = %{version}
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
Recommends:     springlobby
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  libxslt-tools

%description
Spring is an open source game engine that supports 3D multiplayer gameplay,
mods & being capable of loading the content of the game Total Annihilation.

This package includes no maps, mods or a multiplayer client. Download SpringLobby
to get the multiplayer client which can be used for singleplayer, too. Maps and
mods are available via springlobby's p2p system or community websites.

%package gamedata
Summary:        Game releated files
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name}-engine = %{version}
BuildArch:      noarch

%description gamedata
Game related files for the open source rts game engine spring.

%package engine-default
Summary:        Meta package for the spring game engine
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name}-gamedata = %{version}

%description engine-default
Installs all spring engine related files and the gamedata.

%package engine-dedicated
Summary:        Dedicated server for the spring game engine
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name}-gamedata = %{version}

%description engine-dedicated
A dedicated server for the open source rts game engine spring.

%package engine-headless
Summary:        Spring without graphics
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name}-gamedata = %{version}

%description engine-headless
The Spring version without a GUI.

%package -n libunitsync
Summary:        A library for Spring
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name}-gamedata = %{version}

%description -n libunitsync
Utility library for Spring.

## meta packages

%package engine
Summary:        Metapackage default and mutlithreaded
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name}-engine-default = %{version}
BuildArch:      noarch

%description engine
Metapackage for the default components of springrts including the multithreaded version of Spring.

%package pr-downloader_shared
Summary:        Maps/Mod Downloader for Spring
Group:          Amusements/Games/Strategy/Real Time

%description pr-downloader_shared
Tool to download maps and games for the Spring engine.

%prep
%setup -q -n spring_%{_version}
%patch0 -p1
%patch1 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RELWITHDBGINFO \
      -DAI_LIBS_DIR=%{relto %{_libdir}/spring} \
      -DLIBDIR=%{_lib} \
      -DDOCDIR=%{relto %{_docdir}/%{name}} \
%if %{?suse_version} > 1320
      -DLTO=ON \
%endif
      -DDATADIR="%{relto %{_datadir}/%{name}}"
make %{?_smp_mflags}

%install
%cmake_install
%fdupes %{buildroot}

%post engine
%mime_database_post
%desktop_database_post

%postun engine
%desktop_database_postun
%mime_database_postun

%post -n %{name}-engine-default -p /sbin/ldconfig
%postun -n %{name}-engine-default -p /sbin/ldconfig
%post -n libunitsync -p /sbin/ldconfig
%postun -n libunitsync -p /sbin/ldconfig

%files engine
%defattr(-,root,root)
%{_datadir}/applications/spring.desktop
%{_datadir}/mime/packages/spring.xml
%{_datadir}/pixmaps/application-x-spring-demo.png
%{_datadir}/pixmaps/spring.png
%{_mandir}/man6/spring-legacy.6%{ext_man}

%files gamedata
%defattr(-,root,root)
%{_datadir}/%{name}

%files engine-default
%defattr(-,root,root)
%{_bindir}/spring
%{_libdir}/spring
%{_mandir}/man6/spring.6%{ext_man}

%files engine-dedicated
%defattr(-,root,root)
%{_bindir}/spring-dedicated
%{_mandir}/man6/spring-dedicated.6%{ext_man}

%files engine-headless
%defattr(-,root,root)
%{_bindir}/spring-headless
%{_mandir}/man6/spring-headless.6%{ext_man}

%files -n libunitsync
%defattr(-,root,root)
%{_libdir}/libunitsync.so

%files pr-downloader_shared
%defattr(-,root,root)
%{_bindir}/pr-downloader

%changelog
