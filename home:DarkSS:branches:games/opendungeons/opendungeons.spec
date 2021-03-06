#
# spec file for package opendungeons
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           opendungeons
Version:        0.7.1
Release:        0
Summary:        RTS game in dark, damp and dangerous dungeons
License:        GPL-3.0+ and Zlib
Group:          Amusements/Games/Strategy/Real Time
Url:            http://opendungeons.github.io
Source0:        https://github.com/OpenDungeons/OpenDungeons/archive/%{version}/%{name}-%{version}.tar.gz

%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
%else
BuildRequires:  boost-devel >= 1.54
%endif
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(CEGUI-0)
BuildRequires:  pkgconfig(OGRE-Overlay) >= 1.9
BuildRequires:  pkgconfig(OGRE-RTShaderSystem) >= 1.9
BuildRequires:  pkgconfig(OIS)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sfml-audio)
BuildRequires:  pkgconfig(sfml-network)
BuildRequires:  pkgconfig(sfml-system)
Requires:       %{name}-data = %{version}
Requires:       libOgreMain1_9_0-plugins

%description
OpenDungeons is an open source, real time strategy game sharing game
elements with the Dungeon Keeper series and Evil Genius. Players build
an underground dungeon which is inhabited by creatures. Players fight
each other for control of the underground by indirectly commanding their
minions, directly casting spells in combat, and luring enemies
into sinister traps.

%package        data
Summary:        Data files for OpenDungeons
License:        GPL-2.0+ and CC-BY-SA-3.0 and MIT and OFL-1.1 and SUSE-Public-Domain
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    data
This package contains arch-independent data files for OpenDungeons.
It is meant to be used with the "opendungeons" binary package.

%prep
%setup -q -n OpenDungeons-%{version}

%build
# Gcc 4.8 & OBS.
tmpflags="%{optflags} -fPIC"
%if 0%{?suse_version} <= 1320
tmpflags="%{optflags} -fno-stack-protector"
%endif
%cmake \
       -Wno-dev \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_CXX_FLAGS="${tmpflags}" \
       -DOD_BIN_PATH=%{_bindir} \
       -DOD_DATA_PATH="%{_datadir}/%{name}"
make %{?_smp_mflags}

%install
%cmake_install

# Runtime error fix.
sed -i 's@PluginFolder=@PluginFolder=%{_libdir}/OGRE@g' \
        %{buildroot}/%{_sysconfdir}/%{name}/plugins.cfg

# W: desktopfile-without-binary
sed -i 's@%{_bindir}/%{name}@%{name}@g' %{buildroot}%{_datadir}/applications/%{name}.desktop

# Let's use %%doc macro.
rm -rf %{buildroot}/%{_datadir}/doc/opendungeons

chmod +x %{buildroot}/%{_datadir}/%{name}/scripts/unix/run_unit_tests.sh

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%defattr(-,root,root)
%doc README.md RELEASE-NOTES.md
%if 0%{?suse_version} > 1320
%license AUTHORS CREDITS LICENSE.md
%else
%doc AUTHORS CREDITS LICENSE.md
%dir %{_datadir}/appdata
%endif
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man6/%{name}.6*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/plugins.cfg

%files data
%defattr(-,root,root)
%{_datadir}/%{name}/

%changelog
