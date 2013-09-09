#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           miniracer
Version:        1.04
Release:        1
Summary:        MiniRacer game
Url:            http://miniracer.sourceforge.net
Group:          games
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Copyright: GPL
Vendor:    Martin Weiss <plattfisch@epost.de>
Packager:  Martin Weiss <plattfisch@epost.de>

%description
 MiniRacer is an OpenGL car racing game, based on the Quake1 engine.
 It was written by Thomas Jakobsson for the win32 platform and ported
 to Linux by Martin Weiss. This Release can still contain bugs.
 See the website http://miniracer.sourceforge.net for details.
 Enjoy!

%prep
%setup -q

%build
make

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
make clean

%files
%defattr(-,root,root)
%attr(0755,-,-) %{_datadir}/games/MiniRacer/engine.glx
%attr(0644,-,-) %{_datadir}/games/MiniRacer/data/pak0.pak
%attr(0644,-,-) %{_datadir}/games/MiniRacer/data/config.cfg
%attr(0644,-,-) %{_datadir}/games/MiniRacer/data/maps/*.bsp
%attr(0644,-,-) %{_datadir}/games/MiniRacer/data/maps/maps1.lst
%attr(0755,-,-) %{_bindir}/miniracer
%attr(0644,-,-) %{_mandir}/man6/miniracer.6.gz



%changelog
