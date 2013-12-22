#
# spec file for package python-annchienta
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


Name:           python-annchienta
Version:        2.0.svn903
Release:        0
Summary:        Annchienta game engine
License:        GPL-3.0+
Group:          Amusements/Games/Other
Url:            http://annchienta.sf.net
Source0:        http://optimate.dl.sourceforge.net/project/annchienta/annchienta/current/annchienta-svn903-src.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(python2)

%description
This package is the core Annchienta engine.

%prep
%setup -q -n annchienta

%build
cmake \
      -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_INSTALL_PREFIX:PATH="%{_prefix}"

make V=1 %{?_smp_mflags}

%install
make V=1 install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*annchienta*

%changelog
