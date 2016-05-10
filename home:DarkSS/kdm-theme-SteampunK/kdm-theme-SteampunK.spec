#
# spec file for package kdm-theme-SteampunK
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define dir_name SteampunK

Name:           kdm-theme-SteampunK
Version:        3.0
Release:        0
Summary:        SteampunK KDE4 login and display manager theme
License:        CC-BY-SA-2.5 or CC-BY-SA-3.0 or CC-BY-SA-3.0 or CC-BY-SA-4.0
Group:          System/GUI/KDE
Url:            http://kde-look.org/content/show.php?content=142139
Source0:        SPL_KDM.tar.gz

BuildRequires:  kde4-filesystem
Requires:       kdm
Recommends:     ksplashx-theme-SteampunK
BuildArch:      noarch

%description
This item is a part of Steam-Powered Linux KDE theme set.
The idea is to apply steampunk style to every themeable part of KDE-based
distro. Any constructive feedback is highly appreciated. I will try to
implement your propositions/fix bugs once I have spare time.

%prep
%setup -qn %{dir_name}

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/%{dir_name}
cp -R * %{buildroot}%{_kde4_appsdir}/kdm/themes/%{dir_name}

%files
%defattr(-,root,root)
%dir %{_kde4_appsdir}/kdm/
%dir %{_kde4_appsdir}/kdm/themes/
%{_kde4_appsdir}/kdm/themes/%{dir_name}

%changelog
