#
# spec file for package ode
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


%define so_maj  3
%define lname   libode%{so_maj}

Name:           ode
Url:            http://ode.org/
Summary:        Open Dynamics Engine Library
License:        LGPL-2.1+ or BSD-3-Clause or Zlib
Group:          Development/Libraries/C and C++
Version:        0.13
Release:        0
Source0:        https://sourceforge.net/projects/opende/files/ODE/%{version}/ode-%{version}.tar.bz2
Source9:        ode-config.1

BuildRequires:  Mesa-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and
virtual creatures. It is currently used in many computer games, 3D
authoring tools and simulation tools.

%package -n %{lname}
Summary:        Open Dynamics Engine Library development files
Group:          System/Libraries

%description -n %{lname}
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and
virtual creatures. It is currently used in many computer games, 3D
authoring tools and simulation tools.

%package devel
Summary:        Open Dynamics Engine Library development files
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Provides:       libode-devel = %{version}

%description devel
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and
virtual creatures. It is currently used in many computer games, 3D
authoring tools and simulation tools.

%prep
%setup -q -n ode-%{version}

%build
#autoreconf -fi
CFLAGS="%{optflags} -fno-strict-aliasing"
CXXFLAGS="$CFLAGS"
export CFLAGS CXXFLAGS
export X_LIBS="-lX11"
%configure --enable-shared --disable-static
make V=1 %{?_smp_mflags}

%install
make V=1 %{?_smp_mflags} DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c9 %{SOURCE9} | tee -a %{buildroot}%{_mandir}/man1/ode-config.1.gz
find %{buildroot} -type f -name "*.la" -delete -print

%ifarch %{ix86}
# Fail.
%else
%check
make V=1 %{?_smp_mflags} check
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc LICENSE.TXT README.txt CHANGELOG.txt COPYING
%{_libdir}/libode.so.%{so_maj}.*

%files devel
%defattr(-,root,root)
%{_bindir}/ode-config
%{_mandir}/man1/ode-config.1.gz
%{_includedir}/ode
%{_libdir}/libode.so
%{_libdir}/libode.so.%{so_maj}
%{_libdir}/pkgconfig/*.pc

%changelog
