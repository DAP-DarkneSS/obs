#
# spec file for package ghc-SDL-image
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


%global pkg_name SDL-image

Name:           ghc-SDL-image
Version:        0.6.1
Release:        0
Summary:        Binding to libSDL_image
License:        BSD-3-Clause
Group:          System/Libraries

Url:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE vs. "linking error: undefined reference to IMG_*".
Patch0:         ghc-SDL-image-pc.patch

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-SDL-devel
# End cabal-rpm deps
BuildRequires:  SDL_image-devel

%description
SDL_image is an image file loading library. It loads images as SDL surfaces,
and supports the following formats: BMP, GIF, JPEG, LBM, PCX, PNG, PNM, TGA,
TIFF, XCF, XPM, XV.


%package devel
Summary:        Haskell %{pkg_name} library development files
Group:          Development/Libraries/Other
Provides:       %{name}-static = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires:       pkgconfig(SDL_image)

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}
%patch0 -p1

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
%doc LICENSE TODO README

%files devel -f %{name}-devel.files
%defattr(-,root,root,-)

%changelog
