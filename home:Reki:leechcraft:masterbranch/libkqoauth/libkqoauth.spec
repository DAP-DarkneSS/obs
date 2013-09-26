#
# spec file for package libkqoauth
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define pack_summ C++/Qt OAuth 1.0 RFC 5849 library

%define pack_desc kQOAuth is a OAuth 1.0 library written for Qt in C++. \
The goals for the library have been to provide easy integration to existing \
Qt applications utilizing Qt signals describing the OAuth process, and to provide a \
convenient approach to OAuth authentication. \
\
kQOAuth has support for retrieving the user authorization from the service \
provider's website. kQOAuth will open the user's web browser to the \
authorization page, give a local URL as the callback URL and setup a HTTP \
server on this address to listen for the reply from the service and then \
process it.


Name:           libkqoauth
Version:        0.97
Release:        0
License:        LGPL-2.1+ and LGPL-3.0+
Summary:        %{pack_summ}
Group:          System/Libraries

Url:            https://github.com/kypeli/kQOAuth
# https://github.com/kypeli/kQOAuth/archive/0.97.tar.gz
Source0:        kQOAuth-%{version}.tar.gz
Patch0:         libdir.patch

BuildRequires:  pkgconfig(QtNetwork) >= 4.7

%description
%{pack_desc}


%package        -n %{name}0
Summary:        %{pack_summ}
Group:          System/Libraries

%description    -n %{name}0
%{pack_desc}


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}0 = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n kQOAuth-%{version}
%patch0 -p1


%build
qmake \
PREFIX=%{_prefix} \
KQOAUTH_LIBDIR=%{_libdir} \
QMAKE_STRIP="" \
QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}


%install
%make_install INSTALL_ROOT=%{buildroot}


%post -n %{name}0 -p /sbin/ldconfig

%postun -n %{name}0 -p /sbin/ldconfig


%files -n %{name}0
%defattr(-,root,root)
%doc COPYING CHANGELOG README*
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/QtKOAuth/
%{_libdir}/%{name}.so
%{_libdir}/%{name}.prl
%{_libdir}/pkgconfig/kqoauth.pc
%{_datadir}/qt4/mkspecs/features/kqoauth.prf

%changelog
