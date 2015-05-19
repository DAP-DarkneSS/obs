#
# spec file for package allegro
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define allegro_so_nr 5_1
%define allegro_acodec_so_nr 5_1
%define allegro_audio_so_nr 5_1
%define allegro_color_so_nr 5_1
%define allegro_dialog_so_nr 5_1
%define allegro_font_so_nr 5_1
%define allegro_image_so_nr 5_1
%define allegro_main_so_nr 5_1
%define allegro_memfile_so_nr 5_1
%define allegro_physfs_so_nr 5_1
%define allegro_primitives_so_nr 5_1
%define allegro_ttf_so_nr 5_1

%define dot_allegro_so_nr %(echo %{allegro_so_nr} | sed s/_/./)
%define dot_allegro_acodec_so_nr %(echo %{allegro_acodec_so_nr} | sed s/_/./)
%define dot_allegro_audio_so_nr %(echo %{allegro_audio_so_nr} | sed s/_/./)
%define dot_allegro_color_so_nr %(echo %{allegro_color_so_nr} | sed s/_/./)
%define dot_allegro_dialog_so_nr %(echo %{allegro_dialog_so_nr} | sed s/_/./)
%define dot_allegro_font_so_nr %(echo %{allegro_font_so_nr} | sed s/_/./)
%define dot_allegro_image_so_nr %(echo %{allegro_image_so_nr} | sed s/_/./)
%define dot_allegro_main_so_nr %(echo %{allegro_main_so_nr} | sed s/_/./)
%define dot_allegro_memfile_so_nr %(echo %{allegro_memfile_so_nr} | sed s/_/./)
%define dot_allegro_physfs_so_nr %(echo %{allegro_physfs_so_nr} | sed s/_/./)
%define dot_allegro_primitives_so_nr %(echo %{allegro_primitives_so_nr} | sed s/_/./)
%define dot_allegro_ttf_so_nr %(echo %{allegro_primitives_so_nr} | sed s/_/./)

