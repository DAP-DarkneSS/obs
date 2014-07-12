# vim: set ts=4 sw=4 et:

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


Name:           smplayer-themes
Version:        20140607
Release:        1.pm.1
Summary:        Icon Themes for SMPlayer
Source:         http://prdownloads.sourceforge.net/smplayer/smplayer-themes-%{version}.tar.bz2
URL:            http://smplayer.sourceforge.net/
Group:          Productivity/Multimedia/Video/Players
License:        GPL-2.0+
BuildRoot:      %{_tmppath}/build-%{name}-%{version}
BuildRequires:  make
BuildRequires:  fdupes
Requires:       smplayer-core
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

%install
%makeinstall PREFIX="%{_prefix}"

%fdupes -s "%{buildroot}%{_datadir}/smplayer"

%files
%defattr(-,root,root)
%doc Changelog README.txt
%dir %{_datadir}/smplayer
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*

%changelog
