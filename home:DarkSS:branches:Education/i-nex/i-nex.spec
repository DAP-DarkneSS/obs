#
# spec file for package i-nex
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


Name:           i-nex
Version:        0.5.6
Release:        1
Summary:        System information tool

License:        LGPL-3.0+
Url:            https://launchpad.net/i-nex
Group:          System/X11/Utilities
Source0:        https://launchpad.net/i-nex/trunk/%{version}/+download/i-nex_%{version}.orig.tar.xz
# series of patches to have full/correct functionality in openSUSE
Patch1:         %{name}_src.patch

BuildArch:      noarch

%if 0%{?suse_version} <= 1210
BuildRequires:  freeglut
%else
BuildRequires:  Mesa-demo-x
%endif
BuildRequires:  gambas3-devel >= 3.5.0
BuildRequires:  gambas3-gb-desktop >= 3.5.0
BuildRequires:  gambas3-gb-form >= 3.5.0
BuildRequires:  gambas3-gb-form-dialog >= 3.5.0
BuildRequires:  gambas3-gb-form-stock >= 3.5.0
BuildRequires:  gambas3-gb-gtk >= 3.5.0
BuildRequires:  gambas3-gb-gui >= 3.5.0
BuildRequires:  gambas3-gb-image >= 3.5.0
BuildRequires:  gambas3-gb-qt4 >= 3.5.0
BuildRequires:  gambas3-gb-qt4-ext >= 3.5.0
BuildRequires:  gambas3-gb-settings >= 3.5.0
BuildRequires:  hicolor-icon-theme
BuildRequires:  lsb-release
BuildRequires:  net-tools
BuildRequires:  pciutils
BuildRequires:  procps
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11 >= 7.5
BuildRequires:  xz
Requires:       gambas3-gb-desktop >= 3.5.0
Requires:       gambas3-gb-form >= 3.5.0
Requires:       gambas3-gb-form-dialog >= 3.5.0
Requires:       gambas3-gb-form-stock >= 3.5.0
Requires:       gambas3-gb-geom >= 3.4.0
Requires:       gambas3-gb-gtk >= 3.5.0
Requires:       gambas3-gb-gui >= 3.5.0
Requires:       gambas3-gb-image >= 3.5.0
Requires:       gambas3-gb-qt4 >= 3.5.0
Requires:       gambas3-gb-qt4-ext >= 3.5.0
Requires:       gambas3-gb-settings >= 3.5.0
Requires:       gambas3-runtime >= 3.5.0
%if 0%{?suse_version} <= 1210
Recommends:     freeglut
%else
Recommends:     Mesa-demo-x
Recommends:     xrandr
%endif
Recommends:     lsb-release
Recommends:     net-tools
Recommends:     pastebinit >= 1.3
Recommends:     pciutils
Recommends:     procps
Recommends:     python
Recommends:     python-configobj
Recommends:     xorg-x11 >= 7.5

%description
An application that gathers information for hardware
components available on your system and displays it using an
user interface similar to the popular Windows tool CPU-Z.
pastebinit required for publishing the hardware configuration.

%prep
%setup -qc
# A hack to be able to run the program via the name execution.
#+ some info tools are under *sbin
cat > %{name}.sh <<HERE
#!/bin/sh

export LIBOVERLAY_SCROLLBAR=0 PATH=/sbin:/usr/sbin:\$PATH
exec %{_bindir}/%{name}.gambas
HERE
%patch1 -p1
#using system's pastebinit
%__sed -i '\|/usr/share/i-nex/pastebinit/|s|/usr/share/i-nex/pastebinit/||' src/i-nex/.src/Reportm.module
%__cp src/i-nex/logo/i-nex.0.4.x.png $RPM_SOURCE_DIR/%{name}.png
%{__sed} -e 's|env LIBOVERLAY_SCROLLBAR=0 /usr/bin/i-nex.gambas|i-nex|' \
         -e '/^Icon=/s|=.*|=%{name}|' debian/%{name}.desktop > %{name}.desktop

%build
make V=1 %{?_smp_mflags}

%install
%{__install} -D -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}
%{__install} -m 755 src/i-nex/%{name}.gambas debian/check_kernel %{buildroot}%{_bindir}/
%suse_update_desktop_file -i -G "I-Nex, system information tool" %{name} HardwareSettings

%files
%defattr(-,root,root,-)
%doc debian/changelog* COPYING LICENSE README
%{_bindir}/%{name}*
%{_bindir}/check_kernel
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
