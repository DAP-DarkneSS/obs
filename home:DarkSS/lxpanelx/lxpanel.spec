#
# spec file for package lxpanel
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


Name:           lxpanel
Version:        0.5.12
Release:        0
Summary:        Lightweight X11 desktop panel based on fbpanel
License:        GPL-2.0
Group:          System/GUI/LXDE
Url:            http://www.lxde.org/
Source0:        http://sourceforge.net/projects/lxde/files/LXPanel%20%28desktop%20panel%29/LXPanel%20%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libiw-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  wireless-tools
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(libwnck-1.0)
Provides:       %name-plugins >= %version
Obsoletes:      %name-plugins < %version
Recommends:     %name-lang
Requires:       menu-cache

%description
LXPanel is a lightweight X11 desktop panel containing:
1. User-friendly application menu automatically generated from *.desktop files on the system
2. Launcher bar (Small icons clicked to launch apps)
3. Task bar supporting urgency hint (Can flash when gaim gets new incoming messages)
4. Notification area (System tray)
5. Digital clock
6. Run dialog (A dialog lets you type a command and run it, can be called in external programs)
7. Net status icon plug-in (optional, ported from gnome-netstatus-applet)
8. Volume control plug-in (optional, written by jserv)
9. lxpanelctl, an external controller lets you control lxpanel in other programs.
For example, "lxpanelctl run" will show the Run dialog in lxpanel, and "lxpanelctl menu"
will show the application menu. This is useful in key bindings provided by window managers.

%package devel
Summary:        Devel files for %name
Group:          Development/Libraries/C and C++
Requires:       %name
Requires:       glib2-devel
Requires:       menu-cache-devel

%description devel
Headers and development %name files.


%lang_package
%prep
%setup -q

%build
%configure \
	--enable-man \
	--with-plugins=all
%__make %{?jobs:-j%jobs} V=1

%install
%makeinstall
%find_lang %{name}
%fdupes -s %buildroot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc ChangeLog README COPYING
%{_bindir}/%{name}
%{_bindir}/lxpanelctl
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/profile
%dir %{_datadir}/%{name}/profile/default
%dir %{_datadir}/%{name}/profile/default/panels
%dir %{_datadir}/%{name}/profile/two_panels
%dir %{_datadir}/%{name}/profile/two_panels/panels
%dir %{_datadir}/%{name}/ui
%dir %{_datadir}/%{name}/images
%dir %{_datadir}/%{name}/images/xkb-flags/
%dir %{_datadir}/%{name}/xkeyboardconfig
%{_datadir}/%{name}/images/xkb-flags/*.png
%{_datadir}/%{name}/images/*.png
%{_datadir}/%{name}/profile/default/config
%{_datadir}/%{name}/profile/default/panels/panel
%{_datadir}/%{name}/profile/two_panels/config
%{_datadir}/%{name}/profile/two_panels/panels/bottom
%{_datadir}/%{name}/profile/two_panels/panels/top
%{_datadir}/%{name}/xkeyboardconfig/layouts.cfg
%{_datadir}/%{name}/xkeyboardconfig/models.cfg
%{_datadir}/%{name}/xkeyboardconfig/toggle.cfg

%{_datadir}/%{name}/ui/*.ui
%{_mandir}/man1/*.1.gz
%{_libdir}/%{name}/plugins/batt.so
%{_libdir}/%{name}/plugins/cpu.so
%{_libdir}/%{name}/plugins/deskno.so
%{_libdir}/%{name}/plugins/kbled.so
%{_libdir}/%{name}/plugins/netstatus.so
%{_libdir}/%{name}/plugins/thermal.so
%{_libdir}/%{name}/plugins/volumealsa.so
%{_libdir}/%{name}/plugins/xkb.so           
%{_libdir}/%{name}/plugins/cpufreq.so
%{_libdir}/%{name}/plugins/monitors.so
%{_libdir}/%{name}/plugins/netstat.so
%{_libdir}/%{name}/plugins/wnckpager.so

%files devel
%defattr(-,root,root)
%dir %_includedir/%{name}
%_includedir/%{name}/*.h
%_libdir/pkgconfig/%{name}.pc

%files lang -f %name.lang

%changelog
