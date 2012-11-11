#
# spec file for package lipsofsuna
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2007-2012 Ari Mustonen aka amuzen & Ketchetwah South
# aka shatikar (source [LGPLv3] and data [CC BY-SA 3.0])
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           lipsofsuna
Version:        0.6.0
Release:        0
License:        LGPL-3.0
Summary:        Lips of Suna: binary files
Url:            http://lipsofsuna.org/
Group:          Amusements/Games/3D/Other
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM lipsofsuna-lua52.patch
Patch0:         %{name}-lua52-new.patch
BuildRequires:  ImageMagick
%if 0%{?suse_version} > 1210
BuildRequires:  libGLw-devel
%endif
%if 0%{?suse_version} <= 1210
BuildRequires:  MesaGLw-devel
%endif
BuildRequires:  automake
BuildRequires:  curl
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glibc-devel
BuildRequires:  libOIS-devel
BuildRequires:  libOgreMain-devel
BuildRequires:  libOgreTerrain-devel
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_ttf-devel
BuildRequires:  libbullet-devel
BuildRequires:  libcurl-devel
BuildRequires:  libenet-devel
BuildRequires:  libinotifytools-devel
BuildRequires:  libpng14-devel
BuildRequires:  libvorbis-devel
%if 0%{?suse_version} >= 1220
BuildRequires:  lua51-devel
%else
BuildRequires:  lua-devel
%endif
BuildRequires:  openal-soft-devel
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
Requires:       %{name}-data = %{version}
Requires:       libOgreMain-plugins

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
%patch0

%build
./waf configure --prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--bindir=%{_bindir} \
		--relpath=false \
		--optimize=true

%install
./waf install --destdir=%{buildroot}
%suse_update_desktop_file %{name}

%fdupes %{buildroot}

%files
%defattr (-,root,root)
%doc COPYING README NEWS AUTHORS
%{_bindir}/%{name}*

%files data
%defattr(-,root,root)
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*

%changelog
