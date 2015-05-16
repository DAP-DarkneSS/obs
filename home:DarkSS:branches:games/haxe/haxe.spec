#
# spec file for package haxe
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define haxelib %{_libdir}/%{name}

Name:           haxe
Version:        3.2.0
Release:        0
Summary:        Multiplatform opensource programming language
License:        GPL-2.0+
Group:          Development/Languages/Other
Url:            http://www.haxe.org
# from https://github.com/HaxeFoundation/haxe/archive/{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
# Tarball to download provides empty directories, so builds fail.
# See more at https://github.com/HaxeFoundation/haxe/issues/4200
# git clone git@github.com:HaxeFoundation/ocamllibs.git && cd ocamllibs
# git archive --format=tar master | xz -z9e > ocamllibs.tar.xz
Source1:        ocamllibs.tar.xz
# git clone git@github.com:HaxeFoundation/haxelib.git && cd haxelib
# git archive --format=tar master | xz -z9e > haxelib.tar.xz
Source2:        haxelib.tar.xz
BuildRequires:  fdupes
BuildRequires:  nekovm
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  pkgconfig(zlib)
Requires:       nekovm

%description
Haxe is an open-source high-level multiplatform programming language and compiler that can produce applications and source code for many different platforms from a single code-base. Code written in the Haxe language can be compiled into Adobe Flash applications, JavaScript programs, C++ standalone applications (to some extent), PHP, Apache CGI, and NodeJS server-side applications.

%prep
%setup -q
cd libs && tar -xf %{SOURCE1} && cd ..
cd extra/haxelib_src && tar -xf %{SOURCE2} && cd ../..
# WARNING: script-without-shebang.
chmod -x std/js/_std/Type.hx
chmod -x std/js/Boot.hx
chmod -x std/php/_std/haxe/ds/StringMap.hx
# WARNING: non-executable-script.
chmod +x extra/haxelib_src/src/tools/legacyhaxelib/haxelib.sh

%build
make V=1 %{?_smp_mflags} clean
make V=1 %{?_smp_mflags} libs
make V=1 %{?_smp_mflags}
make V=1 %{?_smp_mflags} tools

%install
# `make install` is broken for packaging by design, so:
mkdir -p %{buildroot}/%{haxelib}
mkdir -p %{buildroot}/%{_bindir}

cp -rf std %{buildroot}/%{haxelib}/std
cp -rf extra %{buildroot}/%{haxelib}
mkdir -p %{buildroot}/%{haxelib}/lib
cp haxe %{buildroot}/%{haxelib}

ln -s ../../%{haxelib}/haxe %{buildroot}/%{_bindir}/haxe
echo "#!/bin/sh" > %{buildroot}/%{_bindir}/haxelib
echo "export HAXE_STD_PATH=%{haxelib}/std" >> %{buildroot}/%{_bindir}/haxelib
echo "exec haxe -cp %{haxelib}/extra/haxelib_src/src --run tools.haxelib.Main \"\$$@\"" >> %{buildroot}/%{_bindir}/haxelib
chmod +x %{buildroot}/%{_bindir}/haxelib

# Windows only file cause "E: devel-file-in-non-devel-package"
# & "W: incorrect-fsf-address".
rm %{buildroot}/%{haxelib}/extra/setup.cpp
# Git, travis, htaccess and other trash.
find %{buildroot} -name '.*' -type f -delete -print
%fdupes -s %{buildroot}/%{haxelib}/extra/haxelib_src

%check
%{buildroot}/%{_bindir}/haxe --help

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/haxe*
%{haxelib}

%changelog
