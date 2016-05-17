#
# spec file for package krusader
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           krusader
Version:        2.4.0~beta3+git129
Release:        0
Summary:        A File Manager
License:        GPL-2.0+
Group:          Productivity/File utilities
Url:            http://krusader.sourceforge.net/
Source:         %{name}-%{version}.tar.xz
Source1:        krusader_browse_iso.desktop

BuildRequires:  fdupes
BuildRequires:  libkde4-devel
BuildRequires:  libkonq-devel
Requires:       kio_iso = %{version}
Requires:       libktexteditor
Suggests:       %{name}-doc
%{kde4_runtime_requires}

%description
An advanced twin panel (commander style) file manager for KDE.

%package -n kio_iso
Summary:        KIO slave to access ISO images
Group:          System/GUI/KDE
Provides:       kde4-kio_iso = 1.80.99
Obsoletes:      kde4-kio_iso < 1.80.99
%{kde4_runtime_requires}

%description -n kio_iso
KIO slave to access ISO images like zip- or tar.gz-archives in your
file-browser.

%package doc
Summary:        A File Manager
Group:          Productivity/File utilities

%description doc
An advanced twin panel (commander style) file manager for KDE.

%prep
%setup -q
sed -i 's/2.4.0-beta3/v2.4.0-beta3-129-ge5c4d9a/g' CMakeLists.txt
sed -i 's/Single Step/KDE4 the last/g' CMakeLists.txt

%build
export RPM_OPT_FLAGS="%{optflags} -fno-strict-aliasing"
%cmake_kde4 -d build
%make_jobs

%install
pushd build
%make_install
popd
mkdir -p %{buildroot}%{_kde4_servicesdir}/ServiceMenus/
cp %{SOURCE1} %{buildroot}%{_kde4_servicesdir}/ServiceMenus/
%suse_update_desktop_file krusader_root-mode FileManager Utility
%kde_post_install
%find_lang %{name}
%fdupes %{buildroot}

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog TODO SVNNEWS
%{_kde4_applicationsdir}/krusader*.desktop
%{_kde4_appsdir}/krusader
%{_kde4_bindir}/krusader
%{_kde4_iconsdir}/??color/*/apps/krusader*.png
%{_kde4_modules}/kio_krarc.so
%{_kde4_servicesdir}/krarc.protocol
%{_kde4_mandir}/man1/krusader.1.gz
%exclude %{_kde4_htmldir}/*/krusader

%files -n kio_iso
%defattr(-,root,root)
%config %{_kde4_configdir}/kio_isorc
%{_kde4_modules}/kio_iso.so*
%{_kde4_servicesdir}/iso.protocol
%{_kde4_servicesdir}/ServiceMenus/krusader_browse_iso.desktop

%files doc
%defattr(-,root,root)
%doc %lang(en) %{_kde4_htmldir}/en/krusader

%changelog
