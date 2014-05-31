#
# spec file for package smplayer
#
# Copyright (c) 2006-2012 Ricardo Villalba aka rvm (GPLv2)
#
# Please submit bugfixes or comments via
# http://sourceforge.net/tracker/?group_id=185512
# or http://bugs.opensuse.org/

Name:           smplayer-qt5
Version:        14.3.0
Release:        0
License:        GPL-2.0+
Summary:        Complete Frontend for MPlayer
Url:            http://smplayer.sourceforge.net/
Group:          Productivity/Multimedia/Video/Players
Source:         http://prdownloads.sourceforge.net/smplayer/smplayer-%{version}.tar.bz2
Patch1:         smplayer-makeflags.patch
Patch2:         smplayer-disable-debug.patch
Patch4:         smplayer-default_ao.patch
Patch8:         smplayer-simple-resize.patch
# FIX-UPSTREAM to play network shared video correctly: #PM-48
Patch9:         smplayer-add_kde_protocols_to_desktop_file.patch

BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libstdc++-devel
BuildRequires:  make
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
%if 0%{?suse_version} > 1310
BuildRequires:  libQt5Gui-private-headers-devel
%else
BuildRequires:  libqt5-qtbase-private-headers-devel
%endif
BuildRequires:  libqt5-qttools-devel
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
# requires at least this version for closed caption channel support:
Requires:       MPlayer >= 1.0rc4_r32607
Conflicts:      smplayer
Provides:       smplayer-core = %{version}
Recommends:     smplayer-skins
Suggests:       smplayer-themes

%description
SMPlayer intends to be a complete front-end for MPlayer, from basic features
like playing videos, DVDs, and VCDs to more advanced features like support for
MPlayer filters and more.

One of the most interesting features of SMPlayer:it remembers the settings of
all files you play. So you start to watch a movie but you have to leave...
don't worry, when you open that movie again it will resume at the same point
you left it, and with the same settings: audio track, subtitles, volume...

%lang_package
%prep
%setup -q -n "smplayer-%{version}"
%patch1
%patch2
%patch4
%patch9
%__perl -n -e 'print $1,"\n" if /^\+{3}\s+(.+?)\s+/' < "%{PATCH4}" | while read f; do
%__sed -i 's/@@DEFAULT@@/pulse/g' "$f"
done

pushd src
%patch8
popd

# fix CRLF in .txt files:
%__sed -i 's/\r$//' *.txt

find . -type f -name '*.pro' | while read f; do
cat <<EOF >>"$f"

QMAKE_CFLAGS = %{optflags}
QMAKE_CXXFLAGS = %{optflags}

EOF
done

%build
%__make \
    MAKEFLAGS="%{?_smp_flags}" \
    CONF_PREFIX="" \
    PREFIX="%{_prefix}" \
    DOC_PATH="%{_docdir}/%{name}" \
    QMAKE="%{_libqt5_bindir}/qmake" \
    LRELEASE="%{_libqt5_bindir}/lrelease"

%install
%__make \
    MAKEFLAGS="" \
    CONF_PREFIX="%{buildroot}" \
    PREFIX="%{buildroot}%{_prefix}" \
    DOC_PATH="%{buildroot}%{_docdir}/%{name}" \
    QMAKE="%{_libqt5_bindir}/qmake" \
    LRELEASE="%{_libqt5_bindir}/lrelease" \
    install

%__rm -rf "%{buildroot}%{_docdir}/%{name}"

# Append Qt;KDE; categories in desktop files - fix for #PM-48
for desktop in smplayer smplayer_enqueue; do
    %suse_update_desktop_file -r "$desktop" Qt KDE AudioVideo Video Player
done

LANGFILE="$PWD/smplayer.lang"
echo -n > "$LANGFILE"
find "%{buildroot}%{_datadir}/smplayer/translations" -name '*.qm' \
| while read qm; do
    qmfile=${qm##*/}
    l=${qmfile#*_}
    l=${l%%.qm}

    [ "$l" = "en_US" ] && continue    
    echo "%lang(${l}) %{_datadir}/smplayer/translations/${qmfile}" >> "$LANGFILE"
done
%__install -d "%{buildroot}%{_docdir}/%{name}"
pushd docs
for l in *; do
    %__cp -a "$l" "%{buildroot}%{_docdir}/%{name}/${l}"

    [ "$l" = "en" ] && continue
    echo "%lang(${l}) %{_docdir}/%{name}/${l}" >> "$LANGFILE"
done
popd #docs

%__install -m0644 Changelog *.txt "%{buildroot}%{_docdir}/%{name}"/

%files
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/Changelog
%doc %{_docdir}/%{name}/*.txt
%doc %{_docdir}/%{name}/en
%{_bindir}/smplayer
%{_datadir}/applications/smplayer.desktop
%{_datadir}/applications/smplayer_enqueue.desktop
%dir %{_datadir}/icons/*/*
%dir %{_datadir}/icons/*/*/apps
%{_datadir}/icons/*/*/apps/smplayer.*
%dir %{_datadir}/smplayer
%config %{_datadir}/smplayer/input.conf
%dir %{_datadir}/smplayer/shortcuts
%{_datadir}/smplayer/shortcuts/*.keys
%dir %{_datadir}/smplayer/translations
%doc %{_mandir}/man1/smplayer.1%{ext_man}
%lang(en_US) %{_datadir}/smplayer/translations/smplayer_en_US.qm

%files lang -f smplayer.lang
%defattr(-,root,root)

%changelog
