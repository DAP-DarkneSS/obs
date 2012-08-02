#
# spec file for package fortunes-lor-quotes
#
# Copyright (c) 2005-2012 lorquotes.ru (quotes), (c) 2012 Perlow Dmitriy A. (spec file)
#

%define _date 20120802

Name:           fortunes-lor-quotes
Version:        date.%{_date}
Release:        0
Summary:        Quotes for fortune from linux.org.ru

License:        Unknown
URL:            http://lorquotes.ru/fortunes.php
Source0:        lor-quotes-%{version}.bz2
Group:          Amusements/Games/Other
Patch1:         gtk.patch
Patch2:         my.patch

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
%patch2

%build
%if 0%{suse_version} < 1220
/usr/sbin/strfile lor-quotes
%else
strfile lor-quotes
%endif

%install
mkdir -p %{buildroot}%{_datadir}/fortune
%{__install} lor-quotes lor-quotes.dat %{buildroot}%{_datadir}/fortune

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/fortune/lor-quotes*

%changelog
* Thu Aug 02 2012 DA <dap.darkness@gmail.com> - 20120802-1
- Date 20120802.

* Wed Aug 01 2012 DA <dap.darkness@gmail.com> - 20120801-1
- Date 20120801.

* Sun Jul 22 2012 DA <dap.darkness@gmail.com> - 20120722-1
- Date 20120722.

* Fri Jul 20 2012 DA <dap.darkness@gmail.com> - 20120720-1
- Date 20120720.

* Wed Jun 13 2012 DA <dap.darkness@gmail.com> - 20120613-1
- Date 20120613.

* Mon May 28 2012 DA <dap.darkness@gmail.com> - 20120528-1
- Date 20120528.

* Wed May 02 2012 DA <dap.darkness@gmail.com> - 20120502-1
- Date 20120502.

* Sat Apr 21 2012 DA <dap.darkness@gmail.com> - 20120421-1
- Date 20120421.
- Two my favorite quotes were added.

* Fri Feb 10 2012 DA <dap.darkness@gmail.com> - 20120210-1
- Date 20120210.
- Package got an architecture in order to fix a bug.

* Wed Feb 08 2012 DA <dap.darkness@gmail.com> - 20120208-1
- Date 20120208.
- A quote about programming with GTK was added.

* Sun Jan 22 2012 DA <dap.darkness@gmail.com> - 20120122-1
- Date 20120122.
