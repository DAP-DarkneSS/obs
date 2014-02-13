#
# spec file for package vokoscreen
#
# Copyright (c) 2013 Mariusz Fik <fisiu@opensuse.org>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.links2linux.org/
#

Name:           vokoscreen
Version:		1.8.0
Release:		0
License:		GPL-2.0
Summary:        Screencast creator
Url:            https://github.com/vkohaupt/vokoscreen
Group:          Productivity/Multimedia/Other
### git clone git@github.com:vkohaupt/vokoscreen.git
### cd vokoscreen
### git archive 1.8.0 --prefix=vokoscreen-1.8.0/ | xz > ../vokoscreen-1.8.0.tar.xz
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libqt4-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(opencv)
### Required for recording
Requires:       ffmpeg
### Required for pause during record
Requires:       mkvtoolnix
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
vokoscreen is an easy to use screencast creator to record educational videos, 
live recordings of browser, installation, videoconferences, etc.

%prep
%setup -q

%build
qmake
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING CREDITS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}.png

%changelog
