#
# spec file for package kdm-theme-spacetuxdisk
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


Name:           kdm-theme-spacetuxdisk
Version:        0.8
Release:        0
Summary:        KDE login and display manager — theme

License:        GPL-3.0
Url:            http://opendesktop.org/content/show.php?content=129192
Group:          System/GUI/KDE
Source0:        http://dl.dropbox.com/u/2164801/Posts%%20Kronbus/space-tux-disk.tar.gz

BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
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
install ./* %{buildroot}%{_kde4_appsdir}/kdm/themes/space-tux-disk
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%dir %{_kde4_appsdir}/kdm/
%dir %{_kde4_appsdir}/kdm/themes/
%{_kde4_appsdir}/kdm/themes/space-tux-disk
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/space-tux-disk/space-disk.xml
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/space-tux-disk/KdmGreeterTheme.desktop

%changelog
