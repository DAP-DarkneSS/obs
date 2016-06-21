#
# spec file for package Qross
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


%define so_postfix 0_1

%define pack_summ A Qt-only fork of Kross

%define pack_desc Qross is a Qt-only fork of Kross, \
the KDE scripting framework. \
\
The Qross scripting framework is not a scripting language itself. \
It merely serves to plug into C++/Qt applications the support for \
other, already existing scripting languages, like JavaScript or \
Python.

Name:           Qross
Version:        0.3.1
Release:        0
Summary:        %{pack_summ}
License:        LGPL-2.0+
Group:          System/Libraries
Url:            https://github.com/0xd34df00d/Qross
# WARNING: don't forget to remove at least
# src/bindings/csharp directory from upstream sources,
# really only src/bindings/python works now, see more at
# https://bugzilla.novell.com/show_bug.cgi?id=861882
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  cmake >= 3
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(QtCore)

%description
%{pack_desc}

%package        -n libqross%{so_postfix}
Summary:        %{pack_summ}
Group:          System/Libraries

%description    -n libqross%{so_postfix}
%{pack_desc}

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       libqross%{so_postfix} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(QtCore)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}/src/qross

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%fdupes -s %{buildroot}%{_datadir}

%post   -n libqross%{so_postfix} -p /sbin/ldconfig

%postun -n libqross%{so_postfix} -p /sbin/ldconfig

%files -n libqross%{so_postfix}
%defattr(-,root,root)
%{_libdir}/*qross*.so.*
%{_libdir}/qt4/plugins/script/*qross*.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/qross
%{_includedir}/qross
%{_libdir}/*qross*.so
%{_libdir}/qt4/plugins/script/*qross*.so
%dir %{_datadir}/leechcraft
%dir %{_datadir}/leechcraft/cmake
%{_datadir}/*/*/FindQrosscore.cmake

%changelog
