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
Release:        1
License:        GPL-2.0+
Summary:        Extensible scalable on-screen virtual keyboard
Url:            http://florence.sourceforge.net
Group:          System/X11/Utilities
Source0:        http://downloads.sourceforge.net/florence/%{name}-%{version}.tar.bz2

BuildRequires:  at-spi2-core-devel
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libXtst-devel
BuildRequires:  librsvg2-devel
BuildRequires:  pkg-config
BuildRequires:  scrollkeeper
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-doc
Recommends:     %{name}-lang
Requires(post): glib2-tools
Requires(postun): glib2-tools

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

%package doc
License:        GFDL-1.2
Summary:        Florence documentation
Requires:       yelp
BuildArch:      noarch

%description doc
This packages provides Florence documentation.

%lang_package

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}


%install
make install \
     DESTDIR=%{buildroot} \
     INSTALL="install -p"

%suse_update_desktop_file -r %{name} 'Utility;Accessibility;'

mkdir -p %{buildroot}%{_datadir}/pixmaps/

install -p -m 0644 data/%{name}.svg \
    %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%find_lang %{name}

%fdupes -s %{buildroot}%{_datadir}/gnome/help/%{name}


%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING-DOCS NEWS README
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.*
%{_datadir}/pixmaps/%{name}.svg
%exclude %{_localstatedir}/lib/scrollkeeper/*/*.xml
%exclude %{_localstatedir}/lib/scrollkeeper/scrollkeeper_docs
%doc %{_mandir}/man*/%{name}*
%{_datadir}/glib-2.0/schemas/*%{name}*

%files doc
%defattr(-,root,root,-)
%doc %{_datadir}/gnome/help/%{name}

%files lang -f %{name}.lang
%defattr(-,root,root,-)
%exclude %{_datadir}/gnome/help/%{name}

%changelog
