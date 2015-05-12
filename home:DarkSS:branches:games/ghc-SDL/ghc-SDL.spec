#
# spec file for package ghc-SDL
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


%global pkg_name SDL

Name:           ghc-SDL
Version:        0.6.5
Release:        0
Summary:        Binding to libSDL
License:        BSD-3-Clause
Group:          System/Libraries 

Url:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  SDL-devel
# End cabal-rpm deps

%description
Simple DirectMedia Layer (libSDL) is a cross-platform multimedia library
designed to provide low level access to audio, keyboard, mouse, joystick, 3D
hardware via OpenGL, and 2D video framebuffer. It is used by MPEG playback
software, emulators, and many popular games, including the award winning Linux
port of "Civilization: Call To Power.".


%package devel
Summary:        Haskell %{pkg_name} library development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
# Begin cabal-rpm deps:
Requires:       SDL-devel
# End cabal-rpm deps

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package doc
Summary:        Haskell %{pkg_name} documentation
Group:          Documentation/Other
Recommends:     %{name}

%description doc
This package provides the Haskell %{pkg_name} library documentation.


%prep
%setup -q -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install
rm -rf %{buildroot}%{_datadir}/%{pkg_name}-%{version}

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%defattr(-,root,root,-)
%doc LICENSE README

%files devel -f %{name}-devel.files
%defattr(-,root,root,-)

%changelog
