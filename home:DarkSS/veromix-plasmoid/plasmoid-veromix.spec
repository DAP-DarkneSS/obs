#
# spec file for package plasmoid-veromix
#
# Copyright (c) 2010-2012 Veronix: http://code.google.com/p/veromix-plasmoid/people/list
#
# Please submit bugfixes or comments via http://code.google.com/p/veromix-plasmoid/issues/list
#

%define _git 369

Name:           plasmoid-veromix
Version:        0.15.1.git%{_git}
Release:        0
Summary:        Mixer plasmoid for the Pulseaudio sound server

License:        GPL-3.0+
Url:            http://code.google.com/p/veromix-plasmoid/
Group:          System/GUI/KDE
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  fdupes
BuildRequires:  kdebase4-workspace-devel
BuildRequires:  update-desktop-files
Requires:       kdebase4-workspace
Requires:       pulseaudio
Requires:       python-kde4
Requires:       python-qt4
Requires:       python-xdg python-devel
Requires:       python-kdebase4
Requires:       ladspa-swh-plugins
%kde4_runtime_requires
BuildArch:      noarch

%description
Veromix is a mixer plasmoid for the Pulseaudio sound server.

Features:
- Media Player Controls (aka nowplaying)
- Per application volume control (replay & record)
- Global hotkeys
- Can live in system tray

%prep
%setup -q
# Fix permissions
chmod 755 dbus-service/*.py
for i in PulseCard.py PulseClient.py PulseSink.py PulseSource.py PulseStream.py PulseVolume.py; do chmod 755 dbus-service/pulseaudio/$i; done
chmod 755 contents/code/Dummy-Testclient-dbus.py

%build

%install
%make_install

# Fix icon installation
mkdir -p %{buildroot}%{_kde4_iconsdir}/hicolor/128x128/apps
rm %{buildroot}%{_kde4_iconsdir}/veromix-plasmoid.png
%{__install} -pm 0644 contents/icons/veromix-plasmoid-128.png %{buildroot}%{_kde4_iconsdir}/hicolor/128x128/apps/veromix-plasmoid.png

# Remove po files
find %{buildroot}%{_kde4_appsdir}/plasma/plasmoids/veromix-plasmoid/contents/locale -name *.po -exec rm -f {} \;

%find_lang veromix-plasmoid

%kde_post_install

%fdupes -s %{buildroot}

%clean
rm -rf %{buildroot}

%files -f veromix-plasmoid.lang
%defattr(-,root,root,-)
%dir %{_kde4_appsdir}/plasma/plasmoids
%{_kde4_appsdir}/plasma/plasmoids/veromix-plasmoid/
%{_kde4_iconsdir}/hicolor/128x128/apps/veromix-plasmoid.png
%{_kde4_servicesdir}/plasma-widget-veromix.desktop
%{_datadir}/dbus-1/services/org.veromix.pulseaudio.service

%changelog
* Wed Feb 01 2012 DA <dap.darkness@gmail.com> - 20120201-1
- Version 0.15.0. Revision 369:
- Support for changing ports of sinks by Jonathan Challinger.
- Fixes Issue 85: Cannot switch microphone inputs.
- Update italian translation.

* Sun Jan 28 2012 DA <dap.darkness@gmail.com> - 20120128-1
- Version 0.14.1. Revision 343:
- Adding right click context menu.
- The button on the right opens the context menu.
- Moving all channel related settings to the context menu (dropping in channel checkbox and/or comboboxes).
- Adding a configuration option to hide the context menu button.
- Adding a fallback for the brooken mpris support in deadbeef.
- Fix: Record streams no longer showing up in veromix.
- Rearranging context menu items.
- Updating translation files.

* Wed Jan 25 2012 DA <dap.darkness@gmail.com> - 20120125-1
- Version 0.13.2. Revision 317:
- fix: Dropdownbox of audiooutput lies not on top of the sliders (Issue 37).
- enable "apply" button when the user changes settings in the settings dialog.
- add an option to disable album art (fixes issue 75).

* Tue Jan 10 2012 DA <dap.darkness@gmail.com> - 20120110-1
- Version 0.13.1. Revision 303:
- fix sorting of sources
- fix sink-output selection in combobox
- fix label of tooltip
- improve label position for bigger fonts
