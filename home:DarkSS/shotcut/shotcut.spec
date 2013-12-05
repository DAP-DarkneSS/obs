#
# spec file for package shotcut
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


Name:           shotcut
Version:        131205
Release:        0
Summary:        A free, open source, cross-platform video editor
License:        GPL-3.0+
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://www.shotcut.org/
Source:         http://d1av856udzjaks.cloudfront.net/shotcut/shotcut-src-%{version}.tar.bz2

BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(mlt++)
BuildRequires:  pkgconfig(mlt-framework)


%description
These are all currently implemented features:
 * supports oodles of audio and video formats and codecs;
 * supports many image formats as image sequences;
 * no import required - native editing;
 * frame-accurate seeking for many formats;
 * multi-format timeline;
 * screen capture (Linux only) including background capture;
 * webcam capture (Linux only);
 * audio capture (Linux only; PulseAudio, JACK, or ALSA);
 * network stream playback (HTTP, HLS, RTMP, RTSP, MMS, UDP);
 * frei0r video generator plugins (e.g. color bars and plasma);
 * Blackmagic Design SDI and HDMI for input and preview monitoring;
 * JACK transport sync;
 * deinterlacing;
 * detailed media properties panel;
 * recent files panel with search;
 * drag-n-drop files from file manager;
 * save and load trimmed clip as MLT XML file;
 * load and play complex MLT XML file as a clip;
 * audio signal level meter;
 * volume control;
 * scrubbing and transport control;
 * flexible UI through dock-able panels;
 * encode/transcode to a variety of formats and codecs;
 * capture (record);
 * stream (encode to IP) files and any capture source;
 * batch encoding with job control;
 * MLT XML playlists;
 * unlimited undo and redo for playlist edits;
 * connect to Melted servers over MVCP TCP protocol;
 * control the transport playback of Melted units;
 * edit Melted playlists including support for undo/redo;
 * OpenGL GPU-based image processing;
 * multi-core parallel image processing when not using GPU;
 * video filters;
 * audio filters;
 * 3-way color wheels for color correction and grading;
 * eye dropper tool to pick neutral color for white balancing;
 * HTML5 (sans audio and video) as video source and filters;
 * Leap Motion for jog/shuttle control;
 * DeckLink SDI keyer output - internal or external;
 * UI themes/skins: native-OS look and custom dark and light;
 * control video zoom in the player.


%prep
%setup -q -n src/shotcut


%build
qmake-qt5 \
          QMAKE_STRIP="" \
          PREFIX=%{buildroot}%{_prefix} \
          QMAKE_CFLAGS+="%{optflags}" \
          QMAKE_CXXFLAGS+="%{optflags}"

make %{?_smp_mflags}


%install
%make_install


%files
%defattr(-,root,root)
%{_bindir}/%{name}


%changelog
