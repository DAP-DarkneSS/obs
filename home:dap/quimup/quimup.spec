# norootforbuild

Name:		quimup
Version:	1.3.1
Release:	1

License:	GPL-3.0+
Summary:	A client for the music player daemon (MPD)
Group:		Productivity/Multimedia/Sound/Players
URL:		http://www.coonsden.com/

Source0:	http://sourceforge.net/projects/musicpd/files/Quimup/%{version}/%{name}_%{version}_src.tar.gz
Source1:	%{name}.desktop

Patch0:		quimup-gcc47.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}

BuildRequires:	libmpdclient-devel libqt4-devel update-desktop-files

Requires:	mpd

%description
QUIMUP is a client for the music player daemon (MPD) written in C++ and QT3.

The program can be used with most Linux desktops (KDE, GNOME, XFCE) and is covered
by the General Public License: it is free and 'open source'.
The clean interface makes controlling MPD's many features easy and intuitive.
The focus is on mouse handling: playlist management is done entirely by drag-&-drop;
playback functions are directly accessible from the system tray.
Quimup turns MPD into a perfect desktop music player.





%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
%__sed -i -e "s|/usr/lib/libmpdclient.so|/usr/%{_lib}/libmpdclient.so|g" %{name}.pro

qmake \
QMAKE_STRIP="" \
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}" \
%{name}.pro

%__make %{?jobs:-j%{jobs}}


%install
%makeinstall
%__install -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
%__install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
%__install -D -m 644 src/resources/mn_icon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -r %{name} AudioVideo Player


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc COPYING changelog description FAQ.txt README todo
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
