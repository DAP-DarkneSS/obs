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
Version:        0.4.0
Release:        0
Summary:        GNOME shell like dashboard for Xfce
License:        GPL-2.0+
Url:            http://xfdashboard.froevel.de
Source0:        https://github.com/gmc-holle/xfdashboard/archive/%{version}.tar.gz

# WARNING! Please don't add OnlyShowIn key to the desktop file
# to save possibility to be run from under different desktop environments.

# PATCH-FIX-OPENSUSE gh#gmc-holle/xfdashboard#70 xfdashboard-0.3.8-desktop-category.diff dap.darkness@gmail.com -- fixes not-sufficient desktop file category.
Patch0:         xfdashboard-0.3.8-desktop-category.diff

# PATCH-FIX-OPENSUSE xfdashboard-desktopfile-without-binary.diff dap.darkness@gmail.com -- fixes "W: desktopfile-without-binary".
Patch2:         xfdashboard-desktopfile-without-binary.diff

BuildRequires:  clutter-devel
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  libxfce4util-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(garcon-1)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xinerama)
Requires(pre):  update-desktop-files
Requires(post): update-desktop-files
Recommends:     %{name}-lang
Recommends:     %{name}-themes

%description
Xfdashboard provides a GNOME shell dashboard like interface for use with Xfce
desktop. It can be configured to run to any keyboard shortcut and when executed
provides an overview of applications currently open enabling the user to switch
between different applications. The search feature works like Xfce's app finder
which makes it convenient to search for and start applications.

%lang_package

%package themes
BuildArch:      noarch
Summary:        Themes for Xfdashboard
Requires:       %{name}

%description themes
Additional themes for use with Xfdashboard.

%prep
%setup -q
%patch0 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags}"
./autogen.sh --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} V=1
%fdupes -s %{buildroot}%{_datadir}/themes/%{name}-*
%find_lang %{name} %{?no_lang_C}

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
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_datadir}/themes/%{name}
%if 0%{?suse_version} <= 1310
%{_datadir}/appdata
%endif

%files lang -f %{name}.lang

%files themes
%defattr(-,root,root)
%{_datadir}/themes/%{name}-*

%changelog
