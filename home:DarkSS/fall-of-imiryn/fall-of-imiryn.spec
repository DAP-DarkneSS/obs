#
# spec file for package fall-of-imiryn
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


Name:           fall-of-imiryn
Version:        2.0.svn903
Release:        0
Summary:        2D RPG game
License:        GPL-3.0+
Group:          Amusements/Games/RPG
Url:            http://annchienta.sf.net/?page=fall_of_imiryn
Source0:        http://heanet.dl.sourceforge.net/project/annchienta/annchienta/current/fall_of_imiryn-svn903-src.tar.gz
Source1:        fall-of-imiryn.sh

BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       python-annchienta

%description
Fall of Imiryn tells the story of three aspiring young
warriors, hoping to join the Fifth Guard, the elite section
of the army of the Imiryn Empire. However, their last test
doesn't exactly turn out as they expected…

%prep
%setup -q -n fall_of_imiryn

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -R * %{buildroot}/%{_datadir}/%{name}

install -D -m755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}
%suse_update_desktop_file -c %{name} "Fall of Imiryn" "Fall of Imiryn 2D RPG game" %{name} "%{_datadir}/%{name}/images/storyline/title.png" "Game;RolePlaying;"

%fdupes -s %{buildroot}/%{_datadir}/%{name}/tiles

%files
%defattr(-,root,root)
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
