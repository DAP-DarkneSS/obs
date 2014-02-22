#
# spec file for package audacity
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
%bcond_with twolame

Name:           audacity
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4.0
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(vamp-hostsdk)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
# This would require to patch our portaudio package with "PortMixer"... an extra API that never got integrated in PortAudio.
#BuildRequires:  portaudio-devel
%if %{with ffmpeg}
BuildRequires:  libffmpeg_oldabi-devel
%endif
%if %{with mad}
BuildRequires:  pkgconfig(mad)
%endif
%if %{with twolame}
BuildRequires:  pkgconfig(twolame)
%endif
Version:        2.0.4
Release:        0
Summary:        A Free, Cross-Platform Digital Audio Editor
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Url:            http://audacity.sourceforge.net/
Source0:        http://audacity.googlecode.com/files/audacity-minsrc-%{version}.tar.xz
Source1:        audacity-license-nyquist
# PATCH-FIX-OPENSUSE audacity-no_buildstamp.patch reddwarf@opensuse.org -- this patch removes the buildstamp
Patch0:         audacity-no_buildstamp.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends:     libmp3lame0
Recommends:     libavformat52
Recommends:     libavcodec52
Recommends:     libavutil50

%description
Audacity is a program that manipulates digital audio wave forms. In
addition to recording sounds directly from within the program, it
imports many sound file formats, including WAV, AIFF, AU, IRCAM, MP,
and Ogg Vorbis.  With Audacity, you can edit wave data larger than the
physical memory size of your computer.

%prep
%setup -q -n audacity-src-%{version}
%patch0
cp %{SOURCE1} LICENSE_NYQUIST.txt
# Make sure we use the system versions
rm -r lib-src/libvamp/
%if %{with ffmpeg}
rm -r lib-src/ffmpeg/
%endif

%build
%configure --docdir=%{_defaultdocdir}/audacity/ \
%ifnarch %ix86 x86_64
  --disable-sse
%endif

make %{?_smp_mflags}

%install
%make_install
# email wrote to feedback@audacityteam.org
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/
mv %{buildroot}%{_datadir}/pixmaps/gnome-mime-application-x-audacity-project.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-audacity-project.xpm
rm -r %{buildroot}%{_datadir}/pixmaps
%find_lang %{name}

%post
%icon_theme_cache_post
%mime_database_post
%desktop_database_post

%postun
%desktop_database_postun
%mime_database_postun
%icon_theme_cache_postun

%files -f %{name}.lang
%defattr(-,root,root)
%doc LICENSE.txt README.txt LICENSE_NYQUIST.txt
%{_defaultdocdir}/audacity/
%{_mandir}/man1/audacity.1*
%{_bindir}/audacity
%{_datadir}/audacity/
%{_datadir}/applications/audacity.desktop
%{_datadir}/mime/packages/audacity.xml
%{_datadir}/icons/hicolor/*/apps/audacity.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-audacity-project.*

%changelog
