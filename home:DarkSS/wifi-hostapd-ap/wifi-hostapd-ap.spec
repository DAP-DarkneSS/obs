#
# spec file for package wifi-hostapd-ap
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wifi-hostapd-ap
Version:        1.1.1
Release:        0
Summary:        WiFi access point creator
License:        GPL-2.0
Group:          Productivity/Networking/Other
Url:            https://launchpad.net/wifi-hostapd-ap
Source0:        https://launchpad.net/~ekozincew/+archive/ubuntu/ppa/+files/wifi-hostapd-ap_%{version}-0~1~ubuntu15.04.1.tar.gz
# PATCH-FIX-OPENSUSE to prevent "W: invalid-desktopfile".
Patch0:         wifi-hostapd-ap-desktop.patch
# PATCH-FIX-OPENSUSE to set right dnsmasq.pid file directory.
Patch1:         wifi-hostapd-ap-dnsmasq_pid.patch
Patch10:        ROSA-0-unistd.patch
Patch11:        ROSA-1-kdesu.patch
Patch14:        ROSA-4-mainwindow.patch

BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(QtCore)
Requires:       bridge-utils
Requires:       dnsmasq
Requires:       hostapd
Requires:       wireless-tools

%description
А GUI to create WiFi access point based on Hostapd.

%prep
%setup -q
%patch0
%patch1
%patch10 -p0
%patch11 -p0
%patch14 -p0

%build
`pkg-config --variable=exec_prefix QtCore`/bin/qmake \
QMAKE_STRIP="" \
PREFIX=%{_prefix} \
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}"

make V=1 %{?_smp_mflags}

%install
mkdir -p %{buildroot}
make V=1 INSTALL_ROOT=%{buildroot} install
%suse_update_desktop_file -r %{name} 'System;Network;'
%suse_update_desktop_file -r %{name}-KDE 'System;Network;'

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/scalable/apps/WiFi_logo_litle.png
%{_datadir}/%{name}

%changelog
