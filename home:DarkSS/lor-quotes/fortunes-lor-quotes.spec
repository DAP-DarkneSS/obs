#
# spec file for package fortunes-lor-quotes
#
# Copyright (c) 2005-2012 lorquotes.ru (quotes), (c) 2012 Perlow Dmitriy A. (spec file)
#

%define _date 20120306

Name:           fortunes-lor-quotes
Version:        date.%{_date}
Release:        0
Summary:        Quotes for fortune from linux.org.ru

License:        Unknown
URL:            http://lorquotes.ru/fortunes.php
Source0:        lor-quotes-%{version}.bz2
Group:          Amusements/Games/Other
Patch1:         gtk.patch

BuildRequires:  glibc bzip2
BuildRequires:  fortune
Requires:       fortune

%description
Favorite quotes for fortune from the site linux.org.ru.

Fortune displays a random text string from a set of files in a certain
format. This occurs each time you start a login shell. To get this
feature just uncomment the respective lines in the user's .profile.

%prep
bunzip2 -c -k %{SOURCE0} > lor-quotes-%{version}
iconv -f koi8-r -t utf-8 lor-quotes-%{version} > lor-quotes
%patch1

%build
/usr/sbin/strfile lor-quotes

%install
mkdir -p %{buildroot}%{_datadir}/fortune
%{__install} lor-quotes lor-quotes.dat %{buildroot}%{_datadir}/fortune

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/fortune/lor-quotes*

%changelog
* Tue Mar 06 2012 DA <dap.darkness@gmail.com> - 20120306-1
- Date 20120306.

* Sun Feb 26 2012 DA <dap.darkness@gmail.com> - 20120226-1
- Date 20120226.

* Fri Feb 10 2012 DA <dap.darkness@gmail.com> - 20120210-1
- Date 20120210.
- Package got an architecture in order to fix a bug.

* Thu Feb 09 2012 DA <dap.darkness@gmail.com> - 20120209-1
- Date 20120209.

* Wed Feb 08 2012 DA <dap.darkness@gmail.com> - 20120208-1
- Date 20120208.
- A quote about programming with GTK was added.

* Wed Jan 24 2012 DA <dap.darkness@gmail.com> - 20120125-1
- Date 20120125.

* Sun Jan 22 2012 DA <dap.darkness@gmail.com> - 20120122-1
- Date 20120122.
