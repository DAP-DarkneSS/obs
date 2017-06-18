#
# spec file for package bmake
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        20170510
Release:        0
Summary:        The NetBSD make(1) tool
License:        BSD-2-Clause and BSD-3-Clause and BSD-4-Clause
Group:          Development/Tools/Building
Url:            https://ftp.NetBSD.org/pub/NetBSD/misc/sjg/
Source0:        https://ftp.NetBSD.org/pub/NetBSD/misc/sjg/bmake-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE allow-overriding-compiler-variables.patch -- Based on Linux.sys.mk which was previously shipped with this package
# patch generated using `git diff master opensuse` from https://github.com/RichardsonAlex/bmake
Patch0:         allow-overriding-compiler-variables.patch

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
%patch0 -p1

%build
unset MAKEFLAGS
%if 0%{?suse_version} > 1325
env CFLAGS="-fmessage-length=0 -grecord-gcc-switches -O2 -Wall -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -g" \
%else
env CFLAGS="%{optflags}" \
%endif
./boot-strap -o Linux \
  --prefix="%{_prefix}" \
  --sysconfdir="%{_sysconfdir}" \
  --with-default-sys-path="%{_datadir}/mk" \
  --without-filemon \
  op=build

%install
./boot-strap -o Linux \
  --prefix="%{_prefix}" \
  --sysconfdir="%{_sysconfdir}" \
  --with-default-sys-path="%{_datadir}/mk" \
  --install-prefix="%{_prefix}" \
  --install-destdir="%{buildroot}" \
  op=install
mv "%{buildroot}%{_mandir}/cat1" "%{buildroot}%{_mandir}/man1"

%check
./boot-strap op=test

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_bindir}/bmake
%{_mandir}/man1/bmake.1%{ext_man}
%{_datadir}/mk/

%changelog
