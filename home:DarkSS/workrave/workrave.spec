#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           workrave
Version:        1.9.4
Release:        1
License:        LGPL, GPL, BSD-like
Summary:        Recovery and prevention of Repetitive Strain Injury program
Url:            http://www.workrave.org
Group:          Productivity/Other
Source:         %{name}-%{version}.tar.gz
%if 0%{?suse_version} >= 1220
BuildRequires:  autoconf
BuildRequires:  automake
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gdome2-devel
BuildRequires:  gnet-devel
BuildRequires:  gnome-panel-devel
BuildRequires:  intltool
BuildRequires:  libbonobo-devel
BuildRequires:  libgmodule-2_0-0
BuildRequires:  libgthread-2_0-0
BuildRequires:  libpulse-devel
BuildRequires:  libsigc++2-devel
%if 0%{?suse_version} >= 1220
BuildRequires:  libtool
%endif
BuildRequires:  glibmm2-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  gtkmm2-devel
BuildRequires:  python-cheetah
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-devel

%description
Workrave is a program that assists in the recovery and prevention of Repetitive Strain Injury (RSI). The program frequently alerts you to take micro-pauses, rest breaks and restricts you to your daily limit.

%if 0%{?suse_version} > 1140
%package devel
Summary:        Development Files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
 
%description devel
This package contains header files needed for developing plugins for
Workrave.

%package -n libworkrave-1_0-0
Summary:        The Workrave runtime library
Group:          Productivity/Other
 
%description -n libworkrave-1_0-0
 The Workrave runtime library
%endif

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%makeinstall
%suse_update_desktop_file %{name}
%fdupes %{buildroot}
%find_lang %{name}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%if 0%{?suse_version} > 1140
%post -n libworkrave-1_0-0 -p /sbin/ldconfig
 
%postun -n libworkrave-1_0-0  -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}/*

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%attr(0755,root,root) %{_bindir}/workrave
%dir %{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus*/*
%{_datadir}/icons/hicolor/48x48/apps/workrave-icon-huge.png
%{_datadir}/icons/hicolor/scalable/apps/workrave-sheep.svg
%dir %{_datadir}/sounds/%{name}
%{_datadir}/sounds/%{name}/*
%{_datadir}/%{name}/*
%{_libexecdir}/workrave-applet
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%dir %{_datadir}/gnome-shell/extensions/workrave@workrave.org
%{_datadir}/gnome-shell/extensions/workrave@workrave.org/*
%if 0%{?suse_version} > 1140
%{_datadir}/glib-2.0/schemas/org.workrave.enums.xml
%{_datadir}/glib-2.0/schemas/org.workrave.gschema.xml
%{_datadir}/glib-2.0/schemas/org.workrave.gui.gschema.xml
%{_datadir}/gnome-panel/4.0/applets/org.workrave.WorkraveApplet.panel-applet
%dir %{_datadir}/gnome-panel/ui
%{_datadir}/gnome-panel/ui/workrave-gnome-applet-menu.xml
%else
%{_libdir}/bonobo/servers/Workrave-Applet.server
%{_datadir}/gnome-2.0/ui/GNOME_WorkraveApplet.xml
%endif

%if 0%{?suse_version} > 1140
%files devel
%defattr(-,root,root)
%{_libdir}/libworkrave-1.0.a
%{_libdir}/libworkrave-1.0.la
%{_libdir}/libworkrave-1.0.so
%{_libdir}/girepository-1.0/Workrave-1.0.typelib
%{_datadir}/gir-1.0/Workrave-1.0.gir

%files -n libworkrave-1_0-0
%defattr(-,root,root)
%{_libdir}/libworkrave-1.0.so.0
%{_libdir}/libworkrave-1.0.so.0.0.0
%endif

%changelog
