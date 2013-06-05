#
# Please submit bugfixes or comments via https://bugs.links2linux.org/
#

%define _libtag_ver %(version="`rpm -q --qf '%{VERSION}' libtag-devel`"; echo "$version")

Name:           xbmc
Version:        12.2
Release:        0
License:        GPL-2.0+ and GPL-3.0+
Summary:        XBMC Media center
Url:            http://www.xbmc.org/
Group:          Productivity/Multimedia/Video/Players
Source0:        http://mirrors.xbmc.org/releases/source/xbmc-%{version}.tar.gz
Source1:        https://github.com/opdenkamp/xbmc-pvr-addons/archive/frodo.zip
# PATCH-FIX-UPSTREAM xbmc-12.2-subtitles.patch -- already merged in git rev
Patch0:         xbmc-12.2-subtitles.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    ppc64

%if 0%{?suse_version} < 1140
BuildRequires:  hal-devel
%endif
%if 0%{?fedora} >= 14
BuildRequires:  gettext-autopoint
%else
BuildRequires:  gettext
%endif

BuildRequires:  -post-build-checks
BuildRequires:  avahi-devel
BuildRequires:  boost-devel
BuildRequires:  ccache
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  enca-devel
BuildRequires:  fdupes
BuildRequires:  ffmpeg-devel
BuildRequires:  flac-devel
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  fribidi-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glibc-devel
BuildRequires:  gperf
BuildRequires:  java
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libass-devel >= 0.9.7
BuildRequires:  libbluray-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcdio-devel
BuildRequires:  libcrystalhd-devel
BuildRequires:  libdca-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libexpat-devel
BuildRequires:  libfaac-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libhdhomerun-devel
BuildRequires:  libjasper-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmad-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpeg2-devel
BuildRequires:  libnfs-devel
BuildRequires:  libogg-devel
BuildRequires:  libpcrecpp0
BuildRequires:  libplist-devel
BuildRequires:  libpng-devel
BuildRequires:  libpulse-devel
BuildRequires:  librtmp-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtag-devel >= 1.8
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libyajl-devel
BuildRequires:  lzo-devel
BuildRequires:  mysql-devel
BuildRequires:  nasm
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  sqlite-devel
BuildRequires:  swig
BuildRequires:  tinyxml-devel
BuildRequires:  unzip
BuildRequires:  xorg-x11-devel
BuildRequires:  yasm
BuildRequires:  zip
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glib-2.0)
## xbmc needs the same libtag version which was used to build against
Requires:       libtag1 = %{_libtag_ver}

%description
XBMC media center is a free cross-platform media-player jukebox and
entertainment hub.  XBMC can play a spectrum of of multimedia formats,
and featuring playlist, audio visualizations, slideshow, and weather
forecast functions, together third-party plugins.

%package devel
Summary:        XBMC Media center devel files
Group:          Development/Languages/C and C++
Requires:       %{name}
BuildArch:      noarch

%description devel
Development files for the XBMC media Center

%prep
%setup -q
%patch0 -p1
unzip -q %{S:1}
mv xbmc-pvr-addons-frodo pvr-addons
pushd pvr-addons
./bootstrap
popd
chmod +x bootstrap
./bootstrap

%build
./configure \
--prefix=%{_prefix} --bindir=%{_bindir} --includedir=%{_includedir} \
--libdir=%{_libdir} --datadir=%{_datadir} \
--enable-goom \
--enable-libusb \
--enable-airplay \
--enable-external-libraries \
--enable-external-ffmpeg \
--enable-vaapi \
--enable-libbluray \
--disable-debug \
CPPFLAGS="-I/usr/include/ffmpeg" \
CFLAGS="%{optflags} -fPIC -I/usr/include/ffmpeg -D__STDC_CONSTANT_MACROS" \
CXXFLAGS="%{optflags} -fPIC -I/usr/include/ffmpeg -D__STDC_CONSTANT_MACROS" \
LDFLAGS="-fPIC" \
LIBS="-L%{_libdir}/mysql -lhdhomerun $LIBS" \
ASFLAGS=-fPIC

make %{?_smp_mflags} VERBOSE=1

%install

rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# remove the doc files from unversioned /usr/share/doc/xbmc, they should be in versioned docdir
rm -r %{buildroot}/%{_datadir}/doc/

# copy manpages
install -m 644 -D docs/manpages/xbmc-standalone.1 %{buildroot}%{_mandir}/man1/xbmc-standalone.1
install -m 644 -D docs/manpages/xbmc.bin.1 %{buildroot}%{_mandir}/man1/xbmc.1

desktop-file-install \
 --dir=%{buildroot}%{_datadir}/applications \
 %{buildroot}%{_datadir}/applications/xbmc.desktop

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc copying.txt  LICENSE.GPL docs/README.linux
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%{_libdir}/xbmc
#%%{_datadir}/xbmc
%{_datadir}/xsessions/XBMC.desktop
%{_datadir}/applications/xbmc.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_mandir}/man1/xbmc-standalone.1.gz
%{_mandir}/man1/xbmc.1.gz

