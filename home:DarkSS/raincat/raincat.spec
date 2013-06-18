#
# spec file for package Raincat
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


%define pack_desc Raincat is a 2d puzzle game similar to the Incredible \
Machine and Lemmings series. Your goal is simple: guide the cat safe and \
dry to the end of each level. Just mind the rain, puddles, and loose fire \
hydrants in your path!

Name:           raincat
Version:        1.1.1.2
Release:        0
Summary:        Guide the fuzzy cat to safety
License:        BSD-3-Clause
Group:          Amusements/Games/Board/Puzzle
Url:            http://raincat.bysusanlin.com/
Source0:        http://hackage.haskell.org/packages/archive/Raincat/%{version}/Raincat-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-GLUT-devel
BuildRequires:  ghc-OpenGL-devel
BuildRequires:  ghc-SDL-devel
BuildRequires:  ghc-SDL-image-devel
BuildRequires:  ghc-SDL-mixer-devel
BuildRequires:  ghc-compiler
BuildRequires:  ghc-extensible-exceptions-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-time-devel
BuildRequires:  update-desktop-files
Requires:       %{name}-data = %{version}

%description
%{pack_desc}

The binary file.

%package data
Summary:        Raincat: art and other architecture independent data
License:        CC-BY-SA-3.0
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%{pack_desc}

Art and other architecture independent data.

%prep
%setup -q -n Raincat-%{version}

%build
runhaskell Setup configure --prefix=/usr --datasubdir=%{name} -O
runhaskell Setup build

%install
runhaskell Setup copy --destdir=%{buildroot}
%suse_update_desktop_file -c %{name} "Raincat" "Guide the fuzzy cat to safety" "%{name}" "%{_datadir}/%{name}/data/cat/cat-umbrella/cat-umbrella1.png" "Game;PuzzleGame;"

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%files data
%defattr(-,root,root)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%exclude %{_datadir}/doc/Raincat-%{version}/LICENSE

%changelog
