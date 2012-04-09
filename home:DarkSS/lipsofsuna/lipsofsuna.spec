%define Werror_cflags %nil
%define	Summary	Lips of Suna is a tongue-in-cheek dungeon crawl game

Summary:	%{Summary}
Name:		lipsofsuna
Version:	0.5.0
Release:	%mkrel 1
Source0:	http://sourceforge.net/projects/%{name}/files/%name}/%{version}/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/lipsofsuna/
Group:		Games/Arcade
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automake SDL-devel desktop-file-utils ImageMagick sqlite3-devel bullet-devel
BuildRequires:	SDL_mixer-devel	GL-devel SDL_ttf-devel glew-devel openal-devel libflac-devel libvorbis-devel enet-devel 
BuildRequires:	lua-devel inotify-tools-devel 

%description
Lips of Suna is a tongue-in-cheek dungeon crawl game that takes place in the chaotic dungeons of Suna. 
The five intelligent races of the world descend to the dungeons with their goal to save the world from a conclusive disaster.

In your journey to the depths of the dungeons, you will, among other things, have to fight creatures of different varieties, 
solve quests, explore new places, and craft custom items. Luckily you don't need to do all this alone since you can crawl the dungeons with your friends.

%prep 
%setup -q

%build
./waf configure --prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--bindir=%{_bindir} \
		--relpath=false \
		--optimize=true

%install
rm -rf %{buildroot}
./waf install --destdir=$RPM_BUILD_ROOT

cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Lips of Suna
Comment=%{Summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF


%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps


%changelog
* Wed Oct 26 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.5.0-1mdv2012.0
+ Revision: 707405
- lua and initify requirement fix
- oops dot in summary fix
- updated to upstream version rpmlint spec fixes

  + Zombie Ryushu <ryushu@mandriva.org>
    - imported package lipsofsuna

