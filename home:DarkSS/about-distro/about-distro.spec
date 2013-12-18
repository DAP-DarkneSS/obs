#
# spec file for package about-distro
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


Name:           about-distro
Version:        1.0.0
Release:        0
Summary:        KCM module to show info about system
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            https://projects.kde.org/projects/playground/base/about-distro
Source0:        ftp://ftp.kde.org/pub/kde/stable/about-distro/%{version}/src/about-distro-%{version}.tar.xz
Source1:        kcm-about-distrorc
BuildRequires:  libkde4-devel
Requires:       kdebase4-workspace
# The distro logo file:
Requires:       kdebase4-workspace-branding-openSUSE
%kde4_runtime_requires


%description
KCM module to show info about system.

It can be customized by kcm-about-distrorc file
in KDE config directory.


%prep
%setup -q


%build
%cmake_kde4 -d build
%make_jobs

%install
cd build
%make_install
%find_lang kcm-about-distro
install -D -m644 %{SOURCE1} %{buildroot}/%{_kde4_configdir}/kcm-about-distrorc


%kde_post_install


%files -f build/kcm-about-distro.lang
%defattr(-,root,root)
%doc COPYING README
%{_kde_libdir}/kde4/kcm_about_distro.so
%{_kde4_servicesdir}/%{name}.desktop
%{_kde4_configdir}/*%{name}*

%changelog
