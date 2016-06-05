#
# spec file for package exfat-utils
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Sidlovsky, Yaroslav <zawertun@gmail.com>
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


Name:           exfat-utils
Version:        1.2.3
Release:        0
Summary:        Utilities for exFAT file system
License:        GPL-2.0+
Group:          System/Filesystems
Url:            https://github.com/relan/exfat
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
Recommends:     fuse-exfat
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

%prep
%setup -q

%build
# force installation of manual pages
sed -i -e 's/no-installman//' configure.ac
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
#UsrMerge
mkdir  %{buildroot}/sbin
ln -sf %{_sbindir}/{dumpexfat,exfatfsck,exfatlabel,fsck.exfat,mkexfatfs,mkfs.exfat} %{buildroot}/sbin
pushd %{buildroot}%{_mandir}/man8
#EndUsrMerge
ln -s exfatfsck.8.gz fsck.exfat.8.gz
ln -s mkexfatfs.8.gz mkfs.exfat.8.gz
popd

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
#UsrMerge
/sbin/*
#EndUsrMerge
%{_sbindir}/dumpexfat
%{_sbindir}/exfatfsck
%{_sbindir}/exfatlabel
%{_sbindir}/fsck.exfat
%{_sbindir}/mkexfatfs
%{_sbindir}/mkfs.exfat
%{_mandir}/man8/dumpexfat.8%{ext_man}
%{_mandir}/man8/exfatfsck.8%{ext_man}
%{_mandir}/man8/exfatlabel.8%{ext_man}
%{_mandir}/man8/fsck.exfat.8%{ext_man}
%{_mandir}/man8/mkexfatfs.8%{ext_man}
%{_mandir}/man8/mkfs.exfat.8%{ext_man}

%changelog
