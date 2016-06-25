#
# spec file for package libbullet
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


Name:           libbullet
%define lname   libbullet2_82
%define rev     2704
Version:        2.82
Release:        0
Summary:        Bullet Continuous Collision Detection and Physics Library
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            http://bulletphysics.org/
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
Source:         bullet-%{version}-r%{rev}.tar.xz
# NOTICE Please purge Extras and Glut dirs from a vanilla tarball:
# https://bullet.googlecode.com/files/bullet-{version}-r{rev}.tgz
# See more at https://bugzilla.novell.com/show_bug.cgi?id=889897
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Bullet is a Collision Detection and Rigid Body Dynamics Library. The
Library is Open Source and free for commercial use, under the ZLib
license. This means you can use it in commercial games, even on
next-generation consoles like Sony Playstation 3.

%package -n %lname
Summary:        Bullet Continuous Collision Detection and Physics Library
Group:          System/Libraries
Obsoletes:      libbullet < %{version}-%{release}
Provides:       libbullet = %{version}-%{release}

%description -n %lname
Bullet is a Collision Detection and Rigid Body Dynamics Library. The
Library is Open Source and free for commercial use, under the ZLib
license. This means you can use it in commercial games, even on
next-generation consoles like Sony Playstation 3.

%package -n %lname-devel
Summary:        Development package for bullet library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description -n %lname-devel
This package contain all that is needed to developer or compile
appliancation with the Bullet library.

%prep
%setup -q -n bullet-%{version}-r%{rev}

%build
LIB_DIR=%{_lib}
cmake . -DMAKE_SKIP_RPATH=ON \
 -DBUILD_SHARED_LIBS=ON \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DLIB_SUFFIX=${LIB_DIR#lib} \
 -DBUILD_EXTRAS=OFF \
 -DBUILD_DEMOS=OFF

make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%fdupes %{buildroot}/%{_includedir}

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_libdir}/libB*.so.*
%{_libdir}/libLinearMath*.so.*

%files -n %lname-devel
%defattr(-,root,root)
%{_includedir}/bullet/
%{_libdir}/pkgconfig/bullet.pc
%{_libdir}/libB*.so
%{_libdir}/libLinearMath*.so
%dir %{_libdir}/cmake
%{_libdir}/cmake/bullet

%changelog
