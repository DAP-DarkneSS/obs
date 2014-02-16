#
# spec file for package cinelerra
#
# Copyright (c) Leon Freitag (leon@links2linux.de).
# Copyright (c) 2013 Mariusz Fik <fisiu@opensuse.org>.
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

Name:           cinelerra
Version:        2.2cv20120923
Release:        0
License:        GPL-2.0
Summary:        A non linear video editor and effects processor
Url:            http://cvs.cinelerra.org
Group:          Productivity/Multimedia/Video/Editors and Convertors
Source0:        %{name}-%{version}.tar.bz2
# TODO Rewrite BuildRequires to pkgconfig(foo) style
BuildRequires:  IlmBase-devel
BuildRequires:  Mesa-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs-devel
BuildRequires:  fftw3-devel
BuildRequires:  flac-devel
BuildRequires:  fltk-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
%if 0%{?suse_version} >= 1230
BuildRequires:  glu-devel
%endif
%if 0%{?suse_version} == 1220
BuildRequires:  Mesa-libGLU-devel
%endif
BuildRequires:  liba52dec-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libdv-devel
BuildRequires:  libfaac-devel
BuildRequires:  libfaad-devel
BuildRequires:  libffmpeg_oldabi-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmjpegutils-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  libmpeg3-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libsndfile
BuildRequires:  libsndfile-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libx264-devel
BuildRequires:  nasm
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-devel
BuildRequires:  yasm
Requires:       mjpegtools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

#disable the code checks, I'm not going to mess with the Cinelerra code, although the warnings seem strange.
BuildRequires:  -post-build-checks

%description
Heroine Virtual Ltd. presents an advanced content creation system for Linux. 
Cinelerra takes what normally is a boring server - studied in computer science 
classrooms, hidden in back offices - and turns it into a 50,000 watt 
flamethrower of multimedia editing.
That's right kids. Unlike most of the Linux solutions out there, Cinelerra 
requires no emulation of proprietary operating systems, no commercial add-ons, 
no banner advertizements, no corporate dependencies, no terrorists, just a 
boring old Linux box.
Cinelerra does primarily 3 main things: capturing, compositing, and editing 
audio and video with sample level accuracy. It's a seamless integration of 
audio, video, and still photos rarely experienced on a web server.
If you want to make movies, you just want to defy the establishment, you want 
the same kind of compositing and editing suite that the big boys use, on the 
world's most efficient UNIX operating system, it's time for Cinelerra.

The version you'll find in this package is the cinelerra.org community version.

%package devel
Summary:        Cinelerra header files and development libraries
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
%description devel
Cinelerra files needed for compiling stuff

%{lang_package}

%prep
%setup -q

%build
./autogen.sh
CXXFLAGS="-O3 -pipe -D__STDC_CONSTANT_MACROS"
%configure \
    --with-plugindir=%{_libdir}/%{name} \
    --with-buildinfo=cust/Packman\ build \
    --with-external-ffmpeg \
    --enable-opengl

make %{?_smp_mflags}

%install
%makeinstall
# rename the mpeg3 utils so they can be installed alongside SuSE native versions
pushd %{buildroot}/%{_bindir}
mv mpeg3toc mpeg3toc.hv
mv mpeg3cat mpeg3cat.hv
mv mpeg3dump mpeg3dump.hv
popd

%suse_update_desktop_file cinelerra -r Multimedia AudioVideoEditing
%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc
%{_bindir}/cinelerra
%{_bindir}/mplexlo
%{_bindir}/mpeg3dump.hv
%{_bindir}/mpeg3toc.hv
%{_bindir}/mpeg3cat.hv
%{_libdir}/cinelerra/*
%{_libdir}/libguicast.so.*
%{_libdir}/libmpeg3hv*.so.*
%{_libdir}/libquicktimehv*.so.*
%{_datadir}/applications/cinelerra.desktop
%{_datadir}/pixmaps/cinelerra.xpm

%files devel
%defattr(-,root,root)
%{_libdir}/libmpeg3hv.so
%{_libdir}/libmpeg3hv.la
%{_libdir}/libquicktimehv.so
%{_libdir}/libquicktimehv.la
%{_libdir}/libguicast.so
%{_libdir}/libguicast.la
%{_includedir}/*

%files lang -f %{name}.lang
%defattr(-,root,root)

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
