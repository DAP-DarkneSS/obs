#
# spec file for package diskscan
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


Name:           diskscan
Version:        0.13
Release:        0
Summary:        Scan disk for bad or near failure sectors
License:        GPL-3.0+
Group:          Hardware/Other
Url:            http://blog.disksurvey.org/proj/diskscan/
Source0:        https://github.com/baruch/diskscan/archive/%{version}.tar.gz

BuildRequires:  python-beautifulsoup
BuildRequires:  python-markdown


%description
DiskScan is a Unix/Linux tool to scan a block device and check
if there are unreadable sectors, in addition it uses read
latency times as an assessment for a near failure as sectors
that are problematic to read usually entail many retries. This
can be used to assess the state of the disk and maybe decide
on a replacement in advance to its imminent failure. The disk
self test may or may not pick up on such clues depending on
the disk vendor decision making logic.


%prep
%setup -q


%build
make V=1 %{?_smp_mflags}


%install
make V=1 install DESTDIR=%{buildroot}
# Let's use %%doc macro.
rm %{buildroot}/%{_datadir}/doc/%{name}/README.md


%files
%defattr(-,root,root)
%doc COPYING README*
%{_bindir}/%{name}
%doc %{_mandir}/man*/%{name}.*.gz

%changelog
