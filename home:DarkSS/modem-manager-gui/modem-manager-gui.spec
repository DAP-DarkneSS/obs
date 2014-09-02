#
# spec file for package modem-manager-gui
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

Name:           modem-manager-gui
Version:        0.0.16
Release:        0
License:        GPL-3.0+
Summary:        Modem Manager GUI
Url:            http://linuxonly.ru/cms/page.php?7
Group:          Hardware/Mobile
Source:         http://download.tuxfamily.org/gsf/source/modem-manager-gui-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  gdbm-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.1
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
Requires:       ModemManager >= 0.5.0.0
Recommends:     %{name}-lang
Suggests:       evolution-data-server >= 3.4.1
Suggests:       libcanberra0 >= 0.28
Suggests:       libnotify-tools >= 0.7.5

# PATCH-UPSTREAM from Mageia package.
Patch1:         modem-manager-gui-0.0.16-notifications-icon.patch
# PATCH-FIX-UPSTREAM to prevent gcc warnings.
Patch2:         modem-manager-gui-0.0.16-fix-gcc-warnings.patch

%description
This program is simple graphical interface for Modem Manager
daemon dbus interface.
Current features:
- View device information: Operator name, Mode, IMEI, IMSI,
  Signal level.
- Send and receive SMS messages with long massages
  concatenation and store messages in database.
- Send USSD requests and read answers in GSM7 and UCS2 formats
  converted to system UTF8 charset.
- Scan available mobile networks.

%lang_package

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure
make %{?_smp_mflags}

%install
make install INSTALLPREFIX=%{buildroot}
%find_lang %{name}
%suse_update_desktop_file -r %{name} 'Internet;Monitor;'
%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%doc LICENSE
%doc AUTHORS
%doc Changelog
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*

%files lang -f %{name}.lang

%changelog
