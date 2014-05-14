#
# spec file for package kaffeinety
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


Name:           kaffeinety
Version:        0.0.3
Release:        0
License:        GPL-2.0+
Summary:        A screen saver suppressor
Url:            http://kde-apps.org/content/show.php?content=159860
Group:          System/GUI/KDE
Source0:        http://kde-apps.org/CONTENT/content-files/159860-kaffeinety-%{version}.tar.gz

BuildRequires:  kdebase4-workspace-devel >= 4.8.0
BuildRequires:  unzip

%kde4_runtime_requires

%description
KaffeineTY - a application to temporarity prevents dim screen action
of power management and screensaver for KDE environment.

CONFIGURE IT:
 * go to: System settings > Power Management > KaffeineTY
 * enter name of application you want to run it without dim screen
   and screensaver action in 'Parameter'
 * syntax: name1{titleoptional1}|name2{titleoptional2}|....

By default, it enable for flash run in fullscreen model on chromium
and firefox browser by: chromium{exe}|plugin-container

%prep
%setup -q -n %{name}

%build
%cmake_kde4 -d build
make %{?_smp_mflags}

%install
cd build
%make_install

%kde_post_install

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{name}
%{_kde4_modules}/kcm_%{name}.so
%{_datadir}/autostart/%{name}_autostart.desktop
%{_kde4_servicesdir}/%{name}.desktop

%changelog
