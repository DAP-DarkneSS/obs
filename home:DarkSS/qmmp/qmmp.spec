#
# spec file for package qmmp
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


%bcond_with ffmpeg
%bcond_with mad
%bcond_with faad

%define soname 0

Name:           qmmp
Version:        0.6.8
Release:        0
Summary:        XMMS-like audio player
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Players
Url:            http://qmmp.ylsoftware.com/
Source0:        http://qmmp.googlecode.com/files/qmmp-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE qmmp-0.6.1-default_pulse.patch reddwarf@opensuse.org -- Use PulseAudio instead of ALSA by default
Patch0:         qmmp-0.6.1-default_pulse.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmpcdec-devel
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtOpenGL)
BuildRequires:  pkgconfig(QtXml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(enca) >= 1.9
BuildRequires:  pkgconfig(flac)
# Standard Jack version is not new enough until openSUSE 12.1
%if 0%{?suse_version} > 1140
BuildRequires:  pkgconfig(jack)
%endif
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmms)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libprojectM)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%endif
%if %{with mad}
BuildRequires:  pkgconfig(mad)
%endif
%if %{with faad}
BuildRequires:  libfaad-devel
%endif
Requires:       qmmp(%{soname})(Input)
Requires:       qmmp(%{soname})(Output)
Requires:       qmmp(%{soname})(Ui)

%description
This program is an audio-player, written with help of Qt library. The program
has user interface, similar winamp or xmms.

%package -n libqmmp%{soname}
Summary:        Qmmp library
Group:          System/Libraries
Recommends:     libqmmp%{soname}-plugin-mplayer
Recommends:     libqmmp%{soname}-plugins

%description -n libqmmp%{soname}
Qmmp library.

%package -n libqmmp%{soname}-plugins
Summary:        Plugins for libqmmp
Group:          System/Libraries
Provides:       qmmp(%{soname})(Input)
Provides:       qmmp(%{soname})(Output)
Provides:       qmmp(%{soname})(Ui)

%description -n libqmmp%{soname}-plugins
Plugins for libqmmp.

%package -n libqmmp%{soname}-plugin-mplayer
Summary:        MPlayer plugin for libqmmp
Group:          System/Libraries
Requires:       %{_bindir}/mplayer

%description -n libqmmp%{soname}-plugin-mplayer
MPlayer plugin for libqmmp.

%package -n libqmmp-devel
Summary:        Development files for libqmmp
Group:          Development/Libraries/C and C++
Requires:       libqmmp%{soname} = %{version}

%description -n libqmmp-devel
Development files for libqmmp.

%prep
%setup -q
%patch0

%build
mkdir build
cd build
export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
cmake -DCMAKE_BUILD_WITH_INSTALL_RPATH=1 \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB_DIR=%{_lib} \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DUSE_HAL=FALSE \
      -DUSE_OSS=FALSE \
      -DUSE_OSS4=FALSE \
      ..
make %{?_smp_mflags}

%install
cd build
%make_install

%post
%icon_theme_cache_post
%desktop_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%post -n libqmmp%{soname} -p /sbin/ldconfig

%postun -n libqmmp%{soname} -p /sbin/ldconfig

%post -n libqmmp%{soname}-plugins
%desktop_database_post

%postun -n libqmmp%{soname}-plugins
%desktop_database_postun

%files
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING README
%attr(0755,root,root) %{_bindir}/qmmp
%{_datadir}/qmmp
%{_datadir}/applications/qmmp.desktop
%{_datadir}/applications/qmmp_enqueue.desktop
%{_datadir}/applications/qmmp_dir.desktop
%{_datadir}/icons/hicolor/*/apps/qmmp*

%files -n libqmmp%{soname}
%defattr(0644,root,root,0755)
%{_libdir}/libqmmp.so.%{soname}*
%{_libdir}/libqmmpui.so.%{soname}*

%files -n libqmmp%{soname}-plugins
%defattr(0644,root,root,0755)
%{_libdir}/qmmp
%exclude %{_libdir}/qmmp/Engines/libmplayer.so
%{_datadir}/applications/qmmp_cue.desktop

%files -n libqmmp%{soname}-plugin-mplayer
%defattr(0644,root,root,0755)
%{_libdir}/qmmp/Engines/libmplayer.so

%files -n libqmmp-devel
%defattr(0644,root,root,0755)
%{_includedir}/qmmp
%{_includedir}/qmmpui
%{_libdir}/libqmmp.so
%{_libdir}/libqmmpui.so
%{_libdir}/pkgconfig/qmmp.pc
%{_libdir}/pkgconfig/qmmpui.pc

%changelog
