#
# spec file for package boswars
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Version:        2.7
Release:        0
Summary:        Bos Wars
License:        GPL-2.0+
Group:          Amusements/Games/Strategy/Real Time
Source:         %{name}-%{version}-src.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        %{name}.png
Source100:      %{name}-rpmlintrc
Provides:       bos = %{version}
Obsoletes:      bos < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Bos Wars is a futuristic real-time strategy game. It is possible to
play against human opponents over LAN, internet, or against the
computer.



Authors:
--------
    Tina Petersen Jensen
    Francois Beerten

%prep
%setup -q -n %{name}-%{version}-src
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

%files
%defattr(-,root,root)
%doc CHANGELOG COPYRIGHT.txt LICENSE.txt README.txt doc/
%{_bindir}/%{name}
%{_bindir}/%{name}.bin
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%attr(775, -, users) %{_datadir}/%{name}/maps

%changelog
