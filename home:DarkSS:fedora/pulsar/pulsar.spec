#
# spec file for package pulsar
#
# Copyright (c) 2011-2013 Vasily 'YuBerion' Kiniv (source),
# (c) 2012-2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via [russian]
# http://forum.ubuntu.ru/index.php?topic=203220
#

%define subver 6

Name:           pulsar
Version:        0.92
Release:        1
Summary:        Vk.com audio player

License:        GPL-2.0
Url:            http://forum.ubuntu.ru/index.php?topic=203220
Group:          Productivity/Other
Source0:        https://launchpad.net/~yuberion/+archive/pulsar/+files/%{name}_%{version}-%{subver}.tar.gz

BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqxt-devel
BuildRequires:  pkgconfig(Qt)
BuildRequires:  pkgconfig(QtGStreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-0.10)

Requires:       gstreamer-0_10-plugins-ugly

%description
Russian social network vkontakte (vk.com) audio player.

%prep
%setup -q -n %{name}
chmod -x src/%{name}.desktop
mkdir build

%build
cd build
qmake-qt4 \
QMAKE_STRIP="" \
PREFIX=%{_prefix} \
QMAKE_LRELEASE=lrelease-qt4 \
../%{name}.pro \
QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}
cd build
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/%{name}/translations/
%{__install} src/translations/%{name}*.qm %{buildroot}%{_datadir}/%{name}/translations/

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
