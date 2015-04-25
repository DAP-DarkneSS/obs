#
# spec file for package modem-manager-gui
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.0.17.1
Release:        0
Summary:        Modem Manager GUI
License:        GPL-3.0+
Group:          Hardware/Mobile
Url:            http://linuxonly.ru/cms/page.php?7
Source:         http://download.tuxfamily.org/gsf/source/modem-manager-gui-%{version}.tar.gz

# PATCH-FIX-UPSTREAM vs. evolution data server 3.16 libebook api break.
Patch0:         modem-manager-gui-0.0.17.1-fix-libebook-api-break.patch

BuildRequires:  fdupes
BuildRequires:  gdbm-devel
BuildRequires:  itstool >= 1.2
BuildRequires:  man
BuildRequires:  po4a
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.1
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
Requires:       ModemManager >= 0.5.0.0
Recommends:     %{name}-lang
Suggests:       evolution-data-server >= 3.4.1
Suggests:       libcanberra0 >= 0.28
Suggests:       libnotify-tools >= 0.7.5

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
# NOTE: if evolution-data-server >= 3.16.
%if 0%{?suse_version} > 1320
%patch0 -p1
%endif

%build
%configure
make %{?_smp_mflags}

%install
make install INSTALLPREFIX=%{buildroot}
%find_lang %{name}
%suse_update_desktop_file -r %{name} 'Internet;Monitor;'
%fdupes -s %{buildroot}%{_datadir}

%post
%desktop_database_post

%postun
%desktop_database_postun

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
%{_mandir}/man*/%{name}.1.*
%dir %{_mandir}/en_US
%dir %{_mandir}/en_US/man1
%dir %{_mandir}/uz@Latn
%dir %{_mandir}/uz@Latn/man1
%{_mandir}/*/man*/%{name}.1.*
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%files lang -f %{name}.lang

%changelog
