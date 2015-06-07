#
# spec file for package megaglest
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           megaglest
Version:        3.11.1
Release:        0
Summary:        Free 3D Real-Time Customizable Strategy Game
License:        GPL-2.0+
Group:          Amusements/Games/Strategy/Real Time
Url:            http://megaglest.org/

Source:         https://github.com/MegaGlest/megaglest-source/releases/download/%{version}/%{name}-source-%{version}.tar.xz
# PATCH-FIX-UPSTREAM vs. Factory's "undefined reference to symbol XLoadQueryFont".
Patch0:         http://filux.megaglest.org/patches/megaglest-3.11.1_cmake3.2-x11.patch

BuildRequires:  boost-jam
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  krb5-devel
BuildRequires:  libcares-devel
BuildRequires:  libdrm-devel
BuildRequires:  libidn-devel
BuildRequires:  libircclient-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpng-devel
BuildRequires:  libssh2-devel
BuildRequires:  libvorbis-devel
BuildRequires:  lua-devel
BuildRequires:  openldap2-devel
BuildRequires:  subversion
BuildRequires:  pkgconfig(libxml-2.0)
%if 0%{?suse_version} > 1210
BuildRequires:  libGLw-devel
%endif
%if 0%{?suse_version} <= 1210
BuildRequires:  MesaGLw-devel
%endif
%if 0%{?suse_version}
BuildRequires:  libSDL-devel
BuildRequires:  libcurl-devel >= 7.21
BuildRequires:  libopenssl-devel
BuildRequires:  openal-soft-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-Mesa-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xz
%endif
%if 0%{?suse_version} < 1140
BuildRequires:  wxGTK-compat
BuildRequires:  wxGTK-devel
BuildRequires:  wxGTK-gl
%endif
%if 0%{?suse_version} >= 1140
BuildRequires:  wxWidgets-devel
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
%endif
%if 0%{?suse_version} >= 1120
BuildRequires:  libxerces-c-devel
%endif
%if 0%{?suse_version} < 1120
BuildRequires:  libXerces-c-devel
%endif
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
BuildRequires:  SDL-devel
BuildRequires:  libX11-devel
BuildRequires:  libcurl-devel
BuildRequires:  libssl-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openal-soft-devel
BuildRequires:  wxBase
BuildRequires:  wxGTK-devel
BuildRequires:  xerces-c-devel
BuildRequires:  xorg-x11-Mesa-devel
%endif
%if 0%{?mandriva_version}
BuildRequires:  libSDL-devel
BuildRequires:  libSDL-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmesaglu-devel
BuildRequires:  libmesaglu-devel
BuildRequires:  libmesaglw
BuildRequires:  libmesaglw
BuildRequires:  libopenal-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libx11-devel
BuildRequires:  wxgtku-devel
BuildRequires:  xerces-c-devel
%endif
Requires:       freefont
Requires:       gnu-free-fonts
Requires:       linux-libertine-fonts
Requires:       megaglest-data >= %{version}
Requires:       p7zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MegaGlest takes place in a context that could be compared to that of
pre-Renaissance Europe with the license that magic forces exist in the
environment and can be controlled.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
#
mkdir build
cd build
cmake -DCFLAGS="%{optflags}" -DCXXFLAGS="%{optflags}" -DWANT_SVN_STAMP=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
# unforce link against libcurl.a
find . -name link.txt -exec sed -ie 's!/usr/lib/libcurl.a!-lcurl!g' {} \;
find . -name link.txt -exec sed -ie 's!/usr/lib64/libcurl.a!-lcurl!g' {} \;
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_datadir}/%{name}/data

%files
%defattr(-, root, root)
%{_bindir}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/pixmaps/
%{_datadir}/applications/

%changelog
