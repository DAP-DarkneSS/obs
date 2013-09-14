#
# spec file for package racer
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


%define pack_desc  A computer game with racing cars. The game is in 2D. \
Offeres several tracks and different cars. Also career is available.

Name:           racer
Version:        1.1
Release:        0
License:        GPL-3.0
Summary:        A cars racing game
Url:            http://hippo.nipax.cz
Group:          Amusements/Games/Other
Source0:        http://hippo.nipax.cz/src/racer-%{version}.tar.gz
# PATCH-FIX-OPENSUSE to prevent "mkdir was not declared in this scope".
Patch0:         racer-gcc-include.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  fdupes
BuildRequires:  gcc-c++
# If liballegro-devel, /bin/sh: allegro-config: command not found.
BuildRequires:  liballeg-devel
BuildRequires:  libjpeg-devel
Requires:       %{name}-data = %{version}

%description
%{pack_desc}

%package        data
Summary:        Racer: art and other architecture independent data
Group:          Amusements/Games/Other

Requires:       %{name} = %{version}
BuildArch:      noarch

%description    data
%{pack_desc}

%prep
%setup -q
make clean
%patch0

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make DESTDIR=%{buildroot}/%{_prefix} install
%fdupes -s %{buildroot}%{_datadir}/%{name}/gfx

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{name}

%files data
%defattr(-,root,root)
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man*/%{name}*
%{_datadir}/%{name}
%{_datadir}/pixmaps/racer.xpm

%changelog
