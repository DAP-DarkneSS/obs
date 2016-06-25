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


%define lname   libbullet2_83
Name:           libbullet
Version:        2.83.7
Release:        0
Summary:        Bullet Continuous Collision Detection and Physics Library
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            http://bulletphysics.org/
Source:         https://github.com/bulletphysics/bullet3/archive/%{version}/bullet3-%{version}.tar.gz
Patch0:         fix-gtest.patch
Patch1:         fix-pkgconfig-cflags.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Bullet is a Collision Detection and Rigid Body Dynamics Library. The
Library is Open Source and free for commercial use, under the ZLib
license. This means you can use it in commercial games, even on
next-generation consoles like Sony Playstation 3.

%package -n %{lname}
Summary:        Bullet Continuous Collision Detection and Physics Library
Group:          System/Libraries
Obsoletes:      libbullet < %{version}-%{release}
Provides:       libbullet = %{version}-%{release}

%description -n %{lname}
Bullet is a Collision Detection and Rigid Body Dynamics Library. The
Library is Open Source and free for commercial use, under the ZLib
license. This means you can use it in commercial games, even on
next-generation consoles like Sony Playstation 3.

%package devel
Summary:        Development package for bullet library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This package contain all that is needed to developer or compile
appliancation with the Bullet library.

%prep
%setup -q -n bullet3-%{version}
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' README.md

%build
LIB_DIR=%{_lib}
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DINCLUDE_INSTALL_DIR="%{_includedir}/bullet" \
       -DBUILD_BULLET2_DEMOS=OFF \
       -DBUILD_OPENGL3_DEMOS=OFF

make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install
%fdupes %{buildroot}/%{_includedir}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc README.md LICENSE.txt AUTHORS.txt
%{_libdir}/libB*.so.*
%{_libdir}/libLinearMath*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/bullet/
%{_libdir}/pkgconfig/bullet.pc
%{_libdir}/libB*.so
%{_libdir}/libLinearMath*.so
%dir %{_libdir}/cmake
%{_libdir}/cmake/bullet

%changelog
