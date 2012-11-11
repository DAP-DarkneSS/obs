#
# spec file for package promoe
#
# Copyright (c) 2005-2009, XMMS2 Team (source),
# (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via http://bugs.xmms2.xmms.se/
#

Name:           promoe
Version:        0.1.1
Release:        1
Summary:        Qt/C++ WinAMP like client for XMMS2

License:        GPL-2.0
Group:          Productivity/Multimedia/Sound/Players
URL:            http://xmms2.org/wiki/Client:Promoe
Source0:        http://home.in.tum.de/~frauendo/%{name}-%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files
BuildRequires:  xmms2-devel
Requires:       xmms2
Requires:       xmms2-plugin-curl
Requires:       xmms2-plugin-id3v2
Requires:       xmms2-plugin-m3u
Requires:       xmms2-plugin-mad
Requires:       xmms2-plugin-pulse
Requires:       xmms2-plugin-wave

%description
Promoe is a client for the XMMS2 music daemon. Promoe’s interface
is modeled after XMMS/WinAMP classic and supports Winamp 2 skins.
It's written in C++ and uses the Qt4 toolkit.

%prep
%setup -q

%build
qmake QMAKE_CXXFLAGS+="%{optflags}" PREFIX=/usr
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
%suse_update_desktop_file -r %{name} 'AudioVideo;Player;Qt;'

%files
%defattr(-,root,root)
%doc README COPYING TODO AUTHORS
%doc %{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
