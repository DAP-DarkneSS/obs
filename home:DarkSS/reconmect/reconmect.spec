#
# spec file for package reconmect
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           reconmect
Version:        0
Release:        0
Summary:        Restarts Network Manager after disconnect
License:        LGPL-2.0+
Group:          Productivity/Networking/Web/Utilities
Url:            http://kubuntu.ru/node/10667
Source0:        reconmect.sh

BuildRequires:  NetworkManager
Requires:       NetworkManager
Requires:       bash
Requires:       fping
Requires:       systemd
BuildArch:      noarch

%description
If any of two selected hosts couldn't be pinged,
Network Manager service will be restarted via systemd.

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d
install %{SOURCE0} %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d


%files
%defattr(-,root,root)
%attr(755,root,root) %{_sysconfdir}/NetworkManager/dispatcher.d/%{name}.sh

%changelog
