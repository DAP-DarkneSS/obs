#
# spec file for package kwin-effect-snow
#
# Copyright (c) KDE team, (c) 2012, Ivan Safonov <safonov.ivan.s@gmail.com>
# (source), (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via http://kubuntu.ru/node/10695
#

Name:           kwin-effect-snow
Version:        0.4
Release:        1
Summary:        A kwin effect Snow

License:        GPL-2.0+
Url:            http://kubuntu.ru/node/10695
Group:          System/GUI/KDE
Source0:        https://launchpad.net/~ivan-safonov/+archive/ppa/+files/%{name}_%{version}~precise~ppa1.tar.gz

BuildRequires:  kdebase4-workspace-devel
BuildRequires:  update-desktop-files
%kde4_runtime_requires

%description
A kwin effect "Snow" revived!

%prep
%setup -q -n %{name}-%{version}~precise~ppa1

%build
mkdir build && cd build
export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS
cmake ..  \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/kwin/snow*

%files
%defattr(-,root,root)
%dir %{_libdir}/kde4
%{_libdir}/kde4/*kwin4_effect_snow.so
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/*/kwin
%{_datadir}/kde4/*/kwin/snow*

%changelog
