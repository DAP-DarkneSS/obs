#
# spec file for package [spectemplate]
#
# Copyright (c) 2011-2012 star wolf (theme), (c) 2012 Perlow Dmitriy A. (spec file)
#

%define _path scifi34splz

Name:           ksplashx-theme-sci2010
Version:        0
Release:        0
Summary:        KDE splashx — Sci Fi theme

License:        Artistic 2.0
Url:            http://opendesktop.org/content/show.php?content=144067
Group:          System/GUI/KDE
Source0:        %{_path}.tar.gz

BuildRequires:  kdebase4-workspace-devel
Requires:       kdebase4-workspace
BuildArch:      noarch

%description
This package contains a Sci Fi theme for KDE 4's splashx screen.

%prep
%setup -n %{_path}

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/%{_path}
cp -r ./* %{buildroot}%{_kde4_appsdir}/ksplash/Themes/%{_path}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_kde4_appsdir}/ksplash/Themes/%{_path}
%{_kde4_appsdir}/ksplash/Themes/%{_path}/*

%changelog
