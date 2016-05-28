#
# spec file for package mk-configure
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


Name:           mk-configure
Version:        0.29.1
Release:        0
Summary:        Lightweight replacement for GNU autotools
License:        BSD-2-Clause and BSD-2-Clause and MIT and ISC
Group:          Development/Tools
Url:            http://sourceforge.net/projects/mk-configure/
Source:         http://prdownloads.sf.net/%{name}/%{name}-%{version}.tar.gz
Source1:        mkcmake.macros
Source9:        mk-configure-rpmlintrc

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bmake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  groff
BuildRequires:  info
BuildRequires:  lua-devel
BuildRequires:  makedepend
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
Requires:       bmake
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
rm -rf %{buildroot}%{_datadir}/doc/%{name}
# E: wrong-script-interpreter (Badness: 533)
chmod -x examples/hello_lua/foobar.in
chmod -x examples/hello_scripts/hello_world3.in
chmod -x examples/hello_subdirs/prog1/prog1.awk.in
# HACK vs. duplicates after %%doc macro.
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
cp -r examples %{buildroot}%{_docdir}/%{name}-doc
%fdupes -s %{buildroot}%{_docdir}/%{name}-doc
# rpm macros
install -m644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/rpm/macros.mkcmake

%check
unset MAKEFLAGS
env \
    LEXLIB=-lfl \
    NOSUBDIR='hello_lex hello_superfs hello_progs subprojects hello_lua hello_lua2 hello_lua3 hello_yacc hello_calc2 tools hello_dictd hello_libdeps' \
    bmake \
    test
bmake cleandir-examples
bmake cleandir-tests
# E: suse-filelist-forbidden-backup-file
rm -rf examples/*/*/*~

%files
%defattr(-,root,root)
%doc README doc/FAQ doc/LICENSE doc/NEWS doc/TODO
%{_bindir}/mkc*
%{_datadir}/mk-configure/
%{_datadir}/mkc-mk/
%{_mandir}/man1/*
%{_mandir}/man7/*
%config %{_sysconfdir}/rpm/macros.mkcmake

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}-doc/examples
%doc presentation/presentation.pdf

%changelog
