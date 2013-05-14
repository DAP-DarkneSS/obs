#
# spec file for package reconmect
#
# Copyright (c) 2013 Perlow Dmitriy A.
#

Name:           reconmect
Version:        0
Release:        1
Summary:        Restarts Network Manager after disconnect

License:        LGPL-2.0+
Group:          Productivity/Networking/Web/Utilities
URL:            http://kubuntu.ru/node/10667
Source0:        reconmect.sh

BuildArch:      noarch

Requires:       NetworkManager
Requires:       bash
Requires:       fping
Requires:       systemd

%description
If any of two selected hosts couldn't be pinged,
Network Manager service will be restarted via systemd.

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d
%{__install} %{SOURCE0} %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%attr(755,root,root) %{_sysconfdir}/NetworkManager/dispatcher.d/%{name}.sh

%changelog
