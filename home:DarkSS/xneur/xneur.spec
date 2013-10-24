#
# spec file for package xneur
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define major   16

Name:           xneur
Version:        0.16.0
Release:        0
License:        GPL-2.0+
Summary:        X Neural Switcher
Url:            http://www.xneur.ru
Group:          System/X11/Utilities
Source0:        http://dists.xneur.ru/release-%{version}/tgz/%{name}-%{version}.tar.bz2
BuildRequires:  alsa-utils
BuildRequires:  fdupes
BuildRequires:  xosd-devel
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpcre)
Requires:       alsa-utils
Requires:       aspell
Recommends:     %{name}-lang
Recommends:     gxneur
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
X Neural Switcher (XNeur).
Automatical switcher of keyboard layout.

%package -n libxneur-devel
Summary:        Include Files and Libraries
Group:          Development/Libraries/X11
Requires:       libxneur%{major} = %{version}
Requires:       pkgconfig(enchant)
Provides:       xneur-devel = %{version}
Obsoletes:      xneur-devel < 0.9.9

%description -n libxneur-devel
Development files for the package XNeur.

%package -n libxneur%{major}
Summary:        XNeur Shared Library
Group:          System/Libraries

%description -n libxneur%{major}
Shared libraries for the package XNeur.

%lang_package

%prep
%setup -q

%build
%configure \
    --disable-static \
    --with-sound=aplay \
    --with-gtk=gtk2 \
    --with-spell=enchant
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/{%{name}/*.*a,*.*a}
rm -rf %{buildroot}%{_datadir}/icons/hicolor
%fdupes -s %{buildroot}%{_datadir}
%find_lang %{name}

%post -n libxneur%{major} -p /sbin/ldconfig

%postun -n libxneur%{major} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_libdir}/%{name}/
%doc %{_mandir}/man?/*
%dir %{_sysconfdir}/%{name}/
# Upstream updates a config file. So we must replace it.
%config %{_sysconfdir}/%{name}/*

%files -n libxneur%{major}
%defattr(-,root,root,-)
%{_libdir}/libxn*.so.*

%files -n libxneur-devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang

%changelog
