#
# spec file for package qtcmd2
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


Name:           qtcmd2
# NOTE CMakeLists.txt provides version:
Version:        0.3.1+git
Release:        0
Summary:        Qt Filemanager
License:        GPL-2.0+
Group:          Productivity/File utilities
Url:            http://www.qtcmd.org
Source0:        qtcmd2-%{version}.tar.xz
Source9:        qtcmd2.1

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(phonon)


%description
QtCommander is a two-panel file manager for Linux, similar to application
for Microsoft Windows named Total Commander or Krusader for KDE.


%prep
%setup -q
# SED-FIX-OPENSUSE to set right library directory:
sed -i 's/DESTINATION lib/DESTINATION %{_lib}/g' \
    libs/*/CMakeLists.txt
sed -i 's/DESTINATION lib/DESTINATION %{_lib}/g' \
    plugins/*/*/CMakeLists.txt
sed -i 's/\/..\/lib\/qtcmd2\/plugins/\/..\/%{_lib}\/qtcmd2\/plugins/g' \
    src/mainwindow.cpp

%build
cmake \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags} V=1 -k


%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c9 %{SOURCE9} | tee -a %{buildroot}%{_mandir}/man1/%{name}.1.gz
%fdupes -s %{buildroot}%{_datadir}/icons/%{name}/default


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc COPYING qtcmd-FAQ.txt README
%{_bindir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/%{name}
%{_datadir}/icons/%{name}
%exclude %{_datadir}/icons/%{name}/default/svg2png.sh
%{_mandir}/man1/%{name}.1.gz

%changelog
