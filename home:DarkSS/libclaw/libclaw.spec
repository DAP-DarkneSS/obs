#
# spec file for package libclaw
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
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define pack_summ C++ Library of various utility functions

%define pack_desc Claw (C++ Library Absolutely Wonderful) is a C++ library \
of various utility functions. In doesn't have a particular objective but \
being useful to anyone.

Name:           libclaw
Version:        1.7.4
Release:        0
License:        LGPL-2.1+
Summary:        %{pack_summ}
Url:            http://libclaw.sourceforge.net/
Group:          System/Libraries

Source0:        http://dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
# FEATURE-OPENSUSE not to strip libs.
Patch0:         libclaw-1.6.1-nostrip.patch
# FIX-OPENSUSE to set libs dir.
Patch1:         libclaw-1.7.0-libdir.patch
# FEATURE-OPENSUSE to prevent doxygen "W: file-contains-date-and-time".
Patch2:         libclaw-doxy-w-date-time.patch

BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.8.8
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel

%description
%{pack_desc}


%package        -n %{name}1
Summary:        %{pack_summ}

%description    -n %{name}1
%{pack_desc}


%package devel
Summary:        Development files for Claw library
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       %{name}1 = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .nostrip
%patch1 -p1 -b .libdir
%patch2


%build
cmake . \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags} VERBOSE=1
find examples -type f |
while read F
do
        iconv -f iso8859-1 -t utf-8 $F |sed 's/\r//' >.utf8
        touch -r $F .utf8
        mv .utf8 $F
done


%install
make install DESTDIR=%{buildroot} VERBOSE=1
cp -R examples %{buildroot}%{_datadir}/doc/%{name}1

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
%{_libdir}/*.a
%doc %{_datadir}/doc/%{name}1

%changelog
