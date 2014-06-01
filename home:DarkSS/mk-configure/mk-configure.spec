#
# spec file for package mk-configure
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


Name:           mk-configure
Version:        0.26.0
Release:        0
Summary:        Lightweight replacement for GNU autotools
License:        BSD-2-Clause and BSD-2-Clause and MIT and ISC
Group:          Development/Tools
Url:            http://sourceforge.net/projects/mk-configure/
Source:         http://prdownloads.sf.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  bmake
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  groff
BuildRequires:  info
BuildRequires:  lua-devel
BuildRequires:  makedepend
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
Requires:       bmake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Recommends:     %{name}-doc

%description
mk-configure is a lightweight replacement for GNU autotools, written in
bmake (portable version of NetBSD make), POSIX shell and POSIX utilities.

%package doc
Summary:        MK-C' documentation
Group:          Documentation/Other
Requires:       %{name}

%description doc
Mk-configure package: examples and presentation.

%prep
%setup -q

%define env \
        unset MAKEFLAGS \
        export PREFIX=%{_prefix} \
        export MANDIR=%{_mandir}

# examples are built and tested either,
# let's keep a pristine copy
cp -al examples doc

%build
%{env}
bmake all

%install
%{env}
bmake install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_docdir}/%{name}
# E: wrong-script-interpreter (Badness: 533)
chmod -x examples/hello_lua/foobar.in

%check
unset MAKEFLAGS
env \
    LEXLIB=-lfl \
    NOSUBDIR='hello_lex hello_superfs hello_progs subprojects hello_lua hello_lua2 hello_lua3 hello_yacc hello_calc2 tools hello_dictd' \
    bmake \
    test

%files
%defattr(-,root,root)
%doc README doc/FAQ doc/LICENSE doc/NEWS doc/TODO
%{_bindir}/*
%{_datadir}/mk-configure/
%{_datadir}/mkc-mk/
%{_mandir}/man1/*
%{_mandir}/man7/*

%files doc
%defattr(-,root,root)
%doc examples
%doc presentation/presentation.pdf

%changelog
