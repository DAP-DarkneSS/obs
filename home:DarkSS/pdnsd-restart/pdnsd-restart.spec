#
# spec file for package pdnsd-restart
#
# Copyright (c) 2012 Perlow Dmitriy A.
#

Name:           pdnsd-restart
Version:        0
Release:        1
Summary:        Restarts pdnsd after NM (re)connect

License:        LGPL-2.0
Group:          Productivity/Networking/DNS/Utilities
URL:            http://dap-darkness.livejournal.com/73664.html
Source0:        pdnsd-restart.sh

BuildArch:      noarch

Requires:       NetworkManager
Requires:       pdnsd
Requires:       systemd

%description
Restarts pdnsd service via systemd after NetworkManager (re)connect.

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
