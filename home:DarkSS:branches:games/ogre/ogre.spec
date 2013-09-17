#
# spec file for package ogre
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


Name:           ogre
Version:        1.8.1
Release:        0.0
%define _version %(echo %{version} | sed 's/\\./-/g')
%define soname %(echo %{version} | sed 's/\\./_/g')
%define major_minor %(echo %{version} | cut -b-3)
Summary:        Object-Oriented Graphics Rendering Engine
License:        LGPL-2.1
Group:          System/Libraries
Url:            http://www.ogre3d.org/
Source0:        http://sourceforge.net/projects/ogre/files/ogre/%{major_minor}/ogre_src_v%{_version}.tar.bz2
# PATCH-FIX-UPSTREAM ogre-1.8,1-system_tinyxml.patch reddwarf@opensuse.org -- Use system libtinyxml. The patch should be improved to make it optional before submitting upstream
Patch0:         ogre-1.8.1-system_tinyxml.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  boost-devel
BuildRequires:  cg-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  libcppunit-devel
BuildRequires:  pkg-config
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(OIS)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zziplib)
Obsoletes:      libOgreMain <= %{version}

%description
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreMain%{soname}
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Recommends:     libOgreMain%{soname}-plugins
Provides:       libOgreMain = %{version}

%description -n libOgreMain%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreMain%{soname}-plugins
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgreMain-plugins = %{version}

%description -n libOgreMain%{soname}-plugins
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world

%package -n libOgreMain%{soname}-plugin-Cg
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgreMain-plugin-Cg = %{version}

%description -n libOgreMain%{soname}-plugin-Cg
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the Cg plugin

%package -n libOgrePaging%{soname}
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgrePaging = %{version}

%description -n libOgrePaging%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreProperty%{soname}
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgreProperty = %{version}

%description -n libOgreProperty%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreRTShaderSystem%{soname}
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgreRTShaderSystem = %{version}

%description -n libOgreRTShaderSystem%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreTerrain%{soname}
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgreTerrain = %{version}

%description -n libOgreTerrain%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreMain-devel
Summary:        Ogre 3D: an open source graphics engine
Group:          Development/Libraries/C and C++
# _includedir/OGRE/Threading/OgreThreadHeadersBoost.h includes headers from boost
Requires:       boost-devel
Requires:       libOgreMain%{soname} = %{version}

%description -n libOgreMain-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the development headers.

%package -n libOgrePaging-devel
Summary:        Ogre 3D: an open source graphics engine
Group:          Development/Libraries/C and C++
Requires:       libOgrePaging%{soname} = %{version}
Requires:	libOgreMain-devel

%description -n libOgrePaging-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the development headers.

%package -n libOgreProperty-devel
Summary:        Ogre 3D: an open source graphics engine
Group:          Development/Libraries/C and C++
Requires:       libOgreProperty%{soname} = %{version}
Requires:	libOgreMain-devel

%description -n libOgreProperty-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the development headers.

%package -n libOgreRTShaderSystem-devel
Summary:        Ogre 3D: an open source graphics engine
Group:          Development/Libraries/C and C++
Requires:       libOgreRTShaderSystem%{soname} = %{version}
Requires:	libOgreMain-devel

%description -n libOgreRTShaderSystem-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the development headers.

%package -n libOgreTerrain-devel
Summary:        Ogre 3D: an open source graphics engine
Group:          Development/Libraries/C and C++
Requires:       libOgreTerrain%{soname} = %{version}
Requires:	libOgreMain-devel

%description -n libOgreTerrain-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the development headers.

%package -n ogre-demos
Summary:        Ogre 3D: an open source graphics engine
Group:          Development/Libraries/C and C++
Requires:       libOgreMain%{soname}-plugin-Cg = %{version}

%description -n ogre-demos
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains demo applications.

%package -n ogre-demos-devel
Summary:        Ogre 3D: an open source graphics engine
Group:          Development/Sources
Requires:       libOIS-devel
Requires:       libOgreMain-devel = %{version}
Requires:       libOgreRTShaderSystem-devel = %{version}
Requires:       libOgreTerrain-devel = %{version}

%description -n ogre-demos-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the source of the demo applications.

%package -n ogre-tools
Summary:        Ogre 3D: an open source graphics engine
Group:          Development/Libraries/C and C++

%description -n ogre-tools
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains various tools that make working with ogre easier.

%package -n ogre-docs
Summary:        Ogre 3D: an open source graphics engine
Group:          Documentation/Other
# libOgreMain-doc was last used in openSUSE 11.4
Provides:       libOgreMain-doc = %{version}
Obsoletes:      libOgreMain-doc < %{version}

%description -n ogre-docs
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains documentation for OGRE.

%prep
%setup -q -n ogre_src_v%{_version}
%patch0
# Be sure we use system tinyxml
rm Tools/XMLConverter/src/tiny*
rm Tools/XMLConverter/include/tiny*

# Fixes FS#30088 (crashes with skeleton animations)
sed "51 s/GNUC/GNUCC/" -i OgreMain/src/OgreSIMDHelper.h

%if 0%{?sles_version}
    sed -e "s/ -Wno-unused-but-set-parameter//" -i CMakeLists.txt
%endif


%build
mkdir build
cd build
cmake -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS:STRING="%{optflags}" \
      -DCMAKE_CXX_FLAGS:STRING="%{optflags}" \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DOGRE_LIB_DIRECTORY=%{_lib} \
      -DOGRE_INSTALL_SAMPLES=ON \
      -DOGRE_INSTALL_SAMPLES_SOURCE=ON \
      -DOGRE_INSTALL_DOCS=ON \
      ..

