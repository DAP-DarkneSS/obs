#
# spec file for package dolphin-plugin-itmages
#
# Copyright (c) 2009-2012 ITmages: http://itmages.com/
#
# Please submit bugfixes or comments via
# https://github.com/itmages/itmages-dolphin-extension/issues
#

Name:           dolphin-plugin-itmages
Version:        1.08
Release:        1
Summary:        ITmages Dolphin extension to upload pictures to ITmages.ru

License:        LGPL-3.0+
URL:            https://github.com/itmages/itmages-dolphin-extension
Source0:        https://github.com/itmages/itmages-dolphin-extension/tarball/v%{version}
Group:          Productivity/Networking/Other

Provides:       itmages-dolphin-extension
Requires:       python-itmages-service
Requires:       kdelibs4-core
Recommends:     dolphin
BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files

%description
This extension for the file manager Dolphin, which allows you to quickly
download your images to free image hosting ITmages.ru, in "two clicks".

%prep
%setup -q -n itmages-itmages-dolphin-extension-62e1e36
chmod -x itmages-dolphin-extension.desktop

%build
export PATH="$PATH:/usr/lib/qt4/bin/:/usr/lib64/qt4/bin"
qmake
make %{?_smp_mflags}

%install
make INSTALL_ROOT=${RPM_BUILD_ROOT} install
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
%{_datadir}/kde4/services/ServiceMenus/itmages-dolphin-extension.desktop
%dir %{_datadir}/itmages
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/ServiceMenus

%changelog
