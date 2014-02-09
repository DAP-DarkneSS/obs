#
# spec file for package sdl-ball
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright Vincent Petry <PVince81@yahoo.fr>
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


Name:           sdl-ball
Version:        1.01
Release:        0
Summary:        A Free/OpenSource brick-breaking game with pretty graphics
License:        GPL-3.0
Group:          Amusements/Games/Action/Breakout
Url:            http://sdl-ball.sourceforge.net/
# The source tarball from Sourceforge contains already compiled sources
# So to prepare the final source a "make clean" and "rm *.bin" is necessary.
# The following bug report addresses this issue:
# https://sourceforge.net/tracker/?func=detail&aid=2538468&group_id=225210&atid=1064137
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
# PATCH-FIX-UPSTREAM sdl-ball-makefile.patch https://sourceforge.net/tracker/?func=detail&aid=2787306&group_id=225210&atid=1064139 PVince81@yahoo.fr
Patch0:         %{name}-makefile.patch
# PATCH-FIX-UPSTREAM sdl-ball-dontstrip.patch
Patch1:         %{name}-dontstrip.patch
# PATCH-FIX-UPSTREAM sdl-ball-gcc47.patch
Patch2:         %{name}-gcc47.patch
BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_ttf-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif

%description
SDL-Ball is a Free/OpenSource brick-breaking game with pretty graphics. It is written in C++ using SDL and OpenGL.
Features:
* 50 levels.
* OpenGL eye candy. (Nice graphics, really)
* Lots of powerups and powerdowns.
* Powerup Shop - You get special coins for collecting powerups, you can spend them on more powerups.
* Highscores.
* Sound.
* Easy to use level editor.
* Themes - Selectable from options menu. Themes support loading new gfx,snd and levels. A theme can be partial, if a file is missing, it will be loaded from the default theme. You can even mix between gfx,snd and level themes!
* Controllable with Mouse/Keyboard/Joystick and WiiMote.
* Save and Load games
* Cool Introscreen
* Screenshot function

%prep
%setup -q -n %{name}
%patch0
%patch1 -p1
%patch2 -p1

%build
# The source tarball from Sourceforge contains already compiled sources
# So to prepare the final source a "make clean" and "rm *.bin" is necessary.
# The following bug report addresses this issue:
# https://sourceforge.net/tracker/?func=detail&aid=2538468&group_id=225210&atid=1064137
make clean
rm *.bin
export CFLAGS="%{optflags}"
make %{?_smp_mflags} PREFIX=%{_prefix} BINDIR=%{_bindir} DATADIR=%{_datadir}/%{name}/

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} BINDIR=%{_bindir} DATADIR=%{_datadir}/%{name}/ install
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%if 0%{?suse_version}
%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}
%endif

%files
%defattr(-,root,root,-)
%doc README LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
