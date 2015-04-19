#
# spec file for package HuffmanArchiver
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


%ifarch %ix86 x86_64 aarch64 armv7l ppc ppc64 ppc64le
%define checkbyvalgrind 1
%else
%define checkbyvalgrind 0
%endif

# ARMv6: https://bugzilla.opensuse.org/show_bug.cgi?id=927269
# PPC64: https://bugzilla.opensuse.org/show_bug.cgi?id=927268

%ifarch %ix86 x86_64 armv6l armv7l ppc64 ppc64le
%define clangisntalie 1
%ifarch %ix86 x86_64 armv7l
%define buildviaclang 1
%else
%define buildviaclang 0
%endif
%else
%define clangisntalie 0
%define buildviaclang 0
%endif

%if 0%{?rhel_version} || 0%{?centos_version}
%define clangisntalie 0
%define buildviaclang 0
%endif

%if 0%{?fedora}
%define buildviaclang 0
%endif

Name:           HuffmanArchiver
Version:        0
Release:        0
Summary:        Huffman Archiver
License:        LGPL-2.0+
Url:            https://github.com/DAP-DarkneSS/HuffmanArchiver
Source0:        HuffmanArchiver-%{version}.tar.xz

BuildRequires:  cmake
%if %{clangisntalie}
%if 0%{?suse_version}
BuildRequires:  llvm-clang
%else
BuildRequires:  clang-analyzer
%endif
%endif
%if %{checkbyvalgrind}
BuildRequires:  valgrind
%endif

%description
A C99 Huffman archiver for EPAM Linux cource:
https://github.com/epam-llpd/linux_courses/tree/master/epam

%prep
%setup -q

%build
%if %{buildviaclang}
export CC=%{_bindir}/clang
%endif

%cmake \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo

%if %{clangisntalie}
scan-build \
%endif
make %{?_smp_mflags} V=1 -k

%install
%if 0%{?suse_version}
cd build
%endif
%make_install V=1 -k

%check
# Simple text check.
%if %{checkbyvalgrind}
valgrind \
         --tool=memcheck \
         --leak-check=full \
         --track-fds=yes \
         --track-origins=yes \
         --show-reachable=yes \
         -v \
%endif
         %{buildroot}/%{_bindir}/huffar \
         %{_builddir}/%{name}-%{version}/COPYING.LESSER \
         -c \
         /tmp/COPYING.LESSER.ha

%if %{checkbyvalgrind}
valgrind \
         --max-stackframe=8388607 \
         --tool=memcheck \
         --leak-check=full \
         --track-fds=yes \
         --track-origins=yes \
         --show-reachable=yes \
         -v \
%endif
         %{buildroot}/%{_bindir}/huffar \
         /tmp/COPYING.LESSER.ha \
         -x \
         /tmp/COPYING.LESSER
diff \
     -u \
     %{_builddir}/%{name}-%{version}/COPYING.LESSER \
     /tmp/COPYING.LESSER

# Binary file check.

dd if=/dev/urandom of=/tmp/megabyte bs=1M count=1

md5sum -b /tmp/megabyte > /tmp/megabyte.md5

%if %{checkbyvalgrind}
valgrind \
         --tool=memcheck \
         --leak-check=full \
         --track-fds=yes \
         --track-origins=yes \
         --show-reachable=yes \
         -v \
%endif
         %{buildroot}/%{_bindir}/huffar \
         /tmp/megabyte \
         -c \
         /tmp/megabyte.ha

%if %{checkbyvalgrind}
valgrind \
         --max-stackframe=8388607 \
         --tool=memcheck \
         --leak-check=full \
         --track-fds=yes \
         --track-origins=yes \
         --show-reachable=yes \
         -v \
%endif
         %{buildroot}/%{_bindir}/huffar \
         /tmp/megabyte.ha \
         -x \
         /tmp/megabyte

md5sum -c /tmp/megabyte.md5

# Single symbol file check.

dd if=/dev/zero of=/tmp/megabyte bs=1M count=1

md5sum -b /tmp/megabyte > /tmp/megabyte.md5

%if %{checkbyvalgrind}
valgrind \
         --tool=memcheck \
         --leak-check=full \
         --track-fds=yes \
         --track-origins=yes \
         --show-reachable=yes \
         -v \
%endif
         %{buildroot}/%{_bindir}/huffar \
         /tmp/megabyte \
         -c \
         /tmp/megabyte.ha

%if %{checkbyvalgrind}
valgrind \
         --max-stackframe=8388607 \
         --tool=memcheck \
         --leak-check=full \
         --track-fds=yes \
         --track-origins=yes \
         --show-reachable=yes \
         -v \
%endif
         %{buildroot}/%{_bindir}/huffar \
         /tmp/megabyte.ha \
         -x \
         /tmp/megabyte

md5sum -c /tmp/megabyte.md5

# Blank file check.

touch /tmp/blank

%if %{checkbyvalgrind}
valgrind \
         --tool=memcheck \
         --leak-check=full \
         --track-fds=yes \
         --track-origins=yes \
         --show-reachable=yes \
         -v \
%endif
         %{buildroot}/%{_bindir}/huffar \
         /tmp/blank \
         -c \
         /tmp/blank.ha

%if %{checkbyvalgrind}
valgrind \
         --max-stackframe=8388607 \
         --tool=memcheck \
         --leak-check=full \
         --track-fds=yes \
         --track-origins=yes \
         --show-reachable=yes \
         -v \
%endif
         %{buildroot}/%{_bindir}/huffar \
         /tmp/blank.ha \
         -x \
         /tmp/blank.back
diff \
     -u \
     /tmp/blank \
     /tmp/blank.back

%files
%defattr(-,root,root)
%doc COPYING* README*
%{_bindir}/huffar

%changelog
