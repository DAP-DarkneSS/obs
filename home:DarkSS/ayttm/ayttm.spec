#
# spec file for package ayttm
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

Name:           ayttm
Version:        0.6.3
Release:        0
License:        GPL-2.0+ and GPL-3.0+ and LGPL-2.0+
Summary:        Universal Instant Messaging Client
Url:            http://ayttm.sourceforge.net/
Group:          Productivity/Networking/Instant Messenger
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  aspell-devel
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  enchant-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXpm-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libjasper-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0)

Recommends:     %{name}-lang
Recommends:     aspell
Recommends:     xawtv

%description
Ayttm is designed to become a Universal Instant Messaging client, seamlessly
integrating all existing Instant Messaging clients and providing a single
consistant user interface. Currently, Ayttm supports sending and receiving
messages through AOL, ICQ, Yahoo, MSN, IRC and Jabber.

%lang_package

%prep
%setup -q

%build
%configure \
          --enable-smtp \
          --enable-jasper-filter \
          --enable-posix-dlopen \
          --disable-esd \
          --disable-static \
          --disable-arts \
          --with-gnu-ld
make %{?_smp_mflags}

%install
%make_install INSTALL="install -p"
%find_lang %{name}

mkdir -p %{buildroot}%{_datadir}/applications
%{__install} %{buildroot}%{_datadir}/applnk/Internet/ayttm.desktop \
             %{buildroot}%{_datadir}/applications
rm -rf %{buildroot}%{_datadir}/applnk/ %{buildroot}%{_datadir}/gnome
%suse_update_desktop_file %{name}


%files
%defattr(-,root,root)
%doc COPYING AUTHORS README ChangeLog TODO
%doc %{_mandir}/man*/%{name}*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_libdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}*

%files lang -f %{name}.lang

%changelog
