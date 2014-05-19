#
# spec file for package transparency
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Version:        2.7.4
Release:        0
Summary:        A set of transparent applications
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            http://hugo.pereira.free.fr/software/index.php?page=package&package_list=software_list_qt4&package=transparency&full=0
Source:         http://hugo.pereira.free.fr/software/tgz/transparency-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(xrender)
BuildConflicts: post-build-checks

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

%build
mkdir build && cd build

cmake .. \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

make V=1 %{?_smp_mflags}

%install
cd build
make V=1 install DESTDIR=%{buildroot}

cd ..
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

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/transparen*
%{_datadir}/pixmaps/transparen*
%{_datadir}/applications/transparen*

%changelog
