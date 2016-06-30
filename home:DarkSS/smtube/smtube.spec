#
# spec file for package smtube
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           smtube
Version:        16.7.0
Release:        0
Summary:        Small Youtube Browser
License:        GPL-2.0+
Group:          Productivity/Multimedia/Video/Players
Url:            http://www.smtube.org/
Source0:        http://downloads.sourceforge.net/smtube/SMTube/%{version}/%{name}-%{version}.tar.bz2
Source9:        %{name}.1
# Fix 'File is compiled without RPM_OPT_FLAGS'
Patch0:         %{name}-src_%{name}.pro.patch
# PATCH-FIX-OPENSUSE Video downloading from Youtube seems to be illegal.
Patch1:         smtube-no-download-option.diff
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
%if 0%{?suse_version} > 1310
BuildRequires:  libqt5-linguist
%else
BuildRequires:  libqt5-qttools
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
Suggests:       MPlayer
Suggests:       dragon
Suggests:       gnome-mplayer
Suggests:       mpv
Recommends:     smplayer
Suggests:       totem
Suggests:       vlc
Suggests:       youtube-dl

%description
SMTube is an application that allows to browse, search and play YouTube
videos. Videos are played back with a media player (by default SMPlayer)
instead of a flash player, this allows better performance, particularly
with HD content. Read more at http://www.smtube.org/

SMTube is included in SMPlayer's menus, to run it just select Youtube browser
in the Options menu in the SMPlayer main window, or just press F11.

%lang_package

%prep
%setup -q
%patch0
%patch1

# SED-FIX-OPENSUSE -- Fix paths
sed -i -e 's|/usr/local|/usr|;
           s|/share/doc/|/share/doc/packages/|' Makefile

# Some docs have the DOS line ends
dos2unix *.txt

%build
make %{?_smp_mflags} \
     PREFIX="%{_prefix}" \
     DATA_PATH="%{_datadir}/%{name}" \
     DOC_PATH="%{_docdir}/%{name}" \
     KDE_PREFIX="%{_prefix}" \
     QMAKE=qmake-qt5 \
     LRELEASE=lrelease-qt5 \
     OPTFLAGS="%{optflags}"

%install
%make_install
%find_lang %name --with-qt

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

mkdir -p %{buildroot}%{_mandir}/man1
cp %{SOURCE9} %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc Changelog *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man?/%{name}.?.*

%files lang -f %{name}.lang
%defattr(-,root,root)
%{_datadir}/%{name}

%changelog
