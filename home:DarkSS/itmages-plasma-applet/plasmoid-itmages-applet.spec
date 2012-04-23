#
# spec file for package plasmoid-itmages-applet
#
# Copyright (c) 2009-2012 ITmages: https://launchpad.net/itmages
#
# Please submit bugfixes or comments via https://bugs.launchpad.net/itmages
#

Name:           plasmoid-itmages-applet
Version:        0.29
Release:        3
Summary:        Plasma extension to upload pictures to service ITmages.ru

License:        GPL-2.0+
URL:            https://launchpad.net/itmages/itmages-plasma-applet
Source0:        %{name}-%{version}.tar.bz2
Group:          System/GUI/KDE

%kde4_runtime_requires
Provides:       itmages-plasma-applet
BuildRequires:  update-desktop-files fdupes
BuildRequires:  libkde4-devel
Requires:       dolphin-plugin-itmages
Requires:       python-itmages-service

%description
Plasma extension to upload pictures to service ITmages.ru
This extension allows you to upload your favorite images, photos, 
screenshots of image hosting ITmages.ru

%prep
%setup -q

%build
cmake .
lrelease itmages-plasma-applet-ru.ts
make

%install
make install DESTDIR=%{buildroot}
%fdupes -s %{buildroot}%{_datadir}
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/plasma-applet-itmages.desktop

%files
%defattr(-,root,root)
%doc debian/copyright
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
