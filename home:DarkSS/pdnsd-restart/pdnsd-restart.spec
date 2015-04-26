#
# spec file for package pdnsd-restart
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pdnsd-restart
Version:        1
Release:        0
Summary:        Restarts pdnsd when needed
License:        LGPL-2.0+
Group:          Productivity/Networking/DNS/Utilities

Source0:        pdnsd-restart.sh
Source1:        pdnsd-sleep.sh

BuildRequires:  NetworkManager
BuildRequires:  systemd
Requires:       NetworkManager
Requires:       pdnsd
Requires:       systemd

BuildArch:      noarch

%description
Restarts pdnsd service via systemd after NetworkManager (re)connect.
It also stops it before sleeping and starts after awakening.

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d
install %{SOURCE0} %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d

mkdir -p %{buildroot}%{_libexecdir}/systemd/system-sleep
install %{SOURCE1} %{buildroot}%{_libexecdir}/systemd/system-sleep

%files
%defattr(-,root,root)
%attr(755,root,root) %{_sysconfdir}/NetworkManager/dispatcher.d/%{name}.sh
%attr(755,root,root) %{_libexecdir}/systemd/system-sleep/pdnsd-sleep.sh

%changelog
