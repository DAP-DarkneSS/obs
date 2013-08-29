#
# spec file for package kwin-effect-snow
#
# Copyright (c) KDE team, (c) 2012, Ivan Safonov <safonov.ivan.s@gmail.com>
# (source), (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via http://kubuntu.ru/node/10695
#

%define postfix raring~ppa2

Name:           kwin-effect-snow
Version:        0.5
Release:        1
Summary:        A kwin effect Snow

License:        GPL-2.0+
Url:            http://kubuntu.ru/node/10695
Group:          System/GUI/KDE
Source0:        https://launchpad.net/~ivan-safonov/+archive/ppa/+files/%{name}_%{version}~%{postfix}.tar.gz

BuildRequires:  kdebase4-workspace-devel
BuildRequires:  update-desktop-files
%kde4_runtime_requires

%description
A kwin effect "Snow" revived!

%prep
%setup -q -n %{name}-%{version}~%{postfix}

%build
%cmake_kde4 -d build
make %{?_smp_mflags}

%install
cd build
%make_install
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/kwin/snow*

%kde_post_install

%files
%defattr(-,root,root)
%dir %{_libdir}/kde4
%{_libdir}/kde4/*kwin4_effect_snow.so
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/*/kwin
%{_datadir}/kde4/*/kwin/snow*

%changelog
