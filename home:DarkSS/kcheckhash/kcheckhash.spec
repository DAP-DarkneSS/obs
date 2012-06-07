#
# spec file for package kcheckhash
#
# Copyright (c) 2011-2012 PetrovSE https://github.com/PetrovSE
#
# Please submit bugfixes or comments via
# http://forum.ubuntu.ru/index.php?topic=178697.0
#

Name:           kcheckhash
Version:        0.2
Release:        1
Summary:        Qt/C++ tool to calculate hashes

License:        LGPL-3.0+
URL:            https://github.com/PetrovSE/kcheckhash
Source0:        %{name}.tar.gz
Group:          Productivity/Other

Recommends:     dolphin-plugin-checksum
BuildRequires:  libqt4-devel
BuildRequires:  mhash-devel
BuildRequires:  update-desktop-files

%description
Program to calculate crc32, md5, sha1 and sha256 via libmhash2.

%package -n dolphin-plugin-checksum
Summary:        Dolphin extension to calculate hashes
Requires:       %{name}
Requires:       dolphin
BuildArch:      noarch

%description -n dolphin-plugin-checksum
Dolphin extension to calculate crc32, md5, sha1 and sha256 via libmhash2.

%prep
%setup -q -n %{name}

%build
qmake
make %{?_smp_mflags} 

%install
make install INSTALL_ROOT=%{buildroot}

# # mkdir -p %{buildroot}%{_datadir}/pixmaps
# # %{__install} resource/main.png %{buildroot}%{_datadir}/pixmaps/security-high.png
# # 
# # mkdir -p %{buildroot}%{_datadir}/kde4/services
# # %{__install} usr/share/kde4/services/checksum.desktop %{buildroot}%{_datadir}/kde4/services
# # 
# # mkdir -p %{buildroot}%{_datadir}/applications/kde4
# # %{__install} usr/share/applications/kde4/kcheckhash.desktop %{buildroot}%{_datadir}/applications/kde4
# # 
# # mkdir -p %{buildroot}%{_bindir}
# # %{__install} usr/bin/kcheckhash %{buildroot}%{_bindir}

echo "MimeType=all/allfiles;" | tee -a %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/kde4/kcheckhash.desktop -r 'Utility;DesktopUtility;'
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/checksum.desktop -r 'Utility;DesktopUtility;'

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
