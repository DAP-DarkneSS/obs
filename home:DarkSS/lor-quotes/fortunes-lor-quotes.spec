#
# spec file for package fortunes-lor-quotes
#
# Copyright (c) 2005-2012 lorquotes.ru (quotes), (c) 2012 Perlow Dmitriy A. (spec file)
#

%define _date 20140224

Name:           fortunes-lor-quotes
Version:        date.%{_date}
Release:        0
Summary:        Quotes for fortune from linux.org.ru

License:        SUSE-Public-Domain
URL:            http://lorquotes.ru/fortunes.php
Source0:        lor-quotes-%{version}.bz2
Group:          Amusements/Games/Other
Patch1:         bonus.patch

BuildRequires:  bzip2
BuildRequires:  fortune
BuildRequires:  glibc
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
%if 0%{?suse_version} < 1220
/usr/sbin/strfile lor-quotes
%else
strfile lor-quotes
%endif

%install
mkdir -p %{buildroot}%{_datadir}/fortune
%{__install} lor-quotes lor-quotes.dat %{buildroot}%{_datadir}/fortune

%check
fortune lor-quotes

%files
%defattr(644,root,root,755)
%{_datadir}/fortune/lor-quotes*

%changelog
