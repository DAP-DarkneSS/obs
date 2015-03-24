#
# spec file for package smplayer-qt5
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           smplayer-qt5
Version:        14.9.0.6690
Release:        0
Summary:        Complete frontend for MPV
License:        GPL-2.0+
Group:          Productivity/Multimedia/Video/Players
Url:            http://smplayer.sourceforge.net/
Source:         http://downloads.sf.net/%{name}/smplayer-%{version}.tar.bz2
Patch1:         smplayer-makeflags.patch
Patch2:         smplayer-default_ao.patch
Patch3:         smplayer-default_mpv.patch
Patch4:         smplayer-simple-resize.patch
# FIX-UPSTREAM to play network shared video correctly: #PM-48
Patch5:         smplayer-add_kde_protocols_to_desktop_file.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libstdc++-devel
BuildRequires:  make
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
# Either mpv >= 0.6.2 or MPlayer >= 1.0rc4_r32607.
Requires:       mpv >= 0.6.2
Recommends:     smplayer-lang = %{version}
Recommends:     smplayer-skins
Suggests:       smplayer-themes
Provides:       smplayer-core = %{version}
Conflicts:      smplayer
%if 0%{?suse_version} > 1310
BuildRequires:  libQt5Gui-private-headers-devel
%else
BuildRequires:  libqt5-qtbase-private-headers-devel
%endif

%description
SMPlayer intends to be a complete front-end for MPV/MPlayer, from
basic features like playing videos, DVDs, and VCDs to more
advanced features like support for MPV filters and more.

One of the most interesting features of SMPlayer: it remembers the
settings of all files you play. So you start to watch a movie but
you have to leave... don't worry, when you open that movie again it
will resume at the same point you left it, and with the same
settings: audio track, subtitles, volume...

%lang_package

%prep
%setup -q -n smplayer-%{version}
%patch1
%patch2
sed -e '/^+\{3\}/!d;s|^+\{3\} \([^ ]*\).*$|\1|' < %{PATCH2} | xargs sed -i 's/@@DEFAULT@@/pulse/g'
%patch3
%patch4
%patch5

# Fix CRLF in .txt files.
sed -i 's/\r$//' *.txt

find . -type f -name '*.pro' | while read f; do
cat <<EOF >>"$f"

QMAKE_CFLAGS = %{optflags}
QMAKE_CXXFLAGS = %{optflags}

EOF
done

%build
make \
  QMAKE_OPTS=DEFINES+=NO_DEBUG_ON_CONSOLE \
  MAKEFLAGS="%{?_smp_mflags}"             \
  CONF_PREFIX=""                          \
  PREFIX=%{_prefix}                       \
  DOC_PATH=%{_docdir}/%{name}             \
  QMAKE=%{_libqt5_bindir}/qmake           \
  LRELEASE=%{_libqt5_bindir}/lrelease

%install
%make_install \
  PREFIX=%{_prefix}                       \
  DOC_PATH=%{_docdir}/%{name}             \
  QMAKE=%{_libqt5_bindir}/qmake           \
  LRELEASE=%{_libqt5_bindir}/lrelease

rm -rf %{buildroot}%{_docdir}/%{name}/*

# Append Qt;KDE; categories in desktop files – fix for #PM-48.
for desktop in smplayer smplayer_enqueue; do
    %suse_update_desktop_file -r "$desktop" Qt AudioVideo Video Player
done
%find_lang smplayer --with-qt

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc Changelog *.txt
%{_bindir}/smplayer
%{_datadir}/applications/smplayer.desktop
%{_datadir}/applications/smplayer_enqueue.desktop
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/smplayer.*
%dir %{_datadir}/smplayer/
%{_datadir}/smplayer/shortcuts/
%{_datadir}/smplayer/input.conf
%{_mandir}/man1/smplayer.1%{ext_man}

%files lang -f smplayer.lang
%defattr(-,root,root)
%dir %{_datadir}/smplayer/translations/

%changelog
