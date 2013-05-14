Summary:  A caching dns proxy for small networks or dialin accounts
Name:     pdnsd
Version:  1.2.9
Release:  0
License:  GPLv3
Group:    Productivity/Networking/DNS/Servers
Source0:  http://members.home.nl/p.a.rombouts/%{name}/releases/%{name}-%{version}-par.tar.gz
Source1:  pdnsd
URL:      http://members.home.nl/p.a.rombouts/pdnsd.html
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
pdnsd is a proxy DNS daemon with permanent (disk-)cache and the ability
to serve local records. It is designed to detect network outages or hangups
and to prevent DNS-dependent applications like Netscape Navigator from hanging.

The original author of pdnsd is Thomas Moestl, but pdnsd is no longer maintained
by him. This is an extensively revised version by Paul A. Rombouts.
For a description of the changes see http://www.phys.uu.nl/~rombouts/pdnsd.html
and the file README.par in %{_docdir}/%{name}-%{version}

%prep
%setup

%build
%configure --with-cachedir="/var/cache/pdnsd" \
	--enable-specbuild \
	--with-query-method=udptcp \
	--enable-ipv6 \
	--with-par-queries=3 \
	--with-debug=0

make

%install
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/init.d
mkdir -p %{buildroot}/usr/sbin/
cp %{S:1} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/
chmod 755 $RPM_BUILD_ROOT%{_sysconfdir}/init.d/pdnsd
cp $RPM_BUILD_ROOT%{_sysconfdir}/pdnsd.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/pdnsd.conf
ln -s /etc/init.d/%{name} %{buildroot}/usr/sbin/rc%{name}

%clean
rm -rf "$RPM_BUILD_ROOT"

%preun
%stop_on_removal

%postun
%insserv_cleanup
%restart_on_update

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/pdnsd.conf
%attr(755,root,root) %{_sysconfdir}/init.d/pdnsd
%{_sysconfdir}/pdnsd.conf.sample
%{_prefix}/sbin/*
%{_prefix}/share/man/man*/*
%attr(-,nobody,nobody) %config(noreplace) /var/cache/pdnsd/pdnsd.cache
%dir /var/cache/pdnsd

%changelog
