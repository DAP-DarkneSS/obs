#
# spec file for mib-ossigeno-icons packages
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
Source1:        http://mib.pianetalinux.org/MIB/2010.1/others/projects/MIB-Ossigeno-Ultimate/Tarball/%{oname}-Black-4.2.tar.gz
Source2:        http://mib.pianetalinux.org/MIB/2010.1/others/projects/MIB-Ossigeno-Ultimate/Tarball/%{oname}-Green-4.2.tar.gz
Source3:        http://mib.pianetalinux.org/MIB/2010.1/others/projects/MIB-Ossigeno-Ultimate/Tarball/%{oname}-Magenta-4.2.tar.gz
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

%package        black
Summary:        MIB Ossigeno Ultimate Icons Black theme
Version:        4.2

%description    black
MIB-Ossigeno Ultimate Icons Black is a black icon theme derived from Oxygen Icons.
It differs from Oxygen mainly for folder icons, completely redesigned.
MIB-Ossigeno Ultimate Icons theme has been developed by emanueleeeee.

%package        green
Summary:        MIB Ossigeno Ultimate Icons Green theme
Version:        4.2

%description    green
MIB-Ossigeno Ultimate Icons Green is a green icon theme derived from Oxygen Icons.
It differs from Oxygen mainly for folder icons, completely redesigned.
MIB-Ossigeno Ultimate Icons theme has been developed by emanueleeeee.

%package        magenta
Summary:        MIB Ossigeno Ultimate Icons Magenta theme
Version:        4.2

%description    magenta
MIB-Ossigeno Ultimate Icons Magenta is a magenta icon theme derived from Oxygen Icons.
It differs from Oxygen mainly for folder icons, completely redesigned.
MIB-Ossigeno Ultimate Icons theme has been developed by emanueleeeee.

%prep
tar -xf %{SOURCE0}
tar -xf %{SOURCE1}
tar -xf %{SOURCE2}
tar -xf %{SOURCE3}
# %%setup -q -n %%{oname}

%build

%install
%__mkdir_p %{buildroot}%{_kde4_iconsdir}

%__cp -rf ./* %{buildroot}%{_kde4_iconsdir}

%__rm -f %{buildroot}%{_kde4_iconsdir}/*/README
%__rm -f %{buildroot}%{_kde4_iconsdir}/*/Changelog

%fdupes -s %{buildroot}%{_kde4_iconsdir}/%{oname}
%fdupes -s %{buildroot}%{_kde4_iconsdir}/%{oname}-Black-4.2
%fdupes -s %{buildroot}%{_kde4_iconsdir}/%{oname}-Green-4.2
%fdupes -s %{buildroot}%{_kde4_iconsdir}/%{oname}-Magenta-4.2

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{oname}/README %{oname}/Changelog
%dir %{_kde4_iconsdir}/%{oname}
%{_kde4_iconsdir}/%{oname}/*

%files black
%defattr(644,root,root,755)
%doc %{oname}-Black-4.2/README %{oname}-Black-4.2/Changelog
%dir %{_kde4_iconsdir}/%{oname}-Black-4.2
%{_kde4_iconsdir}/%{oname}-Black-4.2/*

%files green
%defattr(644,root,root,755)
%doc %{oname}-Green-4.2/README %{oname}-Green-4.2/Changelog
%dir %{_kde4_iconsdir}/%{oname}-Green-4.2
%{_kde4_iconsdir}/%{oname}-Green-4.2/*

%files magenta
%defattr(644,root,root,755)
%doc %{oname}-Magenta-4.2/README %{oname}-Magenta-4.2/Changelog
%dir %{_kde4_iconsdir}/%{oname}-Magenta-4.2
%{_kde4_iconsdir}/%{oname}-Magenta-4.2/*

%changelog
