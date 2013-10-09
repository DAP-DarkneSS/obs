#
# spec file for package kdm-theme-neon
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


Name:           kdm-theme-neon
Version:        4.0
Release:        0
Summary:        KDE login and display manager — theme

License:        GPL-3.0
Url:            http://opendesktop.org/content/show.php?content=128745
Group:          System/GUI/KDE
Source0:        kdm-theme-neon.tar.xz

BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
BuildRequires:  xz
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
install ./* %{buildroot}%{_kde4_appsdir}/kdm/themes/kdm_neon_4
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%dir %{_kde4_appsdir}/kdm/
%dir %{_kde4_appsdir}/kdm/themes/
%{_kde4_appsdir}/kdm/themes/kdm_neon_4
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/kdm_neon_4/neon.xml
%attr(644,root,root) %{_kde4_appsdir}/kdm/themes/kdm_neon_4/KdmGreeterTheme.desktop

%changelog
