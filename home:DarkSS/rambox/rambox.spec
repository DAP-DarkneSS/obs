#
# spec file for package rambox
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


Name:           rambox
Version:        0.4.0
Release:        0
Summary:        Combines common messaging and emailing apps
License:        MIT
Group:          Productivity/Networking/Instant Messenger
Url:            http://rambox.pro
ExclusiveArch:  x86_64 %ix86
%ifarch x86_64
Source0:        https://github.com/saenzramiro/rambox/releases/download/%{version}/Rambox-linux-x64.zip
Source9:        https://github.com/saenzramiro/rambox/releases/download/%{version}/Rambox-linux-ia32.zip
%endif
%ifarch %ix86
Source0:        https://github.com/saenzramiro/rambox/releases/download/%{version}/Rambox-linux-ia32.zip
Source9:        https://github.com/saenzramiro/rambox/releases/download/%{version}/Rambox-linux-x64.zip
%endif
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.sh
Source4:        %{name}.1

BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
Free and Open Source messaging and emailing app that combines common web
applications into one.

%prep
%setup -qc

%build

%install
install -d %{buildroot}/{opt/rambox,usr/{bin,share/{pixmaps,man/man1}}}
cp -R * %{buildroot}/opt/%{name}
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE4} %{buildroot}%{_datadir}/man/man1
%suse_update_desktop_file -i %{name}
chmod +x %{buildroot}/opt/%{name}/Rambox

# Let's use %%doc macro.
rm %{buildroot}/opt/%{name}/LICENSE*

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc LICENSE*
/opt/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*.?.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
