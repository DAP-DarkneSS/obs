#
# spec file for package sakura
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


%define cmake_version %(rpm -q --qf='%{VERSION}' cmake || echo NOTFOUND)
%define cmake_major %(echo %{cmake_version} | cut -f1 -d.)
%define cmake_minor %(echo %{cmake_version} | cut -f2 -d.)

Name:           sakura
Version:        3.1.3
Release:        0
License:        GPL-2.0
Summary:        Terminal Emulator based on the VTE Library
Url:            https://launchpad.net/sakura
Group:          System/X11/Utilities

Source:         https://launchpad.net/sakura/trunk/%{version}/+download/sakura-%{version}.tar.bz2
Patch1:         sakura-icon.patch
Patch2:         sakura-cmake-usepkgconfig.patch
Patch4:         sakura-fix_pod2man.patch

# to convert SVG to PNG:
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libstdc++-devel
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0) >= 2.20
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vte-2.90) >= 0.28

%description
sakura is a vte-based terminal emulator. It aims to provide a terminal
emulator that only depends on GTK and VTE. It uses a notebook to allow
multiple tabs in the same window.

%prep
%setup -q
%patch1
%__mv terminal-tango.svg sakura.svg
convert sakura.svg sakura.png
%if %cmake_major == 2 && %cmake_minor < 6
%patch2
%endif
%patch4
# replace hard-coded ICON_DIR
%__sed -i -r 's|^(\s*#define\s*ICON_DIR\s+").+("\s*)$|\1%{_datadir}/pixmaps\2|g' src/sakura.c

%build
%__mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      ..

%__make %{?jobs:-j%{jobs}} VERBOSE=1 V=1
popd #build

%install
pushd build
%makeinstall
popd #build
%__rm -rf "%{buildroot}%{_datadir}/doc"

%find_lang "%{name}"

%files -f "%{name}.lang"
%defattr(-,root,root)
%doc AUTHORS GPL
%{_bindir}/sakura
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%doc %{_mandir}/man1/sakura.1%{ext_man}

%changelog
# Local Variables:
# mode: rpm-spec
# tab-width: 3
# End:
