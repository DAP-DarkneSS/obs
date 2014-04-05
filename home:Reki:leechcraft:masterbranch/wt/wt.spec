#
# spec file for package wt
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           wt
Version:        3.3.2
Release:        0
Summary:        Web Toolkit
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.webtoolkit.eu/wt/
Source0:        https://downloads.sourceforge.net/project/witty/wt/%{version}/wt-%{version}.tar.gz

BuildRequires:  FastCGI-devel
%if 0%{?suse_version} < 1220
BuildRequires:  Mesa-devel
%endif
# wt will build with boost-devel < 1.36.0 but it won't work
BuildRequires:  boost-devel >= 1.36.0
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
%if 0%{?suse_version} >= 1220
BuildRequires:  firebird-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  graphviz
%if 0%{?suse_version} >= 1230
BuildRequires:  libharu-devel
%endif
BuildRequires:  libqt4-devel
BuildRequires:  openssl-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel

Requires:       FastCGI
Requires:       openssl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Wt is a C++ library and application server for developing and
deploying web applications. The widget-centric API is inspired by
existing C++ GUI APIs.	It offers complete abstraction of any
web-specific implementation details.  Most importantly, the entire
application is written in only one compiled language (C++), from which
the library generates the necessary HTML, Javascript, CGI, and AJAX
code.

%package        devel
Summary:        Web Toolkit - Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       FastCGI-devel
Requires:       Xerces-c-devel
Requires:       boost-devel >= 1.34.1
Requires:       mxml-devel >= 2.3
Requires:       openssl-devel

%description devel
Development files for the Wt library.

Wt is a C++ library and application server for developping and
deploying web applications. The widget-centric API is inspired by
existing C++ GUI APIs.	It offers complete abstraction of any
web-specific implementation details.  Most imporantly, the entire
application is written in only one compiled language (C++), from which
the library generates the necessary HTML, Javascript, CGI, and AJAX
code.

%package        doc
Summary:        Web Toolkit - Doxygen Documentation
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
Doxygen documentation for the Wt library.

Wt is a C++ library and application server for developping and
deploying web applications. The widget-centric API is inspired by
existing C++ GUI APIs.  It offers complete abstraction of any
web-specific implementation details.  Most imporantly, the entire
application is written in only one compiled language (C++), from which
the library generates the necessary HTML, Javascript, CGI, and AJAX
code.

%prep
%setup -q

%build
%define WTSRVDIR /srv/wt
# path to runtime session data
%define WTRUNDIR %{WTSRVDIR}/run
# webserve user and group
%define WTRUNUSER wwwrun
%define WTRUNGROUP www
mkdir wt-build
cd wt-build
cmake .. \
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
    -DCMAKE_INSTALL_PREFIX="/usr" \
    -DLIB_INSTALL_DIR=%{_lib} \
    -DCONNECTOR_HTTP=ON \
    -DCONNECTOR_FCGI=ON \
%if 0%{?suse_version} < 1220
    -DWT_NO_BOOST_RANDOM=ON \
%endif
    -DENABLE_EXT=True \
    -DWEBGROUP="%{WTRUNGROUP}" -DWEBUSER="%{WTRUNUSER}" \
    -DRUNDIR="%{WTRUNDIR}" \
    -DBUILD_EXAMPLES=ON
make V=1 %{?_smp_mflags}

%install
cd wt-build
make V=1 DESTDIR="%{buildroot}" install
# hack for broken cmake configs on archs with /lib64
%ifarch ppc64 s390x
mv %{buildroot}/usr/lib/* %{buildroot}/usr/%{_lib} || true
rm -Rf %{buildroot}/usr/lib
%endif
# end hack
mkdir -p %{buildroot}/%{_docdir}/%{name}
mkdir -p %{buildroot}/%{WTSRVDIR}
mkdir -p %{buildroot}/%{WTRUNDIR}
mkdir %{buildroot}/%{_docdir}/%{name}-devel/
cp -rv ../doc/* %{buildroot}/%{_docdir}/%{name}-devel/
mv -v %{buildroot}/%{_datadir}/Wt %{buildroot}/%{_datadir}/wt

# We mustn't package .orig files
find %{buildroot}/%{_includedir}/Wt -name '*.orig' -delete

# Remove the installdox script used for the installation of documentation.
rm %{buildroot}/%{_docdir}/%{name}-devel/examples/html/installdox

# Remove shell scripts used for generating some images.
rm %{buildroot}/%{_datadir}/wt/resources/themes/*/*/generate.sh

# Move cmake module to the correct location.
install -v -m 0755 -d %{buildroot}/%{_datadir}/cmake/Modules
mv -v %{buildroot}/%{_prefix}/cmake/*.cmake \
      %{buildroot}/%{_datadir}/cmake/Modules

%fdupes %{buildroot}/%{_docdir}
%fdupes %{buildroot}/%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.%{version}
%doc Changelog LICENSE
%dir %{WTSRVDIR}
%dir %{_sysconfdir}/wt
%{_datadir}/wt
%config(noreplace) %{_sysconfdir}/wt/wt_config.xml
%attr(-,%{WTRUNUSER},%{WTRUNGROUP}) %{WTRUNDIR}

%files devel
%defattr(-,root,root)
%{_includedir}/Wt
%exclude %{_libdir}/*.so.%{version}
%{_libdir}/*.so.*
%{_libdir}/*.so
%exclude %{_docdir}/%{name}-devel/reference
%doc %{_docdir}/%{name}-devel
%{_datadir}/cmake/Modules/*

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}-devel/reference

%changelog
