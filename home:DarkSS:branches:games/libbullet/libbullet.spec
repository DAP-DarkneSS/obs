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


%define sover   2_83
%define lname   libbullet%{sover}
%define pdesc   Bullet is a Collision Detection and Rigid Body Dynamics \
Library. The Library is Open Source and free for commercial use, under \
the ZLib license. This means you can use it in commercial games, even on \
next-generation consoles like Sony Playstation 3.

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
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)

%description
%{pdesc}

%package -n %{lname}
Summary:        Bullet Continuous Collision Detection and Physics Library
Group:          System/Libraries
Obsoletes:      libbullet < %{version}-%{release}
Provides:       libbullet = %{version}-%{release}

%description -n %{lname}
%{pdesc}

%package -n libBulletFileLoader%{sover}
Summary:        Bullet File Loader Library
Group:          System/Libraries

%description -n libBulletFileLoader%{sover}
%{pdesc}

%package -n libBulletInverseDynamicsUtils%{sover}
Summary:        Bullet Inverse Dynamics Utils Library
Group:          System/Libraries

%description -n libBulletInverseDynamicsUtils%{sover}
%{pdesc}

%package -n libBulletWorldImporter%{sover}
Summary:        Bullet World Importer Library
Group:          System/Libraries

%description -n libBulletWorldImporter%{sover}
%{pdesc}

%package -n libBulletXmlWorldImporter%{sover}
Summary:        Bullet Xml World Importer Library
Group:          System/Libraries

%description -n libBulletXmlWorldImporter%{sover}
%{pdesc}

%package -n libConvexDecomposition%{sover}
Summary:        Bullet Convex Decomposition Library
Group:          System/Libraries

%description -n libConvexDecomposition%{sover}
%{pdesc}

%package -n libGIMPACTUtils%{sover}
Summary:        Bullet GIMPACT Utils Library
Group:          System/Libraries

%description -n libGIMPACTUtils%{sover}
%{pdesc}

%package -n libHACD%{sover}
Summary:        Bullet HACD Library
Group:          System/Libraries

%description -n libHACD%{sover}
%{pdesc}

%package devel
Summary:        Development package for bullet library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libBulletFileLoader%{sover} = %{version}
Requires:       libBulletInverseDynamicsUtils%{sover} = %{version}
Requires:       libBulletWorldImporter%{sover} = %{version}
Requires:       libBulletXmlWorldImporter%{sover} = %{version}
Requires:       libConvexDecomposition%{sover} = %{version}
Requires:       libGIMPACTUtils%{sover} = %{version}
Requires:       libHACD%{sover} = %{version}
Provides:       bullet-fileloader
Provides:       bullet-worldimporter

%description devel
This package contain all that is needed to developer or compile
appliancation with the Bullet library.

%prep
%setup -q -n bullet3-%{version}
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' README.md

%build
tmpflags="%{optflags} -fno-strict-aliasing"
%ifarch %ix86
%if 0%{suse_version} == 1320
tmpflags="${tmpflags} -fno-stack-protector"
%endif
%endif
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_FLAGS="${tmpflags}" \
       -DCMAKE_CXX_FLAGS="${tmpflags}" \
       -DINCLUDE_INSTALL_DIR="%{_includedir}/bullet" \
       -DBUILD_SHARED_LIBS=ON \
       -DBUILD_EXTRAS=ON \
       -DBUILD_CPU_DEMOS=OFF \
       -DINSTALL_LIBS=ON \
       -DINSTALL_EXTRA_LIBS=on \
       -DBUILD_BULLET2_DEMOS=OFF \
       -DBUILD_OPENGL3_DEMOS=OFF

make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install
%fdupes %{buildroot}/%{_includedir}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%post -n libBulletFileLoader%{sover} -p /sbin/ldconfig
%postun -n libBulletFileLoader%{sover} -p /sbin/ldconfig

%post -n libBulletInverseDynamicsUtils%{sover} -p /sbin/ldconfig
%postun -n libBulletInverseDynamicsUtils%{sover} -p /sbin/ldconfig

%post -n libBulletWorldImporter%{sover} -p /sbin/ldconfig
%postun -n libBulletWorldImporter%{sover} -p /sbin/ldconfig

%post -n libBulletXmlWorldImporter%{sover} -p /sbin/ldconfig
%postun -n libBulletXmlWorldImporter%{sover} -p /sbin/ldconfig

%post -n libConvexDecomposition%{sover} -p /sbin/ldconfig
%postun -n libConvexDecomposition%{sover} -p /sbin/ldconfig

%post -n libGIMPACTUtils%{sover} -p /sbin/ldconfig
%postun -n libGIMPACTUtils%{sover} -p /sbin/ldconfig

%post -n libHACD%{sover} -p /sbin/ldconfig
%postun -n libHACD%{sover} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc README.md LICENSE.txt AUTHORS.txt
%{_libdir}/libB*.so.*
%{_libdir}/libLinearMath*.so.*
%exclude %{_libdir}/libBulletFileLoader.so.*
%exclude %{_libdir}/libBulletInverseDynamicsUtils.so.*
%exclude %{_libdir}/libBulletWorldImporter.so.*
%exclude %{_libdir}/libBulletXmlWorldImporter.so.*

%files -n libBulletFileLoader%{sover}
%defattr(-,root,root)
%{_libdir}/libBulletFileLoader.so.*

%files -n libBulletInverseDynamicsUtils%{sover}
%defattr(-,root,root)
%{_libdir}/libBulletInverseDynamicsUtils.so.*

%files -n libBulletWorldImporter%{sover}
%defattr(-,root,root)
%{_libdir}/libBulletWorldImporter.so.*

%files -n libBulletXmlWorldImporter%{sover}
%defattr(-,root,root)
%{_libdir}/libBulletXmlWorldImporter.so.*

%files -n libConvexDecomposition%{sover}
%defattr(-,root,root)
%{_libdir}/libConvexDecomposition.so.*

%files -n libGIMPACTUtils%{sover}
%defattr(-,root,root)
%{_libdir}/libGIMPACTUtils.so.*

%files -n libHACD%{sover}
%defattr(-,root,root)
%{_libdir}/libHACD.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/bullet/
%{_libdir}/pkgconfig/bullet.pc
%{_libdir}/lib*.so
%{_libdir}/cmake/bullet

%changelog
