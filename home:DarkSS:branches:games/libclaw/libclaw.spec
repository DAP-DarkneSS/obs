#
# spec file for package libclaw
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


%define pack_summ C++ Library of various utility functions
%define pack_desc Claw (C++ Library Absolutely Wonderful) is a C++ library \
of various utility functions. In doesn't have a particular objective but \
being useful to anyone.
Name:           libclaw
Version:        1.7.4
Release:        0
Summary:        %{pack_summ}
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://libclaw.sourceforge.net/
Source0:        http://dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
# FEATURE-OPENSUSE not to strip libs.
Patch0:         libclaw-1.6.1-nostrip.patch
# FIX-OPENSUSE to set libs dir.
Patch1:         libclaw-1.7.0-libdir.patch
# FEATURE-OPENSUSE to prevent doxygen "W: file-contains-date-and-time".
Patch2:         libclaw-doxy-w-date-time.patch
# PATCH-FIX-UPSTREAM fix-cmake.patch
Patch3:         fix-cmake.patch
BuildRequires:  boost-devel >= 1.42
BuildRequires:  cmake >= 2.8.8
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  graphviz
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel

%description
%{pack_desc}

%package        -n %{name}1
Summary:        %{pack_summ}
Group:          Development/Libraries/C and C++

%description    -n %{name}1
%{pack_desc}

%package devel
Summary:        Development files for Claw library
Group:          Development/Libraries/C and C++
Requires:       %{name}1 = %{version}
Requires:       cmake

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for Claw library
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
The %{name}-doc package contains the documentation and examples for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .nostrip
%patch1 -p1 -b .libdir
%patch2
%patch3 -p1
# Fix encoding of examples
find examples -type f |
while read F
do
        iconv -f iso8859-1 -t utf-8 $F |sed 's/\r//' >.utf8
        touch -r $F .utf8
        mv .utf8 $F
done

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install
cp -R examples %{buildroot}%{_datadir}/doc/%{name}1/examples
rm %{buildroot}%{_libdir}/*.a
%fdupes -s %{buildroot}%{_datadir}/doc/%{name}1
%find_lang %{name}

%post -n %{name}1 -p /sbin/ldconfig

%postun -n %{name}1 -p /sbin/ldconfig

%files -n %{name}1 -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc COPYING

%files devel
%defattr(-,root,root)
%{_bindir}/claw-config
%dir %{_datadir}/cmake/%{name}
%{_datadir}/cmake/libclaw/%{name}*.cmake
%{_includedir}/claw
%{_libdir}/*.so

%files doc
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}1

%changelog
