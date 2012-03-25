#
# spec file for package dolphin-plugin-itmages
#
# Copyright (c) 2009-2012 ITmages team. See more at https://launchpad.net/itmages
#
# Please submit bugfixes or comments via https://bugs.launchpad.net/itmages
#

Name:           dolphin-plugin-itmages
Version:        1.07.bzr
Release:        0
Summary:        ITmages Dolphin extension

License:        GPL-3.0
URL:            https://launchpad.net/itmages/itmages-dolphin-extension
Source0:        %{name}-%{version}.tar.bz2
Group:          Productivity/Networking/Other

Provides:       itmages-dolphin-extension = %{version}
Obsoletes:      itmages-dolphin-extension < %{version}

Requires:       python-itmages-service dbus-1-python kdelibs4-core
BuildRequires:  update-desktop-files
BuildRequires:  make
BuildRequires:  gcc gcc-c++
BuildRequires:  kdebase4 kdebase4-workspace
BuildRequires:  qt qt-devel libqt4-devel

%description
This extension for the file manager Dolphin, which allows you to quickly
download your images to free image hosting ITmages.ru, in "two clicks". Your
suggestions for improving the script and bug reports can be left on the pages:
https://blueprints.launchpad.net/itmages (requests);
https://bugs.launchpad.net/itmages (bug tracker).

%prep
%setup -q
chmod -x itmages-dolphin-extension.desktop

%build
export PATH="$PATH:/usr/lib/qt4/bin/:/usr/lib64/qt4/bin"
qmake -config releas
make

%install
make INSTALL_ROOT=${RPM_BUILD_ROOT} install
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/ServiceMenus/itmages-dolphin-extension.desktop
%suse_update_desktop_file -c itmages-uploader "ITmages Uploader" "Upload images to ITmages" "itmages-dolphin-extension %U" "%{_datadir}/icons/hicolor/scalable/apps/itmages.svg" "Utility;WebUtility;"
echo "MimeType=image/png;image/jpeg;image/gif;" | tee -a %{buildroot}%{_datadir}/applications/itmages-uploader.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_bindir}/itmages-dolphin-extension
%{_datadir}/icons/hicolor/scalable/apps/itmages.svg
%{_datadir}/itmages/itmages-dolphin-extension_ru.qm
%{_datadir}/applications/itmages-uploader.desktop
%{_datadir}/kde4/services/ServiceMenus/itmages-dolphin-extension.desktop
%dir %{_datadir}/itmages
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/ServiceMenus

%changelog
* Sun Mar 25 2012 DA <dap.darkness@gmail.com> - 20120325-1
- Added desktop file with "Type=Application".

* Mon Jan 09 2012 DA <dap.darkness@gmail.com> - 20120109-1
- Revision #42.
