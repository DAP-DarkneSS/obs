#
# spec file for package cpufreqd
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


%define lib_name %{mklibname} %{name}
# (misc) about the rpmlint warning.
#
# file in /usr/lib are plugin, so they do not have a soname
# and they do not nned to be installable side by side with another
# version, so it is safe to ignore the error.
Name:           cpufreqd
Version:        2.4.2
Release:        0
Summary:        CPU frequency scaling daemon
License:        GPL-2.0+
Group:          System/Kernel and hardware
Url:            http://www.linux.it/~malattia/wiki/index.php/Cpufreqd
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.init
Source2:        cpufreq_defaults
Patch0:         %{name}.Makefile.patch
# (fc) 1.2.3-2mdk add more cpu intensive programs to full power mode
Patch1:         cpufreqd-2.1.1-defaults.patch
# add patch from upstream to fix a buffer overflow with gcc-4.5
Patch2:         cpufreqd-2.4.2-fix-segfault-when-calling-realpath.patch
BuildRequires:  automake
BuildRequires:  libcpufreq-devel
BuildRequires:  libsysfs-devel
Requires:       %{lib_name}
Requires(preun,post): rpm-helper

%description
cpufreqd is meant to be a replacement of the speedstep applet you
can find on some other OS, it monitors battery level, AC state and
running programs and adjusts the frequency of the processor according to
a set of rules specified in the config file (see cpufreqd.conf (5)).

It works only with a kernel patched with the cpufreq patch, such as the
standard %{_vendor} kernel.

You also need a supported processor, often found in laptops.

%package -n %{lib_name}
Summary:        Library for %{name}
Group:          System/Kernel and hardware

%description -n %{lib_name}
This packages contains some library needed
by %{name}.

%prep
%setup -q
%patch0
%patch1 -p1 -b .defaults
%patch2 -p1 -b .segfault

# fix build with new automake 1.13
sed -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,g' configure.*

%build
autoreconf -vfi
%{configure2_5x}
%{make}

%install
%{makeinstall_std}

install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_sysconfdir}/%{name}
install -D -p -m 755 %{SOURCE1} %{buildroot}/%{_initddir}/%{name}
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/cpufreq_defaults

%post
%{_post_service} %{name}

%preun
%{_preun_service} %{name}

%files
%defattr(-,root,root,0755)
%doc AUTHORS README TODO NEWS ChangeLog
%attr(755,root,root) %{_sbindir}/cpufreqd
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/cpufreqd.conf
%config(noreplace) %{_initddir}/%{name}
%dir %{_sysconfdir}/%{name}/
%{_datadir}/%{name}/cpufreq_defaults
%dir %{_datadir}/%{name}/
%attr(644,root,root) %{_mandir}/*/*
%{_bindir}/*

%files -n %{lib_name}
%defattr(-,root,root,0755)
%{_libdir}/cpufreqd*

%changelog
