#
# spec file for package commandergenius
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


Name:           commandergenius
Version:        1.6.5.5
Release:        0
Summary:        An open clone of the Commander Keen engines
License:        GPL-2.0
Group:          Amusements/Games/Action/Arcade
Url:            http://clonekeenplus.sf.net/

#Git-Clone:	git://github.com/gerstrong/Commander-Genius
Source:         http://downloads.sf.net/clonekeenplus/CGenius-%version-Release-Source.tar.bz2
#Patch1:		keen-compile.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libSDL-devel >= 1.2
BuildRequires:  libSDL_image-devel
BuildRequires:  libvorbis-devel

%description
Clonekeen is a nearly complete reimplementation of the id Software
game "Commander Keen", with new features and enhancements, such as
2-player support, a built-in level editor and alternate game modes.

%prep
%setup -qn CGenius-%version-Release-Source

%build
cmake -DCMAKE_INSTALL_PREFIX=STRING:"%_prefix" -DAPPDIR="%_bindir" \
	-DGAMES_SHAREDIR="%_docdir" .
make %{?_smp_mflags}

%install
b="%buildroot";
make install DESTDIR="$b"
cp -a COPYRIGHT "$b/%_docdir/%name/"
%fdupes %buildroot/%_prefix

%files
%defattr(-,root,root)
%_bindir/CommanderGenius
%doc COPYRIGHT README

%changelog
