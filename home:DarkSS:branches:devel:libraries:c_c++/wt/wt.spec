#
# spec file for package wt
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


%define WTSRVDIR /srv/wt
%define WTRUNDIR %{WTSRVDIR}/run
%define mysqllib libwtdbomysql39
%define pglib libwtdbopostgres39
Name:           wt
Version:        3.3.5
Release:        0
Summary:        Web Toolkit
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.webtoolkit.eu/wt/
Source0:        https://github.com/kdeforche/wt/archive/%{version}.tar.gz

BuildRequires:  FastCGI-devel
# wt will build with boost-devel < 1.36.0 but it won't work
BuildRequires:  GraphicsMagick-devel
BuildRequires:  Mesa-devel
BuildRequires:  apache-rpm-macros
BuildRequires:  boost-devel >= 1.36.0
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glu-devel
BuildRequires:  graphviz
BuildRequires:  libharu-devel
BuildRequires:  libpng-devel
BuildRequires:  libqt4-devel
BuildRequires:  mysql-devel
BuildRequires:  openssl-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  zlib-devel
Requires:       FastCGI
Requires:       openssl
Recommends:     %{name}-dbo = %{version}
Suggests:       %{name}-dbo-mysql = %{version}
Suggests:       %{name}-dbo-postgres = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Wt is a C++ library and application server for developing and
deploying web applications. The widget-centric API is inspired by
existing C++ GUI APIs.	It offers complete abstraction of any
web-specific implementation details.  Most importantly, the entire
application is written in only one compiled language (C++), from which
the library generates the necessary HTML, Javascript, CGI, and AJAX
code.

%package        dbo
Summary:        Wt::Dbo ORM library and Sqlite3 back-end
Group:          Development/Libraries

%description    dbo
This package contains the Wt::Dbo Object-Relational Mapping library
and Sqlite3 back-end of it.

%package -n %{mysqllib}
Summary:        MySQL back-end for the Wt::Dbo ORM library
Group:          Development/Libraries
Provides:       %{name}-dbo-mysql = %{version}
Requires:       %{name}-dbo = %{version}

%description -n %{mysqllib}
This package contains the MySQL back-end for the Wt::Dbo ORM library.

%package -n %{pglib}
Summary:        PostgreSQL back-end for the Wt::Dbo ORM library
Group:          Development/Libraries
Provides:       %{name}-dbo-postgres = %{version}
Requires:       %{name}-dbo = %{version}

%description -n %{pglib}
This package contains the PostgresSQL back-end for the Wt::Dbo ORM library.

%package        devel
Summary:        Web Toolkit - Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-dbo = %{version}
Requires:       %{name}-dbo-mysql = %{version}
Requires:       %{name}-dbo-postgres = %{version}
Requires:       FastCGI-devel
Requires:       Xerces-c-devel
Requires:       boost-devel >= 1.34.1
Requires:       cmake
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

%prep
%setup -q

%build
%cmake \
    -DENABLE_FIREBIRD=OFF \
    -DWT_CPP_11_MODE=-std=c++0x \
    -DUSE_SYSTEM_IBPP=ON \
    -DSHARED_LIBS=ON \
    -DMULTI_THREADED=ON \
    -DUSE_SYSTEM_SQLITE3=ON \
    -DUSE_SYSTEM_GLEW=ON \
    -DCONNECTOR_HTTP=ON \
    -DCONNECTOR_FCGI=ON \
    -DENABLE_EXT=ON \
    -DWEBGROUP="%{apache_group}" -DWEBUSER="%{apache_user}" \
    -DRUNDIR="%{WTRUNDIR}" \
    -DBUILD_EXAMPLES=ON \
    -DENABLE_GM=ON \
    -DWT_WRASTERIMAGE_IMPLEMENTATION=GraphicsMagick \
    -DENABLE_HARU=ON \
    -DENABLE_POSTGRES=ON \
    -DENABLE_SQLITE=ON \
    -DENABLE_MYSQL=ON \
    -DWT_WITH_SSL=ON \
    -DHTTP_WITH_ZLIB=ON
make V=1 %{?_smp_mflags}

%install
%cmake_install

mkdir -p %{buildroot}/%{_docdir}/%{name}
mkdir -p %{buildroot}/%{WTSRVDIR}
mkdir -p %{buildroot}/%{WTRUNDIR}
mkdir %{buildroot}/%{_docdir}/%{name}-devel/
cp -rv doc/* %{buildroot}/%{_docdir}/%{name}-devel/
mv -v %{buildroot}/%{_datadir}/Wt %{buildroot}/%{_datadir}/wt

# Remove shell scripts used for generating some images.
rm %{buildroot}/%{_datadir}/wt/resources/themes/*/*/generate.sh

%fdupes %{buildroot}/%{_docdir}
%fdupes %{buildroot}/%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post dbo -p /sbin/ldconfig

%postun dbo -p /sbin/ldconfig

%post -n %{mysqllib} -p /sbin/ldconfig

%postun -n %{mysqllib} -p /sbin/ldconfig

%post -n %{pglib} -p /sbin/ldconfig

%postun -n %{pglib} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libwt.so.*
%{_libdir}/libwtfcgi.so.*
%{_libdir}/libwthttp.so.*
%{_libdir}/libwttest.so.*
%{_libdir}/libwtext.so.*
%doc Changelog LICENSE
%dir %{WTSRVDIR}
%dir %{_sysconfdir}/wt
%{_datadir}/wt
%config(noreplace) %{_sysconfdir}/wt/wt_config.xml
%attr(-,%{apache_user},%{apache_group}) %{WTRUNDIR}

%files dbo
%defattr(-,root,root)
%{_libdir}/libwtdbo.so.*
%{_libdir}/libwtdbosqlite3.so.*

%files -n %{mysqllib}
%defattr(-,root,root)
%{_libdir}/libwtdbomysql.so.*

%files -n %{pglib}
%defattr(-,root,root)
%{_libdir}/libwtdbopostgres.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/Wt
%{_libdir}/*.so
%doc %{_docdir}/%{name}-devel

%changelog
