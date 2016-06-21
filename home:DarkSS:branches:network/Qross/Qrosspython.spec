#
# spec file for package Qrosspython
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


%if 0%{?suse_version} > 1320
%define cmake34 1
%else
%if 0%{?suse_version} == 1315 && 0%{?sle_version} >= 120200 && 0%{?is_opensuse}
%define cmake34 1
%else
%define cmake34 0
%endif
%endif

%if %{cmake34}
%define sopackname libqrosspython
%else
%define sopackname libqrosspython1
%endif

%define pack_summ A Qt-only fork of Kross

%define pack_desc Qross is a Qt-only fork of Kross, \
the KDE scripting framework. \
\
The Qross scripting framework is not a scripting language itself. \
It merely serves to plug into C++/Qt applications the support for \
other, already existing scripting languages, like JavaScript or \
Python.

Name:           Qrosspython
Version:        0.3.1
Release:        0
Summary:        %{pack_summ}, python2 engine
License:        LGPL-2.0+
Group:          System/Libraries
Url:            https://github.com/0xd34df00d/Qross
# WARNING: don't forget to remove at least
# src/bindings/csharp directory from upstream sources,
# really only src/bindings/python works now, see more at
# https://bugzilla.novell.com/show_bug.cgi?id=861882
Source0:        Qross-%{version}.tar.xz
# https://github.com/0xd34df00d/Qross/commit/9053d214840
# PATCH-FIX-UPSTREAM vs. cmake3 compatibility issue.
Patch0:         Qrosspython-cmake3.patch

BuildRequires:  Qross-devel
BuildRequires:  cmake >= 3
BuildRequires:  pkgconfig
BuildRequires:  python-sip-devel
BuildRequires:  pkgconfig(python2)
%if %{cmake34}
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}
%endif

%description
%{pack_desc}

%package        -n %{sopackname}
Summary:        %{pack_summ}
Group:          System/Libraries
# NOTE! There are no linking against this library so let's take care
# about backward compatibility:
%if %{cmake34}
Provides:       libqrosspython1 = %{version}
Obsoletes:      libqrosspython1 < %{version}
%endif

%description    -n %{sopackname}
%{pack_desc}

%if %{cmake34} == 0
%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{sopackname} = %{version}

%description    devel
The %{name}-devel package contains files for
developing applications that use %{name}.
%endif

%prep
%setup -q -n Qross-%{version}/src/bindings/python/qrosspython
%patch0 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%post   -n %{sopackname} -p /sbin/ldconfig

%postun -n %{sopackname} -p /sbin/ldconfig

%files -n %{sopackname}
%defattr(-,root,root)
%if %{cmake34} == 0
%{_libdir}/*qrosspython*.so.*
%else
%{_libdir}/*qrosspython*.so
%endif

%if %{cmake34} == 0
%files devel
%defattr(-,root,root)
%{_libdir}/*qrosspython*.so
%endif

%changelog
