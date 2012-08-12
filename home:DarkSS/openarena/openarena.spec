#
# spec file for package openarena
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           openarena
Version:        0.8.1
Release:        0
Summary:        Open Arena game engine
License:        GNU General Public License (GPL) - all versions
Group:          Amusements/Games/Action/Shoot
Url:            http://openarena.ws/
Source0:        http://openarena.ws/svn/source/081/%{name}-engine-%{version}-1.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.svg
Patch0:         strcpy-overlap-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  SDL-devel
BuildRequires:  openal-devel
%if 0%{?mandriva_version}
BuildRequires:  GL-devel
BuildRequires:  oggvorbis-devel
%else
BuildRequires:  Mesa-devel
BuildRequires:  libvorbis-devel
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
Requires:       openarena-data = %{version}
Requires:       openarena-doc = %{version}
%define gamelibdir	%{_libdir}/games/%{name}

%description
OpenArena is an open-source content package for Quake III Arena
licensed under the GPL, effectively creating a free stand-alone game.

Authors:
--------
Aardappel       - Maps (Converted with permission)
leileilol       - Leads, gfx, models, anim, sound and textures
Multiplex       - Models, textures
crayon          - Skins, models
JK Makowka      - Models, skins
Democritus      - Textures
jzero           - Models, textures, 2D
Mancubus        - The Announcer
mewse           - Engine compiling, tools, textures and testing
div0            - Engine compiling, fixing
dmn_clown       - Botfiles code
MilesTeg        - 2D art and textures
evillair        - Textures (nicked from Nexuiz)
Shadowdragon    - Models
mightypea       - Models
Morphed         - Skins
toddd           - Sound
DarkThief       - Skins
slyus           - Skins
SavageX         - Maps
Kaz             - Skins
pixie           - Voices (Kyonshi, Major)
Vondur          - Map (kaos)
Tyrann          - Map (Aggressor)
Ed              - Map (Conversion of ce1m7)

%prep
%setup -q -n %{name}-engine-%{version}
%patch0 -p1

%build
# START of configuration of building ----------------
export CFLAGS="$RPM_OPT_FLAGS" # C flags for compiler
export USE_OPENAL=1            # We want openAL
export USE_OPENAL_DLOPEN=1     # Next we want to bind openAL on runtime.
                               # SDL sound will be used if openAL is not installed
export USE_CODEC_VORBIS=1      # We want vorbis support
export BUILD_STANDALONE=1      # Open Arena is a standalone game
export DEFAULT_BASEDIR=%{_datadir}/games/openarena  # Where is directory with openarena-data
# END of configuration of building -----------------------------
make %{?_smp_mflags}

%install
make copyfiles COPYDIR=%{buildroot}/%{gamelibdir}  # Where will come compiled engine files

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{gamelibdir}

%ifarch %ix86
install -m 755 build/release-linux*/o*i386 $RPM_BUILD_ROOT/%{gamelibdir}
ln -sf %{gamelibdir}/openarena.i386 $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -sf %{gamelibdir}/oa_ded.i386 $RPM_BUILD_ROOT%{_bindir}/%{name}-ded

%else
%ifarch x86_64
install -m 755 build/release-linux*/o*x86_64 $RPM_BUILD_ROOT/%{gamelibdir}
ln -sf %{gamelibdir}/openarena.x86_64 $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -sf %{gamelibdir}/oa_ded.x86_64 $RPM_BUILD_ROOT%{_bindir}/%{name}-ded

%else
exit 1

%endif
%endif

# Icon, it is simple official icon
install -D -m 644 %{S:2} $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.svg

# Desktop entry
install -D -m 644 %{S:1} $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

# Magic and unnecessary lines but without them build is not successful
%if 0%{?suse_version}
%suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root)
%dir %{_libdir}/games
%dir %{gamelibdir}
%{gamelibdir}/oa_ded.*
%{gamelibdir}/openarena.*
%{gamelibdir}/*
%{_bindir}/openarena*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
