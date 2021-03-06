#
# spec file for package libqxmpp
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libqxmpp
Version:        0.8.1
Release:        0
Summary:        Qt XMPP Library
License:        LGPL-2.0+
Group:          System/Libraries
Url:            https://code.google.com/p/qxmpp/
Source0:        https://qxmpp.googlecode.com/files/qxmpp-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libqt4-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvpx-devel
BuildRequires:  speex-devel

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
Provides:       libqxmpp-lc1 = %{version}
Obsoletes:      libqxmpp-lc1 < %{version}

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
Requires:       libqxmpp0 = %{version}
Provides:       libqxmpp-lc-devel = %{version}
Obsoletes:      libqxmpp-lc-devel < %{version}

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

%build
qmake \
      PREFIX=%{_prefix} \
      LIBDIR=%{_lib} \
      QMAKE_STRIP="" \
      QMAKE_CXXFLAGS+="%{optflags}" \
      QXMPP_USE_VPX=1 \
      QXMPP_USE_SPEEX=1 \
      QXMPP_USE_THEORA=1

make %{?_smp_mflags}

%install
%makeinstall INSTALL_ROOT=%{buildroot}
%fdupes %{buildroot}%{_datadir}/doc/qxmpp/

%post -n %{name}0 -p /sbin/ldconfig

%postun -n %{name}0 -p /sbin/ldconfig

%files -n %{name}0
%defattr(-,root,root)
%doc AUTHORS CHANGELOG LICENSE.LGPL README*
%{_libdir}/%{name}.so.*

%files -n %{name}-devel
%defattr(-,root,root)
%{_includedir}/qxmpp
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/qxmpp.pc

%files doc
%defattr(-,root,root)
%doc %{_datadir}/doc/qxmpp

%changelog
