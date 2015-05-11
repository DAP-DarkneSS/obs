#
# spec file for package opencity
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           opencity
Version:        0.0.6.5
Release:        0
Summary:        3D City Simulation
License:        GPL-2.0+
Group:          Amusements/Games/3D/Simulation
Url:            http://www.opencity.info/
Source:         %{name}-%{version}stable.tar.bz2
Source1:        texture.png
# PATCH-FIX-OPENSUSE vs. error: ISO C++ forbids casting between
# pointer-to-function and pointer-to-object [-Werror=pedantic]
# https://sourceforge.net/p/opencity/bugs/50
Patch2:         opencity-no-pedantic-errors.patch
BuildRequires:  Mesa-devel
BuildRequires:  SDL
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_ttf
# NOTE: autoconf/automake/libtool/m4 because of patch2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OpenCity is a full 3D city simulator game project.
It is written in standard C++ with OpenGL and SDL
from scratch. It is not intended to be a clone of
any famous city simulator from Max*s. So, if you
are looking to download a free SimCity 4 like,
please forget OpenCity.

%prep
%setup -q -n %{name}-%{version}stable
cp %{S:1} graphism/electricity/nuclear/texture.png
%patch2 -p1
sed -i 's/\r//' docs/README_it.txt docs/FAQ_it.txt docs/INSTALL_it.txt

%build
# NOTE: `autoreconf` because of patch2
autoreconf -fvi
export CFLAGS="%{optflags} -fstack-protector"
export CXXFLAGS="%{optflags} -fstack-protector"
%configure
make %{?_smp_mflags}

%install
%makeinstall
#make DESTDIR=%{buildroot} install
#install -D -m 0644 OpenCity.desktop %{buildroot}%{_datadir}/applications/OpenCity.desktop
#install -D -m 0644 OpenCity.png %{buildroot}%{_datadir}/pixmaps/OpenCity.png
# W: install-file-in-docs
rm %{buildroot}/%{_datadir}/doc/opencity/INSTALL
%suse_update_desktop_file -i opencity
%fdupes %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/opencity.desktop
%{_datadir}/pixmaps/opencity.png
%{_datadir}/%{name}
%{_mandir}/man?/%{name}*
%config %{_sysconfdir}/%{name}
%{_datadir}/doc/%{name}

%changelog
