#
# spec file for package florence
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


Name:           florence
Version:        0.6.0
Release:        0
Summary:        Extensible scalable on-screen virtual keyboard
License:        GPL-2.0+ and GFDL-1.2
Group:          System/X11/Utilities
Url:            http://florence.sourceforge.net
Source0:        http://downloads.sourceforge.net/florence/%{name}-%{version}.tar.bz2
BuildRequires:  at-spi2-core-devel
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libXtst-devel
BuildRequires:  librsvg2-devel
BuildRequires:  pkg-config
BuildRequires:  rarian-scrollkeeper-compat
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-lang
Requires(post):   glib2-tools
Requires(postun): glib2-tools
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description
Florence is an extensible scalable virtual keyboard for GNOME.
You need it if you can't use a real hardware keyboard, for
example because you are disabled, your keyboard is broken or
because you use a tablet PC, but you must be able to use a pointing
device (as a mouse, a trackball or a touchscreen).

Florence stays out of your way when you don't need it:
it appears on the screen only when you need it.
A Timer-based auto-click functionality is available
to help disabled people having difficulties to click.

%lang_package
%prep
%setup -q
sed -i 's|Icon=@ICONDIR@/%{name}.svg|Icon=%{name}|g' data/%{name}.desktop.in.in

%build
%configure \
    --disable-scrollkeeper
make %{?_smp_mflags}

%install
%make_install

# a .svg is not really a pixmap and should not be installed there.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/pixmaps/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
%suse_update_desktop_file -r %{name} Utility Accessibility
%find_lang %{name} %{?no_lang_C}

%post
%glib2_gsettings_schema_post
%desktop_database_post

%postun
%glib2_gsettings_schema_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING COPYING-DOCS NEWS README
%dir %{_datadir}/gnome/help/%{name}
%doc %{_datadir}/gnome/help/%{name}/C/
%dir %{_datadir}/omf
%dir %{_datadir}/omf/%{name}
%doc %{_datadir}/omf/%{name}/%{name}-C.omf
%doc %{_mandir}/man1/%{name}.1%{?ext_man}
%doc %{_mandir}/man1/%{name}_applet.1%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files lang -f %{name}.lang

%changelog
