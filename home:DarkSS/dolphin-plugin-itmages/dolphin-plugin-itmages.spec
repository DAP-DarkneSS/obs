#
# spec file for package dolphin-plugin-itmages
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


Name:           dolphin-plugin-itmages
Version:        1.10
Release:        0
Summary:        ITmages Dolphin extension to upload pictures to ITmages.ru
License:        LGPL-3.0+
Group:          Productivity/Networking/Other
Url:            https://github.com/itmages/itmages-dolphin-extension
Source0:        https://github.com/itmages/itmages-dolphin-extension/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source9:        itmages-dolphin-extension.1
# PATCH-FEATURE-UPSTREAM to make Qt5 build. See more at
# https://github.com/itmages/itmages-dolphin-extension/pull/5
Patch0:         dolphin-plugin-itmages-Qt5.diff

BuildRequires:  hicolor-icon-theme
BuildRequires:  kde4-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       python-itmages-service
Suggests:       dolphin
Suggests:       plasmoid-itmages-applet
Provides:       itmages-dolphin-extension

%description
Qt application and KDE4 file manager Dolphin extension, that allow to
quickly upload images to free image hosting ITmages.ru in "two clicks".

%prep
%setup -q -n itmages-dolphin-extension-%{version}
%patch0 -p1
chmod -x itmages-dolphin-extension.desktop

%build
qmake-qt5 \
      QMAKE_STRIP="" \
      PREFIX=%{_prefix} \
      QMAKE_CXXFLAGS+="%{optflags}"
make V=1 %{?_smp_mflags}

%install
make V=1 INSTALL_ROOT=%{buildroot} install

# Desktop files:
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/ServiceMenus/itmages-dolphin-extension.desktop
%suse_update_desktop_file -c itmages-uploader "ITmages Uploader" "Upload images to ITmages" "itmages-dolphin-extension %U" "%{_datadir}/icons/hicolor/scalable/apps/itmages.svg" "Utility;WebUtility;"
echo "MimeType=image/png;image/jpeg;image/gif;" | tee -a %{buildroot}%{_datadir}/applications/itmages-uploader.desktop

# Man page:
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c9 %{SOURCE9} | tee -a %{buildroot}%{_mandir}/man1/itmages-dolphin-extension.1.gz

%files
%defattr(-,root,root,-)
%doc README COPYING COPYING.LESSER
%{_bindir}/itmages-dolphin-extension
%{_mandir}/man1/itmages-dolphin-extension.1.gz
%{_datadir}/icons/hicolor/scalable/apps/itmages.svg
%{_datadir}/itmages/itmages-dolphin-extension_ru.qm
%{_datadir}/applications/itmages-uploader.desktop
%{_kde4_servicesdir}/ServiceMenus/itmages-dolphin-extension.desktop
%dir %{_datadir}/itmages

%changelog
