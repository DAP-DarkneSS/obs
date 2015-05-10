#
# spec file for package haxe
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           haxe
Version:        3.1.3
Release:        0
Summary:        Multiplatform opensource programming language
License:        GPL-2.0+
Group:          Development/Languages/Other
Url:            http://www.haxe.org
# from https://github.com/HaxeFoundation/haxe/archive/3.1.3.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  nekovm
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Haxe is an open-source high-level multiplatform programming language and compiler that can produce applications and source code for many different platforms from a single code-base. Code written in the Haxe language can be compiled into Adobe Flash applications, JavaScript programs, C++ standalone applications (to some extent), PHP, Apache CGI, and NodeJS server-side applications.

%prep
%setup -q
sed -i 's,%{_libexecdir}/haxe/lib,%{_libdir}/haxe/lib,g' *.ml

%build
make %{?_smp_mflags} clean
make %{?_smp_mflags}
export HAXE_STD_PATH=$PWD/std
make %{?_smp_mflags} tools

%install
mkdir -p %{buildroot}%{_libdir}/haxe/std
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/haxe %{buildroot}%{_bindir}/haxe
# cp extra/haxelib_src/haxelib_script.sh $(INSTALL_DIR)/bin/haxelib
echo "#!/bin/sh" > %{buildroot}%{_bindir}/haxelib
echo 'exec haxe -cp %{_libdir}/haxe/extra/haxelib_src/src --run tools.haxelib.Main "$@"' >> %{buildroot}%{_bindir}/haxelib
cp -R std/* %{buildroot}%{_libdir}/haxe/std

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/haxe
%{_bindir}/haxelib
%{_libdir}/haxe

%changelog
