#
# spec file for package transparency
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


Name:           transparency
Version:        2.8.1
Release:        0
Summary:        A set of transparent applications
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            http://hugo.pereira.free.fr/software/index.php?page=package&package_list=software_list_qt4&package=transparency&full=0
Source:         http://hugo.pereira.free.fr/software/tgz/transparency-%{version}.tar.gz
Source5:        transparency.1
Source6:        transparent-calendar.1
Source7:        transparent-clock.1
Source8:        transparent-pictures.1
Source9:        transparency-settings.1
# PATCH-FIX-OPENSUSE to prevent build issue via gcc6.
Patch0:         transparency-2.8.1-gcc6-abs.diff

BuildRequires:  cmake >= 3
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xrender)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

%description
Transparent applications suite:
- transparent clock;
- transparent calendar;
- transparent cpu load meter;
- transparent memory load meter;
- transparent disk usage meter;
- transparent network load meter;
- transparent temperature meter;
- transparent pictures display.

%prep
%setup -q
%if 0%{?suse_version} > 1320
%patch0 -p0
%endif

%build
%cmake \
        -Wno-dev \
        -DUSE_QT5=True \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

make V=1 %{?_smp_mflags}

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/pixmaps

install transparency.png \
        %{buildroot}%{_datadir}/pixmaps
install calendar/transparent-calendar.png \
        %{buildroot}%{_datadir}/pixmaps
install clock/transparent-clock.png \
        %{buildroot}%{_datadir}/pixmaps
install pictures/transparent-picture-viewer.png \
        %{buildroot}%{_datadir}/pixmaps

%suse_update_desktop_file -i transparency-settings -r "Qt;Utility;DesktopUtility;"
%suse_update_desktop_file -i transparent-calendar  -r "Qt;Utility;DesktopUtility;TimeUtility;"
%suse_update_desktop_file -i transparent-clock     -r "Qt;Utility;DesktopUtility;TimeUtility;"
%suse_update_desktop_file -i transparent-pictures

mkdir -p %{buildroot}%{_mandir}/man1
cd %{_sourcedir}
for MANPAGE in *.1; do
gzip -c9 $MANPAGE | tee -a %{buildroot}%{_mandir}/man1/$MANPAGE.gz
done

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/transparen*
%{_mandir}/man1/transparen*
%{_datadir}/pixmaps/transparen*
%{_datadir}/applications/transparen*

%changelog
