#
# spec file for package soundz
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

Name:           soundz
Version:        3.6.1
Release:        0
License:        GPL-3.0+
Summary:        Minimalistic audio player
Group:          Productivity/Multimedia/Sound/Players
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       dbus-1-python
Requires:       gstreamer-plugins-base
Requires:       python-gstreamer010
Requires:       python-gtk
Requires:       python-mutagen
Requires:       python-xdg
Recommends:     gettext-runtime
Recommends:     google-droid-fonts
Recommends:     gstreamer-0_10-plugins-fluendo_mp3
Recommends:     gstreamer-plugins-ugly
Recommends:     pulseaudio
BuildArch:      noarch

%description
A PyGTK audio player designed for XFCE

%prep
%setup -q
chmod -x */*.py
chmod -x pix/g*
chmod -x */*/*.py

%build

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} bin %{buildroot}%{_bindir}/soundz
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -af {pix,gui,soundz,utils,mods} %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/applications
%{__install} desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}/%{_datadir}/pixmaps
%{__install} pix/48.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -r %{name} 'AudioVideo;Player;'
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
