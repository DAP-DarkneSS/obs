#
# spec file for package QMPlay2
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           QMPlay2
Version:        16.07.07
Release:        0
Summary:        A Qt based media player, streamer and downloader
License:        LGPL-3.0+
Group:          Productivity/Multimedia/Video/Players
Url:            http://qt-apps.org/content/show.php/QMPlay2?content=153339
Source:         http://kent.dl.sourceforge.net/project/zaps166/QMPlay2/QMPlay2-src-%{version}.tar.xz
# PATCH-FIX-UPSTREAM vs. Qt5.3 lrelease issue, read more at
# https://github.com/zaps166/QMPlay2/issues/10#issuecomment-186585268
Patch0:         QMPlay2-Qt53-lrelease.diff
#PATCH-FIX-OPENSUSE vs. Prostopleer extension that provides illegal audio.
Patch1:         QMPlay2-no-prostopleer.diff

%if 0%{?suse_version} > 1310
BuildRequires:  libqt5-linguist
%else
BuildRequires:  libqt5-qttools
%endif
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xv)
Recommends:     youtube-dl
Obsoletes:      %{name}-kde-integration <= %{version}

%description
%{name} is a video player, it can play and stream all formats supported by
ffmpeg and libmodplug (including J2B). It has an integrated Youtube browser.

%package        devel
Summary:        %{name} development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description    devel
It's a development package for %{name}.

%prep
%setup -q -n %{name}-src-%{version}
%if 0%{?suse_version} <= 1320
%patch0
%endif
%patch1

%build
export QT_SUFFIX="-qt5"
%if 0%{?suse_version} <= 1320
export QMAKE=/usr/bin/qmake$QT_SUFFIX
lrelease$QT_SUFFIX QMPlay2.pro
%endif
NOTERM=1 SYSTEM_BUILD=1 ./compile_unix `echo "%{?_smp_mflags}" | grep -o '[0-9]*'`

%install
mkdir -p %{buildroot}%{_prefix}
cp -R app/* %{buildroot}%{_prefix}

# Setting libs to system libdir instead of 'lib'.
%if "%{_lib}" == "lib64"
mv %{buildroot}/%{_prefix}/{lib,lib64}
mkdir -p %{buildroot}/%{_prefix}/lib
ln -s %{_libdir}/qmplay2 %{buildroot}/%{_prefix}/lib/qmplay2
%endif

# Let's use %%doc macro
cd %{buildroot}/%{_datadir}/qmplay2
rm ChangeLog LICENSE README.md TODO

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README.md TODO
%{_bindir}/%{name}
%{_libdir}/qmplay2
%{_libdir}/libqmplay2.so
%{_prefix}/lib/qmplay2
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%if 0%{?suse_version} == 1315
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%endif
%{_datadir}/qmplay2
%{_mandir}/man?/%{name}.?.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}

%changelog
