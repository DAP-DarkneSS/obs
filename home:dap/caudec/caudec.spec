#
# spec file for package caudec
#
# Copyright (c) 2012-2013 Guillaume (source),
# (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# https://bugs.links2linux.org/ or
# http://caudec.outpost.fr/redirect/bugReport
#

Name:           caudec
Version:        1.6.2
Release:        0
License:        GPL-3.0+
Summary:        A multi-process audio transcoder
Url:            http://caudec.outpost.fr/
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Source:         http://caudec.outpost.fr/downloads/caudec-%{version}.tar.gz

BuildArch:      noarch

BuildRoot:      %{_tmppath}/build-%{name}-%{version}

Recommends:     apetag
Recommends:     cksfv
Recommends:     flac
Recommends:     ffmpeg
Recommends:     gawk
Recommends:     mac
Recommends:     mp3gain
Recommends:     opus
Recommends:     python-eyeD3
Recommends:     sox
Recommends:     vorbis-tools
Recommends:     vorbisgain
Recommends:     wavpack
Recommends:     wget
Recommends:     wine

Requires:       bash
Requires:       bc
Requires:       coreutils
Requires:       findutils
Requires:       grep
Requires:       procps
Requires:       sed
Requires:       shntool
Requires:       util-linux

%description
Caudec is a BASH script for GNU/Linux that transcodes audio files from one
format (codec) to another. It leverages multi-core CPUs with lots of RAM by
using a ramdisk, and running multiple processes concurrently (one per file
and per codec).

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} %{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
%{__install} %{name}rc %{buildroot}%{_sysconfdir}

%files
%defattr(-,root,root)
%doc LICENSE CHANGES README
%{_bindir}/%{name}
%{_sysconfdir}/%{name}rc

%changelog
