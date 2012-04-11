#
# spec file for package lipsofsuna
#
# Copyright (c) 2007-2012 Ari Mustonen aka amuzen & Ketchetwah South
# aka shatikar (source [LGPLv3] and data [CC BY-SA 3.0])
#

Summary:        Lips of Suna: binary files
Name:           lipsofsuna
Version:        0.5.0
Release:        0
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
URL:            http://lipsofsuna.org/
Group:          Amusements/Games/3D/Other
License:        LGPLv3

BuildRequires:  automake desktop-file-utils ImageMagick sqlite3-devel
BuildRequires:  libSDL-devel libSDL_mixer-devel libSDL_ttf-devel glew-devel
BuildRequires:  openal-soft-devel flac-devel libvorbis-devel libenet-devel
BuildRequires:  lua-devel libinotifytools-devel libbullet-devel MesaGLw-devel
BuildRequires:  libcurl-devel curl glibc-devel gcc-c++
BuildRequires:  update-desktop-files
Requires:       python
Requires:       %{name}-data = %{version}

%description
Lips of Suna: binary files.

Lips of Suna is a tongue-in-cheek dungeon crawl game that takes place in the
chaotic dungeons of Suna. The five intelligent races of the world descend to
the dungeons with their goal to save the world from a conclusive disaster.

In your journey to the depths of the dungeons, you will, among other things,
have to fight creatures of different varieties, solve quests, explore new
places, and craft custom items. Luckily you don't need to do all this alone
since you can crawl the dungeons with your friends.

%package data
Summary:        Lips of Suna: architecture independent data
License:        CC-BY-SA 3.0
Group:          Amusements/Games/3D/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Lips of Suna: architecture independent data.

Lips of Suna is a tongue-in-cheek dungeon crawl game that takes place in the
chaotic dungeons of Suna. The five intelligent races of the world descend to
the dungeons with their goal to save the world from a conclusive disaster.

In your journey to the depths of the dungeons, you will, among other things,
have to fight creatures of different varieties, solve quests, explore new
places, and craft custom items. Luckily you don't need to do all this alone
since you can crawl the dungeons with your friends.

%prep 
%setup -q

%build
./waf configure --prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--bindir=%{_bindir} \
		--relpath=false \
		--optimize=true

%install
./waf install --destdir=%{buildroot}
%suse_update_desktop_file %{name}

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc COPYING README NEWS AUTHORS
%{_bindir}/%{name}*

%files data
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*

%changelog
