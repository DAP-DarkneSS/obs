#
# spec file for package dolphin-plugin-itmages
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

Name:           dolphin-plugin-itmages
Version:        1.10
Release:        1
Summary:        ITmages Dolphin extension to upload pictures to ITmages.ru

License:        LGPL-3.0+
Url:            https://github.com/itmages/itmages-dolphin-extension
Group:          Productivity/Networking/Other
Source0:        https://codeload.github.com/itmages/itmages-dolphin-extension/tar.gz/v%{version}

BuildRequires:  hicolor-icon-theme
BuildRequires:  kde4-filesystem
BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files
Requires:       kdelibs4-core
Requires:       python-itmages-service
Recommends:     dolphin
Provides:       itmages-dolphin-extension

%description
This extension for the file manager Dolphin, which allows you to quickly
download your images to free image hosting ITmages.ru, in "two clicks".

%prep
%setup -q -n itmages-dolphin-extension-%{version}
chmod -x itmages-dolphin-extension.desktop

%build
export PATH="$PATH:/usr/lib/qt4/bin/:/usr/lib64/qt4/bin"
qmake \
      QMAKE_STRIP="" \
      PREFIX=%{_prefix} \
      QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/ServiceMenus/itmages-dolphin-extension.desktop
%suse_update_desktop_file -c itmages-uploader "ITmages Uploader" "Upload images to ITmages" "itmages-dolphin-extension %U" "%{_datadir}/icons/hicolor/scalable/apps/itmages.svg" "Utility;WebUtility;"
echo "MimeType=image/png;image/jpeg;image/gif;" | tee -a %{buildroot}%{_datadir}/applications/itmages-uploader.desktop

%files
%defattr(-,root,root,-)
%doc README COPYING COPYING.LESSER
%{_bindir}/itmages-dolphin-extension
%{_datadir}/icons/hicolor/scalable/apps/itmages.svg
%{_datadir}/itmages/itmages-dolphin-extension_ru.qm
%{_datadir}/applications/itmages-uploader.desktop
%{_kde4_servicesdir}/ServiceMenus/itmages-dolphin-extension.desktop
%dir %{_datadir}/itmages

%changelog
