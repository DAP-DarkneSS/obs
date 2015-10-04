#
# spec file for package QMPlay2
#
# Copyright (c) 2015 Packman team: http://packman.links2linux.org/
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.links2linux.org/
#


Name:           QMPlay2
Version:        15.10.03
Release:        0
Summary:        A Qt based media player, streamer and downloader
License:        LGPL-3.0+
Group:          Productivity/Multimedia/Video/Players
Url:            http://qt-apps.org/content/show.php/QMPlay2?content=153339
Source:         http://kent.dl.sourceforge.net/project/zaps166/QMPlay2/QMPlay2-src-%{version}.tar.bz2

BuildRequires:  kdebase4-workspace
BuildRequires:  portaudio-devel
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xv)
Recommends:     youtube-dl
Suggests:       %{name}-kde-integration

%description
%{name} is a video player, it can play and stream all formats supported by
ffmpeg and libmodplug (including J2B). It has an integrated Youtube browser.

%package        kde-integration
Summary:        %{name} KDE integration subpackage
Requires:       %{name}
Requires:       kdebase4-workspace
BuildArch:      noarch

%description    kde-integration
Media playing actions for removable devices in KDE.

%package        devel
Summary:        %{name} development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description    devel
It's a development package for %{name}.

%prep
%setup -q -n %{name}-src


%build
NOTERM=1 SYSTEM_BUILD=1 ./compile_unix `echo "%{?_smp_mflags}" | grep -o '[0-9]*'`

%install
mkdir -p %{buildroot}%{_prefix}
cp -R app/* %{buildroot}%{_prefix}

# Setting libs to system libdir instead of 'lib'.
%if "%{_lib}" == "lib64"
mv %{buildroot}/%{_prefix}/{lib,lib64}
%endif

# Don't package binary modules in datadir.
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}/%{_datadir}/qmplay2/modules/*.so %{buildroot}%{_libdir}/%{name}
rm -rf %{buildroot}/%{_datadir}/qmplay2/modules
ln -s %{_libdir}/%{name} %{buildroot}/%{_datadir}/qmplay2/modules

# Deleting useless links.
rm -rf %{buildroot}/%{_datadir}/icons/hicolor
# Setting icon to 'pixmaps' instead of 'icons'.
mv %{buildroot}/%{_datadir}/{icons,pixmaps}


%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc COPYING TODO
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_libdir}/libqmplay2.so
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/qmplay2

%files kde-integration
%defattr(-,root,root)
%{_datadir}/kde4/apps/solid/actions/*.desktop

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}

%changelog
