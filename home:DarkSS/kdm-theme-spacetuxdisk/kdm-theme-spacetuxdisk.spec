#
# spec file for package [spectemplate]
#
# Copyright (c) 2010-2012 Ramon C aka kronbus (theme), (c) 2012 Perlow Dmitriy A. (spec file)
#

Name:           kdm-theme-spacetuxdisk
Version:        0.8
Release:        0
Summary:        KDE login and display manager — theme

License:        GPL
Url:            http://opendesktop.org/content/show.php?content=129192
Group:          System/GUI/KDE
Source0:        http://dl.dropbox.com/u/2164801/Posts%%20Kronbus/space-tux-disk.tar.gz

# Provides:       kdm-branding = ?version
# Supplements:    packageand(kdm:branding-zxcity)
# Conflicts:      otherproviders(kdm-branding)

BuildRequires:  update-desktop-files fdupes
BuildRequires:  kdebase4-workspace-devel
Requires:       kdm
BuildArch:      noarch

%description
This package contains a theme
for KDE 4's kdm, the display manager.

%prep
%setup -n space-tux-disk

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/space-tux-disk
%{__install} ./* %{buildroot}%{_kde4_appsdir}/kdm/themes/space-tux-disk
%suse_update_desktop_file %{buildroot}%{_kde4_appsdir}/kdm/themes/space-tux-disk/KdmGreeterTheme.desktop
%fdupes -s %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde4_appsdir}/kdm/
%{_kde4_appsdir}/kdm/themes/
%{_kde4_appsdir}/kdm/themes/space-tux-disk
%{_kde4_appsdir}/kdm/themes/space-tux-disk/*
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/space-tux-disk/space-disk.xml

%changelog
* Tue Jan 31 2012 DA <dap.darkness@gmail.com> - 20120131-1
- Version 0.8.