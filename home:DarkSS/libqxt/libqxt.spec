#
# spec file for package libqxt
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


%define versionhash af08f520f71c
Name:           libqxt
Version:        0.6.2
Release:        0
Summary:        Library extending Qt
License:        CPL-1.0 and LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            http://libqxt.org/
Source0:        v%{version}.tar.bz2
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  libdb-4_8-devel
BuildRequires:  libqt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
License:        CPL-1.0 and LGPL-2.1

%description -n %{name}1
LibQxt is an extension library for Qt providing a suite of cross-platform utility classes to add functionality not readily available in the Qt toolkit by Trolltech, a Nokia company.


%prep
%setup -q -n libqxt-libqxt-%{versionhash}

%build
./configure -prefix /usr -libdir %{_libdir}
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
chrpath --delete %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/qt4/plugins/designer/*.so
find %{buildroot} -name '*.la' -exec rm -f {} ';'
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
