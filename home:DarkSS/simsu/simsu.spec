#
# spec file for package simsu
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


Name:           simsu
Version:        1.2.3
Release:        0
Summary:        A basic Sudoku game
License:        GPL-3.0+
Group:          Amusements/Games/Board/Puzzle
Url:            http://gottcode.org/simsu
Source0:        https://github.com/gottcode/simsu/archive/v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(QtCore)

%description
Simsu is a basic Sudoku game. You can switch between filling
in notes (pencil mode), or filling in answers (pen mode). To
make it easier to see where to place numbers, you can
highlight all instances of a number. You can also check your
answers for correctness while playing. The game stores your
current notes and answers, so that you can pick up where you
left off the next time you play.


%prep
%setup -q


%build
qmake \
      QMAKE_STRIP="" \
      PREFIX=%{_prefix} \
      QMAKE_CXXFLAGS+="%{optflags}"

make V=1 %{?_smp_mflags}


%install
make V=1 install INSTALL_ROOT=%{buildroot}
# W: wrong-icon-size expected: 256x256 actual: 512x512
mv %{buildroot}/%{_datadir}/icons/hicolor/{256x256,512x512}


%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun


%files
%defattr(-,root,root)
%doc ChangeLog COPYING CREDITS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}

%changelog
