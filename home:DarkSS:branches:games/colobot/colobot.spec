#
# spec file for package colobot
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define tarball_ver %{version}-alpha

Name:           colobot
Version:        0.1.9
Release:        0
Summary:        A real-time strategy game with programmable bots
License:        GPL-3.0+
Group:          Amusements/Games/Strategy/Real Time
Url:            http://colobot.info
Source0:        https://github.com/colobot/colobot/archive/colobot-gold-%{tarball_ver}.tar.gz

%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake >= 3
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++ >= 4.6
BuildRequires:  gettext >= 0.18
BuildRequires:  hicolor-icon-theme
BuildRequires:  libphysfs-devel
BuildRequires:  libpng-devel >= 1.2
BuildRequires:  po4a
BuildRequires:  rsvg-view
%if 0%{?suse_version} > 1320 || 0%{?suse_version} == 1315
BuildRequires:  update-desktop-files
%endif
BuildRequires:  xmlstarlet
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(glew) >= 1.8.0
BuildRequires:  pkgconfig(ogg) >= 1.3.0
BuildRequires:  pkgconfig(openal) >= 1.13
BuildRequires:  pkgconfig(sdl2) >= 2.0.4
BuildRequires:  pkgconfig(sndfile) >= 1.0.25
BuildRequires:  pkgconfig(vorbis) >= 1.3.2
Requires:       %{name}-data = %{version}
Recommends:     %{name}-lang
Recommends:     zenity
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

%description
And this is what made the game special in our childhood, or maybe even
early adulthood. Unlike most RTS games, Colobot does not require tactics,
but it does require thinking. An another difference would be the fact,
that we do not control the game from a 'god' camera, seeing everything
from up top, but instead, we are actually controlling each unit we make,
or find. This could potentially cause the problem, of not being able to
control 2 units at once, yet this is when an another twist comes in.
Colobot actually has its own interpretation of robot programming, which is
done fully by the player, together with a few hints and tips from the
trusty SatCom system. The programmed robots function at a level similar to
the brutality of writing an actual program, which does mean it requires
the right amount of accuracy, with the right mix of imagination.


%lang_package


%prep
%setup -q -n colobot-colobot-gold-%{tarball_ver}

%build
%cmake \
       -Wno-dev \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCOLOBOT_INSTALL_BIN_DIR:PATH=%{_bindir} \
       -DCOLOBOT_INSTALL_LIB_DIR:PATH=%{_libdir}
make V=1 %{?_smp_mflags}

%install
%cmake_install
%find_lang %{name} %{?no_lang_C}
%if 0%{?suse_version} > 1320 || 0%{?suse_version} == 1315
%suse_update_desktop_file -r %{name} 'Education;Engineering;Game;AdventureGame;StrategyGame;'
%endif

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc LICENSE.txt README.md
%{_bindir}/%{name}
%{_libdir}/libCBot.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man*/%{name}*
%{_mandir}/*/man*/%{name}*
%{_datadir}/games/colobot

%files lang -f %{name}.lang

%changelog
