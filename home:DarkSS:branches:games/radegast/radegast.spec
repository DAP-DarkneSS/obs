# vim: set sw=4 ts=4 et nu:
#
# spec file for package radegast
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/

Name:           radegast
Version:        2.10
Release:        0
Summary:        Radegast Metaverse Client
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
Source:         http://radegast.googlecode.com/files/radegast-%{version}-src.zip
Url:            http://radegast.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  mono-devel
BuildRequires:  nant
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-fonts-core

%description
Lightweight client for connecting to Second Life and OpenSim based virtual
worlds.

%prep
%setup -q -n "%{name}-%{version}-src"
%__sed -i 's/\r$//' radegast/LICENSE.txt

%build
pushd radegast
sh ./runprebuild-nant.sh
nant Release build
popd

%install
pushd radegast
%__install -d "%{buildroot}%{_libdir}"
%__mv bin "%{buildroot}%{_libdir}/%{name}"
popd

%__install -d "%{buildroot}%{_bindir}"
cat<<EOF > "%{buildroot}%{_bindir}/%{name}"
#!/bin/sh
set -e
cd "%{_libdir}/%{name}"
exec mono ./Radegast.exe "$@"
EOF
%__chmod 0755 "%{buildroot}%{_bindir}/%{name}"

%__install -d "%{buildroot}%{_datadir}/pixmaps"
%__ln_s "%{_libdir}/%{name}/radegast.png" \
    "%{buildroot}%{_datadir}/pixmaps/radegast.png"

%__install -d "%{buildroot}%{_datadir}/applications"
cat<<EOF >"%{buildroot}%{_datadir}/applications/%{name}.desktop"
[Desktop Entry]
Name=Radegast
GenericName=OpenSim Viewer
Comment=Lightweight Second Life and OpenSim Viewer
Exec=%{name}
Terminal=false
Type=Application
Encoding=UTF-8
Icon=radegast
Categories=Network;InstantMessaging;
EOF

%suse_update_desktop_file -r "%{name}" Network InstantMessaging

%fdupes -s "%{buildroot}%{_libdir}/%{name}/"

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc radegast/LICENSE.txt
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*

%changelog
