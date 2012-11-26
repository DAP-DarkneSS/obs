#
# spec file for package fullscreenprojpl
#
# Copyright (c) 2012 Igor Gritsenko (source),
# (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# https://github.com/drone-pl/FullScreenProj.pl/issues
#

Name:           fullscreenprojpl
Version:        0.6.git
Release:        1
Summary:        A screen saver suppresser

License:        Artistic-2.0
Url:            https://github.com/drone-pl/FullScreenProj.pl
Group:          System/X11/Utilities
Source0:        FullScreenProj.pl-%{version}.tar.bz2

Requires:       perl-File-HomeDir
Requires:       perl-Net-DBus
Requires:       perl-Proc-ProcessTable
Requires:       xprop
Requires:       xset
BuildArch:      noarch

%description
A perl daemon to suppress the screen saver
during the full-screen viewing of the video.

%prep
%setup -q -n FullScreenProj.pl-%{version}

%build
# gzip ./man/man1/fsproj.1

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} ./bin/fsproj %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%{__install} ./man/man1/fsproj.1.gz %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc README*
%attr(644,root,root) %doc %{_mandir}/man1/fsproj.1.gz
%attr(755,root,root) %{_bindir}/fsproj

%changelog
