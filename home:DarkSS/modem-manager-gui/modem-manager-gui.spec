Summary: Modem Manager GUI
Name: modem-manager-gui
Version: 0.0.16
Release: %mkrel 3
License: GPLv3
Group: Communications/Mobile
URL: http://linuxonly.ru
Source:	%{name}-%{version}.tar.gz
Vendor:	Alex <alex@linuxonly.ru>

BuildRequires: pkgconfig
BuildRequires: libgtk+3.0-devel >= 3.4.0
BuildRequires: glib2-devel >= 2.32.1
BuildRequires: libgdbm-devel >= 1.10

Requires: gtk+3.0 >= 3.4.0
Requires: glib2 >= 2.32.1
Requires: modemmanager >= 0.5.0.0
Suggests: libnotify >= 0.7.5
Suggests: libcanberra0 >= 0.28
Suggests: evolution-data-server >= 3.4.1

Patch0:	modem-manager-gui-0.0.16-recommended-modules.patch
Patch1:	modem-manager-gui-0.0.16-mageia-mm.patch
Patch2: modem-manager-gui-0.0.16-notifications-icon.patch
Patch3: modem-manager-gui-0.0.16-window-position-and-unix-signals.patch

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALLPREFIX=%{buildroot}
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc LICENSE
%doc AUTHORS
%doc Changelog
%{_bindir}/%{name}
%{_libdir}/%{name}/modules/modmm_mm06.so
%{_libdir}/%{name}/modules/modmm_mm07.so
%{_libdir}/%{name}/modules/modcm_nm09.so
%{_libdir}/%{name}/modules/modcm_pppd245.so
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/pixmaps/%{name}.png
%{_datadir}/%{name}/pixmaps/cont-tb.png
%{_datadir}/%{name}/pixmaps/dev-tb.png
%{_datadir}/%{name}/pixmaps/info-tb.png
%{_datadir}/%{name}/pixmaps/scan-tb.png
%{_datadir}/%{name}/pixmaps/sms-tb.png
%{_datadir}/%{name}/pixmaps/ussd-tb.png
%{_datadir}/%{name}/pixmaps/traffic-tb.png
%{_datadir}/%{name}/pixmaps/sms-read.png
%{_datadir}/%{name}/pixmaps/sms-unread.png
%{_datadir}/%{name}/pixmaps/message-received.png
%{_datadir}/%{name}/pixmaps/message-sent.png
%{_datadir}/%{name}/pixmaps/message-drafts.png
%{_datadir}/%{name}/pixmaps/info-equipment.png
%{_datadir}/%{name}/pixmaps/info-network.png
%{_datadir}/%{name}/pixmaps/info-location.png
%{_datadir}/%{name}/sounds/message.ogg
%{_datadir}/%{name}/ui/%{name}.ui
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/modem-manager-gui.1.xz

%changelog

* Tue Jul 28 2013 Alex <alex@linuxonly.ru>
- Recommended modules and mageia-specific patches

* Tue Jun 18 2013 Alex <alex@linuxonly.ru>
- Version 0.0.16 changes

* Fri Apr 12 2013 AlexL <loginov.alex.valer@gmail.com>
- fixed Group for Mageia
- added modemmanager to Requires
- added networkmanager to Suggests
- added patch modem-manager-gui.ui

* Mon Apr 07 2013 Zomby <Zomby@ukr.net>
- repack for Mageia Russian Community

* Tue Dec 16 2012 Alex <alex@linuxonly.ru>
- added additional pictures for 0.0.15 release

* Wed Aug 08 2012 Alex <alex@linuxonly.ru>
- released spec

