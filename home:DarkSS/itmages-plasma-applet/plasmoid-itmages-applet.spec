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

License:        GNU GPL v3
URL:            https://launchpad.net/itmages/itmages-plasma-applet
Source0:        %{name}-%{version}.tar.bz2
Group:          System/GUI/KDE

%kde4_runtime_requires
Provides:       itmages-plasma-applet
BuildRequires:  update-desktop-files fdupes
BuildRequires:  make cmake
BuildRequires:  gcc gcc-c++
BuildRequires:  kdebase4 libkde4-devel kdebase4-workspace kdebase4-runtime
BuildRequires:  qt qt-devel libqt4-devel
Requires:       itmages-dolphin-extension
Requires:       python-itmages-service dbus-1-python
Requires:       kdelibs4-core

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/kde4/plasma_applet_itmages.so
%{_datadir}/icons/oxygen/scalable/apps/itmages.svg
%{_datadir}/kde4/apps/desktoptheme/default/widgets/itmages.svg
%{_datadir}/kde4/services/plasma-applet-itmages.desktop
%dir %{_datadir}/itmages
%{_datadir}/itmages/itmages-plasma-applet-ru.qm

%changelog
* Mon Jan 09 2012 DA <dap.darkness@gmail.com> - 20120109-1
- Revision #29.
