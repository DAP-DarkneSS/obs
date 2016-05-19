#
# spec file for package toxcore
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


Name:           toxcore
Version:        0.0.0+git20150808.2ab3b14
Release:        0
Summary:        The future of online communications
License:        GPL-3.0
Group:          Productivity/Networking/InstantMessaging
Url:            https://github.com/irungentoo/toxcore
Source:         %{name}-%{version}.tar.xz
# I: Program returns random data in a function
# E: toxcore no-return-in-nonvoid-function ../other/bootstrap_daemon/src/log.c:78, 95
BuildRequires:  -post-build-checks
BuildRequires:  check-devel
BuildRequires:  libconfig-devel
BuildRequires:  libopus-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  libvpx-devel
BuildRequires:  pkg-config
BuildRequires:  yasm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tox aims to be an easy to use, all-in-one communication platform
that ensures their users full privacy and secure message delivery.

%package devel
Summary:	Development headers for toxcore
Group:	Development/Libraries/C and C++
Requires:	%{name} = %{version}

%description devel
Tox aims to be an easy to use, all-in-one communication platform
that ensures their users full privacy and secure message delivery.

This package provides development headers for toxcore.

%package -n libtoxav0
Summary:	Audio/Video library for toxcore
Group:	System/Libraries

%description -n libtoxav0
Audio/Video library for toxcore.

%package -n libtoxcore0
Summary:	Core library for toxcore
Group:	System/Libraries

%description -n libtoxcore0
Core library for toxcore.

%package -n libtoxdns0
Summary:	DNS library for toxcore
Group:	System/Libraries

%description -n libtoxdns0
DNS library for toxcore.

%package -n libtoxencryptsave0
Summary:	Encrypt Save library for toxcore
Group:	System/Libraries

%description -n libtoxencryptsave0
Encrypt Save library for toxcore.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure --enable-daemon
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

find %{buildroot}%{_libdir} -name "*.a" -delete -print
find %{buildroot}%{_libdir} -name "*.la" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libtoxcore0 -p /sbin/ldconfig

%post -n libtoxdns0 -p /sbin/ldconfig

%post -n libtoxencryptsave0 -p /sbin/ldconfig

%post -n libtoxav0 -p /sbin/ldconfig

%postun -n libtoxcore0 -p /sbin/ldconfig

%postun -n libtoxdns0 -p /sbin/ldconfig

%postun -n libtoxencryptsave0 -p /sbin/ldconfig

%postun -n libtoxav0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.md COPYING
%{_bindir}/DHT_bootstrap
%{_bindir}/tox-bootstrapd

%files -n libtoxav0
%defattr(-,root,root)
%{_libdir}/libtoxav.so.0
%{_libdir}/libtoxav.so.0.0.0

%files -n libtoxcore0
%defattr(-,root,root)
%{_libdir}/libtoxcore.so.0
%{_libdir}/libtoxcore.so.0.0.0

%files -n libtoxdns0
%defattr(-,root,root)
%{_libdir}/libtoxdns.so.0
%{_libdir}/libtoxdns.so.0.0.0

%files -n libtoxencryptsave0
%defattr(-,root,root)
%{_libdir}/libtoxencryptsave.so.0
%{_libdir}/libtoxencryptsave.so.0.0.0

%files devel
%defattr(-,root,root)
%{_includedir}/tox
%{_libdir}/libtoxav.so
%{_libdir}/libtoxcore.so
%{_libdir}/libtoxdns.so
%{_libdir}/libtoxencryptsave.so
%{_libdir}/pkgconfig/libtoxav.pc
%{_libdir}/pkgconfig/libtoxcore.pc

%changelog
