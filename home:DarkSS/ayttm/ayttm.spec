Summary: Universal Instant Messaging Client
Name: ayttm
Version: 0.6.3
Release: 7%{?dist}
Group: Applications/Internet
License: GPLv2+ and LGPLv2+
URL: http://ayttm.sourceforge.net/
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: flex
BuildRequires: bison
BuildRequires: libtool-ltdl-devel
BuildRequires: libXpm-devel
BuildRequires: openssl-devel
BuildRequires: jasper-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: gettext
BuildRequires: aspell-devel
BuildRequires: libtool-ltdl
BuildRequires: enchant-devel
BuildRequires: libyahoo2-devel

Requires: xawtv
Requires: aspell

%description
Ayttm is designed to become a Universal Instant Messaging client, seamlessly
integrating all existing Instant Messaging clients and providing a single
consistant user interface. Currently, Ayttm supports sending and receiving
messages through AOL, ICQ, Yahoo, MSN, IRC and Jabber.

%prep

%setup -q -n %{name}-%{version}

tr -d '\r' < AUTHORS > AUTHORS.new
iconv -f ISO-8859-2 -t UTF-8 AUTHORS.new > AUTHORS


%build
%configure --enable-smtp --enable-jasper-filter --enable-posix-dlopen --disable-esd --disable-static --disable-arts --with-gnu-ld
 
make %{?_smp_mflags}

%install
%make_install INSTALL="install -p"
%find_lang %{name}

desktop-file-install                                    \
--delete-original                                       \
--dir=$RPM_BUILD_ROOT%{_datadir}/applications              \
$RPM_BUILD_ROOT/%{_datadir}/applnk/Internet/%{name}.desktop


%files -f %{name}.lang
%doc COPYING AUTHORS README ChangeLog
%doc %{_mandir}/man*/*
%{_datadir}/pixmaps/*.png
%{_datadir}/ayttm/sounds/*
%{_datadir}/ayttm/smileys/*
%{_datadir}/applications/ayttm.desktop
%{_libdir}/ayttm/*.so 
%config(noreplace) %{_sysconfdir}/ayttmrc
%{_bindir}/ayttm_streamer_wrapper
%{_bindir}/ayttm
%exclude %{_libdir}/ayttm/*.la
%exclude %{_datadir}/applnk/Internet/ayttm.desktop
%exclude %{_datadir}/gnome/apps/Internet/ayttm.desktop

%changelog
* Tue Feb 12 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.3-7
- disable esd support since esd is getting dropped in Fedora
- clean up spec to follow current guidelines

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.6.3-6
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.6.3-5
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.3-2
- Rebuild for new libpng

* Tue May 17 2011 Minto Joseph <mvaliyav at redhat.com> 0.6.3-1
- Rebased to new upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 11 2010 Minto Joseph <mvaliyav at redhat.com> 0.6.2-2
- Included Build Requires for enchant-devel

* Tue Mar 11 2010 Minto Joseph <mvaliyav at redhat.com> 0.6.2-1
- Rebased to new upstream release

* Tue Nov 21 2009 Minto Joseph <mvaliyav at redhat.com> 0.6.1-1
- Rebased to new upstream release

* Tue Sep 16 2009 Minto Joseph <mvaliyav at redhat.com> 0.6.0-1
- Rebased to new upstream release
- Cleaned up spec file
- Added patch for msn2.so loading issue 
- Added patch for renaming ayttm_streamer_wrapper

* Tue Jul 28 2009 Minto Joseph <mvaliyav at redhat.com> 0.5.0-1.111
- Rebased to new upstream release

* Fri Jun 26 2009 Parag <panemade@gmail.com > 0.5.0-2
- Use correct way to install translations and rpm macros 
- Correct BuildRequires and follow post release naming

* Mon Jun 10 2009 Minto Joseph <mvaliyav at redhat.com> - 0.5.0-1
- Cleaned up spec file
- Included ifnarch for ppc64 to fix build issue with brp-compress 
- Removed the option for stripping of debug information

* Mon Jun 01 2009 Minto Joseph <mvaliyav at redhat.com> - 0.5.0-0
- initial package


