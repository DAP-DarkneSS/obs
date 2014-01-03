#
# spec file for package plasmoid-on-off-switch
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


Name:           plasmoid-on-off-switch
Version:        0.2
Release:        0
Summary:        A switch to run user's commands
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://kde-apps.org/content/show.php?content=116323
Source0:        http://kde-apps.org/CONTENT/content-files/116323-on_off_switch-%{version}.tar.bz2
BuildRequires:  libkde4-devel
Requires:       kdebase4-workspace
%kde4_runtime_requires


%description
On/Off Switch is a simple plasmoid that executes commands
when the switch is toggled. User can set the On and Off
commands with the plasmoid settings gui.


%prep
%setup -q -n on_off_switch-%{version}


%build
%cmake_kde4 -d build
%make_jobs

%install
cd build
%make_install


%kde_post_install


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_kde_libdir}/kde4/plasma_applet_on_off_switch.so
%dir %{_kde4_appsdir}/desktoptheme
%dir %{_kde4_appsdir}/desktoptheme/default
%dir %{_kde4_appsdir}/desktoptheme/default/widgets
%{_kde4_appsdir}/desktoptheme/default/widgets/on_off_switch.svg
%{_kde4_servicesdir}/plasma-applet-on_off_switch.desktop

%changelog
