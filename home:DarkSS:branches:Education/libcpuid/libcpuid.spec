#
# spec file for package libcpuid
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


%define so_ver 13

Name:           libcpuid
Version:        0.3.0
Release:        0
Summary:        Provides CPU identification for x86
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/anrieff/libcpuid
Source0:        libcpuid-%{version}.tar.gz
# `help2man cpuid_tool > cpuid_tool.1` can't be run without so installed.
Source9:        cpuid_tool.1
ExclusiveArch:  %{ix86} x86_64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libcpuid provides CPU identification for the x86 (and x86_64).


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{so_ver} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
For details about the programming API, please see the docs
on the project's site (http://libcpuid.sourceforge.net/)


%package -n %{name}%{so_ver}
Summary:        Provides CPU identification for x86
Group:          Development/Libraries/C and C++

%description -n %{name}%{so_ver}
Libcpuid provides CPU identification for the x86 (and x86_64).


%prep
%setup -q


%build
libtoolize
autoreconf --install
%configure
make V=1 %{?_smp_mflags}


%install
make V=1 DESTDIR=%{buildroot} install

# WARNING: empty dependency_libs variable. remove the pointless .la
rm %{buildroot}%{_libdir}/*.la

# Man pages:
mkdir -p %{buildroot}%{_mandir}/man1
cp %{SOURCE9} %{buildroot}%{_mandir}/man1

%post -n %{name}%{so_ver} -p /sbin/ldconfig

%postun -n %{name}%{so_ver} -p /sbin/ldconfig


%files -n %{name}%{so_ver}
%defattr(-,root,root)
%{_libdir}/%{name}.so.*


%files devel
%defattr(-,root,root)
%{_bindir}/cpuid_tool
%{_mandir}/man1/cpuid_tool.1.*
%{_includedir}/%{name}
%{_libdir}/%{name}*
%exclude %{_libdir}/%{name}.so.*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
