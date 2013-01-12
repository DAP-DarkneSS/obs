# norootforbuild

Name:		quimup
Version:	1.2.0
Release:	1

License:	GPL
Summary:	A client for the music player daemon (MPD)
Group:		Productivity/Multimedia/Sound/Players
URL:		http://www.coonsden.com/

Source0:	%{name}_%{version}_source.tar.gz
Source1:	%{name}.desktop

Patch0:		quimup-gcc47.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}

BuildRequires:	libmpdclient-devel libqt4-devel update-desktop-files


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
qmake %{name}.pro
%__make %{?jobs:-j%{jobs}}


%install
%makeinstall
%__install -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
%__install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
%__install -D -m 644 Icons/quimup64.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
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
