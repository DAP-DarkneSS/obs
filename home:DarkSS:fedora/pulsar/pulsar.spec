#
# spec file for package pulsar
#
# Copyright (c) 2011-2013 Vasily 'YuBerion' Kiniv (source),
# (c) 2012-2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# http://forum.ubuntu.ru/index.php?topic=203220 [russian only]
# or via http://bugs.opensuse.org/
#

%define majver 0.92
%define subver 7

Name:           pulsar
Version:        %{majver}.%{subver}
Release:        1
Summary:        Vk.com audio player

License:        GPL-3.0+
Url:            http://forum.ubuntu.ru/index.php?topic=203220
Group:          Productivity/Multimedia/Sound/Players
Source0:        https://launchpad.net/~yuberion/+archive/pulsar/+files/pulsar_%{majver}-%{subver}.tar.gz

%if 0%{?fedora} <= 17
BuildRequires:  gcc-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqxt-devel
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGStreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
Requires:       gstreamer-0_10-plugins-fluendo_mp3
Recommends:     gstreamer-plugins-ugly
%else
Requires:       gstreamer-plugins-ugly
%endif

%description
Russian social network vkontakte (vk.com) audio player and downloader.

%prep
%setup -q -n %{name}
mkdir build

%build
cd build

`pkg-config --variable=exec_prefix QtCore`/bin/qmake \
QMAKE_LRELEASE=`pkg-config --variable=exec_prefix QtCore`/bin/lrelease \
QMAKE_STRIP="" \
PREFIX=%{_prefix} \
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}" \
../%{name}.pro

make %{?_smp_mflags}

%install
mkdir -p %{buildroot}
cd build
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/%{name}/translations/
%{__install} src/translations/%{name}*.qm %{buildroot}%{_datadir}/%{name}/translations/

%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} 'AudioVideo;Player;Qt;'
%endif

%files
%defattr(-,root,root)
%attr(644,root,root) %doc debian/changelog
%{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}

%changelog
