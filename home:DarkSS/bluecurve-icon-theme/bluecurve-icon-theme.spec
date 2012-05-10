#
# spec file for package bluecurve-icon-theme
#
# Copyright (c) Red Hat
#

Summary:        Bluecurve icon theme
Name:           bluecurve-icon-theme
Version:        8.0.2
Release:        1
BuildArch:      noarch
License:        GPL-2.0
Group:          System/X11/Icons
# There is no official upstream yet
Source0:        %{name}-%{version}.tar.bz2
URL:            http://www.redhat.com

Recommends:     bluecurve-cursor-theme
Requires(post): coreutils

# we require XML::Parser for our in-tree intltool
BuildRequires:  perl(XML::Parser)
BuildRequires:  fdupes

%description
This package contains Bluecurve style icons.

%package -n bluecurve-cursor-theme
Summary:        Bluecurve cursor theme
Group:          System/GUI/Other
Recommends:     bluecurve-icon-theme

%description -n bluecurve-cursor-theme
This package contains Bluecurve style cursors.

%prep
%setup -q 

%build
%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# These are empty
rm -f ChangeLog NEWS README

touch $RPM_BUILD_ROOT%{_datadir}/icons/Bluecurve/icon-theme.cache

# The upstream packages may gain po files at some point in the near future
%find_lang %{name} || touch %{name}.lang

%fdupes -s %{buildroot}%{_datadir}/icons/Bluecurve/*x*
%fdupes -s %{buildroot}%{_datadir}/icons/*luecurv*/cursors

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
%defattr(-, root, root)
%dir %{_datadir}/icons/Bluecurve
%{_datadir}/icons/Bluecurve/Bluecurve.cursortheme
%{_datadir}/icons/Bluecurve/cursors
%{_datadir}/icons/Bluecurve-inverse
%{_datadir}/icons/LBluecurve
%{_datadir}/icons/LBluecurve-inverse

%changelog
