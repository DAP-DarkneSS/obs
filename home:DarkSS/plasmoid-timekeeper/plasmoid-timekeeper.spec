#
# spec file for package plasmoid-timekeeper
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


Name:           plasmoid-timekeeper
Version:        0.7.0
Release:        0
License:        GPL-3.0
Summary:        A clock and a calendar functions via steampunk interface
Url:            http://store.kde.org/p/1002162
Group:          System/GUI/KDE
Source0:        http://github.com/Joker/timekeeper/archive/v0.7.0.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  zip
###BuildRequires:  unzip
###Requires:       plasma-addons-marble
BuildArch:      noarch

%description
This plasmoid provides a clock and a calendar functions via steampunk
interface. It is written entirely in QML + JavaScript.

Graphics in this plasmoid orginate from Steampunk orrery:
http://lightquick.co.uk/downloads/steampunk-orrery-xwidget.html

For the Moon graphics from Luna QML were used:
http://kde-look.org/content/show.php?content=140204

%prep
%setup -q -n timekeeper-%{version}

# Fix icon name
sed -i "s/Icon=desktop/Icon=timekeeper/" package/metadata.desktop

%build

%install
mkdir -p %{buildroot}%{_kf5_sharedir}/plasma/plasmoids/timekeeper
mkdir -p %{buildroot}%{_kf5_servicesdir}
mkdir -p %{buildroot}%{_kf5_sharedir}/pixmaps
cp -a package/contents/ package/metadata.desktop %{buildroot}%{_kf5_sharedir}/plasma/plasmoids/timekeeper/
cp -a package/metadata.desktop %{buildroot}%{_kf5_servicesdir}/plasma-applet-timekeeper.desktop
cp -a tk.jpg %{buildroot}%{_kf5_sharedir}/pixmaps/timekeeper.jpg

%fdupes -s %{buildroot}

%files
%defattr(-,root,root,-)
%doc package/LICENSE.GPL3
%dir %{_kf5_sharedir}/plasma
%dir %{_kf5_sharedir}/plasma/plasmoids
%{_kf5_sharedir}/plasma/plasmoids/timekeeper
%{_kf5_servicesdir}/plasma-applet-timekeeper.desktop
%{_datadir}/pixmaps/timekeeper.jpg

%changelog
