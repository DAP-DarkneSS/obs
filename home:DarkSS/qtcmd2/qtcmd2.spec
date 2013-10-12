#
# spec file for package qtcmd2
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


Name:           qtcmd2
Version:        20130716_1313
Release:        0
License:        GPL-2.0+
Summary:        Qt Filemanager
Url:            http://qtcmd.nes.pl/
Group:          Productivity/File utilities
Source0:        http://qtcmd.nes.pl/download/snapshots/qtcmd2-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig(QtGui)


%description
QtCommander is an advanced two-panel file manager for Linux
Operating System, similar to similar application for Microsoft
Windows named Total Commander or Krusader for KDE.


%prep
%setup -q -n %{name}
rm iconsets/default/svg2png.sh


%build
cmake \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo

# Don't use {?_smp_mflags} !
make VERBOSE=1


%install
%make_install
%fdupes -s %{buildroot}%{_datadir}/icons/%{name}/default


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc COPYING qtcmd-FAQ.txt README
%{_bindir}/%{name}
%{_prefix}/lib/lib%{name}xdgmime.so
%{_prefix}/lib/%{name}
%{_datadir}/icons/%{name}


%changelog
