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
License:        GPL-2.0
Summary:        Qt/C++ WinAMP like client for XMMS2
Url:            http://xmms2.org/wiki/Client:Promoe
Group:          Productivity/Multimedia/Sound/Players
Source0:        http://home.in.tum.de/~frauendo/promoe-%{version}.tar.gz

BuildRequires:  boost-devel
%if 0%{?fedora} <= 17
BuildRequires:  gcc-c++
%endif
%if 0%{?fedora} == 17
BuildRequires:  samba4-libs
%endif
BuildRequires:  pkgconfig(QtCore)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  xmms2-devel
%if 0%{?suse_version}
Recommends:     xmms2-plugin-curl
Recommends:     xmms2-plugin-id3v2
Recommends:     xmms2-plugin-m3u
Recommends:     xmms2-plugin-mad
Recommends:     xmms2-plugin-pulse
Recommends:     xmms2-plugin-wave
%endif
Requires:       xmms2

%description
Promoe is a client for the XMMS2 music daemon. Promoe’s interface
is modeled after XMMS/WinAMP classic and supports Winamp 2 skins.
It's written in C++ and uses the Qt4 toolkit.

%prep
%setup -q

%build
`pkg-config --variable=exec_prefix QtCore`/bin/qmake \
QMAKE_STRIP="" \
PREFIX=%{_prefix} \
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} 'AudioVideo;Player;Qt;'
%endif

%files
%defattr(-,root,root)
%doc README COPYING TODO AUTHORS
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
