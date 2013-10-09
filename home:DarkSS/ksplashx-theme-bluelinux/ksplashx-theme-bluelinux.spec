#
# spec file for package ksplashx-theme-bluelinux
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


%define _path BlueLinuxSplash

Name:           ksplashx-theme-bluelinux
Version:        0.1
Release:        0
Summary:        KDE splashx — theme

License:        GPL-3.0
Url:            http://opendesktop.org/content/show.php?content=105988
Group:          System/GUI/KDE
Source0:        http://dl.dropbox.com/u/4403301/BlueLinuxSplash.tar.gz

BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
Requires:       kdebase4-workspace
BuildArch:      noarch

%description
This package contains a theme for KDE 4's splashx screen.

%prep
%setup -n %{_path}

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/%{_path}
cp -r ./* %{buildroot}%{_kde4_appsdir}/ksplash/Themes/%{_path}
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%dir %{_kde4_appsdir}/ksplash/
%dir %{_kde4_appsdir}/ksplash/Themes/
%{_kde4_appsdir}/ksplash/Themes/%{_path}

%changelog
