#
# spec file for package jrep
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
%define _mkcmake %{mkcmake} PROG.mvn=/bin/false \\\
                            DOCDIR=%{_docdir}/%{name} \\\
                            JARDIR=%{_datadir}/java
%define libpackname liblib%{name}_jni0

Name:           jrep
Version:        0.6.1
Release:        0
Summary:        Grep-like utility written in Java
License:        Apache-2.0
Group:          Productivity/Text/Utilities
Url:            https://github.com/cheusov/jrep
Source0:        https://github.com/cheusov/jrep/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-0.1-jar-with-dependencies.jar
Source2:        %{name}-jar-howto.txt
Source9:        %{name}-rpmlintrc

BuildRequires:  java-sdk >= 1.7
BuildRequires:  mk-configure-rpm-macros
BuildRequires:  perl
Requires:       %{libpackname} >= %{version}
Requires:       jre >= 1.7

%description
jrep is a command-line grep-like utility written in Java.
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
  -- /usr/share/doc/packages/jrep/jrep.pod
       or
  -- man jrep

%package -n %{libpackname}
Summary:        Library for %{name} — JNI library
Requires:       %{name} >= %{version}

%description -n %{libpackname}
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

%check
%{_mkcmake} test

%post -n %{libpackname} -p /sbin/ldconfig
%postun -n %{libpackname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc scripts/%{name}.pod
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/*/%{name}*
%{_datadir}/java/%{name}-*-jar-with-dependencies.jar

%files -n %{libpackname}
%defattr(-,root,root)
%{_libdir}/lib%{name}_jni.so

%changelog
