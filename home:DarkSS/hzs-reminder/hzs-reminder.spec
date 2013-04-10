#
# spec file for package hzs-reminder
#
# Copyright (c) 2010-2012 Nisel Alexander II (source),
# (c) 2011-2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# http://software.nisel.net/contacts.html
# or via http://bugs.opensuse.org/
#

Name:           hzs-reminder
Version:        2012.09.30
Release:        1
Summary:        Informs about upcoming events from the system tray

License:        GPL-3.0
Group:          Productivity/Other
URL:            http://software.nisel.net/reminder.html
Source0:        http://software.nisel.net/programs/hzs_reminder_source.tar.gz
Source1:        reminder.desktop
# PATCH-FIX-UPSTREAM to be able to load russian locale file.
Patch1:         translation.patch

%if 0%{?fedora} <= 17
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig(QtCore)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
This program informs from the system tray about upcoming events,
for example about the birthdays. It is not an organizer.

%prep
%setup -q -n hzs_reminder_source
%patch1

%build
`pkg-config --variable=exec_prefix QtCore`/bin/qmake \
QMAKE_STRIP="" \
QMAKE_CXXFLAGS+="%{optflags}" \
reminder.pro
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} reminder %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} ./ico/normal.png %{buildroot}%{_datadir}/pixmaps/reminderico.png
mkdir -p %{buildroot}%{_datadir}/applications
%{__install} %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%if 0%{?suse_version}
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop -r Office Calendar
%endif
mkdir -p %{buildroot}%{_datadir}/%{name}/translations
%{__install} ./translations/reminder_ru.qm %{buildroot}%{_datadir}/%{name}/translations/

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/reminder
%{_datadir}/pixmaps/reminderico.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
