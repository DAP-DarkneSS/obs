#
# spec file for package xmahjong
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


Name:           xmahjong
%if 0%{suse_version} > 1220
BuildRequires:  bdftopcf
%endif
BuildRequires:  fontpackages-devel
BuildRequires:  freetype2
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-devel
Conflicts:      xmahjongg
%if 0%{suse_version} > 1010
%define xbindir     /usr/bin
%define xlibdir     /usr/share
%define xmandir     /usr/share/man
%else
%define xbindir     /usr/X11R6/bin
%define xlibdir     /usr/X11R6/lib/X11
%define xmandir     /usr/X11R6/man
%endif
Version:        2010.11.8
Release:        0
Summary:        Mahjongg for X
License:        MIT
Group:          Amusements/Games/Board/Other
%reconfigure_fonts_prereq
Source:         xmahjong.tar.bz2
Patch0:         xmahjong.dif
Patch1:         missing-includes.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mahjongg is a challenging Chinese game similar to domino. It is usually
played by four players. Xmahjongg is the solitaire version designed for
the X Window System. More can be found in the appropriate manual page.

%prep
%setup -q -n xmahjong
%patch0
%patch1 -p1

%build
xmkmf -a
rm -f xmahjongg.man; ln -sf xmahjongg.6 xmahjongg.man
make LIBDIR=%{xlibdir} %{?_smp_mflags}

%install
chmod 644 copyright readme.1 readme.2
make install install.man DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{xlibdir} FONTDIR=%{_miscfontsdir}/..

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc copyright readme.1 readme.2
%dir %{xlibdir}/xmahjongg
%{xbindir}/xmahjongg
%dir %{_miscfontsdir}
%{_miscfontsdir}/xmahjongg.pcf.gz
%{xlibdir}/xmahjongg/bridge
%{xlibdir}/xmahjongg/default
%{xlibdir}/xmahjongg/wedges
%doc %{xmandir}/man1/xmahjongg.1x.gz

%changelog
