# vim: set ts=4 sw=4 et:
#
# spec file for package smplayer-themes
#
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2016 Packman team: http://packman.links2linux.org/
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.links2linux.org
#


Name:           smplayer-themes
Version:        16.6.0
Release:        0
Summary:        Icon Themes for SMPlayer
License:        GPL-2.0+
Group:          Productivity/Multimedia/Video/Players
Url:            http://smplayer.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/smplayer/smplayer-themes-%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  libqt4-devel >= 4.2.0
BuildRequires:  make
Requires:       smplayer-core >= 14.9.0
BuildArch:      noarch

%description
This package provides icon themes for SMPlayer.

SMPlayer intends to be a complete front-end for MPlayer, from basic features
like playing videos, DVDs, and VCDs to more advanced features like support
for Mplayer filters and more. One of the main features is the ability to
remember the state of a played file, so when you play it later it will resume
at the same point and with the same settings. smplayer is developed with
the Qt toolkit, so it's multi-platform.

%prep
%setup -q

%build
make \
     V=1 \
     %{?_smp_mflags}

%install
make \
     V=1 \
     %{?_smp_mflags} \
     PREFIX=%{_prefix} \
     DESTDIR=%{buildroot} \
     install
%fdupes -s "%{buildroot}%{_datadir}/smplayer"

%files
%defattr(-,root,root)
%doc Changelog README.txt
%dir %{_datadir}/smplayer
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*

%changelog
