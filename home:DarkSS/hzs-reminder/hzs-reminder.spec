#
# spec file for package [spectemplate]
#
# Copyright (c) 2010-2012 Nisel Alexander II (source),
# (c) 2011-2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via http://software.nisel.net/contacts.html
#

Name:           hzs-reminder
Version:        2012.01.03
Release:        1
Summary:        Informs about upcoming events from the system tray

License:        GPL-3.0
Group:          Productivity/Other
URL:            http://software.nisel.net/reminder.html
Source0:        %{name}-%{version}.tar.lzma
Patch1:         translation.patch

Provides:       reminder
BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files xz
Recommends:     kdialog
Conflicts:      hzs-reminder-4darkness reminder-4darkness

%description
This program informs from the system tray about upcoming events,
for example about the birthdays. It is not an organizer.

%prep
%setup -q
%patch1

%build
qmake reminder.pro
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} reminder %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} ./deb/usr/share/pixmaps/reminderico.png %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
%{__install} ./deb/usr/share/applications/reminder.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/%{name}/translations
%{__install} ./translations/reminder_ru.qm %{buildroot}%{_datadir}/%{name}/translations/hzs-reminder_ru_RU.qm
%suse_update_desktop_file -r %{name} Office Calendar

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%attr(755,root,root) %{_bindir}/reminder
%{_datadir}/pixmaps/reminderico.png
%{_datadir}/applications/%{name}.desktop
%defattr(644,root,root,755)
%lang(ru_RU) %{_datadir}/%{name}/translations/%{name}_ru_RU.qm

%changelog
