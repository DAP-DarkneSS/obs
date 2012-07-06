%define		oname		MIB-Ossigeno-Ultimate-Icons
%define		oversion	4.3

Name:		mib-ossigeno-icons
Version:	4.3.0
Release:	%mkrel 69.3
Summary:	MIB-Ossigeno icon theme
# http://kde-look.org/content/show.php/?content=128221
Source0:	%{oname}-%{oversion}.tar.gz
License:	LGPL
Group:		Graphical desktop/KDE
URL:		http://mib.pianetalinux.org/mib/
BuildArch:	noarch
Obsoletes:	mib-ossigeno-icon-theme < %{version}

%description
MIB-Ossigeno Ultimate Icons is a blue icon theme derived from Oxygen Icons.
It differs from Oxygen mainly for folder icons, completely redesigned.
MIB-Ossigeno Ultimate Icons theme has been developed by emanueleeeee.

%prep
%setup -q -n %{oname}

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_iconsdir}/%{oname}

%__cp -rf ./* %{buildroot}%{_iconsdir}/%{oname}/

%__rm -f %{buildroot}%{_iconsdir}/%{oname}/README
%__rm -f %{buildroot}%{_iconsdir}/%{oname}/Changelog

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README Changelog
%{_iconsdir}/%{oname}/*



%changelog
* Mon Feb 20 2012 Andrey Bondrov <abondrov@mandriva.org> 4.3.0-69.3
+ Revision: 778079
- imported package mib-ossigeno-icons


* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.3.0-69.3mdv2010.2
- Fix theme icons dir
- Spec optimization
- Obsoletes mib-ossigeno-icon-theme

* Thu Mar 17 2011 Cristobal Lopez <lopeztobal@gmail.com> 4.3.0-69.2mib2010.2
- New release.

* Tue Jan 11 2011 Cristobal Lopez <lopeztobal@gmail.com> 4.2.0-1mib2010.2
- New release.

* Wed Jan 05 2011 Cristobal Lopez <lopeztobal@gmail.com> 4.1.0-1mib2010.2
- First release for Mandriva by MIB.