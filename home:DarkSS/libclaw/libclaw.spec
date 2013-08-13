Name:           libclaw
Version:        1.7.0
Release:        5%{?dist}
Summary:        C++ Library of various utility functions
Group:          System Environment/Libraries
License:        LGPLv2
URL:            http://libclaw.sourceforge.net/
Source0:        http://dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         libclaw-1.6.1-nostrip.patch
Patch1:         libclaw-1.7.0-libdir.patch
Patch5:         libclaw-1.7.0-gcc46.patch
Patch6:		libclaw-1.7.0-zlib-fix.patch
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:	gettext-devel
BuildRequires:	boost-devel

%description
Claw (C++ Library Absolutely Wonderful) is a C++ library of various utility
functions. In doesn't have a particular objective but being useful to
anyone.

%package devel
Summary:        Development files for Claw library
Group:          Development/Libraries
Requires:       libclaw = %{version}-%{release}
Requires:       cmake

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
make install DESTDIR=$RPM_BUILD_ROOT VERBOSE=1

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
* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-5
- Rebuilt for c++ ABI breakage

* Sun Feb  5 2012 Tom Callaway <spot@fedoraproject.org> - 1.7.0-4
- fix png.hpp to include zlib.h

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.7.0-2
- Rebuild for new libpng

* Thu Aug 25 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.0-1
- update to 1.7.0

* Mon Apr 18 2011 Tom Callaway <spot@fedoraproject.org> - 1.6.1-1
- update to 1.6.1

* Fri Feb 11 2011 Lubomir Rintel <lkundrak@v3.sk> - 1.5.4-7
- Fix Rawhide build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.5.4-5
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.4-4
- Fix wrong return type of 'claw::log_system::operator<<'
- Fix incorrect return type in basic_socket.

* Fri Oct 23 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5.4-3
- Really fix the examples encoding

* Fri Oct 02 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5.4-2
- Merge in changes from Xavier Bachelot's package:
- More sensible Group name
- Fix libdir name for 64bit archs
- Add examples to documentation
- Fix examples encoding
- Let -devel require cmake


* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5.4-1
- Initial packaging
