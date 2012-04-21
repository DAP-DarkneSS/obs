#
# spec file for package kbd_alt_shift.map
#
# Copyright (c) 2010-2012 Alexey Gladkov (GPL-2.0),
# (c) 2012 Perlow Dmitriy A. (patch & spec file)
#

Name:           kbd_alt_shift.map
Summary:        Keyboard and Font Utilities: keymap with switching by left Alt+Shift
URL:            http://kbd-project.org/
Source0:        ruwin_ct_sh-UTF-8.map.bz2
Version:        0.1
Release:        0
Patch1:         alt.patch
License:        GPLv2
Group:          System/Console
BuildArch:      noarch
Requires:       kbd

%description
Load and save keyboard mapping. This is needed if you are not using
the US keyboard map. If you install this package, YaST includes an extra
menu to allow you to choose between the different fonts. This package
includes keymap with languages switching by left Alt+Shift.

%prep
bunzip2 -c -k %{SOURCE0} > ruwin_alt_sh-UTF-8.map
%patch1

%build
gzip -9 'ruwin_alt_sh-UTF-8.map'

%install
mkdir -p %{buildroot}%{_datadir}/kbd/keymaps/i386/qwerty
%{__install} ruwin_alt_sh-UTF-8.map.gz %{buildroot}%{_datadir}/kbd/keymaps/i386/qwerty

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/kbd
%dir %{_datadir}/kbd/keymaps
%dir %{_datadir}/kbd/keymaps/i386
%dir %{_datadir}/kbd/keymaps/i386/qwerty
%attr(644,root,root) %{_datadir}/kbd/keymaps/i386/qwerty/ruwin_alt_sh-UTF-8.map.gz

%changelog
