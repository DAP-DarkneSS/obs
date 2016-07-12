#
# spec file for package boswars
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define pack_desc Bos Wars is a futuristic real time strategy game (RTS). \
In a RTS game, the player has to combat his enemies while developing his \
war economy. Everything runs in real-time, as opposed to turn-based games \
where the player always has to wait for his turn. The trick is to balance \
the effort put into building his economy and building an army to defend \
and attack the enemies. \
 \
Bos Wars has a dynamic rate based economy. Energy is produced by power \
plants and magma gets pumped from hot spots. Buildings and mobile units \
are also built at a continuous rate. Control of larger parts of the map \
creates the potential to increase your economy throughput. Holding key \
points like roads and passages allow for different strategies. \
 \
It is possible to play against human opponents over LAN, internet, or \
against the computer. \
 \
Bos Wars aims to create a completely original and fun open source RTS game.

Name:           boswars
BuildRequires:  SDL-devel
BuildRequires:  fdupes
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  libmikmod-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
%if %suse_version > 1210
BuildRequires:  lua51-devel
%else
BuildRequires:  lua-devel
%endif
BuildRequires:  scons
BuildRequires:  update-desktop-files
Url:            http://www.boswars.org/
Version:        2.7+svn10242
Release:        0
Summary:        Bos Wars
License:        GPL-2.0+
Group:          Amusements/Games/Strategy/Real Time
# svn co svn://bos.seul.org/svn/bos/bos/trunk boswars
# tar cfz boswars.tar.gz boswars --exclude-vcs
Source:         %{name}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        %{name}.png
Source6:        %{name}.rpmlintrc
Source9:        %{name}.6
%if %suse_version >= 1310
Requires:       %{name}-data = %{version}
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%endif

%description
%{pack_desc}

%if %suse_version >= 1310
%package data
Summary:        Bos Wars: art and other architecture independent data
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%{pack_desc}
%endif

%prep
%setup -q -n %{name}
%__chmod 644 doc/scripts/findlua.py doc/scripts/makeindex.py doc/scripts/showindex.py
# script-without-shebang (has executable bits set)
find ./ -type f -exec %{__chmod} 0644 {} \;

%build
# has no idea of -l (which may be in %%_smp_mflags)
#scons %%{?jobs:-j%%jobs}
python make.py

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/languages
cp -r campaigns graphics intro maps patches scripts sounds units $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r languages/*po $RPM_BUILD_ROOT%{_datadir}/%{name}/languages
install -D -m 755 fbuild/release/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}.bin
install -D -m 755 $RPM_SOURCE_DIR/%{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 644 $RPM_SOURCE_DIR/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -i %{name} Game StrategyGame
%fdupes %{buildroot}/%{_datadir}/boswars/units 
%fdupes %{buildroot}/%{_datadir}/boswars/campaigns 
# Install man page
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man6
cp %{SOURCE9} $RPM_BUILD_ROOT/%{_mandir}/man6
cp %{SOURCE9} $RPM_BUILD_ROOT/%{_mandir}/man6/%{name}.bin.6

%if %suse_version >= 1310
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%doc CHANGELOG COPYRIGHT.txt LICENSE.txt README.txt doc/
%{_bindir}/%{name}
%{_bindir}/%{name}.bin
%{_mandir}/man?/%{name}*.6.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%if %suse_version >= 1310
%files data
%defattr(-,root,root)
%endif
%{_datadir}/%{name}
%if %suse_version >= 1310
# A very ugly workaround for maps editor
%attr(775, -, users) %{_datadir}/%{name}/maps
%attr(664, -, users) %{_datadir}/%{name}/maps/*/*.sm*
%attr(664, -, users) %{_datadir}/%{name}/maps/*/*.lua
%attr(664, -, users) %{_datadir}/%{name}/maps/*/*/*.sm*
%attr(664, -, users) %{_datadir}/%{name}/maps/*/*/*/*.sm*
%endif

%changelog
