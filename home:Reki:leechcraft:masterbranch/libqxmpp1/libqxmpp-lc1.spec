#
# spec file for package libqxmpp1
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           libqxmpp-lc1
Version:        0.3.47.1
Release:        3
License:        LGPL-2.0+
Source0:        qxmpp-dev-%{version}.tar.bz2
#Source0:        https://github.com/downloads/0xd34df00d/qxmpp-dev/qxmpp-0.3.45.1-extras.tar.bz2 
Source1:        baselibs.conf
#Patch0:    qxmpp.patch
Patch0:         qxmpp-dynamiclib.patch
Group:          System/Libraries
Summary:        Qt XMPP Library
Url:            https://github.com/0xd34df00d/qxmpp-dev

Provides:       libqxmpp1 = %{version}
Obsoletes:      libqxmpp1 < %{version}

BuildRequires:  libqt4-devel
BuildRequires:  speex-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.
 
QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is the only
third party library it is dependent on. Users need to a have working knowledge of
C++ and Qt basics (Signals and Slots and Qt data types). The underlying TCP socket
and the XMPP RFCs (RFC3920 and RFC3921) have been encapsulated into classes and
functions. Therefore the user would not be bothered with these details. But it is
always recommended to the advanced users to read and enjoy the low level details.

%package -n libqxmpp-lc-devel


Summary:        Qxmpp Development Files
Group:          Development/Libraries/C and C++
Requires:       libqxmpp-lc1 = %{version}

Provides:       libqxmpp-devel = %{version}
Obsoletes:      libqxmpp-devel < %{version}

%description -n libqxmpp-lc-devel
It's a development package for qxmpp.

QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

%prep
%setup -q -n qxmpp-dev-%{version}
%patch0

%build
qmake PREFIX=%{_prefix} QMAKE_STRIP="" QMAKE_CXXFLAGS+="%{optflags}"
%__make %{?_smp_mflags}

%install
%makeinstall INSTALL_ROOT=%{buildroot}
%ifarch x86_64
%__mv %{buildroot}/usr/{lib,lib64}
%endif

%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG LICENSE.LGPL README
%{_libdir}/libqxmpp-lc.so.*

%files -n libqxmpp-lc-devel
%defattr(-,root,root,-)
%{_includedir}/qxmpp-lc
%{_libdir}/libqxmpp-lc.so
%{_libdir}/pkgconfig/qxmpp-lc.pc

%changelog
