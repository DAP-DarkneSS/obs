#
# spec file for package qtermwidget
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define qt_ver 5

%define pack_summ Qt4 terminal widget

%define pack_desc QTermWidget is an opensource project based on KDE4 \
Konsole application. The main goal of this project is to provide unicode-\
enabled, embeddable QT4 widget for using as a built-in console (or \
terminal emulation widget). Of course I`m aware about embedding \
abilities of original Konsole, but once I had Qt without KDE, and it was \
a serious problem. I decided not to rely on a chance. I could not find \
any interesting related project, so I had to write it. The original \
Konsole`s code was rewritten entirely with QT4 only; also I have to \
include in the project some parts of code from kde core library. All \
code dealing with user interface parts and session management was \
removed (maybe later I bring it back somehow), and the result is quite \
useful, I suppose.

Name:           qtermwidget-qt5
Version:        0.4.0+git.42
Release:        0
Summary:        %{pack_summ}
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/qterminal/qtermwidget
Source:         qtermwidget-%{version}.tar.gz
# git clone git://github.com/qterminal/qtermwidget.git
# cd qterminal && git archive --prefix=qtermwidget-%%{version}/ \
# --format tar.gz -9 -o qtermwidget-%%{version}.tar.gz master

BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Widgets)

%description
%{pack_desc}

%package -n libqtermwidget%{qt_ver}-0
Summary:        %{pack_summ}
Group:          Development/Libraries/C and C++
Requires:       %{name}-data >= %{version}

%description -n libqtermwidget%{qt_ver}-0
%{pack_desc}

%package data
Summary:        QTermWidget data package
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       libqtermwidget%{qt_ver}-0 = %{version}

%description data
Data files for qtermwidget library.

%package devel
Summary:        QTermWidget devel package
Group:          Development/Libraries/C and C++
Requires:       libqtermwidget%{qt_ver}-0 = %{version}

%description devel
Development environment for qtermwidget library.

%prep
%setup -q -n qtermwidget-%{version}

%build
mkdir build && cd build

# Building Qt designer plugin is not supported for Qt5 yet.
cmake .. \
        -DUSE_QT5=ON \
        -DBUILD_DESIGNER_PLUGIN=0 \
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

make V=1 %{?_smp_mflags}

%install
cd build
make V=1 install DESTDIR=%{buildroot}

%post -n libqtermwidget%{qt_ver}-0 -p /sbin/ldconfig

%postun -n libqtermwidget%{qt_ver}-0 -p /sbin/ldconfig

%files -n libqtermwidget%{qt_ver}-0
%defattr(-,root,root)
%doc AUTHORS COPYING Changelog README
%{_libdir}/libqtermwidget*.so.*

%files data
%defattr(-,root,root)
%{_datadir}/qtermwidget%{qt_ver}

%files devel
%defattr(-,root,root)
%{_includedir}/qtermwidget%{qt_ver}
%{_libdir}/libqtermwidget*.so
# %%{_libdir}/qt%%{qt_ver}/plugins/designer/libqtermwidget*plugin.so
%{_libdir}/pkgconfig/qtermwidget%{qt_ver}.pc
%{_datadir}/cmake/qtermwidget%{qt_ver}


%changelog
