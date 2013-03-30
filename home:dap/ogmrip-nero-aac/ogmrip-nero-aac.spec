# vim: set ts=4 sw=4 et:
# Copyright (c) 2008-2009 oc2pus
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to https://bugs.links2linux.org

%ifnarch x86_64
%define _with_nero				1
%else
%define _with_nero				1
%endif
%define _nero_aac_ver 			1.5.1
%define _ogmrip_nero_aac_ver	0.5

Summary:        OGMRip plugin which adds support for Nero-AAC audio codec
Name:           ogmrip-nero-aac
Version:        %{_ogmrip_nero_aac_ver}
Release:        0.pm.1
Source:         http://surfnet.dl.sourceforge.net/project/ogmrip/ogmrip-nero-aac/%{version}/ogmrip-nero-aac-%{version}.tar.gz
%if "%{_with_nero}" == "1"
Source1:        http://ftp6.nero.com/tools/NeroAACCodec-%{_nero_aac_ver}.zip
%endif
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://ogmrip.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  dos2unix
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libdvdread-devel
BuildRequires:  libogmrip-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
Requires:       MPlayer
%if "%{_with_nero}" == "1"
Requires:       nero-aac >= %{_nero_aac_ver}
%endif
Requires:       ogmrip
BuildRequires:  MPlayer

%if "%{_with_nero}" == "1"
NoSource:       1
%endif

%description
ogmrip-nero-aac is a plugin which adds support for Nero-AAC
audio codec.


%lang_package

%if "%{_with_nero}" == "1"
%package -n nero-aac
Summary:        Nero aac encoder/decoder
Group:          Productivity/Multimedia/Video/Editors and Convertors
Version:        %{_nero_aac_ver}
License:        SUSE-NonFree

%description -n nero-aac
Nero AAC reference quality MPEG-4 and 3GPP audio codec

* Compression ratios ranging from Ultra High (58 CDs fit on one!)
  to High-End Audio (2.5:1), for absolutely perfect audiophile
  encodings
* Crystal-clear, award-winning sound quality at every compression
  ratio and bit rate!
* Support for embedded album art including covers, booklets, and
  lyrics
* Store an entire audio album in a single .mp4 file with all the
  features of an Audio CD embedded inside, but at a fraction of the
  space!
* Reference quality MPEG-4 audio codec
* Fully compatible with the latest version of the state-of-the-art
  MPEG-4 audio standard (LC-AAC, HE-AAC and HE-AAC v2)

Nero AG licenses you to use this software package for personal
non-commercial and/or technology-evaluation purposes.

This License does not provide any rights to reproduce and/or
distribute this software package in whole or in any part.

A written license agreement with Nero AG is needed for any Commercial
use of this software package, including, but not limited to,
exploitation of products, which are incorporating and/or using, in
whole or in part, executables provided in this software package.

Please contact Nero AG for licensing guidance.
%endif

%prep
%setup -q -n %{name}-%{_ogmrip_nero_aac_ver}

%if "%{_with_nero}" == "1"
%__unzip -q %{SOURCE1}
dos2unix -q {} ';' *.txt
%endif

%build
%configure \
    --enable-static=no
%__make %{?_smp_flags}

%install
%makeinstall \
    audio_codecsdir=%{_libdir}/ogmrip/audio-plugins

%if "%{_with_nero}" == "1"
%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 linux/neroAac* \
    %{buildroot}%{_bindir}
%endif

%__rm %{buildroot}%{_libdir}/ogmrip/audio-plugins/*.la

%find_lang %{name}

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%dir %{_libdir}/ogmrip
%dir %{_libdir}/ogmrip/audio-plugins
%{_libdir}/ogmrip/audio-plugins/libogmrip-nero-aac.so

%if "%{_with_nero}" == "1"
%files -n nero-aac
%defattr(-,root,root)
%doc *.txt
%{_bindir}/neroAac*
%endif

%files lang -f %{name}.lang

%changelog
