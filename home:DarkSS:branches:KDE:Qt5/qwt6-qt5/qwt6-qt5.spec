#
# spec file for package qwt6-qt5
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


Name:           qwt6-qt5
Version:        6.1.2+svn2432
Release:        0
Summary:        Qt5 Widgets for Technical Applications
License:        SUSE-QWT-1.0
Group:          Development/Libraries/C and C++
Url:            http://qwt.sourceforge.net/
# svn checkout svn://svn.code.sf.net/p/qwt/code/trunk qwt-code
# cd qwt-code && tar cfJ qwt-%%{version}.tar.xz qwt
Source:         qwt-%{version}.tar.xz
# PATCH-FIX-OPENSUSE to prevent 'ERROR: RPATH "/usr/local/qwt-6.1.0/lib" on
# /usr/lib(64)/qt4/plugins/designer/libqwt_designer_plugin.so is not allowed'.
Patch0:         qwt-rpath.patch
# PATCH-FIX-OPENSUSE to get parallel-installable qt5 version.
Patch1:         qwt-qt5.patch

BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
Requires:       libqwt-qt5-6 = %{version}

%description
The Qwt(Qt5) library contains GUI Components and utility classes which are
primarily useful for programs with a technical background. Beside a 2D
plot widget it provides scales, sliders, dials, compasses, thermometers,
wheels and knobs to control or display values, arrays, or ranges of type
double.

%package -n libqwt-qt5-6
Summary:        Shared library for Qt5 Widgets for Technical Applications
Group:          Development/Libraries/C and C++

%description -n libqwt-qt5-6
This package contains the shared library to run Technical Applications
developed with/for Qwt(Qt5).

%package devel
Summary:        Include headers and Qt Designer plugin for Qwt(Qt5)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       pkgconfig(Qt5Concurrent)
Requires:       pkgconfig(Qt5OpenGL)
Requires:       pkgconfig(Qt5PrintSupport)
Requires:       pkgconfig(Qt5Svg)
Recommends:     %{name}-designer
Recommends:     %{name}-devel-doc
Recommends:     %{name}-examples

%description devel
This package contains the header files of Qwt and its Qt designer plugin
in order to create Qt applications using the Qwt(Qt5) widgets.

%package examples
Summary:        Example programs using Qwt(Qt5)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description examples
This package contains example programs demonstrating the Qwt(Qt5) widgets.

%package designer
Summary:        Plugin for the Qt5 Interface designer
Group:          Development/Tools/GUI Builders
Requires:       %{name}-devel = %{version}

%description designer
The %{name}-designer package contains the plugin for the Qt5 User Interface
designer tool.

%prep
%setup -q -n qwt
%patch0
%patch1 -p1 -b .qt5

%build
export PATH=%{_libdir}/qt5/bin/:$PATH

# Now build the qwt6 library
qmake-qt5 \
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

# Examples
mkdir -p %{buildroot}/%{_bindir}
cp -r examples/bin/* %{buildroot}/%{_bindir}
rm -rf examples/bin
rm -rf examples/*/obj
cp -r examples %{buildroot}%{_docdir}/%{name}/examples
chrpath --delete %{buildroot}/%{_bindir}/*

# Designer plugin
mkdir -p %{buildroot}/%{_libdir}/qt5/plugins/designer
mv -v %{buildroot}/%{_libdir}/libqwt_designer_plugin.so %{buildroot}/%{_libdir}/qt5/plugins/designer/

# BUG: E: invalid-pkgconfig-file. Your .pc file appears to be invalid.
rm %{buildroot}/%{_libdir}/pkgconfig/Qt5Qwt6MathML.pc

%fdupes %{buildroot}

%post -n libqwt-qt5-6 -p /sbin/ldconfig
%postun -n libqwt-qt5-6 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%exclude %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%files -n libqwt-qt5-6
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
%{_libdir}/pkgconfig/*.pc
%{_libdir}/Qwt*

%files examples
%defattr(-,root,root)
%doc %{_docdir}/%{name}/examples
%{_bindir}/*

%changelog
