#
# spec file for package pulsar
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define majver 0.92
%define subver 10

Name:           pulsar
Version:        %{majver}.%{subver}
Release:        1
Summary:        Vk.com audio player
License:        GPL-3.0+
Url:            http://forum.ubuntu.ru/index.php?topic=203220
Group:          Productivity/Multimedia/Sound/Players
Source0:        https://launchpad.net/~yuberion/+archive/pulsar/+files/pulsar_%{majver}-%{subver}.tar.gz

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

make V=1 %{?_smp_mflags}

%install
mkdir -p %{buildroot}
cd build
make V=1 INSTALL_ROOT=%{buildroot} install

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
