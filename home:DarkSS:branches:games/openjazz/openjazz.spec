#
# spec file for package openjazz
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


%define date 250713
Name:           openjazz
Version:        0.0.130725
Release:        0
Summary:        Remake of the classic Jazz Jackrabbit games
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://www.alister.eu/jazz/oj/
Source:         http://www.alister.eu/jazz/oj/OpenJazz-src-%{date}.zip
Patch0:         %{name}-files.patch
BuildRequires:  SDL-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libmodplug-devel
BuildRequires:  unzip
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OpenJazz is an open-source version of the classic Jazz Jackrabbit games.
To play, you will need the files from one of the original games.

%prep
%setup -q -c
%patch0 -p1
dos2unix gpl.txt

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
