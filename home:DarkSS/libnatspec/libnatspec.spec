#
# spec file for package libnatspec
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define tarball %{name}-%{version}-alt2

Name:           libnatspec
Version:        0.3.1
Release:        0
Summary:        Library for national and language-specific issues
License:        LGPL-2.1+
Group:          Development/Tools/Other
Url:            https://github.com/vitlav/libnatspec
Source0:        https://github.com/vitlav/libnatspec/archive/%{version}-alt2.tar.gz#/%{tarball}.tar.gz
# PATCH-FIX-OPENSUSE vs. "W: file-contains-current-date /usr/bin/natspec".
Patch0:         libnatspec-0.3.1-no-date.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(popt)

%description
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.
See detailed description at
http://www.freesource.info/wiki/Lokalizacija/NATSPECDescription
or http://freesource.info/wiki/Lokalizacija/BibliotekaNATSPEC

%package -n natspec
Summary:        Tools for national and language-specific issues
Group:          Development/Tools/Other

%description -n natspec
Tools for national and language-specific issues.
This tool provides userful functions for
mount, submount, mkisofs, multimedia players.
This tool try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.
See detailed description at
http://www.freesource.info/wiki/Lokalizacija/NATSPECDescription
or http://freesource.info/wiki/Lokalizacija/BibliotekaNATSPEC

%package -n %{name}0
Summary:        Library for national and language-specific issues
Group:          System/Libraries

%description -n %{name}0
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.
See detailed description at
http://www.freesource.info/wiki/Lokalizacija/NATSPECDescription
or http://freesource.info/wiki/Lokalizacija/BibliotekaNATSPEC

%package -n %{name}-devel

Summary:        Development package of library for national and language-specific issues
Group:          Development/Libraries/C and C++
Requires:       %{name}0 = %{version}
Requires:       natspec

%description -n %{name}-devel
The %name-devel package contains the necessary include files
for developing applications with %name
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.

%prep
%setup -q -n %{tarball}
%patch0

%build
autoreconf -fiv
%configure
make V=1 %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la

%post -n %{name}0 -p /sbin/ldconfig

%postun -n %{name}0 -p /sbin/ldconfig

%files -n natspec
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO README-ru.html
%{_bindir}/natspec
%{_mandir}/man1/natspec.1.*

%files -n %{name}0
%defattr(-,root,root)
%{_libdir}/%{name}.so.*

%files -n %{name}-devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%{_includedir}/natspec.h
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/natspec.m4


%changelog
