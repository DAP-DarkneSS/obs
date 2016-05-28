#
# spec file for package jgrep
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


# Maven is unneeded when jar is bundled.
%define _mkcmake %{mkcmake} PROG.mvn=/bin/false
%define so_maj_ver 0

Name:           jgrep
Version:        0.5.2
Release:        0
Summary:        Grep-like utility written in Java
License:        Apache-2.0
Group:          Productivity/Text/Utilities
Url:            https://github.com/cheusov/jgrep
Source0:        https://github.com/cheusov/jgrep/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-0.1-jar-with-dependencies.jar
Source9:        %{name}-rpmlintrc

BuildRequires:  java-sdk >= 1.7
BuildRequires:  config(mk-configure)
BuildRequires:  perl
Requires:       jre >= 1.7
Requires:       libjgrep_jni%{so_maj_ver} >= %{version}

%description
jgrep is a command-line grep-like utility written in Java.
Features:
  -- Java regular expressions
     (https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html)
  -- Support for RE2J
     (https://github.com/google/re2)
  -- POSIX options (excluding -E and -G)
     (http://pubs.opengroup.org/onlinepubs/009604499/utilities/grep.html)
  -- most GNU grep(1) options
     (https://www.gnu.org/software/grep/)
  -- Extensions over GNU grep(1):
     options -O, -2 and -8
Documentation:
  -- /usr/share/doc/packages/jgrep/jgrep.pod
       or
  -- man jgrep

%package -n libjgrep_jni%{so_maj_ver}
Summary:        Library for jgrep — JNI library
Requires:       %{name} >= %{version}

%description -n libjgrep_jni%{so_maj_ver}
A library for command-line grep-like utility written in Java.

%prep
%setup -q
mkdir -p jar/target
cp %{SOURCE1} jar/target
# Jar might have recent modification time to prevent rebuild.
touch jar/target/%{name}-*-jar-with-dependencies.jar

%build
%{_mkcmake} all

%install
%{_mkcmake} install
cd %{buildroot}%{_libdir}
# There are no linking so let's remove useless files.
rm libjgrep_jni.a libjgrep_jni.so libjgrep_jni.so.%{so_maj_ver}
mv libjgrep_jni.so.%{so_maj_ver}.* libjgrep_jni.so

%check
%{_mkcmake} test

%post -n libjgrep_jni%{so_maj_ver}
/sbin/ldconfig

%postun -n libjgrep_jni%{so_maj_ver}
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc scripts/jgrep.pod
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/*/%{name}*
%{_datadir}/java/%{name}-*-jar-with-dependencies.jar

%files -n libjgrep_jni%{so_maj_ver}
%defattr(-,root,root)
%{_libdir}/libjgrep_jni.so

%changelog
