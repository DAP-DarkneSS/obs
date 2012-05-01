Name:		speed-dreams
Version:	2.0.0
Release:	%mkrel 1
Summary:	Speed Dreams 2.0 a racing cars game
License:	GPLv2
Group:		Games/Arcade
URL:		http://speed-dreams.sourceforge.net/
Source0:	%{name}-src-base-2.0.0-r4687.tar.xz
BuildRequires:	cmake
BuildRequires:	ImageMagick 
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(freealut)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	png-devel 
BuildRequires:	enet-devel
BuildRequires:	mesa-common-devel 
BuildRequires:	plib-devel 
BuildRequires:	freeglut-devel
BuildRequires:	libxi-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxrandr-devel
BuildRequires:	jpeg-devel
Requires:	libSDL >= 1.2.13
Requires:	openal
Requires:	mesa
Requires:	%{name}-data-base = %{version}

%description
A fork of the open racing car simulator Torcs, 
aiming to implement exciting new features, cars, tracks and 
AI opponents to make a more enjoyable game for the player, 
as well as constantly improving visual and physics realism.

%package	robots-hq
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Requires:	%{name}-data-hq >= %{version}
Summary:	Basic robots for %{name}

%description	robots-hq
HQ robots for LS1 and 36GP series cars in %{name}

%package	robots-more-hq
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Requires:	%{name}-robots-hq >= %{version}
Requires:	%{name}-data-more-hq
Summary:	More hq robots for %{name}

%description	robots-more-hq
more HQ robots for TRB1 series cars and add kilo2008 robot in %{name}

%package	robots-wip
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Requires:	%{name}-robots-more-hq >= %{version}
Requires:	%{name}-data-wip
Summary:	Wip robots for %{name}

%description	robots-wip
wip robots for LS2, MP5 and RS series cars in %{name}

%package	devel
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Summary:	Development file for %{name}

%description	devel
includes files for development robots for %{name}

%prep
%setup -n %{name}-2 -q

%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF -DBUILD_SHARED_LIBS:BOOL=OFF -DOPTION_TRACE:BOOL=OFF
%make 

%install
rm -rf %{buildroot}

cd build
%makeinstall_std

