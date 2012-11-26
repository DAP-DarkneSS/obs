#
# spec file for package sysinfo
#
# Copyright (c) 2007-2012 Alexey S. Smirnov (binary),
# (c) 2012 Perlow Dmitriy A. (spec file)
#

Name:           sysinfo
Version:        0.7.4
Release:        1
Summary:        System Profiler and Benchmark

License:        MIT
Url:            http://betatester.bir.ru/sysinfolinux.html
Group:          System/Benchmark
Source0:        http://betatester.bir.ru/Downloads/%{name}4linux074.tar.bz2
Source1:        %{name}.png

BuildRequires:  update-desktop-files
Recommends:     libcpubench1

%description
SysInfo can gather information about your system's hardware
and operating system and perform benchmarks.

%package -n libcpubench1
Summary:        Sysinfo library

%description -n libcpubench1
It's a library for sysinfo.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} ./%{name} %{buildroot}%{_bindir}/%{name}-bin

mkdir -p %{buildroot}%{_prefix}/lib
cp -P ./libcpubench.s* %{buildroot}%{_prefix}/lib

echo -e '#!/bin/sh'"\n\ncd /usr/lib\n%{name}-bin" > %{buildroot}%{_bindir}/%{name}4linux
# The binary file should be run from the libs directory.

mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name} %{name} "System Profiler and Benchmark" %{name}4linux %{name} "System;HardwareSettings;"

%post -n libcpubench1 -p /sbin/ldconfig

%postun -n libcpubench1 -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%attr(755,root,root) %{_bindir}/%{name}-bin
%attr(755,root,root) %{_bindir}/%{name}4linux

%files -n libcpubench1
%defattr(-,root,root)
%{_prefix}/lib/libcpubench.s*

%changelog