make %{?_smp_mflags} VERBOSE=1

%install
cd build
%make_install VERBOSE=1

# remove and link duplicate files
%fdupes %{buildroot}%{_datadir}/OGRE

%post -n libOgreMain%{soname} -p /sbin/ldconfig

%postun -n libOgreMain%{soname} -p /sbin/ldconfig

%post -n libOgrePaging%{soname} -p /sbin/ldconfig

%postun -n libOgrePaging%{soname} -p /sbin/ldconfig

%post -n libOgreProperty%{soname} -p /sbin/ldconfig

%postun -n libOgreProperty%{soname} -p /sbin/ldconfig

%post -n libOgreRTShaderSystem%{soname} -p /sbin/ldconfig

%postun -n libOgreRTShaderSystem%{soname} -p /sbin/ldconfig

%post -n libOgreTerrain%{soname} -p /sbin/ldconfig

%postun -n libOgreTerrain%{soname} -p /sbin/ldconfig

%files -n libOgreMain%{soname}
%defattr(0644,root,root,0755)
%doc AUTHORS BUGS README COPYING
%{_libdir}/libOgreMain.so.%{version}

%files -n libOgreMain%{soname}-plugins
%defattr(0644,root,root,0755)
%dir %{_libdir}/OGRE/
%{_libdir}/OGRE/RenderSystem_GL.so
%{_libdir}/OGRE/Plugin_OctreeSceneManager.so
%{_libdir}/OGRE/Plugin_ParticleFX.so
%{_libdir}/OGRE/Plugin_BSPSceneManager.so
%{_libdir}/OGRE/Plugin_OctreeZone.so
%{_libdir}/OGRE/Plugin_PCZSceneManager.so
%{_libdir}/OGRE/RenderSystem_GL.so.%{version}
%{_libdir}/OGRE/Plugin_OctreeSceneManager.so.%{version}
%{_libdir}/OGRE/Plugin_ParticleFX.so.%{version}
%{_libdir}/OGRE/Plugin_BSPSceneManager.so.%{version}
%{_libdir}/OGRE/Plugin_OctreeZone.so.%{version}
%{_libdir}/OGRE/Plugin_PCZSceneManager.so.%{version}

%files -n libOgreMain%{soname}-plugin-Cg
%defattr(0644,root,root,0755)
%dir %{_libdir}/OGRE/
%{_libdir}/OGRE/Plugin_CgProgramManager.so
%{_libdir}/OGRE/Plugin_CgProgramManager.so.%{version}

%files -n libOgrePaging%{soname}
%defattr(0644,root,root,0755)
%{_libdir}/libOgrePaging.so.%{version}

%files -n libOgreProperty%{soname}
%defattr(0644,root,root,0755)
%{_libdir}/libOgreProperty.so.%{version}

%files -n libOgreRTShaderSystem%{soname}
%defattr(0644,root,root,0755)
%{_libdir}/libOgreRTShaderSystem.so.%{version}

%files -n libOgreTerrain%{soname}
%defattr(0644,root,root,0755)
%{_libdir}/libOgreTerrain.so.%{version}

%files -n libOgreMain-devel
%defattr(0644,root,root,0755)
%dir %{_libdir}/OGRE/
%{_libdir}/OGRE/cmake/
%dir %{_includedir}/OGRE/
%{_includedir}/OGRE/*.h
%{_includedir}/OGRE/GLX/
%{_includedir}/OGRE/Plugins/
%{_includedir}/OGRE/RenderSystems/
%{_includedir}/OGRE/Threading/
%{_libdir}/libOgreMain.so
%{_libdir}/pkgconfig/OGRE.pc
%{_libdir}/pkgconfig/OGRE-PCZ.pc

%files -n libOgrePaging-devel
%defattr(0644,root,root,0755)
%{_includedir}/OGRE/Paging/
%{_libdir}/libOgrePaging.so
%{_libdir}/pkgconfig/OGRE-Paging.pc

%files -n libOgreProperty-devel
%defattr(0644,root,root,0755)
%{_includedir}/OGRE/Property/
%{_libdir}/libOgreProperty.so
%{_libdir}/pkgconfig/OGRE-Property.pc

%files -n libOgreRTShaderSystem-devel
%defattr(0644,root,root,0755)
%{_includedir}/OGRE/RTShaderSystem/
%{_libdir}/libOgreRTShaderSystem.so
%{_libdir}/pkgconfig/OGRE-RTShaderSystem.pc

%files -n libOgreTerrain-devel
%defattr(0644,root,root,0755)
%{_includedir}/OGRE/Terrain/
%{_libdir}/libOgreTerrain.so
%{_libdir}/pkgconfig/OGRE-Terrain.pc

%files -n ogre-demos
%defattr(-,root,root)
%dir %{_libdir}/OGRE/
%{_libdir}/OGRE/Samples/
%{_bindir}/SampleBrowser
%dir %{_datadir}/OGRE/
%{_datadir}/OGRE/media/
%{_datadir}/OGRE/plugins.cfg
%{_datadir}/OGRE/samples.cfg
%{_datadir}/OGRE/resources.cfg
%{_datadir}/OGRE/quakemap.cfg
%{_datadir}/OGRE/tests.cfg

%files -n ogre-demos-devel
%defattr(0644,root,root,0755)
%{_datadir}/OGRE/Samples/
%{_datadir}/OGRE/CMakeLists.txt

%files -n ogre-tools
%defattr(-,root,root)
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter

%files -n ogre-docs
%defattr(0644,root,root,0755)
%doc %{_datadir}/OGRE/docs/

%changelog
