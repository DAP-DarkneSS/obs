#
# spec file for package smplayer-skins
#
# Copyright (c) 2006-2012 Ricardo Villalba aka rvm (GPLv2)
#
# Please submit bugfixes or comments via http://sourceforge.net/tracker/?group_id=185512
#

Name:           smplayer-skins
Version:        20121029
Release:        0
License:        GPL-2.0+
Summary:        Skins for SMPlayer
Url:            http://smplayer.sourceforge.net/
Group:          Productivity/Multimedia/Video/Players
Source:         http://downloads.sourceforge.net/project/smplayer/SMPlayer-skins/%{version}/smplayer-skins-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  fdupes

BuildRoot:      %{_tmppath}/build-%{name}-%{version}

Requires:       smplayer >= 0.8.2

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

%install
make %{?_smp_mflags} PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%{_datadir}/smplayer

%changelog
