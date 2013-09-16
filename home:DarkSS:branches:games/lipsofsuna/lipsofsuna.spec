#
# spec file for package lipsofsuna
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Version:        0.7.0
Release:        0
Summary:        Lips of Suna: binary files
License:        LGPL-3.0
Group:          Amusements/Games/3D/Other
Url:            http://lipsofsuna.org/
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz

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
BuildRequires:  freeimage-devel
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
BuildRequires:  libvorbis-devel
%if 0%{?suse_version} >= 1220
BuildRequires:  lua51-devel
%else
BuildRequires:  lua-devel
%endif
BuildRequires:  openal-soft-devel
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(zlib)
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

%build
./waf configure --prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--bindir=%{_bindir} \
		--disable-relpath \
		--enable-optimization

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
