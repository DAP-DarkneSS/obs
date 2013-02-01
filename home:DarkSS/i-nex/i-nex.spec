#
# spec file for package i-nex
#
# Copyright (c) 2012, https://launchpad.net/~i-nex-development-team (source),
# (c) 2013 Perlow Dmitriy A. (spec file).
#
# Please submit bugfixes or comments via https://bugs.launchpad.net/i-nex
#

Name:           i-nex
Version:        0.5.2
Release:        1
Summary:        System information tool

License:        LGPL-3.0+
Url:            https://launchpad.net/i-nex
Group:          System/X11/Utilities
Source0:        https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}_%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gambas3-devel
BuildRequires:  gambas3-gb-desktop
BuildRequires:  gambas3-gb-form-dialog
BuildRequires:  gambas3-gb-gui
BuildRequires:  gambas3-gb-image
BuildRequires:  gambas3-gb-settings
BuildRequires:  update-desktop-files

Requires:       gambas3-gb-desktop
Requires:       gambas3-gb-form-dialog
Requires:       gambas3-gb-gui
Requires:       gambas3-gb-image
Requires:       gambas3-gb-qt4
Requires:       gambas3-gb-settings
Requires:       gambas3-runtime

Recommends:     Mesa-demo-x
Recommends:     xrandr

%description
An application that gathers information for hardware
components available on your system and displays it using an
user interface similar to the popular Windows tool CPU-Z.

%prep
%setup -q -n %{name}
sed -i 's|env LIBOVERLAY_SCROLLBAR=0 /usr/bin/i-nex.gambas|i-nex|' debian/%{name}.desktop

%build
cd src/%{name}
gbc3 -eagtpmv
gba3

%install
mkdir -p %{buildroot}%{_bindir}
# A hack to be able to run the program via the name execution.
echo -e '#!/bin/sh'"\n\nenv LIBOVERLAY_SCROLLBAR=0 %{_bindir}/i-nex.gambas" > %{buildroot}%{_bindir}/%{name}
%{__install} src/i-nex/i-nex.gambas %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} src/i-nex/logo/i-nex.0.4.x.png %{buildroot}%{_datadir}/pixmaps/i-nex.0.4.x.png

mkdir -p %{buildroot}%{_datadir}/%{name}/pastebinit
cp -rf pastebin.d utils pastebinit{,.xml} release.conf test.sh %{buildroot}%{_datadir}/%{name}/pastebinit
chmod +x %{buildroot}%{_datadir}/%{name}/pastebinit/test.sh
chmod +x %{buildroot}%{_datadir}/%{name}/pastebinit/utils/pbput

%suse_update_desktop_file -i -r %{name} "System;HardwareSettings;"

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}*

%changelog
