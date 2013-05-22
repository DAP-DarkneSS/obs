Name:           kQOAuth
Version:        0.97
Release:        1%{?dist}
Summary:        Qt OAuth support library

License:        LGPLv2+
URL:            https://github.com/kypeli/kQOAuth
# https://github.com/kypeli/kQOAuth/archive/0.97.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  qt4-devel

%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
kQOAuth is a OAuth 1.0 library written for Qt in C++. The goals for the
library have been to provide easy integration to existing Qt applications
utilizing Qt signals describing the OAuth process, and to provide a
convenient approach to OAuth authentication.

kQOAuth has support for retrieving the user authorization from the service
provider's website. kQOAuth will open the user's web browser to the
authorization page, give a local URL as the callback URL and setup a HTTP
server on this address to listen for the reply from the service and then
process it.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt4-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%{_qt4_qmake}
make %{?_smp_mflags}


%install
install -m 644 -pD kqoauth.prf %{buildroot}%{_libdir}/qt4/mkspecs/features/kqoauth.prf
install -m 644 -pD include/QtKOAuth %{buildroot}%{_includedir}/QtKOAuth/QtKOAuth
install -m 644 -p src/kqoauthmanager.h %{buildroot}%{_includedir}/QtKOAuth/
install -m 644 -p src/kqoauthrequest.h %{buildroot}%{_includedir}/QtKOAuth/
install -m 644 -p src/kqoauthrequest_1.h %{buildroot}%{_includedir}/QtKOAuth/
install -m 644 -p src/kqoauthrequest_xauth.h %{buildroot}%{_includedir}/QtKOAuth/
install -m 644 -p src/kqoauthglobals.h %{buildroot}%{_includedir}/QtKOAuth/
install -m 644 -D src/kqoauth.pc %{buildroot}%{_libdir}/pkgconfig/kqoauth.pc
install -m 644 lib/libkqoauth.prl %{buildroot}%{_libdir}
cp -P lib/libkqoauth.so* %{buildroot}%{_libdir}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING CHANGELOG README
%{_libdir}/libkqoauth.so.0*

%files devel
%{_includedir}/QtKOAuth/
%{_libdir}/libkqoauth.so
%{_libdir}/libkqoauth.prl
%{_libdir}/pkgconfig/kqoauth.pc
%{_libdir}/qt4/mkspecs/features/kqoauth.prf

%changelog
* Sun Mar 31 2013 Alexey Kurov <nucleo@fedoraproject.org> - 0.97-1
- Initial RPM release