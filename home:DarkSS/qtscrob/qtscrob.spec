#
# spec file for package qtscrob
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           qtscrob
Version:        0.11
Release:        0
License:        GPL-2.0
Summary:        Submit .scrobbler.log from portable players to Last.fm and Libre.fm
Url:            http://qtscrob.sourceforge.net/
Group:          Productivity/Multimedia/Sound/Utilities
Source0:        http://heanet.dl.sourceforge.net/project/qtscrob/qtscrob/%{version}/qtscrob-%{version}.tar.bz2

BuildRequires:  dos2unix
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(QtCore) >= 4.4
BuildRequires:  pkgconfig(libmtp)

%description
Update your last.fm profile using information from portable player!
QTScrobbler is tool for submitting from portable players to
Last.fm & Libre.fm. It is written in C++ using the QT4 library.

Features: 
 * Parsing iPod's Play Counts file to get recently played tracks;
 * Parsing .scrobbler.log (and .scrobbler-timeless.log);
 * MTP (aka PlaysForSure) support;
 * Ability to recalculate the listen times of any loaded tracks;
 * Proxy support;
 * Protocol 1.2 support;
 * Automatically detect timezone and summertime details;
 * Polish translation.

%prep
%setup -q
dos2unix AUTHORS CHANGELOG COPYING README

%build
cd src
qmake \
      QMAKE_STRIP="" \
      PREFIX=%{_prefix} \
      QMAKE_CXXFLAGS+="%{optflags}"

make %{?_smp_mflags}

%install
cd src
make install INSTALL_ROOT=%{buildroot}
%suse_update_desktop_file -r %{name} 'AudioVideo;Music;'


%files
%defattr(-,root,root)
%attr(644,root,root) %doc AUTHORS CHANGELOG COPYING README
%{_bindir}/*scrob*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%attr(644,root,root) %doc %{_mandir}/man1/*scrob*.1.gz

%changelog
