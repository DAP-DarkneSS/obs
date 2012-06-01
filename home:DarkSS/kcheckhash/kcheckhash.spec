#
# spec file for package kcheckhash
#
# Copyright (c) 2011-2012 PetrovSE
# http://forum.ubuntu.ru/index.php?action=profile;u=12963
#
# Please submit bugfixes or comments via
# http://forum.ubuntu.ru/index.php?topic=178697.0
#

Name:           kcheckhash
Version:        0.2
Release:        1
Summary:        Program to calculate hashes

License:        Unknown
URL:            http://forum.ubuntu.ru/index.php?topic=178697.0
Source0:        %{name}.tar.gz
Group:          System/GUI/KDE

Recommends:     dolphin-plugin-checksum
BuildRequires:  libqt4-devel
BuildRequires:  mhash-devel
BuildRequires:  update-desktop-files

%description
The program to calculate crc32, md5, sha1 и sha256 via libmhash2.

%package -n dolphin-plugin-checksum
Summary:        Dolphin extension to calculate hashes
Requires:       %{name}
Requires:       dolphin
BuildArch:      noarch

%description -n dolphin-plugin-checksum
The Dolphin extension to calculate crc32, md5, sha1 и sha256 via libmhash2.

%prep
%setup -q -n %{name}

%build
qmake
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} resource/main.png %{buildroot}%{_datadir}/pixmaps/security-high.png
mkdir -p %{buildroot}%{_datadir}/kde4/services
%{__install} usr/share/kde4/services/checksum.desktop %{buildroot}%{_datadir}/kde4/services
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/checksum.desktop -r 'Utility;Accessibility;'
mkdir -p %{buildroot}%{_datadir}/applications/kde4
%{__install} usr/share/applications/kde4/kcheckhash.desktop %{buildroot}%{_datadir}/applications/kde4
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/kde4/kcheckhash.desktop -r 'Utility;Accessibility;'
mkdir -p %{buildroot}%{_bindir}
%{__install} usr/bin/kcheckhash %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/pixmaps/security-high.png
%dir %{_datadir}/applications/kde4
%attr(644,root,root) %{_datadir}/applications/kde4/%{name}.desktop

%files -n dolphin-plugin-checksum
%defattr(-,root,root,-)
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%attr(644,root,root) %{_datadir}/kde4/services/checksum.desktop

%changelog
