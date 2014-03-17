#
# spec file for package acestream-local
#
# Copyright (c) 2013-2014 Perlow Dmitriy A. aka DarkneSS.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via [Russian]
# http://forum.torrentstream.org/index.php?topic=1464.0
#


Name:           acestream-local
Version:        2.0.0
Release:        0
Summary:        ACE Stream engine and multimedia player based on VLC
License:        SUSE-NonFree
Group:          Productivity/Multimedia/Video/Players
Url:            http://www.acestream.org
Source1:        http://torrentstream.org/downloads/linux/test/acestream-local_%{version}_amd64.deb
Source2:        http://torrentstream.org/downloads/linux/test/acestream-local_%{version}_i386.deb

BuildRequires:  chrpath
BuildRequires:  deb
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  kde4-filesystem
BuildRequires:  liba52-0
BuildRequires:  libavcodec55
BuildRequires:  libavformat55
BuildRequires:  update-desktop-files
Requires:       libQtWebKit4
Requires:       liba52-0
Requires:       libavcodec55
Requires:       libavformat55
Requires:       libavutil51
Requires:       liblua5_1
Requires:       libopenssl1_0_0
Recommends:     %{name}-lang
ExclusiveArch:  %{ix86} x86_64

%description
This package contains the ACE Stream engine, ACE Stream player,
ACE Stream libs, ACE Stream mozilla plugin.

%lang_package

%prep

%build

%install
%ifarch x86_64
dpkg -X %{SOURCE1} %{buildroot}
mv %{buildroot}%{_prefix}/{lib,lib64}
%endif
%ifarch %{ix86}
dpkg -X %{SOURCE2} %{buildroot}
%endif
mv %{buildroot}%{_libdir}/python2.7/{dist-packages,site-packages}

%find_lang acestreamplayer
%suse_update_desktop_file acestreamplayer
chrpath --delete %{buildroot}%{_libdir}/acestreamplayer/acestreamplayer-cache-gen
chrpath --delete %{buildroot}%{_bindir}/acestreamplayer
chrpath --delete %{buildroot}%{_libdir}/libtsplayer.so.5
dos2unix -q %{buildroot}/doc/acestreamplayer/copyright
%fdupes -s %{buildroot}%{_datadir}
ln -s        %{_libdir}/liba52.so.0 \
 %{buildroot}%{_libdir}/liba52-0.7.4.so
ln -s        %{_libdir}/libavcodec.so.55  \
 %{buildroot}%{_libdir}/libavcodec.so.53
ln -s        %{_libdir}/libavformat.so.55 \
 %{buildroot}%{_libdir}/libavformat.so.53
ln -s        %{_libdir}/liblua.so.5.1 \
 %{buildroot}%{_libdir}/liblua5.1.so.0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*acestream*
%{_libdir}/*acestream*
%dir %{_libdir}/mozilla*
%dir %{_libdir}/xulrunner-addons
%dir %{_libdir}/*/plugins
%{_libdir}/*/plugins/libace_plugin.so
%dir %{_libdir}/python2.7
%dir %{_libdir}/python2.7/site-packages
%{_libdir}/python2.7/site-packages/*acestream*
%{_libdir}/libtsplayer*
%{_datadir}/acestream*
%{_datadir}/applications/acestreamplayer.desktop
%{_datadir}/doc/acestreamplayer
%{_datadir}/icons/hicolor/*x*/apps/acestreamplayer*
%dir %{_datadir}/kde4/apps/solid
%dir %{_datadir}/kde4/apps/solid/actions
%{_datadir}/kde4/apps/solid/actions/acestreamplayer*.desktop
%{_mandir}/man*/acestreamplayer*.gz
%exclude %{_datadir}/menu
%{_libdir}/liba52-0.7.4.so
%{_libdir}/libavcodec.so.53
%{_libdir}/libavformat.so.53
%{_libdir}/liblua5.1.so.0

%files lang -f acestreamplayer.lang

%changelog