%{_datadir}/xbmc/FEH.py
%{_datadir}/xbmc/addons/metadata.album.universal/*
%{_datadir}/xbmc/addons/metadata.artists.universal/*
%{_datadir}/xbmc/addons/metadata.common.allmusic.com/*
%{_datadir}/xbmc/addons/metadata.common.amazon.de/*
%{_datadir}/xbmc/addons/metadata.common.fanart.tv/*
%{_datadir}/xbmc/addons/metadata.common.hdtrailers.net/*
%{_datadir}/xbmc/addons/metadata.common.htbackdrops.com/*
%{_datadir}/xbmc/addons/metadata.common.imdb.com/*
%{_datadir}/xbmc/addons/metadata.common.last.fm/*
%{_datadir}/xbmc/addons/metadata.common.musicbrainz.org/*
%{_datadir}/xbmc/addons/metadata.common.theaudiodb.com/*
%{_datadir}/xbmc/addons/metadata.common.themoviedb.org/*
%{_datadir}/xbmc/addons/metadata.musicvideos.theaudiodb.com/*
%{_datadir}/xbmc/addons/metadata.themoviedb.org/*
%{_datadir}/xbmc/addons/metadata.tvdb.com/*
%{_datadir}/xbmc/addons/repository.pvr-android.xbmc.org/*
%{_datadir}/xbmc/addons/repository.pvr-ios.xbmc.org/*
%{_datadir}/xbmc/addons/repository.pvr-osx32.xbmc.org/*
%{_datadir}/xbmc/addons/repository.pvr-osx64.xbmc.org/*
%{_datadir}/xbmc/addons/repository.pvr-win32.xbmc.org/*
%{_datadir}/xbmc/addons/repository.xbmc.org/*
%{_datadir}/xbmc/addons/screensaver.rsxs.euphoria/*
%{_datadir}/xbmc/addons/screensaver.rsxs.plasma/*
%{_datadir}/xbmc/addons/screensaver.rsxs.solarwinds/*
%{_datadir}/xbmc/addons/screensaver.xbmc.builtin.black/*
%{_datadir}/xbmc/addons/screensaver.xbmc.builtin.dim/*
%{_datadir}/xbmc/addons/script.module.pil/*
%{_datadir}/xbmc/addons/script.module.pysqlite/*
%{_datadir}/xbmc/addons/script.module.simplejson/*
%{_datadir}/xbmc/addons/skin.confluence/*
%{_datadir}/xbmc/addons/visualization.dxspectrum/*
%{_datadir}/xbmc/addons/visualization.glspectrum/*
%{_datadir}/xbmc/addons/visualization.goom/*
%{_datadir}/xbmc/addons/visualization.milkdrop/*
%{_datadir}/xbmc/addons/visualization.projectm/*
%{_datadir}/xbmc/addons/visualization.waveform/*
%{_datadir}/xbmc/addons/weather.wunderground/*
%{_datadir}/xbmc/addons/webinterface.default/*
%{_datadir}/xbmc/addons/xbmc.addon/*
%{_datadir}/xbmc/addons/xbmc.core/*
%{_datadir}/xbmc/addons/xbmc.gui/*
%{_datadir}/xbmc/addons/xbmc.json/*
%{_datadir}/xbmc/addons/xbmc.metadata/*
%{_datadir}/xbmc/addons/xbmc.pvr/*
%{_datadir}/xbmc/addons/xbmc.python/*
%{_datadir}/xbmc/addons/pvr.argustv/*
%{_datadir}/xbmc/addons/pvr.demo/*
%{_datadir}/xbmc/addons/pvr.dvbviewer/*
%{_datadir}/xbmc/addons/pvr.hts/*
%{_datadir}/xbmc/addons/pvr.mediaportal.tvserver/*
%{_datadir}/xbmc/addons/pvr.nextpvr/*
%{_datadir}/xbmc/addons/pvr.njoy/*
%{_datadir}/xbmc/addons/pvr.vdr.vnsi/*
%{_datadir}/xbmc/addons/pvr.vuplus/*
%{_datadir}/xbmc/language/*
%{_datadir}/xbmc/media/*
%{_datadir}/xbmc/sounds/*
%{_datadir}/xbmc/system/*
%{_datadir}/xbmc/userdata/*

%files devel
%defattr(-,root,root)
%{_datadir}/xbmc/addons/library.xbmc.addon/dlfcn-win32.cpp
%{_datadir}/xbmc/addons/library.xbmc.addon/dlfcn-win32.h
%{_datadir}/xbmc/addons/library.xbmc.gui/libXBMC_gui.h
%{_datadir}/xbmc/addons/library.xbmc.addon/libXBMC_addon.h
%{_datadir}/xbmc/addons/library.xbmc.pvr/libXBMC_pvr.h

%changelog
