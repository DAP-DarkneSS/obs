#
# spec file for package ap-hotspot
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


%define majver 0.3

Name:           ap-hotspot
Version:        %{majver}.1
Release:        0
Summary:        Access Point Mode Hotspot
License:        GPL-3.0
Group:          Productivity/Networking/Other
Url:            http://www.webupd8.org/2013/06/how-to-set-up-wireless-hotspot-access.html
Source0:        https://launchpad.net/~nilarimogard/+archive/ubuntu/webupd8/+files/ap-hotspot_%{version}-1~webupd8~0.tar.gz
Source9:        %{name}.1

Requires:       dnsmasq
Requires:       hostapd
Requires:       iw
BuildArch:      noarch

%description
A script to create an infrastructure WiFi hotspot (access point mode).

%prep
%setup -q -n %{name}-%{majver}

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c9 %{SOURCE9} | tee -a %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%defattr(-,root,root)
%doc debian/changelog debian/copyright
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
