#
# spec file for package libqxmpp
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


%define build_qt4 1
%define build_qt5 0

Name:           libqxmpp
Version:        0.8.3
Release:        0
Summary:        Qt XMPP Library
License:        LGPL-2.0+
Group:          System/Libraries
Url:            http://qxmpp.org
Source0:        https://github.com/qxmpp-project/qxmpp/archive/v%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FEATURE-OPENSUSE to make Qt5 build.
Patch0:         libqxmpp-qt5.patch

BuildRequires:  fdupes
%if %build_qt4
BuildRequires:  pkgconfig(QtCore)
%endif
%if %build_qt5
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Xml)
%endif
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vpx)

%description
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is the only
third party library it is dependent on. Users need to a have working knowledge of
C++ and Qt basics (Signals and Slots and Qt data types). The underlying TCP socket
and the XMPP RFCs (RFC3920 and RFC3921) have been encapsulated into classes and
functions. Therefore the user would not be bothered with these details. But it is
always recommended to the advanced users to read and enjoy the low level details.

%package -n %{name}0
Summary:        Qt XMPP Library
Group:          System/Libraries

%description -n %{name}0
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is the only
third party library it is dependent on. Users need to a have working knowledge of
C++ and Qt basics (Signals and Slots and Qt data types). The underlying TCP socket
and the XMPP RFCs (RFC3920 and RFC3921) have been encapsulated into classes and
functions. Therefore the user would not be bothered with these details. But it is
always recommended to the advanced users to read and enjoy the low level details.

%package -n %{name}-devel

Summary:        Qxmpp Development Files
Group:          Development/Libraries/C and C++
%if %build_qt4
Requires:       %{name}0 = %{version}
%endif
%if %build_qt5
Requires:       %{name}-0 = %{version}
%endif

%description -n %{name}-devel
It's a development package for qxmpp.

QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

%package doc
Summary:        Qxmpp library documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This packages provides documentation of Qxmpp library API.

%prep
%setup -q -n qxmpp-%{version}
%if %build_qt5
%patch0 -p1
%endif
# A hack vs. "E: arch-independent-package-contains-binary-or-object"
# after %%check.
cp -r examples doc/

%build
%if %build_qt4
qmake \
%endif
%if %build_qt5
qmake-qt5 \
%endif
      PREFIX=%{_prefix} \
      LIBDIR=%{_lib} \
      QMAKE_STRIP="" \
      QMAKE_CXXFLAGS+="%{optflags}" \
      QXMPP_USE_OPUS=1 \
      QXMPP_USE_SPEEX=1 \
      QXMPP_USE_THEORA=1 \
      QXMPP_USE_VPX=1

make V=1 %{?_smp_mflags}

%install
%makeinstall INSTALL_ROOT=%{buildroot}
%fdupes %{buildroot}%{_datadir}/doc/qxmpp/

%check
make V=1 %{?_smp_mflags} check

%post -n %{name}0 -p /sbin/ldconfig

%postun -n %{name}0 -p /sbin/ldconfig

%files -n %{name}0
%defattr(-,root,root)
%doc AUTHORS CHANGELOG LICENSE.LGPL README*
%{_libdir}/%{name}.so.*

%files -n %{name}-devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%if %build_qt4
%{_includedir}/qxmpp
%{_libdir}/pkgconfig/qxmpp.pc
%endif
%if %build_qt5
%{_includedir}/qxmpp-qt5
%{_libdir}/pkgconfig/qxmpp-qt5.pc
%endif

%files doc
%defattr(-,root,root)
%doc doc/examples

%changelog
