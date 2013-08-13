#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           libclaw
Version:        1.7.0
Release:        5%{?dist}
License:        LGPLv2
Summary:        C++ Library of various utility functions
Url:            http://libclaw.sourceforge.net/
Group:          System Environment/Libraries
Source0:        http://dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         libclaw-1.6.1-nostrip.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         libclaw-1.7.0-libdir.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch5:         libclaw-1.7.0-gcc46.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch6:         libclaw-1.7.0-zlib-fix.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gettext-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel

%description
Claw (C++ Library Absolutely Wonderful) is a C++ library of various utility
functions. In doesn't have a particular objective but being useful to
anyone.

%package devel
Summary:        Development files for Claw library
Group:          Development/Libraries
Requires:       cmake
Requires:       libclaw = %{version}

%description devel
This package contains files needed to develop and build software against
Claw (C++ Library Absolutely Wonderful).

%prep
%setup -q
%patch0 -p1 -b .nostrip
%patch1 -p1 -b .libdir
%patch5 -p1 -b .gcc46
%patch6 -p1 -b .zlibfix

%build
%cmake .
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

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%{_libdir}/*.so.*
%doc %dir %{_datadir}/doc/libclaw1
%doc %{_datadir}/doc/libclaw1/COPYING

%files devel
%{_bindir}/claw-config
%{_datadir}/cmake/libclaw/libclaw-config.cmake
%{_includedir}/claw
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%doc %{_datadir}/doc/libclaw1
%doc examples

%changelog