rm  -rf %{buildroot}/usr/share/games/%{name}-2/cmake
rm  -rf %{buildroot}/usr/share/games/%{name}-2/data
rm  -rf %{buildroot}/usr/share/games/%{name}-2/config
rm  -rf %{buildroot}/usr/share/games/%{name}-2/drivers
rm  -rf %{buildroot}/usr/share/games/%{name}-2/*.txt
rm  -rf %{buildroot}/%{_libdir}/games/%{name}-2/drivers/networkhuman
rm  -rf %{buildroot}/%{_libdir}/games/%{name}-2/drivers/simplix_mpa1

mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mageia-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}-2
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

%{__install} -d $RPM_BUILD_ROOT{%{_miconsdir},%{_liconsdir}}
convert -size 16x16 ../data/data/icons/icon.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} ../data/data/icons/icon.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -size 48x48 ../data/data/icons/icon.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_mandir}/man6
install -m644 ../doc/man/sd2-accc.6 %{buildroot}%{_mandir}/man6/sd2-accc.6
install -m644 ../doc/man/sd2-nfs2ac.6 %{buildroot}%{_mandir}/man6/sd2-nfs2ac.6
install -m644 ../doc/man/sd2-nfsperf.6 %{buildroot}%{_mandir}/man6/sd2-nfsperf.6
install -m644 ../doc/man/sd2-trackgen.6 %{buildroot}%{_mandir}/man6/sd2-trackgen.6
install -m644 ../doc/man/speed-dreams-2.6 %{buildroot}%{_mandir}/man6/speed-dreams-2.6

%files
%doc CHANGES.txt COPYING.txt INSTALL.txt README.txt TODO.txt
%{_mandir}/man6/*
%attr(755,root,root) %{_gamesbindir}/*
%{_gamesdatadir}/%{name}-2/*
%{_datadir}/applications/mageia-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_libdir}/games/%{name}-2/drivers/human/human.so*
%{_libdir}/games/%{name}-2/drivers/usr_sc/usr_sc.so*
%{_libdir}/games/%{name}-2/drivers/simplix_sc/simplix_sc.so*
%{_libdir}/games/%{name}-2/lib/liblearning.so*
%{_libdir}/games/%{name}-2/lib/libnetworking.so*
%{_libdir}/games/%{name}-2/lib/libraceengine.so*
%{_libdir}/games/%{name}-2/lib/librobottools.so*
%{_libdir}/games/%{name}-2/lib/libtgf.so*
%{_libdir}/games/%{name}-2/lib/libtgfclient.so*
%{_libdir}/games/%{name}-2/lib/libtgfdata.so*
%{_libdir}/games/%{name}-2/lib/libtxml.so*
%{_libdir}/games/%{name}-2/modules/graphic/ssggraph.so*
%{_libdir}/games/%{name}-2/modules/simu/simuv2.1.so*
%{_libdir}/games/%{name}-2/modules/simu/simuv2.so*
%{_libdir}/games/%{name}-2/modules/simu/simuv3.so*
%{_libdir}/games/%{name}-2/modules/telemetry/telemetry.so*
%{_libdir}/games/%{name}-2/modules/track/track.so*
%{_libdir}/games/%{name}-2/modules/userinterface/legacymenu.so*
%{_libdir}/games/%{name}-2/modules/userinterface/textonly.so*

%files robots-hq
%{_libdir}/games/%{name}-2/drivers/simplix_ls1/simplix_ls1.so*
%{_libdir}/games/%{name}-2/drivers/simplix_36GP/simplix_36GP.so*
%{_libdir}/games/%{name}-2/drivers/usr_ls1/usr_ls1.so*
%{_libdir}/games/%{name}-2/drivers/usr_36GP/usr_36GP.so*


%files robots-more-hq
%{_libdir}/games/%{name}-2/drivers/simplix_trb1/simplix_trb1.so*
%{_libdir}/games/%{name}-2/drivers/usr_trb1/usr_trb1.so*
%{_libdir}/games/%{name}-2/drivers/simplix/simplix.so*
%{_libdir}/games/%{name}-2/drivers/usr/usr.so*
%{_libdir}/games/%{name}-2/drivers/kilo2008/kilo2008.so*

%files robots-wip
%{_libdir}/games/%{name}-2/drivers/simplix_mp5/simplix_mp5.so*
%{_libdir}/games/%{name}-2/drivers/simplix_ls2/simplix_ls2.so*
%{_libdir}/games/%{name}-2/drivers/usr_ls2/usr_ls2.so*
%{_libdir}/games/%{name}-2/drivers/usr_rs/usr_rs.so*

%files devel
%{_includedir}/%{name}-2/3D/*.h
%{_includedir}/%{name}-2/SOLID/solid.h
%{_includedir}/%{name}-2/learning/*.h
%{_includedir}/%{name}-2/tmath/*.h
%{_includedir}/%{name}-2/*.*



%changelog

* Mon Apr 09 2012 shadow95 <shadow95> 2.0.0-1.mga2
+ Revision: 229842
- update to Release
- Update to RC2

* Wed Apr 04 2012 luigiwalser <luigiwalser> 2.0.0-0.1.rc1_r4527.2.mga2
+ Revision: 228372
- rebuild for plib

* Tue Feb 28 2012 shadow95 <shadow95> 2.0.0-0.1.rc1_r4527.1.mga2
+ Revision: 215921
- rename in lowercase
- remove provides ...
- changes some BR in pkconfig
- remove %%attr
- fix Requires: libSDL
- fix BuildRequires: libSDL-devel
- update more descriptions
- clean spec
- Update to RC1
- Fix txml license
- Update fsf adress
- fix bug with libsolid
- remove option trace
- update to svn 4414 (RC1 version)
- replace mandriva by mageia in desktop file
- imported package speed-dreams

