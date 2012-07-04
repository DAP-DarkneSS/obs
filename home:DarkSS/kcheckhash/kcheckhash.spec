#
# spec file for package kcheckhash
#
# Copyright (c) 2011-2012 PetrovSE https://github.com/PetrovSE
#
# Please submit bugfixes or comments via
# https://github.com/PetrovSE/kcheckhash/issues or
# http://forum.ubuntu.ru/index.php?topic=178697.0
#

Name:           kcheckhash
Version:        0.3
Release:        1
Summary:        Qt/C++ tool to calculate hashes

License:        LGPL-3.0+
URL:            https://github.com/PetrovSE/kcheckhash
Source0:        https://github.com/PetrovSE/kcheckhash/tarball/v%{version}
Group:          Productivity/Other

Recommends:     dolphin-plugin-checksum
Requires:       oxygen-icon-theme
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
%setup -q -n PetrovSE-%{name}-d8e8cc1

%build
qmake QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags} 

%install
make install INSTALL_ROOT=%{buildroot}

# A hack against https://bugzilla.novell.com/show_bug.cgi?id=766385
mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} resource/main.png %{buildroot}%{_datadir}/pixmaps/security-high.png

%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/kde4/kcheckhash.desktop 'Utility;DesktopUtility;'
%suse_update_desktop_file -r %{buildroot}%{_datadir}/kde4/services/checksum.desktop 'Utility;DesktopUtility;'

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%exclude %attr(644,root,root) %{_datadir}/pixmaps/security-high.png
%dir %{_datadir}/applications/kde4
%attr(644,root,root) %{_datadir}/applications/kde4/%{name}.desktop

%files -n dolphin-plugin-checksum
%defattr(-,root,root,-)
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%attr(644,root,root) %{_datadir}/kde4/services/checksum.desktop

%changelog
