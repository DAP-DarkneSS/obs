#
# spec file for package wt
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Url:            http://www.webtoolkit.eu/wt/
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Version:        3.2.0
Release:        1
Summary:        Web Toolkit
Source0:        %{name}-%{version}.tar.bz2
Requires:       FastCGI openssl
BuildRequires:  gcc-c++
BuildRequires:  FastCGI-devel openssl-devel

# wt will build with boost-devel < 1.36.0 but it won't work
BuildRequires:  boost-devel >= 1.36.0

BuildRequires:  graphviz postgresql-devel
BuildRequires:  cmake libqt4-devel pkgconfig
BuildRequires:  fdupes
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
Requires:       FastCGI-devel openssl-devel Xerces-c-devel
Requires:       boost-devel >= 1.34.1
Requires:       mxml-devel >= 2.3
Requires:       %{name} = %{version}

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
CFLAGS=$RPM_OPT_FLAGS CXXFLAGS="$RPM_OPT_FLAGS" \
cmake .. \
    -DCMAKE_INSTALL_PREFIX="/usr" \
    -DWT_CMAKE_FINDER_INSTALL_DIR="share/cmake/Modules" \
    -DLIB_INSTALL_DIR=%{_lib} \
    -DCONNECTOR_HTTP=ON \
    -DCONNECTOR_FCGI=ON \
    -DWEBGROUP="%{WTRUNGROUP}" -DWEBUSER="%{WTRUNUSER}" \
    -DRUNDIR="%{WTRUNDIR}" \
    -DBUILD_EXAMPLES=OFF
# FIXME: Examples are temporarily disabled to avoid a boost bug that produces
# some errors while compiling the tests.
make %{?_smp_mflags}

%install
cd wt-build
make DESTDIR="$RPM_BUILD_ROOT" install
# hack for broken cmake configs on archs with /lib64
%ifarch ppc64 s390x
mv $RPM_BUILD_ROOT/usr/lib/* $RPM_BUILD_ROOT/usr/%{_lib} || true
rm -Rf $RPM_BUILD_ROOT/usr/lib
%endif
# end hack
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{WTSRVDIR}
mkdir -p $RPM_BUILD_ROOT/%{WTRUNDIR}
mkdir $RPM_BUILD_ROOT/%{_docdir}/%{name}-devel/
cp -rv ../doc/* $RPM_BUILD_ROOT/%{_docdir}/%{name}-devel/
mv -v $RPM_BUILD_ROOT/%{_datadir}/Wt $RPM_BUILD_ROOT/%{_datadir}/wt

# We mustn't package .orig files
find $RPM_BUILD_ROOT/%{_includedir}/Wt -name '*.orig' -delete

# Remove the installdox script used for the installation of documentation.
rm $RPM_BUILD_ROOT/%{_docdir}/%{name}-devel/reference/html/installdox

# Remove shell scripts used for generating some images.
rm $RPM_BUILD_ROOT/%{_datadir}/wt/resources/themes/*/*/generate.sh

%fdupes $RPM_BUILD_ROOT/%{_docdir}
%fdupes $RPM_BUILD_ROOT/%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.%{version}
%doc Changelog INSTALL LICENSE
%dir %{WTSRVDIR}
%dir /etc/wt
%{_datadir}/wt
%config(noreplace) /etc/wt/wt_config.xml
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
