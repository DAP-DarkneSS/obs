Summary: Bluecurve icon theme
Name: bluecurve-icon-theme
Version: 8.0.2
Release: 7%{?dist} 
BuildArch: noarch
License: GPL+
Group: User Interface/Desktops
# There is no official upstream yet
Source0: %{name}-%{version}.tar.bz2
URL: http://www.redhat.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

Requires: system-logos
Requires: bluecurve-cursor-theme
Requires(post): coreutils

# we require XML::Parser for our in-tree intltool
BuildRequires: perl(XML::Parser)

%description
This package contains Bluecurve style icons.

%package -n bluecurve-cursor-theme
Summary: Bluecurve cursor theme
Group: User Interface/Desktops

%description -n bluecurve-cursor-theme
This package contains Bluecurve style cursors.

%prep
%setup -q 

%build
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# These are empty
rm -f ChangeLog NEWS README

touch $RPM_BUILD_ROOT%{_datadir}/icons/Bluecurve/icon-theme.cache

# The upstream packages may gain po files at some point in the near future
%find_lang %{name} || touch %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/Bluecurve
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache -f --quiet %{_datadir}/icons/Bluecurve || :
fi

%postun
touch --no-create %{_datadir}/icons/Bluecurve
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache -f --quiet %{_datadir}/icons/Bluecurve || :
fi


%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING
%{_datadir}/icons/Bluecurve/index.theme
%{_datadir}/icons/Bluecurve/16x16
%{_datadir}/icons/Bluecurve/20x20
%{_datadir}/icons/Bluecurve/24x24
%{_datadir}/icons/Bluecurve/32x32
%{_datadir}/icons/Bluecurve/36x36
%{_datadir}/icons/Bluecurve/48x48
%{_datadir}/icons/Bluecurve/64x64
%{_datadir}/icons/Bluecurve/96x96
%ghost %{_datadir}/icons/Bluecurve/icon-theme.cache

%files -n bluecurve-cursor-theme
%dir %{_datadir}/icons/Bluecurve
%{_datadir}/icons/Bluecurve/Bluecurve.cursortheme
%{_datadir}/icons/Bluecurve/cursors
%{_datadir}/icons/Bluecurve-inverse
%{_datadir}/icons/LBluecurve
%{_datadir}/icons/LBluecurve-inverse

%changelog
* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 23 2009 Ray Strode <rstrode@redhat.com> - 8.0.2-4
- Require coreutils for touch in post (bug 507581)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Matthias Clasen <mclasen@redhat.com> - 8.0.2-2
- Split off cursor theme as a separate package

* Mon Apr  7 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8.0.2-1
- Add some symlinks to make Bluecurve work well with KDE 4 (#408151)

* Fri Feb  1 2008 Matthias Clasen <mclasen@redhat.com> - 8.0.1-1
- Fix some lrt <-> ltr typos
- Flip some redo icons

* Fri Oct 12 2007 Ray Strode <rstrode@redhat.com> - 8.0.0-1
- Add a lot of missing icons back (bug 328391)
- redo Bluecurve Makefile to scale better to all the new icons
- bump version to 8.0.0

* Tue Sep 25 2007 Ray Strode <rstrode@redhat.com> - 1.0.0-1
- Initial import, version 1.0.0
