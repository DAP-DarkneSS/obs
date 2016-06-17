#
# spec file for package libqxt
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


%define versionhash af08f520f71c
Name:           libqxt
Version:        0.6.2
Release:        0
Summary:        Library extending Qt
License:        CPL-1.0 and LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            https://bitbucket.org/libqxt/libqxt/wiki/Home

# SourceUrl seems to be unavailable.
Source0:        v%{version}.tar.bz2
# PATCH-FIX-OPENSUSE to support multimedia keys on keyboards.
# http://dev.libqxt.org/libqxt-old-hg/issue/75
Patch0:         libqxt-media-keys.patch
# PATCH-FIX-OPENSUSE to respect X11 event filters already set.
# http://dev.libqxt.org/libqxt/pull-request/41
Patch1:         libqxt-event-filters.patch
# PATCH-FIX-OPENSUSE to resolve build time issue via gcc6 (bnc#985109).
Patch2:         libqxt-gcc6.patch

BuildRequires:  chrpath
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(xrandr)

%description
LibQxt is an extension library for Qt providing a suite of cross-platform utility classes to add functionality not readily available in the Qt toolkit by Trolltech, a Nokia company.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}1 = %{version}-%{release}
Provides:       %{name}1-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n %{name}1
Summary:        Library extending Qt
Group:          Development/Libraries/C and C++

%description -n %{name}1
LibQxt is an extension library for Qt providing a suite of cross-platform utility classes to add functionality not readily available in the Qt toolkit by Trolltech, a Nokia company.


%prep
%setup -q -n libqxt-libqxt-%{versionhash}
%patch0 -p1
%patch1
%if 0%{?suse_version} > 1320
%patch2 -p1
%endif

%build
# Does not use GNU configure
./configure -prefix %{_prefix} -libdir %{_libdir}
make V=1 %{?_smp_mflags}

%install
make V=1 INSTALL_ROOT=%{buildroot} install
chrpath --delete %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/qt4/plugins/designer/*.so
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_includedir}/

%post -n %{name}1 -p /sbin/ldconfig

%postun -n %{name}1 -p /sbin/ldconfig

%files -n %{name}1
%defattr(-,root,root)
%{_libdir}/libQxt*.so.?*

%files devel
%defattr(-,root,root)
%{_libdir}/libQxt*.so
%{_includedir}/*
%{_libdir}/qt4/plugins/designer/libQxtDesignerPlugins.so
%{_datadir}/qt4/mkspecs/features/qxt.prf
%{_datadir}/qt4/mkspecs/features/qxtvars.prf

%changelog
