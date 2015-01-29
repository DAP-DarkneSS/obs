#
# spec file for package xfdashboard
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


Name:           xfdashboard
Version:        0.3.8
Release:        0
Summary:        GNOME shell like dashboard for Xfce
License:        GPL-2.0+
Url:            http://xfdashboard.froevel.de
Source0:        https://github.com/gmc-holle/xfdashboard/archive/%{version}.tar.gz
# https://github.com/gmc-holle/xfdashboard/pull/70
# PATCH-FIX-OPENSUSE to fit openSUSE desktop files rules.
Patch0:         xfdashboard-0.3.8-desktop-category.diff
# https://github.com/gmc-holle/xfdashboard/issues/68#issuecomment-71727748
# PATCH-FIX-UPDTREAM to fix serious compiler warnings.
Patch1:         xfdashboard-0.3.8-void-return.diff

BuildRequires:  clutter-devel
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  libxfce4util-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(garcon-1)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libwnck-1.0) >= 2.30
BuildRequires:  pkgconfig(libxfconf-0)
Requires(pre):  update-desktop-files
Requires(post): update-desktop-files
Recommends:     %{name}-autostart
Recommends:     %{name}-themes

%description
Xfdashboard provides a GNOME shell dashboard like interface for use with Xfce
desktop. It can be configured to run to any keyboard shortcut and when executed
provides an overview of applications currently open enabling the user to switch
between different applications. The search feature works like Xfce's app finder
which makes it convenient to search for and start applications.

%package themes
BuildArch:      noarch
Summary:        Themes for Xfdashboard
Requires:       %{name}

%description themes
Additional themes for use with Xfdashboard.

%package autostart
BuildArch:      noarch
Summary:        Autostarts Xfdashboard
Requires:       %{name}

%description autostart
Let Xfdashboard start automatically when openSUSE boots.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
./autogen.sh --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} V=1
%fdupes -s %{buildroot}%{_datadir}/themes/%{name}-*

%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_bindir}/%{name}-settings
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_datadir}/themes/%{name}
%if 0%{?suse_version} <= 1310
%{_datadir}/appdata
%endif

%files autostart
%defattr(-,root,root)
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop

%files themes
%defattr(-,root,root)
%{_datadir}/themes/%{name}-*

%changelog
