#
# spec file for package qlivebittorrent
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

Name:           qlivebittorrent
Version:        git
Release:        0
License:        GPL-1.0+
Summary:        A simple bittorrent client with very interesting live feature
Url:            https://github.com/vtyulb/QLiveBittorrent
Group:          Productivity/Networking/File-Sharing
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  fuse-devel
BuildRequires:  grep
BuildRequires:  libGeoIP-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 0.16

%description
A bittorrent client that allows to read files before they would be downloaded.

Plus and Minus keys — to increase/decrease download rate limit;
'q' — for exit; 'a' — to switch agressive/non-agressive piece picking.

%prep
%setup -q
echo "Disabling portable version"
grep -v PORTABLE src/QLiveBittorrent.pro > src/%{name}.pro


%build
export XCFLAGS="%{optflags}"
gcc -g -o %{name}-driver src/driver.c `pkg-config fuse --cflags --libs`

export PATH=%_libqt5_bindir:$PATH
qmake-qt5 \
            QMAKE_STRIP="" \
            QMAKE_CXXFLAGS+="%{optflags}" \
            src/%{name}.pro

make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
%{__install} QLiveBittorrent %{buildroot}%{_bindir}/%{name}
%{__install} %{name}-driver %{buildroot}%{_bindir}


%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/%{name}*


%changelog
