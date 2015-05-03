#
# spec file for package blobby
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


Name:           blobby
Version:        1.0
Release:        0
Summary:        2D Arcade Beach Volleyball Game
License:        GPL-2.0
Group:          Amusements/Games/Action/Other
Url:            http://blobby.sourceforge.net
Source0:        http://sourceforge.net/projects/blobby/files/Blobby%20Volley%202%20%28Linux%29/1.0/%{name}2-linux-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
BuildRequires:  boost-devel
BuildRequires:  cmake
%if 0%{?suse_version} >= 1030
BuildRequires:  fdupes
%endif
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  physfs-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl2)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  zip
%if 0%{?suse_version} > 1220
BuildRequires:  zlib-devel
%endif
Provides:       blobby2 = %{version}
Obsoletes:      blobby2 < %{version}
Provides:       blobbyvolley = %{version}
Obsoletes:      blobbyvolley < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Blobby Volley is one of the most popular freeware games. This is caused
first by the simple play principle and second by the funny design of
the player. The short duration of a game is a reason for playing this
game in meantime.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
make %{?_smp_mflags}

%install
# TODO https://sourceforge.net/apps/mantisbt/blobby/view.php?id=107
%make_install

install -D %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%if 0%{?suse_version}
%suse_update_desktop_file %{name}
%endif
install -D %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%if 0%{?suse_version} >= 1030
%fdupes %{buildroot}%{_datadir}/%{name}
%endif

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
