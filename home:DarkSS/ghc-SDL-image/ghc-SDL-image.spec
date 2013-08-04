#
# spec file for package ghc-SDL-image
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


%global pkg_name SDL-image
%global common_summary Haskell binding for %{pkg_name} library
%global common_description SDL_image is an image file loading library. \
It loads images as SDL surfaces, and supports the following formats: \
BMP, GIF, JPEG, LBM, PCX, PNG, PNM, TGA, TIFF, XCF, XPM, XV.

Name:           ghc-SDL-image
Version:        0.6.1
Release:        0
Summary:        %{common_summary}
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-SDL-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  pkgconfig(SDL_image)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{common_description}

%package devel
Summary:        %{common_summary} development
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       ghc-compiler
Requires:       pkgconfig(SDL_image)
Requires(post): ghc-compiler
Requires(postun): ghc-compiler

%description devel
%{common_description}

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install
# Deletes text stuff, let's include it via doc-macro.
rm -rf %{buildroot}%{_datadir}/%{pkg_name}-%{version}

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%defattr(-,root,root,-)
%doc LICENSE README TODO

%files devel -f %{name}-devel.files
%defattr(-,root,root,-)

%changelog
