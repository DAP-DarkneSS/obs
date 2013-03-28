#
# spec file for package zsh-notifyosd-kde
#
# (c) 2013 Brandon Pierce aka ihashacks & Vladimir aka shockone (sources)
# (c) 2013 Perlow Dmitriy A. (patch & spec file)
#

Name:           zsh-notifyosd-kde
Version:        date.20130328
Release:        0
License:        SUSE-Public-Domain
Summary:        Pseudo undistract-me implementation in zsh and KDE
Url:            https://gist.github.com/shockone/5255331
Group:          System/Shells
Source:         %{name}

BuildArch:      noarch

BuildRequires:  zsh

Requires:       kdialog
Requires:       zsh

%description
Displays a notification when a command, that takes over 10 seconds to
execute, finishes and only if the current window isn't the terminal. Add to
your ~/.zshrc:
[ -e /usr/share/zsh/functions/Misc/notifyosd-kde ] && . /usr/share/zsh/functions/Misc/notifyosd-kde

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/zsh/functions/Misc/
%{__install} %{SOURCE0} %{buildroot}%{_datadir}/zsh/functions/Misc/notifyosd-kde

%files
%defattr(-,root,root)
%dir %{_datadir}/zsh/functions
%dir %{_datadir}/zsh/functions/Misc
%attr(644,root,root) %{_datadir}/zsh/functions/Misc/notifyosd-kde

%changelog
