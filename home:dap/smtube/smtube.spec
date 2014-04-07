# vim: set sw=4 ts=4 et nu:

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

Name:               smtube
Version:            1.5
Release:            0.pm.1
Summary:            Small Youtube Browser
Source:             http://prdownloads.sourceforge.net/smplayer/smtube-%{version}.tar.bz2
Patch1:             smtube-optflags.patch
URL:                http://smplayer.sourceforge.net/
Group:              Productivity/Multimedia/Video/Players
License:            GPL-2.0+
BuildRoot:          %{_tmppath}/build-%{name}-%{version}
BuildRequires:      libqt4-devel
BuildRequires:      gcc-c++ make pkgconfig
BuildRequires:      update-desktop-files
BuildRequires:      hicolor-icon-theme
Requires:           smplayer >= 0.8.0
# just to make the build fail if not avail:
BuildRequires:      smplayer >= 0.8.0

%description
This is a youtube browser for smplayer. You can browse, search, download and
play youtube videos. The videos are currently played in smplayer but in the
future it may be added the possibility to use other players.

The code has been taken from UMPlayer (http://www.umplayer.com), with some
modifications to make it a stand-alone application and added a few
improvements.

%lang_package

%prep
%setup -q
%patch1

%__sed -i 's/\r$//' *.txt

%build
%__make \
    PREFIX="%{_prefix}" \
    DATA_PATH="%{_datadir}/%{name}" \
    DOC_PATH="%{_docdir}/%{name}" \
    KDE_PREFIX="%{_prefix}" \
    OPTFLAGS="%{optflags}"

%install
%__make \
    PREFIX="%{_prefix}" \
    DATA_PATH="%{_datadir}/%{name}" \
    DOC_PATH="%{_docdir}/%{name}" \
    KDE_PREFIX="%{_prefix}" \
    OPTFLAGS="%{optflags}" \
    DESTDIR="%{buildroot}" \
    install

%suse_update_desktop_file -r "%{name}" AudioVideo Player

L="$PWD/%{name}.lang"
echo -n >"$L"
pushd "%{buildroot}%{_datadir}/%{name}/translations"
/bin/ls -1 *.qm | while read qm; do
    l="${qm%.qm}"
    l="${l#smtube_}"
    [ "$l" = "en" ] && continue
    echo "%lang($l) %{_datadir}/%{name}/translations/$qm" >>"$L"
done
popd

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc Changelog Copying*txt Readme.txt Release_notes.txt
%{_bindir}/smtube
%{_datadir}/applications/smtube.desktop
%{_datadir}/icons/*/*/apps/smtube.*
%dir %{_datadir}/smtube
%dir %{_datadir}/%{name}/translations
%lang(en) %{_datadir}/%{name}/translations/smtube_en.qm

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
