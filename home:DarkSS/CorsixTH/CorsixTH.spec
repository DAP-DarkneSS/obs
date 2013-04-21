#
# spec file for package CorsixTH
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


Name:           CorsixTH
Version:        0.20
Release:        0
Url:            http://code.google.com/p/corsix-th/
Summary:        Theme Hospital clone
License:        MIT
Group:          Amusements/Games/Strategy/Other
Source:         http://corsix-th.googlecode.com/files/CorsixTH-%{version}-Source.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libffmpeg-devel
%if 0%{?suse_version} > 1210
BuildRequires:  lua51-devel
%else
BuildRequires:  lua-devel
%endif
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
Recommends:     timidity

%description
This project aims to reimplement the game engine of Theme Hospital, and be
able to load the original game data files. This means that you will need a
purchased copy of Theme Hospital, or a copy of the demo, in order to use
CorsixTH. After most of the original engine has been reimplemented in open
source code, the project will serve as a base from which extensions and
improvements to the original game can be made.

%prep
%setup -q -n CorsixTH-%{version}-Source/CorsixTH
dos2unix changelog.txt
dos2unix LICENSE.txt
dos2unix README.txt
chmod -x ./{LICENSE,README}.txt

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export FFLAGS="%{optflags}"
cd ..
cmake . -DCMAKE_INSTALL_PREFIX=%{_libdir}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}/Data
make DESTDIR=%{buildroot} install
# create wrapper
cat <<EOF >%{buildroot}%{_bindir}/%{name}
#!/bin/sh
cd %{_libdir}/%{name}
./%{name}
cd -
EOF
chmod +x %{buildroot}%{_bindir}/%{name}
# install icons and desktop file
mkdir %{buildroot}%{_datadir}
mkdir %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_libdir}/CorsixTH/CorsixTH.ico %{buildroot}%{_datadir}/pixmaps
install -p -m 644 Original_Logo.svg %{buildroot}%{_datadir}/pixmaps/CorsixTH.svg
%suse_update_desktop_file -c CorsixTH CorsixTH "A Theme Hospital Clone" CorsixTH CorsixTH Game Simulation
%fdupes

%files
%defattr(-,root,root)
%doc ./LICENSE.txt ./README.txt
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
