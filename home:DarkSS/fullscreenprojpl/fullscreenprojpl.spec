#
# spec file for package fullscreenprojpl
#
# Copyright (c) 2012 Igor Gritsenko (source),
# (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# https://github.com/drone-pl/FullScreenProj.pl/issues
#

%define binname fsproj
%define gitname FullScreenProj.pl

Name:           fullscreenprojpl
Version:        0.8.git
Release:        1
Summary:        A screen saver suppressor

License:        Artistic-2.0
Url:            https://github.com/drone-pl/FullScreenProj.pl
Group:          System/X11/Utilities
Source0:        %{gitname}-%{version}.tar.bz2

BuildRequires:  update-desktop-files

Requires:       perl-File-HomeDir
Requires:       perl-Net-DBus
Requires:       perl-Proc-ProcessTable
Requires:       perl-Wx
Requires:       xprop
Requires:       xset

%{perl_requires}

BuildArch:      noarch

%description
A perl daemon to suppress the screen saver
during the full-screen viewing of the video.

%prep
%setup -q -n %{gitname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} ./bin/%{binname} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%{__install} ./share/man/man1/%{binname}.1.gz %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/icons/%{binname}
%{__install} ./share/icons/%{binname}/*.xpm %{buildroot}%{_datadir}/icons/%{binname}
mkdir -p %{buildroot}%{_datadir}/applications
%{__install} ./share/applications/%{binname}.desktop %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{perl_vendorlib}/FSProj
%{__install} ./lib/FSProj/*.pm %{buildroot}%{perl_vendorlib}/FSProj
%suse_update_desktop_file -r %{binname} 'Utility;Accessibility;'

%files
%defattr(-,root,root)
%doc ./share/doc/%{name}/*
%attr(644,root,root) %doc %{_mandir}/man1/%{binname}.1.gz
%attr(755,root,root) %{_bindir}/%{binname}
%dir %{_datadir}/icons/%{binname}
%attr(644,root,root) %{_datadir}/icons/%{binname}/*.xpm
%dir %{perl_vendorlib}/FSProj
%attr(644,root,root) %{perl_vendorlib}/FSProj/*.pm
%{_datadir}/applications/%{binname}.desktop

%changelog
