#
# spec file for package glabels
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


Name:           glabels
Version:        3.0.1
Release:        0
Summary:        Label Editing and Printing Tool
License:        GPL-3.0+
Group:          Productivity/Office/Other
Url:            http://glabels.sourceforge.net/
Source:         http://download.gnome.org/sources/glabels/3.0/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM glabels-eds-3.6.patch bgo#685130 dimstar@opensuse.org -- Fix build with evolution-data-server 3.6
Patch0:         glabels-eds-3.6.patch
BuildRequires:  barcode-devel
BuildRequires:  qrencode-devel
BuildRequires:  fdupes
BuildRequires:  intltool
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.2
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.28.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.9
BuildRequires:  pkgconfig(libebook-1.2) >= 3.6.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(pango) >= 1.28.1
BuildRequires:  pkgconfig(pangocairo) >= 1.28.1
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%glib2_gsettings_schema_requires

%description
Labels is a powerful tool for editing and printing all kinds of labels.
It comes with a lot of templates of standard labels.

%package devel
Summary:        Label Editing and Printing Tool - Development Files
License:        GPL-2.0+
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
Labels is a powerful tool for editing and printing all kinds of labels.
It comes with a lot of templates of standard labels.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package
%prep
%setup -q
%patch0 -p1
translation-update-upstream

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
# FIXME: Build as root modifies system!
%configure\
        --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file glabels-3.0 WordProcessor
%find_lang %{name}-3.0 %{?no_lang_C}
%fdupes -s %{buildroot}

%clean
%{?buildroot:rm -rf %{buildroot}}

%post
/sbin/ldconfig
%glib2_gsettings_schema_post
%icon_theme_cache_post
%desktop_database_post
%mime_database_post

%postun
/sbin/ldconfig
%glib2_gsettings_schema_postun
%icon_theme_cache_postun
%desktop_database_postun
%mime_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README TODO
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/%{name}-3.0/
%doc %{_datadir}/gnome/help/%{name}-3.0/C/
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/glabels-3.0/
%{_datadir}/libglabels-3.0/
%{_datadir}/glib-2.0/schemas/org.gnome.glabels-3.gschema.xml
%{_datadir}/mime/packages/glabels-3.0.xml
%{_datadir}/icons/hicolor/*/apps/glabels-3.0.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-glabels.png
%doc %{_mandir}/man?/*.*

%files devel
%defattr(-,root,root)
%{_includedir}/libglabels-3.0/
%{_includedir}/libglbarcode-3.0/
%{_libdir}/pkgconfig/libglabels-3.0.pc
%{_libdir}/pkgconfig/libglbarcode-3.0.pc
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/libglabels-3.0/
%{_datadir}/gtk-doc/html/libglbarcode-3.0/

%files lang -f %{name}-3.0.lang

%changelog
