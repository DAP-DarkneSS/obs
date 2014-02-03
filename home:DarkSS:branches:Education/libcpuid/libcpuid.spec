#
# spec file for package libcpuid
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


Name:           libcpuid
Version:        0.1.0+git.2014.01.21
Release:        0
Summary:        Provides CPU identification for x86
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/eloaders/libcpuid
Source0:        libcpuid-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libcpuid provides CPU identification for the x86 (and x86_64).


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}11 = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
For details about the programming API, please see the docs
on the project's site (http://libcpuid.sourceforge.net/)


%package -n %{name}11
Summary:        Provides CPU identification for x86
Group:          Development/Libraries/C and C++

%description -n %{name}11
Libcpuid provides CPU identification for the x86 (and x86_64).


%prep
%setup -q


%build
%configure
make V=1 %{?_smp_mflags}


%install
make V=1 DESTDIR=%{buildroot} install
# WARNING: empty dependency_libs variable. remove the pointless .la
rm %{buildroot}%{_libdir}/*.la


%post -n %{name}11 -p /sbin/ldconfig

%postun -n %{name}11 -p /sbin/ldconfig


%files -n %{name}11
%defattr(-,root,root)
%{_libdir}/%{name}.so.*


%files devel
%defattr(-,root,root)
%{_bindir}/cpuid_tool
%{_includedir}/%{name}
%{_libdir}/%{name}*
%exclude %{_libdir}/%{name}.so.*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
