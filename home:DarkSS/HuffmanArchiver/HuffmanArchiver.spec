#
# spec file for package HuffmanArchiver
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           HuffmanArchiver
Version:        0
Release:        0
Summary:        Huffman Archiver
License:        LGPL-2.0+
Url:            https://github.com/DAP-DarkneSS/HuffmanArchiver
Source0:        HuffmanArchiver-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  llvm-clang

%description
A C99 Huffman archiver for EPAM Linux cource:
https://github.com/epam-llpd/linux_courses/tree/master/epam

%prep
%setup -q
rm -rf build

%build
export CC=%{_bindir}/clang
%cmake \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo
scan-build make %{?_smp_mflags} V=1 -k

%install
cd build
%make_install V=1 -k

%files
%defattr(-,root,root)
%doc COPYING* README*
%{_bindir}/huffar

%changelog
