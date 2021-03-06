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
Version:        1.7.5
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
Recommends:     nero-aac
Recommends:     opus
Recommends:     python-eyeD3
Recommends:     vorbis-tools
Recommends:     vorbisgain
Recommends:     wavegain
Recommends:     wavpack
Recommends:     wget
Recommends:     wine

Requires:       bash
Requires:       bc
Requires:       findutils
Requires:       procps
Requires:       sed
Requires:       sox
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
install -m 0755 %{name} APEv2 %{buildroot}%{_bindir}
install -D %{name}rc %{buildroot}%{_sysconfdir}/%{name}rc

%files
%defattr(-,root,root)
%doc LICENSE* CHANGES README
%{_bindir}/%{name}
%{_bindir}/APEv2
%{_sysconfdir}/%{name}rc

%changelog
