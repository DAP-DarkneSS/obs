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
# series of patches to have full/correct functionality in openSUSE
Patch:          %{name}-check_kernel.patch
Patch1:         %{name}_src.patch

BuildArch:      noarch

BuildRequires:  gambas3-devel >= 3.4.0
BuildRequires:  gambas3-gb-image >= 3.4.0
BuildRequires:  gambas3-gb-gtk >= 3.4.0
BuildRequires:  gambas3-gb-qt4 >= 3.4.0 gambas3-gb-qt4-ext >= 3.4.0
BuildRequires:  gambas3-gb-form >= 3.4.0
BuildRequires:  gambas3-gb-desktop >= 3.4.0
BuildRequires:  gambas3-gb-form-dialog >= 3.4.0
BuildRequires:  gambas3-gb-settings >= 3.4.0
BuildRequires:  gambas3-gb-form-stock >= 3.4.0
BuildRequires:  gambas3-gb-gui >= 3.4.0
BuildRequires:  lsb-release
BuildRequires:  pciutils
BuildRequires:  procps
BuildRequires:  net-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%if 0%{?suse_version} <= 1210
BuildRequires:  freeglut
%else
BuildRequires:  Mesa-demo-x
%endif
BuildRequires:  xorg-x11 >= 7.5

Requires:       gambas3-runtime >= 3.4.0
Requires:       gambas3-gb-image >= 3.4.0
Requires:       gambas3-gb-gtk >= 3.4.0
Requires:       gambas3-gb-qt4 >= 3.4.0 gambas3-gb-qt4-ext >= 3.4.0
Requires:       gambas3-gb-form >= 3.4.0
Requires:       gambas3-gb-desktop >= 3.4.0
Requires:       gambas3-gb-form-dialog >= 3.4.0
Requires:       gambas3-gb-gui >= 3.4.0
Requires:       gambas3-gb-settings >= 3.4.0
Requires:       gambas3-gb-form-stock >= 3.4.0
%if 0%{?suse_version} <= 1210
Recommends:     freeglut
%else
Recommends:     Mesa-demo-x
Recommends:     xrandr
%endif
Recommends:     xorg-x11 >= 7.5
Recommends:     net-tools
Recommends:     lsb-release
Recommends:     procps
Recommends:     pciutils
Recommends:     python
Recommends:     python-configobj
Recommends:     pastebinit >= 1.3

%description
An application that gathers information for hardware
components available on your system and displays it using an
user interface similar to the popular Windows tool CPU-Z.
pastebinit required for publishing the hardware configuration.

%prep
%setup -q -n %{name}
# A hack to be able to run the program via the name execution.
#+ some info tools are under *sbin
cat > %{name}.sh <<HERE
#!/bin/sh

export LIBOVERLAY_SCROLLBAR=0 PATH=/sbin:/usr/sbin:\$PATH
exec %{_bindir}/%{name}.gambas
HERE
%patch
%patch1 -p1
#using system's pastebinit
%__sed -i '\|/usr/share/i-nex/pastebinit/|s|/usr/share/i-nex/pastebinit/||' src/i-nex/.src/Reportm.module
%__cp src/i-nex/logo/i-nex.0.4.x.png $RPM_SOURCE_DIR/%{name}.png
%{__sed} -e 's|env LIBOVERLAY_SCROLLBAR=0 /usr/bin/i-nex.gambas|i-nex|' \
         -e '/^Icon=/s|=.*|=%{name}|' debian/%{name}.desktop > %{name}.desktop

%build
/usr/bin/gbc3 -e -a -g -t -p -m  src/i-nex
gba3 src/i-nex

%install
%{__install} -D -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}
%{__install} -m 755 src/i-nex/%{name}.gambas debian/check_kernel %{buildroot}%{_bindir}/
%suse_update_desktop_file -i -G "I-Nex, system information tool" %{name} HardwareSettings

%files
%defattr(-,root,root,-)
%doc debian/changelog* debian/copyright LICENSE
%{_bindir}/%{name}*
%{_bindir}/check_kernel
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
