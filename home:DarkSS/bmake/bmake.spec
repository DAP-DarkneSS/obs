#
# spec file for package bmake
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


Name:           bmake
Version:        20160512
Release:        0
Summary:        The NetBSD make(1) tool
License:        BSD-2-Clause and BSD-3-Clause and BSD-4-Clause
Group:          Development/Tools/Building
Url:            ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/
Source0:        ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/bmake-%{version}.tar.gz
Source1:        Linux.sys.mk
# PATCH-FIX-OPENSUSE to fix MAKE_VERSION variable & mk-configure package.
Patch0:         bmake-MAKE_VERSION.diff

%description
bmake, the NetBSD make(1) tool, is a program designed to simplify the
maintenance of other programs.  The input of bmake is a list of specifications
indicating the files upon which the targets (programs and other files) depend.
bmake then detects which targets are out of date based on their dependencies
and triggers the necessary commands to bring them up to date when that happens.

bmake is similar to GNU make, even though the syntax for the advanced features
supported in Makefiles is very different.

%prep
%setup -q -n %{name}
%patch0

%build
unset MAKEFLAGS
env CFLAGS="%{optflags}" \
./boot-strap -o Linux \
  --prefix="%{_prefix}" \
  --sysconfdir="%{_sysconfdir}" \
  --with-default-sys-path="%{_datadir}/mk" \
  --mksrc none op=build

%install
install -Dp -m0644 bmake.1      %{buildroot}%{_mandir}/man1/bmake.1
install -Dp -m0755 Linux/bmake  %{buildroot}%{_bindir}/bmake
install -Dp -m0644 %{SOURCE1}   %{buildroot}%{_datadir}/mk/sys.mk

%check
./boot-strap op=test

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_bindir}/bmake
%{_mandir}/man1/bmake.1%{ext_man}
%{_datadir}/mk/

%changelog
