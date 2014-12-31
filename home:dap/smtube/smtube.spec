#
# spec file for package smtube
#
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2014 Packman team: http://packman.links2linux.org/
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


Name:           smtube
Version:        14.12.0
Release:        0
Summary:        Small Youtube Browser
License:        GPL-2.0
Group:          Productivity/Multimedia/Video/Players
URL:            http://smplayer.sourceforge.net/smtube.php
Source0:        http://downloads.sourceforge.net/smplayer/SMTube/%{version}/%{name}-%{version}.tar.bz2
# Fix 'File is compiled without RPM_OPT_FLAGS'
Patch0:         %{name}-src_%{name}.pro.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libqt4-devel
BuildRequires:  pkgconfig
Recommends:     MPlayer
Recommends:     smplayer
Recommends:     vlc

%description
SMTube allows to search, play and download Youtube videos.
Videos are played back with a media player (by default SMPlayer)
instead of a flash player, this allows better performance,
particularly with HD content. SMTube also allows to download the videos,
with the quality you choose. Several videos can be downloaded at a time.

SMTube is included in SMPlayer's menus, to run it just select Youtube browser
in the Options menu in the SMPlayer main window, or just press F11.

%lang_package

%prep
%setup -q
%patch0

# Fix paths
sed -i -e 's|/usr/local|/usr|' \
    -i -e 's|/share/doc/|/share/doc/packages/|' Makefile

# Some docs have the DOS line ends
dos2unix Changelog *.txt

%build
make %{?_smp_mflags} \
     PREFIX="%{_prefix}" \
     DATA_PATH="%{_datadir}/%{name}" \
     DOC_PATH="%{_docdir}/%{name}" \
     KDE_PREFIX="%{_prefix}" \
     OPTFLAGS="%{optflags}"

%install
%make_install
%find_lang %name --with-qt

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc Changelog *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files lang -f %{name}.lang
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
