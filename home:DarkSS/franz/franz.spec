#
# spec file for package franz
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


Name:           franz
Version:        3.1.0
Release:        0
Summary:        Combines chat & messaging services into one app
License:        SUSE-Freeware
Group:          Productivity/Networking/Instant Messenger
Url:            http://meetfranz.com
ExclusiveArch:  x86_64 %ix86
%ifarch x86_64
Source0:        https://github.com/imprecision/franz-app/releases/download/%{version}/Franz-linux-x64-%{version}.tgz
Source9:        https://github.com/imprecision/franz-app/releases/download/%{version}/Franz-linux-ia32-%{version}.tgz
%endif
%ifarch %ix86
Source0:        https://github.com/imprecision/franz-app/releases/download/%{version}/Franz-linux-ia32-%{version}.tgz
Source9:        https://github.com/imprecision/franz-app/releases/download/%{version}/Franz-linux-x64-%{version}.tgz
%endif
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.sh
Source4:        %{name}.1

BuildRequires:  update-desktop-files
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
Franz is a free messaging app / former Emperor of Austria and combines
chat & messaging services into one application. Franz currently supports
Slack, WhatsApp, WeChat, HipChat, Facebook Messenger, Telegram, Google
Hangouts, GroupMe, Skype and many more.

%prep
%setup -qc

%build

%install
install -d %{buildroot}/{opt/franz,usr/{bin,share/{pixmaps,man/man1}}}
cp -R * %{buildroot}/opt/%{name}
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE4} %{buildroot}%{_datadir}/man/man1
%suse_update_desktop_file -i %{name}
# chmod +x %%{buildroot}/opt/%%{name}/franz

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
