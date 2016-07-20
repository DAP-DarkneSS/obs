#
# spec file for package QMPlay2
#
# Copyright (c) 2016 Packman team: http://packman.links2linux.org/
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
Version:        16.07.20
Release:        0
Summary:        A Qt based media player, streamer and downloader
License:        LGPL-3.0+
Group:          Productivity/Multimedia/Video/Players
Url:            http://qt-apps.org/content/show.php/QMPlay2?content=153339
Source:         https://github.com/zaps166/QMPlay2/releases/download/%{version}/QMPlay2-src-%{version}.tar.xz

BuildRequires:  cmake >= 3
BuildRequires:  kdebase4-workspace
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(QtCore)
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
Requires(post): hicolor-icon-theme
Requires(post): shared-mime-info
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): shared-mime-info
Requires(postun): update-desktop-files
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
%setup -q -n %{name}-src-%{version}


%build
%cmake \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo
make V=1 %{?_smp_mflags}


%install
%cmake_install

# Let's use %%doc macro. AUTHORS & ChangeLog are required for help window
cd %{buildroot}/%{_datadir}/qmplay2
rm LICENSE README.md TODO

%post
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun


%files
%defattr(-,root,root)
%doc LICENSE README.md TODO
%{_bindir}/%{name}
%{_libdir}/qmplay2
%{_libdir}/libqmplay2.so
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/qmplay2
%{_mandir}/man?/%{name}.?.*
%{_datadir}/mime/packages/x-*.xml

%files kde-integration
%defattr(-,root,root)
%{_datadir}/kde4/apps/solid/actions/*.desktop

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}

%changelog
