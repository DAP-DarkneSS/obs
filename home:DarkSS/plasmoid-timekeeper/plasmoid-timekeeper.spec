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
Version:        0.3.1
Release:        0
License:        GPL-3.0
Summary:        A clock and a calendar functions via steampunk interface
Url:            http://kde-apps.org/content/show.php/Time+Keeper?content=159345
Group:          System/GUI/KDE
Source0:        http://kde-apps.org/CONTENT/content-files/159345-timekeeper-%{version}.plasmoid

BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
BuildRequires:  unzip
Requires:       plasma-addons-marble
BuildArch:      noarch

%description
This plasmoid provides a clock and a calendar functions via steampunk
interface. It is written entirely in QML + JavaScript.

Graphics in this plasmoid orginate from Steampunk orrery:
http://lightquick.co.uk/downloads/steampunk-orrery-xwidget.html

For the Moon graphics from Luna QML were used:
http://kde-look.org/content/show.php?content=140204

%prep

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/plasma/plasmoids/timekeeper
unzip %{SOURCE0} -d %{buildroot}%{_kde4_appsdir}/plasma/plasmoids/timekeeper
%fdupes -s %{buildroot}%{_kde4_appsdir}/plasma/plasmoids/timekeeper

%kde_post_install

%files
%defattr(-,root,root)
%dir %{_kde4_appsdir}/plasma
%dir %{_kde4_appsdir}/plasma/plasmoids
%{_kde4_appsdir}/plasma/plasmoids/timekeeper

%changelog
