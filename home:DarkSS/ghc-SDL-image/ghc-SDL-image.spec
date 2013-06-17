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
%global common_summary Haskell %{pkg_name} library
%global common_description A %{pkg_name} library for Haskell.

Name:           ghc-%{pkg_name}
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Summary:        %{common_summary}
Url:            http://hackage.haskell.org/package/%{pkg_name}
Group:          System/Libraries
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-SDL-devel
BuildRequires:  pkgconfig(SDL_image)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{common_description}

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%ghc_devel_package
Requires:      pkgconfig(SDL_image)
Requires:      ghc-SDL-devel

%ghc_devel_description

%ghc_devel_post_postun

%ghc_files LICENSE README TODO
%exclude %{_datadir}/%{pkg_name}-%{version}

%changelog
