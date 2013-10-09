#
# spec file for package kdm-theme-scify17
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


%define _path sci17kdm

Name:           kdm-theme-scify17
Version:        1.7
Release:        0
Summary:        KDE login and display manager — theme

License:        Artistic-2.0
Url:            http://opendesktop.org/content/show.php?content=117544
Group:          System/GUI/KDE
Source0:        http://opendesktop.org/CONTENT/content-files/117544-sci17kdm.tar.gz

BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
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
install ./* %{buildroot}%{_kde4_appsdir}/kdm/themes/%{_path}
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%dir %{_kde4_appsdir}/kdm/
%dir %{_kde4_appsdir}/kdm/themes/
%{_kde4_appsdir}/kdm/themes/%{_path}
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/%{_path}/input-shadow.svg
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/%{_path}/scifi17.xml
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/%{_path}/KdmGreeterTheme.desktop

%changelog
