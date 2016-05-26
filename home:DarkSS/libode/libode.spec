#
# spec file for package libode
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


Name:           libode
%define lname	libode1
BuildRequires:  Mesa-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  sed
BuildRequires:  unzip
Url:            http://ode.org/
Summary:        Open Dynamics Engine Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Version:        0.11.1
Release:        0
Source0:        ode-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and
virtual creatures. It is currently used in many computer games, 3D
authoring tools and simulation tools.

Authors:
--------
    Russell Smith

%package -n %lname
Summary:        Open Dynamics Engine Library development files
Group:          System/Libraries

%description -n %lname
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and
virtual creatures. It is currently used in many computer games, 3D
authoring tools and simulation tools.

%package devel
Requires:       %lname = %version
Summary:        Open Dynamics Engine Library development files
Group:          Development/Libraries/C and C++

%description devel
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and
virtual creatures. It is currently used in many computer games, 3D
authoring tools and simulation tools.

Authors:
--------
    Russell Smith

%prep
%setup -n ode-%{version}

%build
touch NEWS README AUTHORS ChangeLog
#autoreconf -fi
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
CXXFLAGS="$CFLAGS"
export CFLAGS CXXFLAGS
export X_LIBS="-lX11"
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc LICENSE.TXT README.txt CHANGELOG.txt
%_libdir/libode.so.1*

%files devel
%defattr(-,root,root)
%_bindir/ode-config
%_includedir/ode
%_libdir/libode.so
%_libdir/pkgconfig/*.pc

%changelog
