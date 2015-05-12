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
Source1:        cpufreqd
Source2:        cpufreqd.service

# PATCH-FIX-OPENSUSE not to search libcpufreq.
Patch0:         cpupower.patch
# PATCH-FIX-OPENSUSE with longer video players list.
Patch1:         cpufreqd-2.1.1-defaults.patch
# PATCH-FIX-UPSRTEAM to fix a buffer overflow with gcc-4.5
Patch2:         cpufreqd-2.4.2-fix-segfault-when-calling-realpath.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cpupower-devel
BuildRequires:  libtool
BuildRequires:  sysfsutils-devel
Requires:       lib%{name}

%description
cpufreqd is meant to be a replacement of the speedstep applet you
can find on some other OS, it monitors battery level, AC state and
running programs and adjusts the frequency of the processor according to
a set of rules specified in the config file (see cpufreqd.conf (5)).

It works only with a kernel patched with the cpufreq patch, such as the
standard %{_vendor} kernel.

You also need a supported processor, often found in laptops.

%package -n lib%{name}
Summary:        Library for %{name}
Group:          System/Kernel and hardware

%description -n lib%{name}
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
%configure
make %{?_smp_mflags} V=1

%install
%make_install V=1

install -Dm755 %{SOURCE1} \
                %{buildroot}%{_sysconfdir}/rc.d/cpufreqd
install -Dm644 %{SOURCE2} \
                %{buildroot}%{_libexecdir}/systemd/system/cpufreqd.service


%pre
%service_add_pre cpufreqd.service

%preun
%{stop_on_removal cpufreqd}
%service_del_preun cpufreqd.service

%post
%service_add_post cpufreqd.service

%postun
%{restart_on_update cpufreqd}
%service_del_postun cpufreqd.service

%files
%defattr(-,root,root,0755)
%doc AUTHORS README TODO NEWS ChangeLog
%attr(755,root,root) %{_sbindir}/cpufreqd
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/cpufreqd.conf
%attr(644,root,root) %{_mandir}/*/*
%{_bindir}/*
%{_sysconfdir}/rc.d/cpufreqd
%{_libexecdir}/systemd/system/cpufreqd.service

%files -n lib%{name}
%defattr(-,root,root,0755)
%{_libdir}/cpufreqd*

%changelog
