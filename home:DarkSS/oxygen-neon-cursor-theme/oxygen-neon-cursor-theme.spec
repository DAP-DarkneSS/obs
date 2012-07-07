#
# spec file for package oxygen-neon-cursor-theme
#
# Copyright (c) 2011 qwerta:
# http://kde-look.org/usermanager/search.php?username=qwerta
#

%define         oname oxy-neon

Name:           oxygen-neon-cursor-theme
Version:        0.2
Release:        1
Summary:        Oxygen Neon X11 Mouse Theme
Source0:        http://kde-look.org/CONTENT/content-files/137109-%{oname}-%{version}.tar.gz
License:        GPL
Group:          System/GUI/Other
URL:            http://kde-look.org/content/show.php/?content=137109
BuildArch:      noarch
BuildRequires:  kde4-filesystem

%description
Stylized oxygen mouse theme created for use with dark desktop
and especially for FRUiT's Neon suite.

%prep
%setup -q -n %{oname}

%build

%install
%__mkdir_p %{buildroot}%{_kde4_iconsdir}/%{oname}/cursors

%__cp -rf ./cursors/* %{buildroot}%{_kde4_iconsdir}/%{oname}/cursors
%{__install} index.theme %{buildroot}%{_kde4_iconsdir}/%{oname}

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_kde4_iconsdir}/%{oname}
%{_kde4_iconsdir}/%{oname}/*

%changelog
