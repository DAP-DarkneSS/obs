#
# spec file for package [spectemplate]
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
# norootforbuild

Name:           hzs-reminder-4darkness
Version:        2010.4.20.2
Release:        4
Summary:        This program informs about upcoming events from the system tray

License:        GPL-3.0
Group:          Productivity/Other
URL:            http://software.nisel.net/reminder.html
Source0:        hzs-reminder-4darkness-2010.4.20.2.tar.lzma

Provides:       reminder-4darkness
BuildRequires:  xz
BuildRequires:  update-desktop-files
%ifarch x86_64
Requires:       libqt4-x11-32bit
%else
Requires:       libqt4-x11
%endif
# BuildArch:      noarch
Conflicts:      hzs-reminder reminder

%description
This program informs from the system tray about upcoming events,
for example about the birthdays. It is not the organizer.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
mv reminder %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mv reminderico.png %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
mv reminder.desktop %{buildroot}%{_datadir}/applications
%suse_update_desktop_file -r reminder Office Calendar

%clean
rm -rf %{buildroot}

%files
%attr(755,root,root) %{_bindir}/reminder
%defattr(-,root,root)
%{_datadir}/pixmaps/reminderico.png
%{_datadir}/applications/reminder.desktop

%changelog
