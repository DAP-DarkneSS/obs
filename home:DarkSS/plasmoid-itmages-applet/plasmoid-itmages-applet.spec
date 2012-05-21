#
# spec file for package plasmoid-itmages-applet
#
# Copyright (c) 2009-2012 ITmages: http://itmages.com/
#
# Please submit bugfixes or comments via
# https://github.com/itmages/itmages-plasma-applet/issues
#

Name:           plasmoid-itmages-applet
Version:        0.30
Release:        3
Summary:        Plasma extension to upload pictures to service ITmages.ru

License:        LGPL-3.0+
URL:            https://github.com/itmages/itmages-plasma-applet
Source0:        https://github.com/itmages/itmages-plasma-applet/tarball/v%{version}
Group:          System/GUI/KDE

%kde4_runtime_requires
Provides:       itmages-plasma-applet
BuildRequires:  update-desktop-files fdupes
BuildRequires:  libkde4-devel
Requires:       dolphin-plugin-itmages

%description
Plasma extension to upload pictures to service ITmages.ru
This extension allows you to upload your favorite images, photos, 
screenshots of image hosting ITmages.ru

%prep
%setup -q -n itmages-itmages-plasma-applet-9a6aa23

%build
cmake .
lrelease itmages-plasma-applet-ru.ts
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%fdupes -s %{buildroot}%{_datadir}
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/plasma-applet-itmages.desktop

%files
%defattr(-,root,root)
%doc README COPYING COPYING.LESSER
%{_libdir}/kde4/plasma_applet_itmages.so
%{_datadir}/icons/oxygen/scalable/apps/itmages.svg
%dir %{_datadir}/kde4/apps/desktoptheme
%dir %{_datadir}/kde4/apps/desktoptheme/default
%dir %{_datadir}/kde4/apps/desktoptheme/default/widgets
%{_datadir}/kde4/apps/desktoptheme/default/widgets/itmages.svg
%{_datadir}/kde4/services/plasma-applet-itmages.desktop
%dir %{_datadir}/itmages
%{_datadir}/itmages/itmages-plasma-applet-ru.qm

%changelog
