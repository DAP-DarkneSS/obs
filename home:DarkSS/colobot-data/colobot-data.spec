#
# spec file for package colobot-data
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           colobot-data
Version:        0.1.8
Release:        0
Summary:        A real-time strategy game with programmable bots
License:        GPL-3.0+
Group:          Amusements/Games/Strategy/Real Time
Url:            http://colobot.info
Source0:        https://github.com/colobot/colobot-data/archive/colobot-gold-%{version}-alpha.tar.gz
Source1:        https://colobot.info/files/music/colobot-music_ogg_%{version}-alpha.tar.gz

BuildRequires:  cmake >= 3
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.6
BuildRequires:  python
Requires:       %{name} >= %{version}
BuildArch:      noarch

%description
And this is what made the game special in our childhood, or maybe even
early adulthood. Unlike most RTS games, Colobot does not require tactics,
but it does require thinking. An another difference would be the fact,
that we do not control the game from a 'god' camera, seeing everything
from up top, but instead, we are actually controlling each unit we make,
or find. This could potentially cause the problem, of not being able to
control 2 units at once, yet this is when an another twist comes in.
Colobot actually has its own interpretation of robot programming, which is
done fully by the player, together with a few hints and tips from the
trusty SatCom system. The programmed robots function at a level similar to
the brutality of writing an actual program, which does mean it requires
the right amount of accuracy, with the right mix of imagination.


%prep
%setup -q -n colobot-data-colobot-gold-%{version}-alpha
tar -xf %{SOURCE1} -C %{_builddir}/colobot-data-colobot-gold-%{version}-alpha/music

%build
%cmake
make V=1 %{?_smp_mflags}

%install
%cmake_install
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE* README*
%{_datadir}/games/colobot

%changelog
