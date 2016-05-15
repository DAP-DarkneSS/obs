#
# spec file for package xneur
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define major   17
%define tarballver 0.18.0+git5

Name:           xneur
Version:        0.18.0
Release:        0
Summary:        X Neural Switcher
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://www.xneur.ru
Source0:        https://launchpad.net/~andrew-crew-kuznetsov/+archive/xneur-stable/+files/xneur_%{tarballver}.orig.tar.gz

BuildRequires:  alsa-utils
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  xosd-devel
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpcre)
Requires:       alsa-utils
Requires:       aspell
Recommends:     %{name}-gui
Recommends:     %{name}-lang
Recommends:     aspell-en
Recommends:     aspell-ru
Recommends:     myspell-american
Recommends:     myspell-british
Recommends:     myspell-russian

%description
X Neural Switcher (XNeur).
Automatical switcher of keyboard layout.

%package -n libxneur-devel
Summary:        Include Files and Libraries
Group:          Development/Libraries/X11
Requires:       libxneur%{major} = %{version}
Requires:       pkgconfig
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
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libxn*.so.*
%{_mandir}/man?/*
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
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libxn*.so

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
