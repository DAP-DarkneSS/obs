#
# spec file for package wifi-hostapd-ap
#
# Copyright (c) 2012-2013 Kozincew Egor (source),
# (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments
# via https://bugs.launchpad.net/wifi-hostapd-ap
#

Name:           wifi-hostapd-ap
Version:        1.1.1
Release:        1
License:        GPL-2.0
Summary:        WiFi access point creator
Url:            https://launchpad.net/wifi-hostapd-ap
Group:          Productivity/Networking/Other

Source0:        https://launchpad.net/~ekozincew/+archive/ppa/+files/wifi-hostapd-ap_%{version}-0~1~raring1.tar.gz
# PATCH-FIX-OPENSUSE to prevent "W: invalid-desktopfile".
Patch0:         wifi-hostapd-ap-desktop.patch
# PATCH-FIX-OPENSUSE to set right dnsmasq.pid file directory.
Patch1:         wifi-hostapd-ap-dnsmasq_pid.patch

BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(QtCore)

Requires:       bridge-utils
Requires:       dnsmasq
Requires:       hostapd
Requires:       wireless-tools

%description
А GUI to create WiFi access point based on Hostapd.

%prep
%setup -q -n 'recipe-{debupstream}-0~{revno}'
%patch0
%patch1

%build
`pkg-config --variable=exec_prefix QtCore`/bin/qmake \
QMAKE_STRIP="" \
PREFIX=%{_prefix} \
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}"

make %{?_smp_mflags}

%install
mkdir -p %{buildroot}
make INSTALL_ROOT=%{buildroot} install
rm %{buildroot}%{_datadir}/%{name}/translations/about_*.html
%suse_update_desktop_file -r %{name} 'System;Network;'
%suse_update_desktop_file -r %{name}-KDE 'System;Network;'

%files
%defattr(-,root,root)
%doc README about/about_*.html
%{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/scalable/apps/WiFi_logo_litle.png
%{_datadir}/%{name}

%changelog
