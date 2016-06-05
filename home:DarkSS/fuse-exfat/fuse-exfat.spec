#
# spec file for package fuse-exfat
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


Name:           fuse-exfat
Version:        1.2.4
Release:        0
Summary:        Free exFAT file system implementation
License:        GPL-2.0+
Group:          System/Filesystems
Url:            https://github.com/relan/exfat
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fuse-devel >= 2.6
BuildRequires:  libtool
BuildRequires:  pkg-config
Requires:       fuse >= 2.6
Recommends:     exfat-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

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
ln -sf %{_sbindir}/{mount.exfat,mount.exfat-fuse} %{buildroot}/sbin
#EndUsrMerge

%post
if ! grep -q -e '^exfat$' %{_sysconfdir}/filesystems ; then
    sed -i 's/*/exfat\n*/g' %{_sysconfdir}/filesystems
    echo "Added 'exfat' to the file %{_sysconfdir}/filesystems"
fi

if ! grep -q exfat_fuse %{_sysconfdir}/filesystems ; then
    sed -i 's/*/exfat_fuse\n*/g' %{_sysconfdir}/filesystems
    echo "Added 'exfat_fuse' to the file %{_sysconfdir}/filesystems"
fi

%postun
if [ "$1" == "0" ]; then
    sed -i -e '/exfat_fuse/d' -e '/^exfat$/d' %{_sysconfdir}/filesystems
    echo "Deleted 'exfat' and 'exfat_fuse' from the file %{_sysconfdir}/filesystems"
fi

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
#UsrMerge
/sbin/*
#EndUsrMerge
%{_sbindir}/mount.exfat
%{_sbindir}/mount.exfat-fuse
%{_mandir}/man8/mount.exfat-fuse.8%{ext_man}

%changelog
