#
# spec file for package webmounter
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


Name:           webmounter
Version:        git
Release:        0
License:        LGPL-2.1+
Summary:        A tool to map any http storage as local directory
Url:            https://github.com/ershovdz/webmounter_public
Group:          Productivity/Networking/File-Sharing
Source0:        %{name}-%{version}.tar.xz
# PATCH-OPENSUSE-FIX to build whatever…
Patch0:         min.patch

BuildRequires:  boost-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(QJson)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcurl)

%description
Storages supported by default: Google docs, Yandex.Fotki, Yandex.Disk,
Yandex.Narod, Facebook, Vkontakte.

At startup WebMounter creates local drive with mirrors of remote http
storages. All operations with local files automatically translated to
remote storage.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1


%build
qmake \
      QMAKE_STRIP="" \
      QMAKE_CFLAGS+="%{optflags} -fpermissive"
      QMAKE_CXXFLAGS+="%{optflags} -fpermissive"

make VERBOSE=1 %{?_smp_mflags}


%install
%make_install INSTALL_ROOT=%{buildroot}


%files
%defattr(-,root,root)
%doc Licence Readme
%{_datadir}/%{name}
%dir %{_prefix}/lib/%{name}
%dir %{_prefix}/lib/%{name}/*
%{_prefix}/lib/%{name}/*/libwm*.so.*


%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_prefix}/lib/pkgconfig/libwm*.pc
%dir %{_prefix}/lib/%{name}
%dir %{_prefix}/lib/%{name}/*
%{_prefix}/lib/%{name}/*/libwm*.so


%changelog
