#
# spec file for package miniracer
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


%define pack_desc  MiniRacer is an OpenGL car racing game, based \
on the Quake1 engine. It was written by Thomas Jakobsson for the \
win32 platform and ported to Linux by Martin Weiss. Enjoy!

Name:           miniracer
Version:        1.04
Release:        1
License:        GPL-2.0+
Summary:        An OpenGL car racing game
Url:            http://miniracer.sourceforge.net
Group:          Amusements/Games/3D/Race
Source0:        https://downloads.sourceforge.net/project/miniracer/miniracer/miniracer-%{version}/miniracer-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  i586 i686 x86_64

BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(glu)
Requires:       %{name}-data = %{version}

%description
%{pack_desc}

%package        data
Summary:        MiniRacer: art and other architecture independent data
Group:          Amusements/Games/3D/Race

Requires:       %{name} = %{version}
BuildArch:      noarch

%description    data
%{pack_desc}

%prep
%setup -q

# A hint from https://aur.archlinux.org/packages/mi/miniracer/PKGBUILD
%ifarch x86_64
sed -i 's|ecx|rcx|g' misc/mathlib.c
sed -i 's|eax|rax|g' misc/mathlib.c
%endif

%build
make %{?_smp_mflags} VERBOSE=1 CFLAGS="%{optflags}"

%install
%makeinstall
%suse_update_desktop_file -c %{name} "MiniRacer" "An OpenGL car racing game" "%{name}" "" "Game;3DGame;ArcadeGame;"

# Don't package binary file in datadir.
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}/%{_datadir}/games/MiniRacer/engine.glx %{buildroot}%{_libdir}/%{name}
ln -s %{_libdir}/%{name}/engine.glx %{buildroot}/%{_datadir}/games/MiniRacer/engine.glx

%files
%defattr(-,root,root)
%doc ChangeLog COPYING CREDITS README TODO
%{_libdir}/%{name}

%files data
%defattr(-,root,root)
%{_datadir}/games/MiniRacer
%{_bindir}/%{name}
%{_mandir}/man*/%{name}*
%{_datadir}/applications/%{name}.desktop

%changelog
