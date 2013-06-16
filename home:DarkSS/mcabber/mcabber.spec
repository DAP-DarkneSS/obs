# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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

# vim: set ts=4 sw=4 et:

Name:           mcabber
Version:        0.10.2
Release:        0
License:        GPL-2.0+
Summary:        Small Jabber Console Client
Url:            http://www.lilotux.net/~mikael/mcabber/
Group:          Productivity/Networking/Other
Source:         http://www.lilotux.net/~mikael/mcabber/files/mcabber-%{version}.tar.bz2
Source1:        mcabber.desktop

BuildRequires:  aspell-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  enchant-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gpgme
%if 0%{?suse_version} >= 1010
BuildRequires:  gpgme-devel
%endif
BuildRequires:  libgpg-error-devel
BuildRequires:  libidn-devel
%if 0%{?suse_version} > 1030 && 0%{?suse_version} <= 1100
BuildRequires:  libotr2
%endif
%if 0%{?suse_version} >= 1230
BuildRequires:  libotr2-devel
%else
BuildRequires:  libotr-devel >= 3.1.0
%endif
BuildRequires:  libtool
BuildRequires:  loudmouth-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version:1}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  vim-base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libotr >= 0.3.1

%description
mcabber is a small Jabber console client. It features SSL support, history
logging, and external actions.

%package devel
Summary:        Small Jabber Console Client
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glib2-devel
Requires:       loudmouth-devel

%description devel
mcabber is a small Jabber console client. It features SSL support, history
logging, and external actions.

%prep
%setup -q
find contrib/ -type f -exec %__chmod 0644 {} \;

%build
%configure \
    --enable-otr \
    --enable-aspell \
    --enable-enchant \
    --enable-xep0022 \
    --disable-hgcset

%__make %{?_smp_flags}

%install
%makeinstall

%__rm "%{buildroot}%{_libdir}/mcabber"/*.la

%__install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/mcabber.desktop"
%if 0%{?suse_version}
%suse_update_desktop_file -r "%{name}" Network InstantMessaging
%endif

%__install -D -m0644 contrib/vim/mcabber_log-ftdetect.vim \
    "%{buildroot}%{_datadir}/vim/site/ftdetect/mcabber_log.vim"
%__install -D -m0644 contrib/vim/mcabber_log-syntax.vim \
    "%{buildroot}%{_datadir}/vim/site/syntax/mcabber_log.vim"
%__rm -rf contrib/vim

%__mv mcabberrc.example mcabberrc

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc mcabberrc doc/*.html doc/*.css doc/*.txt
%doc contrib
%{_bindir}/mcabber
%{_datadir}/mcabber
%doc %{_mandir}/man1/mcabber.1%{ext_man}
%{_datadir}/applications/mcabber.desktop
%{_datadir}/vim/site/ftdetect/mcabber_log.vim
%{_datadir}/vim/site/syntax/mcabber_log.vim
%dir %{_libdir}/mcabber
%{_libdir}/mcabber/libbeep.so
%{_libdir}/mcabber/libfifo.so
%{_libdir}/mcabber/liburlregex.so
%{_libdir}/mcabber/libxttitle.so

%files devel
%defattr(-,root,root)
%{_includedir}/mcabber
%{_libdir}/pkgconfig/mcabber.pc

