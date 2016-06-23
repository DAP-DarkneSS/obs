#
# spec file for package fbreader
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


%define			zlui_soname 0_99
%define			zlib_suffix 0_99_4
Name:           fbreader
Version:        0.99.4
Release:        0
Summary:        E-book reader
License:        GPL-2.0+
Group:          Productivity/Other
Url:            http://www.fbreader.org/
Source0:        %{name}-sources-%{version}.tgz
Source1:        FBReader.desktop
Source2:        README.SuSE
Source3:        fbreader.xml
# See https://github.com/geometer/FBReader/issues/232 for more info
Patch0:         FBReader-0.99.4-fix-crash-with-fb2.zip-files.patch
BuildRequires:  enca-devel
BuildRequires:  expat
BuildRequires:  fdupes
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libcurl-devel >= 7.17
BuildRequires:  libexpat-devel
BuildRequires:  libqt4-devel
BuildRequires:  libunibreak-devel
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel
Requires:       libzlui%{zlui_soname} = %{version}
Requires:       zlibrary-%{zlib_suffix} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  update-desktop-files

%description
About FBReader

    A multi-platform ebook reader. FBReader is free (and ad-free).
    Supports popular ebook formats: ePub, fb2, mobi, rtf, html, plain text, and a lot of other formats.
    Provides access to popular network libraries that contain a large set of ebooks. Download books for free or for a fee. Add your own catalog.
    Highly customizable. Choose colors, fonts, page turning animations, dictionaries, bookmarks, etc. to make reading as convenient as you want.


FBReader is an e-book reader for various platforms.
Main features:
    * Supported formats are
          o fb2 e-book format (style attributes are not supported yet).
          o HTML format (tables are not supported).
          o CHM format (tables are not supported).
          o plucker format (tables are not supported).
          o Palmdoc (aportis doc).
          o zTxt (Weasel format).
          o TCR (psion text) format.
          o RTF format (stylesheets and tables are not supported).
          o OEB format (css and tables are not supported).
          o OpenReader format (css and tables are not supported).
          o Non-DRM'ed mobipocket format (tables are not supported).
          o Plain text format.
    * Direct reading from tar, zip, gzip and bzip2 archives.
      (Multiple books in one archive are supported.)
    * Automatic library building.
    * Automatic encoding detection is supported.
    * Automatically generated contents table.
    * Embedded images support.
    * Footnotes/hyperlinks support.
    * Position indicator.
    * Keeps the last open book and the last read positions for all opened
      books between runs.
    * List of last opened books.
    * Automatic hyphenations. Liang's algorithm is used. The same algorithm is
      used in TeX, and TeX hyphenation patterns are used in FBReader. Patterns
      for Czech, English, Esperanto, French, German and Russian are included
      in the current version.
    * Text search.
    * Full-screen mode.
    * Screen rotation by 90, 180 and 270 degrees.

%package -n     zlibrary-%{zlib_suffix}
Summary:        Cross-platform GUI library
Group:          Development/Libraries/C and C++
Requires:       zlibrary-ui = %{version}

%description -n zlibrary-%{zlib_suffix}
ZLibrary is a cross-platform library to build applications running on
desktop Linux, Windows, and different Linux-based PDAs.

%package -n     zlibrary-devel
Summary:        Development files for zlibrary
Group:          Development/Libraries/C and C++
Requires:       zlibrary = %{version}

%description -n zlibrary-devel
This package contains the libraries amd header files that are needed
for writing applications with Zlibrary.

%package -n     libzlui%{zlui_soname}
Summary:        Qt4 interface module for ZLibrary
Group:          Development/Libraries/C and C++
Provides:       zlibrary-ui = %{version}

%description -n libzlui%{zlui_soname}
This package provides a Qt4-based UI for ZLibrary.

%prep
%setup -q
cp %{SOURCE2} .
%patch0 -p1

%build
make %{?_smp_mflags} -C zlibrary/core TARGET_ARCH=desktop LIBDIR=%{_libdir} UI_TYPE=dummy
#TARGET_STATUS=debug
make %{?_smp_mflags} -C zlibrary/text TARGET_ARCH=desktop LIBDIR=%{_libdir} UI_TYPE=dummy
make %{?_smp_mflags} -C zlibrary/ui   TARGET_ARCH=desktop LIBDIR=%{_libdir} UI_TYPE=qt4
make %{?_smp_mflags} -C fbreader      TARGET_ARCH=desktop LIBDIR=%{_libdir} UI_TYPE=dummy

%install
make -C zlibrary/core do_install do_install_dev DESTDIR=%{buildroot} TARGET_ARCH=desktop LIBDIR=%{_libdir} UI_TYPE=dummy
make -C zlibrary/text do_install do_install_dev DESTDIR=%{buildroot} TARGET_ARCH=desktop LIBDIR=%{_libdir} UI_TYPE=dummy
make -C zlibrary/ui              do_install     DESTDIR=%{buildroot} TARGET_ARCH=desktop LIBDIR=%{_libdir} UI_TYPE=qt4
make -C fbreader                 do_install     DESTDIR=%{buildroot} TARGET_ARCH=desktop                   UI_TYPE=dummy

# desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/FBReader.desktop

# mime type
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -m644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/fbreader.xml

# man page
mkdir -p %{buildroot}%{_mandir}/man1
install -m644 fbreader/desktop/FBReader.1 %{buildroot}%{_mandir}/man1

%fdupes -s %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%post   -n zlibrary-%{zlib_suffix} -p /sbin/ldconfig

%postun -n zlibrary-%{zlib_suffix} -p /sbin/ldconfig

%post   -n libzlui%{zlui_soname} -p /sbin/ldconfig

%postun -n libzlui%{zlui_soname} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc fbreader/LICENSE README.SuSE
%{_bindir}/FBReader
%{_datadir}/FBReader
%{_datadir}/applications/FBReader.desktop
%{_datadir}/mime/packages/fbreader.xml
%{_datadir}/pixmaps/FBReader
%{_datadir}/pixmaps/FBReader.png
%{_mandir}/man1/FBReader.1.gz

%files -n zlibrary-%{zlib_suffix}
%defattr(-,root,root,-)
%doc fbreader/LICENSE
%{_libdir}/libzlcore.so.*
%{_libdir}/libzltext.so.*
%dir %{_datadir}/zlibrary
%{_datadir}/zlibrary
%exclude %{_datadir}/zlibrary/keynames-*.xml

%files -n zlibrary-devel
%defattr(-,root,root,-)
%dir %{_includedir}/zlibrary
%{_includedir}/zlibrary/*
%{_libdir}/libzlcore.so
%{_libdir}/libzltext.so
%{_libdir}/libzlui.so

%files -n libzlui%{zlui_soname}
%defattr(-,root,root,-)
%{_datadir}/zlibrary/keynames-qt4.xml
%{_libdir}/libzlui.so.*

%changelog
