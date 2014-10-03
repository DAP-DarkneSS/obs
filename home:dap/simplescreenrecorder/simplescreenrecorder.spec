#
# spec file for package simplescreenrecorder
#
# Copyright (c) 2014 Packman team: http://packman.links2linux.org/
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


Name:           simplescreenrecorder
Version:        0.3.1
Release:        0
License:        GPL-3.0+
Summary:        A feature-rich screen recorder that supports X11 and OpenGL
Url:            http://www.maartenbaert.be/simplescreenrecorder
Group:          System/X11/Utilities
Source:         https://github.com/MaartenBaert/ssr/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(QtCore) >= 4.8
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
# Fix build on => 12.3
%if 0%{?suse_version} > 1220
BuildRequires:  libjpeg8-devel
%endif
%ifarch %ix86 x86_64
Recommends:     libssr-glinject
%if %{_lib} == "lib64"
Recommends:     libssr-glinject-32bit
%endif
%endif

%description
SimpleScreenRecorder is a Linux program that was created to record programs
and games.

The original goal was to create a program that was just really simple to
use, the result is actually a pretty powerful program. It's 'simple' in
the sense that it's easier to use than ffmpeg/avconv or VLC, because it
has a straightforward user interface.

Features:
 * Graphical user interface (Qt-based).
 * Faster than VLC and ffmpeg/avconv.
 * Records the entire screen or part of it, or records OpenGL applications
   directly (similar to Fraps on Windows).
 * Synchronizes audio and video properly (a common issue with VLC and
   ffmpeg/avconv).
 * Reduces the video frame rate if your computer is too slow (rather than
   using up all your RAM like VLC does).
 * Fully multithreaded: small delays in any of the components will never
   block the other components, resulting is smoother video and better
   performance on computers with multiple processors.
 * Pause and resume recording at any time (either by clicking a button or by
   pressing a hotkey).
 * Shows statistics during recording (file size, bit rate, total recording
   time, actual frame rate, ...).
 * Can show a preview during recording, so you don't waste time recording
   something only to figure out afterwards that some setting was wrong.
 * Uses libav/ffmpeg libraries for encoding, so it supports many different
   codecs and file formats (adding more is trivial).
 * Sensible default settings: no need to change anything if you don't want to.
 * Tooltips for almost everything: no need to read the documentation to find
   out what something does.


%ifarch %ix86 x86_64
%package -n libssr-glinject
License:        MIT
Summary:        A feature-rich screen recorder library
Group:          System/Libraries
%description -n libssr-glinject
This package provides SimpleScreenRecorder's optional library.
%endif


%prep
%setup -q -n ssr-%{version}


%build
%ifarch %ix86 x86_64
%configure
%else
%configure \
           --disable-x86-asm \
           --disable-glinjectlib
%endif
make %{?_smp_mflags}


%install
%make_install
%suse_update_desktop_file %{name}


%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun


%files
%defattr(-,root,root)
%doc COPYING *.txt *.md data/resources/about.htm
%{_bindir}/%{name}
%{_bindir}/ssr-glinject
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/%{name}


%ifarch %ix86 x86_64
%files -n libssr-glinject
%defattr(-,root,root)
%{_libdir}/libssr-glinject.*
%endif

%changelog