Name:           allegro
Version:        5.1.10
Release:        0
Summary:        A game programming library
License:        Zlib and BSD-3-Clause
Group:          System/Libraries
Url:            http://alleg.sourceforge.net/
Source0:        http://sourceforge.net/projects/alleg/files/allegro-unstable/%{version}/allegro-%{version}.tar.gz
Source9:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libdumb-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libphysfs-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%package -n liballegro%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro%{allegro_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro%{allegro_so_nr}-devel
Summary:        Development files for liballegro
Group:          Development/Libraries/C and C++
Requires:       liballegro%{allegro_so_nr} = %{version}

%description -n liballegro%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro.

%post -n liballegro%{allegro_so_nr} -p /sbin/ldconfig

%postun -n liballegro%{allegro_so_nr} -p /sbin/ldconfig

%files -n liballegro%{allegro_so_nr}
%defattr(0644,root,root,0755)
%doc CHANGES-5.0.txt CONTRIBUTORS.txt LICENSE.txt
%{_libdir}/liballegro.so.%{dot_allegro_so_nr}*
%config(noreplace) %{_sysconfdir}/allegro5rc

%files -n liballegro%{allegro_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro.so
%{_includedir}/allegro5
%exclude %{_includedir}/allegro5/allegro_acodec.h
%exclude %{_includedir}/allegro5/allegro_audio.h
%exclude %{_includedir}/allegro5/allegro_color.h
%exclude %{_includedir}/allegro5/allegro_native_dialog.h
%exclude %{_includedir}/allegro5/allegro_font.h
%exclude %{_includedir}/allegro5/allegro_image.h
%exclude %{_includedir}/allegro5/allegro_memfile.h
%exclude %{_includedir}/allegro5/allegro_physfs.h
%exclude %{_includedir}/allegro5/allegro_primitives.h
%exclude %{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/pkgconfig/allegro-5.pc

%package -n liballegro_acodec%{allegro_acodec_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_acodec%{allegro_acodec_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_acodec%{allegro_acodec_so_nr}-devel
Summary:        Development files for liballegro_acodec
Group:          Development/Libraries/C and C++
Requires:       liballegro_acodec%{allegro_acodec_so_nr} = %{version}

%description -n liballegro_acodec%{allegro_acodec_so_nr}-devel
Development files needed to build applications which use liballegro_acodec.

%post -n liballegro_acodec%{allegro_acodec_so_nr} -p /sbin/ldconfig

%postun -n liballegro_acodec%{allegro_acodec_so_nr} -p /sbin/ldconfig

%files -n liballegro_acodec%{allegro_acodec_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_acodec.so.%{dot_allegro_acodec_so_nr}*

%files -n liballegro_acodec%{allegro_acodec_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_acodec.so
%{_includedir}/allegro5/allegro_acodec.h
%{_libdir}/pkgconfig/allegro_acodec-5.pc

%package -n liballegro_audio%{allegro_audio_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_audio%{allegro_audio_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_audio%{allegro_audio_so_nr}-devel
Summary:        Development files for liballegro_audio
Group:          Development/Libraries/C and C++
Requires:       liballegro_audio%{allegro_audio_so_nr} = %{version}

%description -n liballegro_audio%{allegro_audio_so_nr}-devel
Development files needed to build applications which use liballegro_audio.

%post -n liballegro_audio%{allegro_audio_so_nr} -p /sbin/ldconfig

%postun -n liballegro_audio%{allegro_audio_so_nr} -p /sbin/ldconfig

%files -n liballegro_audio%{allegro_audio_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_audio.so.%{dot_allegro_audio_so_nr}*

%files -n liballegro_audio%{allegro_audio_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_audio.so
%{_includedir}/allegro5/allegro_audio.h
%{_libdir}/pkgconfig/allegro_audio-5.pc

%package -n liballegro_color%{allegro_color_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_color%{allegro_color_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_color%{allegro_color_so_nr}-devel
Summary:        Development files for liballegro_color
Group:          Development/Libraries/C and C++
Requires:       liballegro_color%{allegro_color_so_nr} = %{version}

%description -n liballegro_color%{allegro_color_so_nr}-devel
Development files needed to build applications which use liballegro_color.

%post -n liballegro_color%{allegro_color_so_nr} -p /sbin/ldconfig

%postun -n liballegro_color%{allegro_color_so_nr} -p /sbin/ldconfig

%files -n liballegro_color%{allegro_color_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_color.so.%{dot_allegro_color_so_nr}*

%files -n liballegro_color%{allegro_color_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_color.so
%{_includedir}/allegro5/allegro_color.h
%{_libdir}/pkgconfig/allegro_color-5.pc

%package -n liballegro_dialog%{allegro_dialog_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_dialog%{allegro_dialog_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_dialog%{allegro_dialog_so_nr}-devel
Summary:        Development files for liballegro_dialog
Group:          Development/Libraries/C and C++
Requires:       liballegro_dialog%{allegro_dialog_so_nr} = %{version}

%description -n liballegro_dialog%{allegro_dialog_so_nr}-devel
Development files needed to build applications which use liballegro_dialog.

%post -n liballegro_dialog%{allegro_dialog_so_nr} -p /sbin/ldconfig

%postun -n liballegro_dialog%{allegro_dialog_so_nr} -p /sbin/ldconfig

%files -n liballegro_dialog%{allegro_dialog_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_dialog.so.%{dot_allegro_dialog_so_nr}*

%files -n liballegro_dialog%{allegro_dialog_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_dialog.so
%{_includedir}/allegro5/allegro_native_dialog.h
%{_libdir}/pkgconfig/allegro_dialog-5.pc

%package -n liballegro_font%{allegro_font_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_font%{allegro_font_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_font%{allegro_font_so_nr}-devel
Summary:        Development files for liballegro_font
Group:          Development/Libraries/C and C++
Requires:       liballegro_font%{allegro_font_so_nr} = %{version}

%description -n liballegro_font%{allegro_font_so_nr}-devel
Development files needed to build applications which use liballegro_font.

%post -n liballegro_font%{allegro_font_so_nr} -p /sbin/ldconfig

%postun -n liballegro_font%{allegro_font_so_nr} -p /sbin/ldconfig

%files -n liballegro_font%{allegro_font_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_font.so.%{dot_allegro_font_so_nr}*

%files -n liballegro_font%{allegro_font_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_font.so
%{_includedir}/allegro5/allegro_font.h
%{_libdir}/pkgconfig/allegro_font-5.pc

%package -n liballegro_image%{allegro_image_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_image%{allegro_image_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_image%{allegro_image_so_nr}-devel
Summary:        Development files for liballegro_image
Group:          Development/Libraries/C and C++
Requires:       liballegro_image%{allegro_image_so_nr} = %{version}

%description -n liballegro_image%{allegro_image_so_nr}-devel
Development files needed to build applications which use liballegro_image.

%post -n liballegro_image%{allegro_image_so_nr} -p /sbin/ldconfig

%postun -n liballegro_image%{allegro_image_so_nr} -p /sbin/ldconfig

%files -n liballegro_image%{allegro_image_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_image.so.%{dot_allegro_image_so_nr}*

%files -n liballegro_image%{allegro_image_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_image.so
%{_includedir}/allegro5/allegro_image.h
%{_libdir}/pkgconfig/allegro_image-5.pc

%package -n liballegro_main%{allegro_main_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_main%{allegro_main_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_main%{allegro_main_so_nr}-devel
Summary:        Development files for liballegro_main
Group:          Development/Libraries/C and C++
Requires:       liballegro_main%{allegro_main_so_nr} = %{version}

%description -n liballegro_main%{allegro_main_so_nr}-devel
Development files needed to build applications which use liballegro_main.

%post -n liballegro_main%{allegro_main_so_nr} -p /sbin/ldconfig

%postun -n liballegro_main%{allegro_main_so_nr} -p /sbin/ldconfig

%files -n liballegro_main%{allegro_main_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_main.so.%{dot_allegro_main_so_nr}*

%files -n liballegro_main%{allegro_main_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_main.so
%{_libdir}/pkgconfig/allegro_main-5.pc

%package -n liballegro_memfile%{allegro_memfile_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_memfile%{allegro_memfile_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_memfile%{allegro_memfile_so_nr}-devel
Summary:        Development files for liballegro_memfile
Group:          Development/Libraries/C and C++
Requires:       liballegro_memfile%{allegro_memfile_so_nr} = %{version}

%description -n liballegro_memfile%{allegro_memfile_so_nr}-devel
Development files needed to build applications which use liballegro_memfile.

%post -n liballegro_memfile%{allegro_memfile_so_nr} -p /sbin/ldconfig

%postun -n liballegro_memfile%{allegro_memfile_so_nr} -p /sbin/ldconfig

%files -n liballegro_memfile%{allegro_memfile_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_memfile.so.%{dot_allegro_memfile_so_nr}*

%files -n liballegro_memfile%{allegro_memfile_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_memfile.so
%{_includedir}/allegro5/allegro_memfile.h
%{_libdir}/pkgconfig/allegro_memfile-5.pc

%package -n liballegro_physfs%{allegro_physfs_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_physfs%{allegro_physfs_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_physfs%{allegro_physfs_so_nr}-devel
Summary:        Development files for liballegro_physfs
Group:          Development/Libraries/C and C++
Requires:       liballegro_physfs%{allegro_physfs_so_nr} = %{version}

%description -n liballegro_physfs%{allegro_physfs_so_nr}-devel
Development files needed to build applications which use liballegro_physfs.

%post -n liballegro_physfs%{allegro_physfs_so_nr} -p /sbin/ldconfig

%postun -n liballegro_physfs%{allegro_physfs_so_nr} -p /sbin/ldconfig

%files -n liballegro_physfs%{allegro_physfs_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_physfs.so.%{dot_allegro_physfs_so_nr}*

%files -n liballegro_physfs%{allegro_physfs_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_physfs.so
%{_includedir}/allegro5/allegro_physfs.h
%{_libdir}/pkgconfig/allegro_physfs-5.pc

%package -n liballegro_primitives%{allegro_primitives_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_primitives%{allegro_primitives_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_primitives%{allegro_primitives_so_nr}-devel
Summary:        Development files for liballegro_primitives
Group:          Development/Libraries/C and C++
Requires:       liballegro_primitives%{allegro_primitives_so_nr} = %{version}

%description -n liballegro_primitives%{allegro_primitives_so_nr}-devel
Development files needed to build applications which use liballegro_primitives.

%post -n liballegro_primitives%{allegro_primitives_so_nr} -p /sbin/ldconfig

%postun -n liballegro_primitives%{allegro_primitives_so_nr} -p /sbin/ldconfig

%files -n liballegro_primitives%{allegro_primitives_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_primitives.so.%{dot_allegro_primitives_so_nr}*

%files -n liballegro_primitives%{allegro_primitives_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_primitives.so
%{_includedir}/allegro5/allegro_primitives.h
%{_libdir}/pkgconfig/allegro_primitives-5.pc

%package -n liballegro_ttf%{allegro_ttf_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_ttf%{allegro_ttf_so_nr}
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n liballegro_ttf%{allegro_ttf_so_nr}-devel
Summary:        Development files for liballegro_ttf
Group:          Development/Libraries/C and C++
Requires:       liballegro_ttf%{allegro_ttf_so_nr} = %{version}

%description -n liballegro_ttf%{allegro_ttf_so_nr}-devel
Development files needed to build applications which use liballegro_ttf.

%package -n liballegro-doc
Summary:        Allegro Documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description -n liballegro-doc
Allegro HTML documentation and man pages.

%files -n liballegro-doc
%defattr(0644,root,root,0755)
%{_datadir}/doc/%{name}/
%{_mandir}/man3/*

%prep
%setup -q

%build
mkdir build
cd build
export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
cmake -DCMAKE_SKIP_RPATH=ON \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB_SUFFIX=$(echo %{_lib} | cut -b4-) \
      -DCMAKE_BUILD_TYPE=Release \
      -DWANT_EXAMPLES=NO \
      -DWANT_DEMO=NO ..
make %{?_smp_mflags} VERBOSE=1

%install
cd build
make DESTDIR=%{buildroot} install VERBOSE=1
cd ..
install -D -m 644 allegro5.cfg %{buildroot}%{_sysconfdir}/allegro5rc
install -d -D %{buildroot}%{_mandir}/man3
cp docs/man/*.3 %{buildroot}%{_mandir}/man3
%fdupes -s %{buildroot}%{_mandir}/man3
install -d -D %{buildroot}%{_datadir}/doc/%{name}
cp -r docs/html/refman/* %{buildroot}%{_datadir}/doc/%{name}

%post -n liballegro_ttf%{allegro_ttf_so_nr} -p /sbin/ldconfig

%postun -n liballegro_ttf%{allegro_ttf_so_nr} -p /sbin/ldconfig

%files -n liballegro_ttf%{allegro_ttf_so_nr}
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_ttf.so.%{dot_allegro_ttf_so_nr}*

%files -n liballegro_ttf%{allegro_ttf_so_nr}-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballegro_ttf.so
%{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/pkgconfig/allegro_ttf-5.pc

%changelog
