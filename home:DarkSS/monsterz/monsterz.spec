Name:    monsterz
Version: 0.7.1
Release: %mkrel 9
# in reality, this is the DWYF license..
License: WTFPL
Group:   Games/Puzzles
Summary: A little addictive puzzle game
Source:  http://sam.zoy.org/projects/monsterz/%{name}-%{version}.tar.bz2
#gw Debian man page
Source1:    monsterz.1
Patch:      monsterz-fix-crash-x86_64.patch
#gw from Debian, fix crash on start (bug #49431)
Patch1:     020_fix_blit_crash.diff
Url:        http://sam.zoy.org/projects/monsterz

Requires:   pygame
BuildArch:  noarch
BuildRequires: imagemagick

%description
Monsterz is a little puzzle game, similar to the famous Bejeweled or Zookeeper.

The goal of the game is to create rows of similar monsters, either horizontally
or vertically. The only allowed move is the swap of two adjacent monsters, on
the condition that it creates a row of three or more. When alignments are
cleared, pieces fall from the top of the screen to fill the board again. Chain
reactions earn you even more points.

This game is mostly about luck, but it remains highly addictive. You have been
warned.

%prep
%setup -q
%patch -p0
%patch1 -p1

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_gamesdatadir}/%{name}
cp -R monsterz.py graphics/ sound/ $RPM_BUILD_ROOT/%{_gamesdatadir}/%{name}

mkdir -p $RPM_BUILD_ROOT/%{_gamesbindir}/

cat > $RPM_BUILD_ROOT/%{_gamesbindir}/%{name} <<EOF
#!/bin/bash
exec python %{_gamesdatadir}/%{name}/monsterz.py
EOF

chmod 755 $RPM_BUILD_ROOT/%{_gamesbindir}/%{name}


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Monsterz
Comment=Addictive puzzle game
Exec=%_gamesbindir/%{name}
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;BlocksGame;
EOF

mkdir -p $RPM_BUILD_ROOT{%{_miconsdir},%{_iconsdir},%{_liconsdir}}/
convert -geometry 16x16 graphics/icon.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert -geometry 32x32 graphics/icon.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -geometry 48x48 graphics/icon.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

install -D %SOURCE1 %buildroot%_mandir/man6/%name.6


%files
%doc AUTHORS COPYING INSTALL README TODO
%{_gamesdatadir}/%{name}/
%{_gamesbindir}/%{name}
%_mandir/man6/%name.6*
%_datadir/applications/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Fri Oct 18 2013 umeabot <umeabot> 0.7.1-9.mga4
+ Revision: 508009
- Mageia 4 Mass Rebuild

* Sat Jan 12 2013 umeabot <umeabot> 0.7.1-8.mga3
+ Revision: 360270
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Mar 04 2012 malo <malo> 0.7.1-7.mga2
+ Revision: 217798
- spec clean-up after import from Mandriva.
- imported package monsterz


* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-7mdv2011.0
+ Revision: 620392
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-6mdv2010.0
+ Revision: 440091
- rebuild

* Thu Apr 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.1-5mdv2009.1
+ Revision: 363488
- fix crash on start (bug #49431)
- add man page
- update menu category

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jul 30 2008 Michael Scherer <misc@mandriva.org> 0.7.1-4mdv2009.0
+ Revision: 254949
- fix bug #40989, patch from upstream

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.7.1-3mdv2009.0
+ Revision: 252763
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 04 2008 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.7.1-1mdv2008.1
+ Revision: 144997
- New release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Michael Scherer <misc@mandriva.org> 0.7.0-2mdv2008.0
+ Revision: 81703
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Mon Jul 31 2006 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2007.0
- xdg menu
- New release 0.7.0

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdk
- drop patch
- New release 0.6.1

* Mon Sep 12 2005 Michael Scherer <misc@mandriva.org> 0.6.0-4mdk
- directly call the python script without cd, fix lack of music

* Mon Sep 12 2005 Michael Scherer <misc@mandriva.org> 0.6.0-3mdk
- patch0 to fix #18471, unlock surface when calling blit()
- mkrel

* Wed Apr 27 2005 Götz Waschk <waschk@mandriva.org> 0.6.0-2mdk
- fix the license

* Wed Apr 06 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.6.0-1mdk
- New release 0.6.0

* Fri Apr 01 2005 Götz Waschk <waschk@linux-mandrake.com> 0.5.0-3mdk
- add missing binary

* Thu Mar 31 2005 Götz Waschk <waschk@linux-mandrake.com> 0.5.0-2mdk
- fix buildrequires

* Thu Mar 31 2005 Michael Scherer <misc@mandrake.org> 0.5.0-1mdk
- New release 0.5.0

* Mon Mar 21 2005 Michael Scherer <misc@mandrake.org> 0.4.1-1mdk
- First Mandrakelinux package

