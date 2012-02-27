#
# spec file for package [spectemplate]
#
# Copyright (c) 2009-2012 ITmages: https://launchpad.net/itmages
#
# Please submit bugfixes or comments via https://bugs.launchpad.net/itmages
#

%define _revision rev.42

Name:           itmages-dolphin-extension
Version:        1.07.%{_revision}
Release:        2
Summary:        ITmages Dolphin extension

License:        GPL-3.0
URL:            https://launchpad.net/itmages/itmages-dolphin-extension
Source0:        %{name}-%{version}.tar.bz2
Group:          Development/Libraries/KDE
BuildRoot:      %{_tmppath}/%{name}-1.07
Provides:       itmages-dolphin
Requires:       python-itmages-service dbus-1-python kdelibs4-core
BuildRequires:  qt update-desktop-files
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kdebase4
BuildRequires:  qt-devel
BuildRequires:  libqt4-devel
BuildRequires:  kdebase4-workspace

%description
This extension for the file manager Dolphin,
which allows you to quickly download your images
to free image hosting ITmages.ru, in "two clicks".
Your suggestions for improving the script and bug
reports can be left on the pages:
requests - https://blueprints.launchpad.net/itmages
bug tracker - https://bugs.launchpad.net/itmages

%prep
%setup -q
chmod -x itmages-dolphin-extension.desktop

%build
export PATH="$PATH:/usr/lib/qt4/bin/:/usr/lib64/qt4/bin"
qmake -config releas
make

%install
make INSTALL_ROOT=${RPM_BUILD_ROOT} install
mkdir -p %{buildroot}%{_datadir}/doc/itmages/dolphin
%{__install} README %{buildroot}%{_datadir}/doc/itmages/dolphin/
%{__install} COPYING %{buildroot}%{_datadir}/doc/itmages/dolphin/
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/ServiceMenus/itmages-dolphin-extension.desktop

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_datadir}/doc/itmages/dolphin
%{_datadir}/doc/itmages/dolphin/*
%{_bindir}/itmages-dolphin-extension
%{_datadir}/icons/hicolor/scalable/apps/itmages.svg
%{_datadir}/itmages/itmages-dolphin-extension_ru.qm
%{_datadir}/kde4/services/ServiceMenus/itmages-dolphin-extension.desktop
%dir %{_datadir}/itmages
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/ServiceMenus

%changelog
* Mon Jan 09 2012 DA <dap.darkness@gmail.com> - 20120109-1
- Revision #42.
