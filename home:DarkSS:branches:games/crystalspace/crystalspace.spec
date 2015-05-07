#
# spec file for package crystalspace
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           crystalspace
Version:        2.0
Release:        0
# most of crystalspace is LGPLv2+, but the sndsys class (and its plugins) and
# the ceguitest demo are GPLv2+. The snsdsys class being GLPv2+ effectively
# makes crystalspace completely GPLv2+. Also the following addons are GPLv2:
# the maya2spr utility, the scripts for exporting to crystalspace format from
# 3DS max and the movierecorder plugin.
Summary:        Crystal Space is a free 3D engine
License:        GPL-2.0+ and GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.crystalspace3d.org/
Source0:        http://sourceforge.net/projects/crystal/files/crystal/2.0/crystalspace-src-2.0.tar.bz2
# PATCH-FIX-UPSTREAM crystalspace-2.0-gcc47.patch
Patch0:         crystalspace-2.0-gcc47.patch
# PATCH-FIX-UPSTREAM crystalspace-2.0-ode012.patch
Patch1:         crystalspace-2.0-ode012.patch
BuildRequires:  SDL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  assimp-devel
BuildRequires:  bison
BuildRequires:  cairomm-devel
BuildRequires:  cal3d-devel
BuildRequires:  cg-devel
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  freealut-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  jam
BuildRequires:  lib3ds-devel
BuildRequires:  libbullet-devel
BuildRequires:  libcegui-devel
BuildRequires:  libjackasyn
BuildRequires:  libjpeg-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libmng-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  ode-devel
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  speex-devel
BuildRequires:  subversion
BuildRequires:  swig
BuildRequires:  valgrind-devel
BuildRequires:  wxGTK-devel
BuildRequires:  wxWidgets-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Crystal Space is a free (LGPL) and portable 3D SDK
written in C++.

%package utils
Summary:        Utilities for Crystal Space free 3D SDK
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description utils
Utilities for Crystal Space free 3D SDK.

%package demos
Summary:        Demos for Crystal Space free 3D SDK
Group:          Development/Libraries/C and C++
Requires:       %{name}-utils = %{version}

%description demos
Demos for Crystal Space free 3D SDK.

%package devel
Summary:        C++ headers and link libraries for Crystal Space free 3D SDK
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       cegui-devel
Requires:       libGL-devel
Requires:       zlib-devel

%description devel
Headers and link libraries needed for building
projects based upon the Crystal Space 3D SDK.

%package doc
Summary:        Documentation for Crystal Space free 3D SDK
Group:          Documentation/Howto

%description doc
Documentation (manual and public API reference)
for Crystal Space free 3D SDK.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%configure --enable-shared --enable-mode=debug --disable-separate-debug-info \
  --enable-cpu-specific-optimizations=no --disable-meta-info-embedding
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

mv %{buildroot}%{_datadir}/%{name}-%{version}/bindings \
  %{buildroot}%{_libdir}/%{name}-%{version}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post utils
for map in castle flarge partsys terrain terrainf; do
  %{_bindir}/cslight -video=null $map 2>&1 > /dev/null || :
done

%files
%defattr(-,root,root,-)
%doc %dir %{_datadir}/doc/%{name}-%{version}
%doc %{_datadir}/doc/%{name}-%{version}/LICENSE
%doc %{_datadir}/doc/%{name}-%{version}/README
%doc %{_datadir}/doc/%{name}-%{version}/history*
%config(noreplace) %{_sysconfdir}/%{name}-%{version}
%{_libdir}/*.so
%{_libdir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}
%exclude %{_datadir}/%{name}-%{version}/data/config-app/autoexec.cfg
%exclude %{_datadir}/%{name}-%{version}/data/config-app/g2dtest.cfg
%exclude %{_datadir}/%{name}-%{version}/data/config-app/heightmapgen.cfg
%exclude %{_datadir}/%{name}-%{version}/data/config-app/lighter2.cfg
%exclude %{_datadir}/%{name}-%{version}/data/config-app/startme.cfg
%exclude %{_datadir}/%{name}-%{version}/data/config-app/walktest.cfg
%exclude %{_datadir}/%{name}-%{version}/data/config-app/waterdemo.cfg
%exclude %{_datadir}/%{name}-%{version}/conversion
%exclude %{_datadir}/%{name}-%{version}/build
%exclude %{_datadir}/%{name}-%{version}/data/startme.zip
%exclude %{_datadir}/%{name}-%{version}/data/ceguitest
%exclude %{_datadir}/%{name}-%{version}/data/maps
%exclude %{_libdir}/%{name}-%{version}/bindings
%{_libdir}/python2.7

%files utils
%defattr(-,root,root,-)
%{_datadir}/%{name}-%{version}/data/config-app/autoexec.cfg
%{_datadir}/%{name}-%{version}/data/config-app/heightmapgen.cfg
%{_datadir}/%{name}-%{version}/data/config-app/lighter2.cfg
%{_datadir}/%{name}-%{version}/data/config-app/walktest.cfg
%{_bindir}/*
%exclude %{_bindir}/cs-config*
%exclude %{_bindir}/ceguitest*
%exclude %{_bindir}/startme*
%{_datadir}/%{name}-%{version}/data/maps
%{_datadir}/%{name}-%{version}/conversion

%files demos
%defattr(-,root,root,-)
%{_datadir}/%{name}-%{version}/data/config-app/g2dtest.cfg
%{_datadir}/%{name}-%{version}/data/config-app/startme.cfg
%{_datadir}/%{name}-%{version}/data/config-app/waterdemo.cfg
%{_bindir}/ceguitest*
%{_bindir}/startme*
%{_datadir}/%{name}-%{version}/data/startme.zip
%{_datadir}/%{name}-%{version}/data/ceguitest

%files doc
%defattr(-,root,root,-)
%doc %dir %{_datadir}/doc/%{name}-%{version}
%doc %{_datadir}/doc/%{name}-%{version}/html

%files devel
%defattr(-,root,root,-)
%{_bindir}/cs-config*
# (vk) Scripting related files are here for now
%{_libdir}/%{name}-%{version}/bindings
%{_datadir}/%{name}-%{version}/build
%{_includedir}/%{name}-%{version}

%changelog
