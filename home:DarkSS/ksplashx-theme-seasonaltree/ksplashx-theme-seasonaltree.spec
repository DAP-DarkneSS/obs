#
# spec file for package ksplashx-theme-seasonaltree
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


%define _path treesplz

Name:           ksplashx-theme-seasonaltree
Version:        0
Release:        0
Summary:        KDE splashx — theme

License:        Artistic-2.0
Url:            http://opendesktop.org/usermanager/search.php?username=starwolf
Group:          System/GUI/KDE
Source0:        ksplashx-theme-seasonaltree.tar.lzma

BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
BuildRequires:  xz
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
