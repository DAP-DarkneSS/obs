Summary:   MiniRacer game
Name:      miniracer
Version:   1.04
Release:   1
Group:     games
Copyright: GPL
Vendor:    Martin Weiss <plattfisch@epost.de>
Url:       http://miniracer.sourceforge.net
Packager:  Martin Weiss <plattfisch@epost.de>
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
 MiniRacer is an OpenGL car racing game, based on the Quake1 engine.
 It was written by Thomas Jakobsson for the win32 platform and ported
 to Linux by Martin Weiss. This Release can still contain bugs.
 See the website http://miniracer.sourceforge.net for details.
 Enjoy!

%prep
%setup -q

%build
%{__make}

%install
install -d %{_tmppath}/%{name}-%{version}-root/usr/bin
install -d %{_tmppath}/%{name}-%{version}-root/usr/share/man/man6
install -d %{_tmppath}/%{name}-%{version}-root/usr/share/games/MiniRacer
install -d %{_tmppath}/%{name}-%{version}-root/usr/share/games/MiniRacer/data
install -d %{_tmppath}/%{name}-%{version}-root/usr/share/games/MiniRacer/data/maps
install -m 755 engine.glx %{_tmppath}/%{name}-%{version}-root/usr/share/games/MiniRacer
install -m 644 data/pak0.pak %{_tmppath}/%{name}-%{version}-root/usr/share/games/MiniRacer/data
install -m 644 data/config.cfg %{_tmppath}/%{name}-%{version}-root/usr/share/games/MiniRacer/data
install -m 755 miniracer %{_tmppath}/%{name}-%{version}-root/usr/bin/miniracer
install -m 644 miniracer.6 %{_tmppath}/%{name}-%{version}-root/usr/share/man/man6
install -m 644 data/maps/*.bsp %{_tmppath}/%{name}-%{version}-root/usr/share/games/MiniRacer/data/maps
install -m 644 data/maps/maps1.lst %{_tmppath}/%{name}-%{version}-root/usr/share/games/MiniRacer/data/maps

%clean
%{__make} clean

%files
%defattr(-,root,root)
%attr(0755,-,-) /usr/share/games/MiniRacer/engine.glx
%attr(0644,-,-) /usr/share/games/MiniRacer/data/pak0.pak
%attr(0644,-,-) /usr/share/games/MiniRacer/data/config.cfg
%attr(0644,-,-) /usr/share/games/MiniRacer/data/maps/*.bsp
%attr(0644,-,-) /usr/share/games/MiniRacer/data/maps/maps1.lst
%attr(0755,-,-) /usr/bin/miniracer
%attr(0644,-,-) /usr/share/man/man6/miniracer.6.gz



%changelog
* Thu May 5 2005 Martin Weiss <plattfisch@users.sourceforge.net>
- Updated RPM release

* Tue Sep 30 2003 Martin Weiss <plattfisch@users.sourceforge.net>
- Updated RPM release

* Mon Mar 10 2003 Martin Weiss <plattfisch@users.sourceforge.net>
- Initial RPM release
