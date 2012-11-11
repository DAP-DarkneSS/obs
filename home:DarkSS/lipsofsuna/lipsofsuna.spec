#
# spec file for package lipsofsuna-ogre
#
# Copyright (c) 2007-2012 Ari Mustonen aka amuzen & Ketchetwah South
# aka shatikar (source [LGPLv3] and data [CC BY-SA 3.0])
#

%define truename lipsofsuna

Summary:        Lips of Suna (Ogre): binary files
Name:           lipsofsuna-ogre
Version:        git.1336940445
Release:        1
Source0:        %{name}-%{version}.tar.bz2
URL:            http://lipsofsuna.org/
Group:          Amusements/Games/3D/Other
License:        LGPLv3

BuildRequires:  automake desktop-file-utils ImageMagick sqlite3-devel
BuildRequires:  libSDL-devel libSDL_mixer-devel libSDL_ttf-devel glew-devel
BuildRequires:  openal-soft-devel flac-devel libvorbis-devel libenet-devel
BuildRequires:  lua-devel libinotifytools-devel libbullet-devel MesaGLw-devel
BuildRequires:  libcurl-devel curl glibc-devel gcc-c++ python
BuildRequires:  libOIS-devel libOgreMain-devel libOgreTerrain-devel libpng-devel
BuildRequires:  update-desktop-files fdupes
Requires:       python libOgreMain1_7_4-plugins
Requires:       %{name}-data = %{version}

Conflicts:      %{truename}

%description
Lips of Suna (Ogre): binary files.

Lips of Suna is a tongue-in-cheek dungeon crawl game that takes place in the
chaotic dungeons of Suna. The five intelligent races of the world descend to
the dungeons with their goal to save the world from a conclusive disaster.

In your journey to the depths of the dungeons, you will, among other things,
have to fight creatures of different varieties, solve quests, explore new
places, and craft custom items. Luckily you don't need to do all this alone
since you can crawl the dungeons with your friends.

%package data
Summary:        Lips of Suna (Ogre): architecture independent data
License:        CC-BY-SA 3.0
Group:          Amusements/Games/3D/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

Conflicts:      %{truename}-data

%description data
Lips of Suna (Ogre): architecture independent data.

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
%suse_update_desktop_file %{truename}
%fdupes -s %{buildroot}%{_datadir}/%{truename}

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc COPYING README NEWS AUTHORS
%{_bindir}/%{truename}*

%files data
%defattr(-,root,root)
%dir %{_datadir}/%{truename}
%{_datadir}/%{truename}/*
%{_datadir}/applications/%{truename}.desktop
%{_datadir}/pixmaps/%{truename}*

%changelog
