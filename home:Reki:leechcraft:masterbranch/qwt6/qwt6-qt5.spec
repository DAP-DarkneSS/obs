#
# spec file for package qwt6-qt5
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


%define build_qt4 0
%define build_qt5 1

Name:           qwt6-qt5
Version:        6.1.2
Release:        0
Summary:        Qt Widgets for Technical Applications
License:        SUSE-QWT-1.0
Group:          Development/Libraries/C and C++
Url:            http://qwt.sourceforge.net/
Source:         http://switch.dl.sourceforge.net/sourceforge/qwt/qwt-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE to prevent 'ERROR: RPATH "/usr/local/qwt-6.1.0/lib" on
# /usr/lib(64)/qt4/plugins/designer/libqwt_designer_plugin.so is not allowed'.
Patch0:         qwt-rpath.patch

BuildRequires:  freetype2-devel
BuildRequires:  libpng-devel
%if 0%{?suse_version} >= 1100
BuildRequires:  fdupes
%endif
%if %build_qt4
BuildRequires:  pkgconfig(QtCore)
%endif
%if %build_qt5
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
%endif
Requires:       libqwt-qt5_6 = %{version}

%description
The Qwt library contains GUI Components and utility classes which are
primarily useful for programs with a technical background. Beside a 2D
plot widget it provides scales, sliders, dials, compasses, thermometers,
wheels and knobs to control or display values, arrays, or ranges of type
double.

%package -n libqwt-qt5_6
Summary:        Shared library for Qt Widgets
Group:          Development/Libraries/C and C++

%description -n libqwt-qt5_6
This package contains the shared library to run Technical Applications
developed with/for Qwt.

%package devel
Summary:        Include headers and Qt Designer plugin for Qwt
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       freetype2-devel
Requires:       gcc-c++
Requires:       libpng-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       qt-devel
%if 0%{?suse_version}
Recommends:     %{name}-devel-doc
Recommends:     %{name}-examples
%endif
Conflicts:      qwt-devel

%description devel
This package contains the header files of Qwt and its Qt designer plugin
in order to create Qt applications using the Qwt widgets.

%package examples
Summary:        Example programs using Qwt
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description examples
This package contains example programs demonstrating the Qwt widgets.

%package designer
Summary:        Plugin for the Qt Interface designer
Group:          Development/Tools/GUI Builders
Requires:       %{name}-devel = %{version}
Requires:       qt-devel

%description designer
The %{name}-designer package contains the plugin for the Qt User Interface
designer tool.

%package devel-doc
Summary:        Development documentation for Qwt
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-doc
This package contains the development documentation of the Qwt widgets
as is it created by doxygen.

%prep
%setup -q -n qwt-%{version}
%patch0

%build
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
%if %build_qt4
export PATH=%{_libdir}/qt4/bin/:$PATH
%endif
%if %build_qt5
export PATH=%{_libdir}/qt5/bin/:$PATH
%endif
%endif

# Now build the qwt6 library
%if %build_qt4
qmake \
%endif
%if %build_qt5
qmake-qt5 \
%endif
	QMAKE_STRIP="" \
	QWT_INSTALL_PREFIX=%{_prefix} \
	CONFIG+=QwtDll CONFIG+=QwtDesigner CONFIG+=QwtExamples -after \
	QMAKE_CXXFLAGS="%{optflags}" \
	target.path=%{_libdir} \
	headers.path=%{_includedir}/%{name} \
	qwtspec.path=%{_datadir}/%{name}/features \
	qwtmathmlspec.path=%{_datadir}/%{name}/features \
	doc.path=%{_docdir}/%{name}-devel-doc

make V=1 %{?_smp_mflags}

%install
make V=1 DESTDIR=%{buildroot} install INSTALL_ROOT=%{buildroot}

# Documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp COPYING README %{buildroot}%{_docdir}/%{name}
cp -r examples %{buildroot}%{_docdir}/%{name}/examples

# Designer plugin
%if %build_qt4
mkdir -p %{buildroot}/%{_libdir}/qt4/plugins/designer
mv -v %{buildroot}/%{_libdir}/libqwt_designer_plugin.so %{buildroot}/%{_libdir}/qt4/plugins/designer/
%endif
%if %build_qt5
mkdir -p %{buildroot}/%{_libdir}/qt5/plugins/designer
mv -v %{buildroot}/%{_libdir}/libqwt_designer_plugin.so %{buildroot}/%{_libdir}/qt5/plugins/designer/
%endif

%if 0%{?suse_version} >= 1100
%fdupes %{buildroot}
%endif

%if %build_qt4
%post -n libqwt6 -p /sbin/ldconfig
%postun -n libqwt6 -p /sbin/ldconfig
%endif
%if %build_qt5
%post -n libqwt-qt5_6 -p /sbin/ldconfig
%postun -n libqwt-qt5_6 -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%exclude %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%files -n libqwt-qt5_6
%defattr(-,root,root)
%{_libdir}/libqwt*
%exclude %{_libdir}/libqwt*.so

%files designer
%defattr(-,root,root)
%{_libdir}/qt5/plugins/designer/libqwt_designer_plugin.so

%files devel
%defattr(-,root,root)
%{_libdir}/libqwt*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_datadir}/%{name}

%files examples
%defattr(-,root,root)
%doc %{_docdir}/%{name}/examples

%files devel-doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}-devel-doc

%changelog
