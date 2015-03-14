#
# spec file for package smplayer-skins
#
# Copyright (c) 2006-2012 Ricardo Villalba aka rvm (GPLv2)
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

# Please submit bugfixes or comments via https://bugs.links2linux.org
#

Name:           smplayer-skins
Version:        15.2.0
Release:        0
License:        GPL-2.0+
Summary:        Skins for SMPlayer
Url:            http://smplayer.sourceforge.net/
Group:          Productivity/Multimedia/Video/Players
Source:         http://downloads.sourceforge.net/project/smplayer/SMPlayer-skins/%{version}/smplayer-skins-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  libqt4-devel >= 4.2.0

BuildRoot:      %{_tmppath}/build-%{name}-%{version}

Requires:       smplayer-core >= 14.9.0

%description
This package provides skin themes for SMPlayer.
SMPlayer intends to be a complete front-end for Mplayer, from basic features
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
%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%{_datadir}/smplayer

%changelog
