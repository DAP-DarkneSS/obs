#
# spec file for package leechcraft
#
# Copyright (c) 2010-2011 emanueleeeee & MIB Mandriva International Backports.
# http://kde-look.org/usermanager/search.php?username=emanueleeeee
# http://mib.pianetalinux.org/mib/
#

%define         oname MIB-Ossigeno-Ultimate-Icons

Name:           mib-ossigeno-icons
Version:        4.3
Release:        1
Summary:        MIB Ossigeno Ultimate Icons theme
Source0:        http://mib.pianetalinux.org/MIB/2010.1/others/projects/MIB-Ossigeno-Ultimate/Tarball/%{oname}-%{version}.tar.gz
License:        LGPL
Group:          System/GUI/KDE
URL:            http://kde-look.org/content/show.php/?content=128221
BuildArch:      noarch
BuildRequires:  kde4-filesystem
BuildRequires:  fdupes

%description
MIB-Ossigeno Ultimate Icons is a blue icon theme derived from Oxygen Icons.
It differs from Oxygen mainly for folder icons, completely redesigned.
MIB-Ossigeno Ultimate Icons theme has been developed by emanueleeeee.

%prep
%setup -q -n %{oname}

%build

%install
%__mkdir_p %{buildroot}%{_kde4_iconsdir}/%{oname}

%__cp -rf ./* %{buildroot}%{_kde4_iconsdir}/%{oname}/

%__rm -f %{buildroot}%{_kde4_iconsdir}/%{oname}/README
%__rm -f %{buildroot}%{_kde4_iconsdir}/%{oname}/Changelog

%fdupes -s %{buildroot}%{_kde4_iconsdir}/%{oname}

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README Changelog
%dir %{_kde4_iconsdir}/%{oname}
%{_kde4_iconsdir}/%{oname}/*

%changelog
