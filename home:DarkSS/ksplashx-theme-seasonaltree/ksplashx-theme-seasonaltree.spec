#
# spec file for package [spectemplate]
#
# Copyright (c) 2009-2012 star wolf (theme), (c) 2012 Perlow Dmitriy A. (spec file)
#

%define _path treesplz

Name:           ksplashx-theme-seasonaltree
Version:        0
Release:        0
Summary:        KDE splashx — theme

License:        Artistic 2.0
Url:            http://opendesktop.org/usermanager/search.php?username=starwolf
Group:          System/GUI/KDE
Source0:        ksplashx-theme-seasonaltree.tar.lzma

# Provides:       ksplashx-branding = ?version
# Supplements:    packageand(ksplashx:branding-treesplz)
# Conflicts:      otherproviders(ksplashx-branding)

BuildRequires:  xz fdupes 
BuildRequires:  kdebase4-workspace-devel
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde4_appsdir}/ksplash/
%{_kde4_appsdir}/ksplash/Themes/
%{_kde4_appsdir}/ksplash/Themes/%{_path}
%{_kde4_appsdir}/ksplash/Themes/%{_path}/*

%changelog
* Tue Jan 31 2012 DA <dap.darkness@gmail.com> - 20120131-1
- Release.