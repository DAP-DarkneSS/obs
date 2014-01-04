Name:		jools
Summary:	Graphical puzzle game
Version: 0.20
Release: %mkrel 11
Url:		http://www.eecs.umich.edu/~pelzlpj/jools/
Source0:	%{name}-%{version}.tar.bz2
Patch0:	%{name}-%{version}-sys.patch
Patch1:	%{name}-%{version}-sharegames.patch
Source11:	%{name}-48.png
Source12:	%{name}-32.png
Source13:	%{name}-16.png
Group:		Games/Puzzles
License:	GPLv2+
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  python-devel
Requires:	pygame
BuildArch:      noarch

%description
Jools is a graphical puzzle game in the tradition of Tetris.
In a nutshell, the goal is to swap adjacent jools (jewels) within a grid,
in order to create rows of three or more of a kind.
These jools will then disappear, and more will fall to fill their places.
Jools features nifty 3D rendered graphics.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
find $RPM_BUILD_ROOT%{_gamesdatadir}/%{name} -name '.arch-ids' -o -name '.placeholder' | xargs rm -rf

install -d -m 755 $RPM_BUILD_ROOT%{_gamesbindir}
mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_gamesbindir}
rmdir $RPM_BUILD_ROOT%{_bindir}

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Jools
Comment=Graphical puzzle game
Exec=%{_gamesbindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;LogicGame;X-MandrivaLinux-MoreApplications-Games-Puzzles;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root,755)
%doc COPYING ChangeLog README doc/manual.html doc/manual.tex doc/detonate.txt doc/POINTS doc/TODO
%{_gamesbindir}/%{name}
%{py_puresitedir}/%{name}*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Fri Nov 12 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.20-11mdv2011.0
+ Revision: 597012
- rebuild for python 2.7

* Sat May 16 2009 Samuel Verschelde <stormi@mandriva.org> 0.20-10mdv2010.0
+ Revision: 376445
- fix desktop file
- fix license
- add icons

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.20-9mdv2009.1
+ Revision: 325672
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.20-8mdv2009.0
+ Revision: 247418
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.20-6mdv2008.1
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Aug 13 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.20-6mdv2008.0
+ Revision: 62665
- use the new menu system
- added missing docs to the package
- exploded patches
- moved path fixes to separated patches, and
- apply them properly
- imported jools, from 2007.0


* Mon Apr 24 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.20-5mdk
- Add BuildRequires
- use mkrel

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.20-4mdk
- Rebuild for new python

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 0.20-3mdk 
- correct menu
- use a macro for python version
- use noarch

* Tue May  4 2004 Olivier Blin <blino@mandrake.org> 0.20-2mdk
- modify setup.py to install directly in share/games
- use --root option of setup.py instead of some dark power
  (GProg poutre more than AEI)

* Mon May  3 2004 Olivier Blin <blino@mandrake.org> 0.20-1mdk
- initial release

