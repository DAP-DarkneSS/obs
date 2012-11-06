#
# spec file for package pulsar
#
# Copyright (c) 2011-2012 Vasily 'YuBerion' Kiniv (source),
# (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via [russian]
# http://forum.ubuntu.ru/index.php?topic=203220
#

%define subver 13

Name:           pulsar
Version:        0.91
Release:        1
Summary:        Vk.com audio player

License:        GPL-2.0
Group:          Productivity/Other
URL:            http://forum.ubuntu.ru/index.php?topic=203220
#Source0:        https://launchpad.net/~yuberion/+archive/pulsar/+files/%{name}_%{version}-%{subver}.tar.gz
Source0:        http://dl.dropbox.com/u/74553863/pulsar/pulsar_0.91-13.tar.gz

#BuildRequires:  -post-build-checks
%if 0%{suse_version} > 1210
BuildRequires:  gstreamer-0_10-plugins-qt-devel
%endif
BuildRequires:  gstreamer-0_10-devel
BuildRequires:  gstreamer-0_10-plugins-base-devel
BuildRequires:  libqt4-devel
BuildRequires:  libQtGStreamer-0_10-devel
BuildRequires:  update-desktop-files
Recommends:     gstreamer-0_10-plugins-ugly

%description
Russian social network vkontakte (vk.com) audio player.

%prep
%setup -q -n %{name}
chmod -x src/%{name}.desktop
mkdir build

%build
cd build
qmake QMAKE_CXXFLAGS+="%{optflags}" PREFIX=/usr ../%{name}.pro
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}
cd build
make INSTALL_ROOT=%{buildroot} install
%suse_update_desktop_file -r %{name} 'AudioVideo;Player;Qt;'

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
