#
# spec file for package quimup
#
# Copyright (c) 2015 Packman team: http://packman.links2linux.org/
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.links2linux.org/
#


Name:           quimup
Version:        1.4.0
Release:        0
Summary:        A client for the music player daemon (MPD)
License:        GPL-3.0+
Group:          Productivity/Multimedia/Sound/Players
Url:            http://www.coonsden.com/
Source0:        http://sourceforge.net/projects/musicpd/files/Quimup/%{version}/%{name}_%{version}_src.tar.gz
Source1:        %{name}.desktop
Patch0:         quimup-gcc47.patch
# PATCH-FIX-UPSTREAM qt5-5.5.patch avvissu@yandex.ru -- Fix build with Qt5 >= 5.5
Patch1:         quimup-1.4.0_qt5-5.5.patch
BuildRequires:  libmpdclient-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(taglib)
Requires:       mpd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
QUIMUP is a client for the music player daemon (MPD) written in C++ and QT3.

The program can be used with most Linux desktops (KDE, GNOME, XFCE) and is covered
by the General Public License: it is free and 'open source'.
The clean interface makes controlling MPD's many features easy and intuitive.
The focus is on mouse handling: playlist management is done entirely by drag-&-drop;
playback functions are directly accessible from the system tray.
Quimup turns MPD into a perfect desktop music player.

%prep
# we don't want a space in the path
%setup -c -T
tar -xzf %{SOURCE0} --strip-components=1
%patch0 -p1
%patch1 -p1

%build
qmake-qt5 \
QMAKE_STRIP="" \
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}" \
%{name}.pro

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m 644 src/resources/mn_icon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -r %{name} AudioVideo Player


%files
%defattr(-,root,root)
%doc COPYING changelog description FAQ.txt README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
