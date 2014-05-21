#
# spec file for package kdenlive
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define kde_version 4.3
%define mlt_version 0.8.6
%define qt_version 4.5

Name:           kdenlive
Version:        0.9.8
Release:        0
Summary:        Non-linear video editor
License:        GPL-3.0+
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://www.kdenlive.org/
Source0:        http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM kdenlive-0.9.2-mlt_datadir.patch http://www.kdenlive.org/mantis/view.php?id=2701 reddwarf@opensuse.org -- Use versioned MLT data dir
Patch0:         kdenlive-0.9.2-mlt_datadir.patch
# PATCH-FIX-UPSTREAM kdenlive-0.9.2-no_avformat.patch http://www.kdenlive.org/mantis/view.php?id=2811 reddwarf@opensuse.org -- Make it work even if the avformat plugin is not available
Patch1:         kdenlive-0.9.2-no_avformat.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libkde4-devel >= %{kde_version}
BuildRequires:  libkdecore4-devel >= %{kde_version}
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(QJson) >= 0.5
BuildRequires:  pkgconfig(QtCore) >= %{qt_version}
BuildRequires:  pkgconfig(QtDBus) >= %{qt_version}
BuildRequires:  pkgconfig(QtGui) >= %{qt_version}
BuildRequires:  pkgconfig(QtOpenGL) >= %{qt_version}
BuildRequires:  pkgconfig(QtScript) >= %{qt_version}
BuildRequires:  pkgconfig(QtSvg) >= %{qt_version}
BuildRequires:  pkgconfig(QtXml) >= %{qt_version}
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(mlt++) >= %{mlt_version}
BuildRequires:  pkgconfig(mlt-framework) >= %{mlt_version}
BuildRequires:  pkgconfig(x11)
%define melt_path %(pkg-config --variable=meltbin mlt-framework)
Requires:       %{melt_path}
# Waiting for the day all libraries have versioned symbols...
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libmlt++.so) --qf '%{NAME}') >= %{mlt_version}
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libmlt.so) --qf '%{NAME}') >= %{mlt_version}
# Without a few of the plugins it crashes on start
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libmlt.so) --qf '%{NAME}')-modules
# It requires the profiles
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libmlt.so) --qf '%{NAME}')-data
Recommends:     %{_bindir}/dvdauthor
Recommends:     %{_bindir}/dvgrab
Recommends:     %{_bindir}/ffmpeg
Recommends:     %{_bindir}/ffplay
Recommends:     %{_bindir}/genisoimage
%define mlt_soname %(pkg-config --variable=moduledir mlt-framework | sed 's/.*-\\([0-9]\\+\\)/\\1/')
Recommends:     mlt(%{mlt_soname})(avformat)
%kde4_runtime_requires

%description
Kdenlive is a non-linear video editor for GNU/Linux and FreeBSD, which supports
DV, AVCHD (experimental support) and HDV editing. Kdenlive relies on several
other open source projects, such as FFmpeg and the MLT video framework. It was
designed to answer all needs, from basic video editing to semi-professional
work.

%prep
%setup -q
%patch0
%patch1

%build
%cmake_kde4 -d build
%make_jobs

%install
pushd build
%kde4_makeinstall
popd
# Debian menu system
rm -r %{buildroot}%{_datadir}/menu
rm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

%find_lang %{name}

%fdupes -s %{buildroot}

%kde_post_install

%post
%icon_theme_cache_post
%icon_theme_cache_post oxygen
%mime_database_post
%desktop_database_post

%postun
%desktop_database_postun
%mime_database_postun
%icon_theme_cache_postun oxygen
%icon_theme_cache_postun

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING README
%attr(0755,-,-) %{_bindir}/%{name}
%attr(0755,-,-) %{_bindir}/%{name}_render
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}_render.1*
%{_kde4_appsdir}/%{name}
%{_kde4_modulesdir}/libkdenlive_sampleplugin.so
%{_kde4_modulesdir}/westleypreview.so
%{_kde4_configdir}/%{name}*
%{_kde4_configdir}.kcfg/%{name}*
%{_kde4_servicesdir}/westleypreview.desktop
%{_kde4_applicationsdir}/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/oxygen/*/*/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mime/packages/westley.xml

%changelog
