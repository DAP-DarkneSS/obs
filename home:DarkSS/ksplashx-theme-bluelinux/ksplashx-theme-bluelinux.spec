#
# spec file for package [spectemplate]
#
# Copyright (c) 2009-2012 Sebastian Z aka ziolo4ever (theme), (c) 2012 Perlow Dmitriy A. (spec file)
#

%define _path BlueLinuxSplash

Name:           ksplashx-theme-bluelinux
Version:        0.1
Release:        0
Summary:        KDE splashx — theme

License:        GPL
Url:            http://opendesktop.org/content/show.php?content=105988
Group:          System/GUI/KDE
Source0:        http://dl.dropbox.com/u/4403301/BlueLinuxSplash.tar.gz

# Provides:       ksplashx-branding = ?version
# Supplements:    packageand(ksplashx:branding-bluelinux)
# Conflicts:      otherproviders(ksplashx-branding)

BuildRequires:  fdupes 
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
- Version 0.1.