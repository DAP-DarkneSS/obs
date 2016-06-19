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
Version:        0.0.18
Release:        0
Summary:        Modem Manager GUI
License:        GPL-3.0+
Group:          Hardware/Mobile
Url:            http://linuxonly.ru/cms/page.php?7
Source:         http://download.tuxfamily.org/gsf/source/modem-manager-gui-%{version}.tar.gz

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
%dir %{_mandir}/tr
%dir %{_mandir}/uk
%dir %{_mandir}/uz*
%{_mandir}/*/*
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
# https://bugzilla.novell.com/show_bug.cgi?id=950215
%exclude %{_datadir}/polkit-1/actions/ru.linuxonly.modem-manager-gui.policy

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
