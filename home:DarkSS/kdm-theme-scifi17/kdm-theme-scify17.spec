#
# spec file for package [spectemplate]
#
# Copyright (c) 2009-2012 star wolf (theme), (c) 2012 Perlow Dmitriy A. (spec file)
#

%define _path sci17kdm

Name:           kdm-theme-scify17
Version:        1.7
Release:        0
Summary:        KDE login and display manager — theme

License:        Artistic 2.0
Url:            http://opendesktop.org/content/show.php?content=117544
Group:          System/GUI/KDE
Source0:        http://opendesktop.org/CONTENT/content-files/117544-sci17kdm.tar.gz

# Provides:       kdm-branding = ?version
# Supplements:    packageand(kdm:branding-sci17kdm)
# Conflicts:      otherproviders(kdm-branding)

BuildRequires:  update-desktop-files fdupes
BuildRequires:  kdebase4-workspace-devel
Requires:       kdm
BuildArch:      noarch

%description
This package contains a theme
for KDE 4's kdm, the display manager.

%prep
%setup -n %{_path}

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/%{_path}
%{__install} ./* %{buildroot}%{_kde4_appsdir}/kdm/themes/%{_path}
%suse_update_desktop_file %{buildroot}%{_kde4_appsdir}/kdm/themes/%{_path}/KdmGreeterTheme.desktop
%fdupes -s %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde4_appsdir}/kdm/
%{_kde4_appsdir}/kdm/themes/
%{_kde4_appsdir}/kdm/themes/%{_path}
%{_kde4_appsdir}/kdm/themes/%{_path}/*
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/%{_path}/input-shadow.svg
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/%{_path}/scifi17.xml

%changelog
* Tue Jan 31 2012 DA <dap.darkness@gmail.com> - 20120131-1
- Version 1.7.