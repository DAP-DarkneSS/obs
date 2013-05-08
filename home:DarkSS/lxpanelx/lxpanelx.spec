#
# spec file for package lxpanelx
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

Name:           lxpanelx
Version:        0.5+r672
Release:        0
Summary:        Lightweight X11 desktop panel, based on lxpanel
License:        GPL-2.0
Group:          System/GUI/LXDE
Url:            http://code.google.com/p/lxpanelx

# svn co http://lxpanelx.googlecode.com/svn/trunk/ lxpanelx-%%{version}
Source0:        lxpanelx-%{version}.tar.bz2

BuildRequires:  docbook-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libfm)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(xcomposite)
Recommends:     %name-lang
Requires:       lxmenu-data
Requires:       menu-cache

%description
LXPanelx is a fork lightweight X11 desktop panel. It's consist more
flexible taskbar plugin configurations and other  many improvements,
not in original lxpanel.

%package devel
Summary:        Devel files for %name
Group:          Development/Libraries/C and C++
Requires:       %name

%description devel
Headers and development %name files.

%lang_package

%prep
%setup -q

%build
%configure \
                --enable-man \
                --disable-maintainer-mode \
                --disable-static \
                --with-plugins=all
make %{?_smp_mflags}

%install
%makeinstall
%find_lang %{name}
%fdupes -s %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1.gz
%{_libdir}/%{name}
%if "%{_lib}" == "lib64"
/usr/lib/%{name}
%endif

%files devel
%defattr(-,root,root)
%_includedir/%{name}
%_libdir/pkgconfig/%{name}.pc

%files lang -f %name.lang

%changelog
