#
# spec file for package libvmime
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


Name:           libvmime
%define lname	libvmime-0_9_2-2
%define majver	0.9.2
Summary:        Library for working with MIME messages and IMAP/POP/SMTP
License:        GPL-3.0+
Group:          Development/Libraries/C and C++
Version:        0.9.2
Release:        0
Url:            http://vmime.org/

#Git-Clone:	git://github.com/kisli/vmime
#Git-Web:	https://github.com/kisli/vmime
#Snapshot:	v0.9.1-432-g674c369
#Source:	http://downloads.sf.net/vmime/%name-%version.tar.bz2
Source:         vmime-%{version}.tar.xz
Patch1:         libvmime-nodatetime.diff
Patch2:         libvmime-sotag.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ImageMagick
%if 0%{?suse_version} < 1310
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake >= 2.8.3
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  inkscape
BuildRequires:  libgnutls-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  postfix
%if 0%{?suse_version} >= 1130
%define with_pdf 1
%if 0%{?suse_version} < 1300
BuildRequires:  texlive-bin-latex
%endif
BuildRequires:  texlive-latex
%if 0%{?suse_version} >= 1230
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(fancyheadings.sty)
BuildRequires:  tex(pcrr7t.tfm)
BuildRequires:  tex(ucs.sty)
%endif
%endif
BuildRequires:  xz

%description
VMime is a powerful C++ class library for working with MIME messages
and Internet messaging services like IMAP, POP or SMTP.

With VMime you can parse, generate and modify messages, and also
connect to store and transport services to receive or send messages
over the Internet. The library offers all the features to build a
complete mail client.

%package -n %lname
Summary:        Library for working with MIME messages and IMAP/POP/SMTP
Group:          System/Libraries

%description -n %lname
VMime is a powerful C++ class library for working with MIME messages
and Internet messaging services like IMAP, POP or SMTP.

With VMime you can parse, generate and modify messages, and also
connect to store and transport services to receive or send messages
over the Internet. The library offers all the features to build a
complete mail client.

%package devel
Summary:        Library for working with MIME messages and IMAP/POP/SMTP
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
VMime is a powerful C++ class library for working with MIME messages
and Internet messaging services like IMAP, POP or SMTP.

With VMime you can parse, generate and modify messages, and also
connect to store and transport services to receive or send messages
over the Internet. The library offers all the features to build a
complete mail client.

%prep
%setup -qn vmime-%{version}
%patch -P 1 -P 2 -p1

%build
%if 0%{?with_pdf}
pushd doc/book/
make book_pdf
popd
%endif

cf="%optflags -DVMIME_ALWAYS_GENERATE_7BIT_PARAMETER=1"
# sendmail's awesome location.
export PATH="$PATH:/usr/sbin";
cmake . \
	-DVMIME_BUILD_SAMPLES:BOOL=OFF \
	-DVMIME_HAVE_SASL_SUPPORT:BOOL=ON \
	-DVMIME_HAVE_TLS_SUPPORT:BOOL=ON \
	-DVMIME_BUILD_STATIC_LIBRARY:BOOL=OFF \
	-DCMAKE_RELEASE_TYPE:STRING="RelWithDebInfo" \
	-DCMAKE_INSTALL_PREFIX:PATH="%_prefix" \
	-DCMAKE_CXX_FLAGS_DEBUG:STRING="-g" \
%if 0%{?suse_version} >= 1310
	-DCMAKE_CXX_FLAGS:STRING="$cf -std=gnu++11" \
%else
	-DCMAKE_CXX_FLAGS:STRING="$cf" \
%endif
	-DCMAKE_C_FLAGS:STRING="$cf"
make %{?_smp_mflags} VERBOSE=1

%install
b="%buildroot";
%if 0%{?with_pdf}
mkdir -p "$b/%_docdir/%name"
cp -a doc/book/book.pdf "$b/%_docdir/%name/"
%endif
make install DESTDIR="$b"
ln -s libvmime-%{majver}.so "$b/%_libdir/libvmime.so"
find "$b" -type f -name "*.la" -delete;

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc COPYING
%_libdir/%name-%{majver}.so.2*

%files devel
%defattr(-,root,root)
%_includedir/vmime
%_libdir/libvmime-%{majver}.so
%_libdir/libvmime.so
%_libdir/pkgconfig/*.pc
%if 0%{?with_pdf}
%_docdir/%name
%endif

%changelog
