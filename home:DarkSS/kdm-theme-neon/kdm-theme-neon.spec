#
# spec file for package [spectemplate]
#
# Copyright (c) 2010-2012 Ramon C aka kronbus (theme), (c) 2012 Perlow Dmitriy A. (spec file)
#

Name:           kdm-theme-neon
Version:        4.0
Release:        0
Summary:        KDE login and display manager — theme

License:        GPL
Url:            http://opendesktop.org/content/show.php?content=128745
Group:          System/GUI/KDE
Source0:        kdm-theme-neon.tar.xz

# Provides:       kdm-branding = ?version
# Supplements:    packageand(kdm:branding-zxcity)
# Conflicts:      otherproviders(kdm-branding)

BuildRequires:  update-desktop-files fdupes xz
BuildRequires:  kdebase4-workspace-devel
Requires:       kdm
BuildArch:      noarch

%description
This package contains a theme
for KDE 4's kdm, the display manager.

%prep
%setup -n kdm_neon_4

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/kdm_neon_4
%{__install} ./* %{buildroot}%{_kde4_appsdir}/kdm/themes/kdm_neon_4
%suse_update_desktop_file %{buildroot}%{_kde4_appsdir}/kdm/themes/kdm_neon_4/KdmGreeterTheme.desktop
%fdupes -s %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde4_appsdir}/kdm/
%{_kde4_appsdir}/kdm/themes/
%{_kde4_appsdir}/kdm/themes/kdm_neon_4
%{_kde4_appsdir}/kdm/themes/kdm_neon_4/*
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/kdm_neon_4/neon.xml

%changelog
* Tue Jan 31 2012 DA <dap.darkness@gmail.com> - 20120131-1
- Version 4.0.