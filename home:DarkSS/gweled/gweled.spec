#
# spec file for package gweled
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


Name:           gweled
Summary:        Clone of Bejeweled, align 3 crystals in a row to make them disappear
Version:        0.9.1
Release:        0
License:        GPL-2.0
Url:            http://gweled.org/
Group:          Amusements/Games/Logic
Source0:        %{name}-%{version}.tar.bz2
Source1:        gweled.desktop
Source2:        gweled.permissions
Source3:        gweled-rpmlintrc
BuildRequires:  gtk2-devel
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  librsvg-devel
BuildRequires:  libmikmod-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Gweled is a Gnome version of a popular PalmOS/Windows/Java game called
"Bejeweled" or "Diamond Mine". The aim of the game is to make
alignment of 3 or more gems, both vertically or horizontally by
swapping adjacent gems. The game ends when there are no possible moves
left.

%lang_package
%debug_package

%prep
%setup -q

%build
export LDFLAGS="-export-dynamic"
%configure

%install
%makeinstall
%if 0%{?suse_version}
%suse_update_desktop_file -i -n %{name} Game LogicGame
install -D -m 644 %{SOURCE2} %buildroot/%{_sysconfdir}/permissions.d/%{name}
%else
install -D -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_datadir}/applications/gweled.desktop
%endif

%find_lang %{name}

%files -f %{name}.lang
%defattr (-, root, root)
%doc NEWS AUTHORS
%attr(2755,games,games) %{_bindir}/gweled
%{_datadir}/applications/gweled.desktop
%{_datadir}/gweled
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/pixmaps/gweled*
%{_datadir}/sounds/gweled
%attr(0664,games,games) %{_localstatedir}/games/gweled.Normal.scores
%attr(0664,games,games) %{_localstatedir}/games/gweled.Timed.scores
%if 0%{?suse_version}
%config %{_sysconfdir}/permissions.d/%{name}
%endif

%changelog
