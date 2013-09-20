#
# spec file for package boost
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


%define ver 1.53.0
%define file_version 1_53_0
%define short_version 1_53
%define lib_appendix 1_53_0

#Only define to 1 to generate the man pages
%define build_docs 0

#Define to 0 to not generate the pdf documentation
%define build_pdf 0
%define package_pdf 1

# Just hardcode build_mpi to 1 as soon as openmpi builds on all
# named architectures.

%ifarch s390 s390x ia64 hppa
%define build_mpi 0
%else
%define build_mpi 1
%endif

# context hasn't been ported to most architectures yet
%ifarch %ix86 x86_64 %arm mips ppc ppc64
%define build_context 1
%else
%define build_context 0
%endif

%ifarch hppa
%define disable_long_double 1
%else
%define disable_long_double 0
%endif

%define boost_libs1 libboost_date_time%{lib_appendix} libboost_filesystem%{lib_appendix} libboost_graph%{lib_appendix}
%define boost_libs2 libboost_iostreams%{lib_appendix} libboost_math%{lib_appendix} libboost_test%{lib_appendix}
%define boost_libs3 libboost_program_options%{lib_appendix} libboost_python%{lib_appendix} libboost_serialization%{lib_appendix}
%define boost_libs4 libboost_signals%{lib_appendix} libboost_system%{lib_appendix} libboost_thread%{lib_appendix}
%define boost_libs5 libboost_wave%{lib_appendix} libboost_regex%{lib_appendix} libboost_regex%{lib_appendix}
%define boost_libs6 libboost_random%{lib_appendix} libboost_chrono%{lib_appendix} libboost_locale%{lib_appendix}
%define boost_libs7 libboost_timer%{lib_appendix}

%define most_libs %boost_libs1 %boost_libs2 %boost_libs3 %boost_libs4 %boost_libs5 %boost_libs6 %boost_libs7

%if %build_mpi
%define all_libs %{most_libs} libboost_mpi%{lib_appendix}
%else
%define all_libs %{most_libs}
%endif

%define debug_package_requires %{all_libs}

Name:           boost
BuildRequires:  boost-jam >= 3.1.19
BuildRequires:  chrpath
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libexpat-devel
BuildRequires:  libicu-devel >= 4.4
BuildRequires:  python-devel
BuildRequires:  xorg-x11-devel
%if %build_mpi
BuildRequires:  openmpi-devel
%endif
%if %build_docs
BuildRequires:  docbook
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt-tools
BuildRequires:  python-devel
BuildRequires:  texlive-latex
%endif
%if 0%suse_version > 1020
BuildRequires:  fdupes
%endif
Url:            http://www.boost.org
Summary:        Boost C++ Libraries
License:        BSL-1.0
Group:          Development/Libraries/C and C++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Version:        1.53.0
Release:        0
Source0:        http://downloads.sourceforge.net/project/boost/boost/1.53.0/%{name}_%{file_version}.tar.bz2
Source1:        boost-rpmlintrc
Source2:        %{name}_%{short_version}_man.tar.bz2
Source3:        %{name}_%{short_version}_pdf.tar.bz2
Source4:        existing_extra_docs
#Source5:        NEWS
Patch1:         boost-thread.patch
Patch2:         boost-no_type_punning.patch
Patch8:         boost-no_segfault_in_Regex_filter.patch
Patch20:        boost-strict_aliasing.patch
Patch50:        boost-use_std_xml_catalog.patch
#PATCH-FIX-UPSTREAM Fix erroneous assembler code for ppc64 [boost#8374]
Patch51:        boost-fix_ppc64_asm.patch
Patch60:        boost-glibc-2.18.patch
Recommends:     %{all_libs}

%define _docdir %{_datadir}/doc/packages/boost-%{version}

%description
Boost provides free peer-reviewed portable C++ source libraries. The
emphasis is on libraries that work well with the C++ Standard Library.
One goal is to establish "existing practice" and provide reference
implementations so that the Boost libraries are suitable for eventual
standardization. Some of the libraries have already been proposed for
inclusion in the C++ Standards Committee's upcoming C++ Standard
Library Technical Report.

Although Boost was begun by members of the C++ Standards Committee
Library Working Group, membership has expanded to include nearly two
thousand members of the C++ community at large.

This package is mainly needed for updating from a prior version, the
dynamic libraries are found in their respective package. For development
using Boost, you also need the boost-devel package. For documentation,
see the boost-doc package.



%package        devel
Summary:        Development package for Boost C++
Group:          Development/Libraries/C and C++
Requires:       %{all_libs}
Requires:       libstdc++-devel

%description    devel
This package contains all that is needed to develop/compile
applications that use the Boost C++ libraries. For documentation see
the documentation packages (html, man or pdf).



%package     -n boost-license%{lib_appendix}
Summary:        Boost License
Group:          Development/Libraries/C and C++
Provides:       boost-license = %{version}-%{release}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description    -n boost-license%{lib_appendix}
This package contains the license boost is provided under.



%package        doc-html
Summary:        HTML documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description    doc-html
This package contains the documentation of the boost dynamic libraries
in HTML format.



%package        doc-man
Summary:        Man documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description    doc-man
This package contains the documentation of the boost dynamic libraries
as man pages.


%if %package_pdf

%package        doc-pdf
Summary:        PDF documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description     doc-pdf
This package contains the documentation of the boost dynamic libraries
in PDF format.
%endif

%package        -n libboost_atomic%{lib_appendix}
Summary:        Run-Time component of boost atomic library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description -n libboost_atomic%{lib_appendix}
Run-Time support for Boost.Atomic, a library that provides atomic data types
and operations on these data types, as well as memory ordering constraints
required for coordinating multiple threads through atomic variables.

%package        -n libboost_context%{lib_appendix}
Summary:        Run-Time component of boost context switching library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description -n libboost_context%{lib_appendix}
Run-Time support for Boost.Context, a foundational library that
provides a sort of cooperative multitasking on a single thread.

%package        -n libboost_date_time%{lib_appendix}
Summary:        Boost::Date.Time Runtime libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description -n libboost_date_time%{lib_appendix}
This package contains the Boost Date.Time runtime libraries.


%package     -n libboost_filesystem%{lib_appendix}
Summary:        Boost::Filesystem Runtime Libraries
Group:          System/Localization
Requires:       boost-license%{lib_appendix}

%description    -n libboost_filesystem%{lib_appendix}
This package contains the Boost::Filesystem libraries.


%package        -n libboost_graph%{lib_appendix}
Summary:        Boost::Graph Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_graph%{lib_appendix}
This package contains the Boost::Graph Runtime libraries.


%package        -n libboost_iostreams%{lib_appendix}
Summary:        Boost::IOStreams Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_iostreams%{lib_appendix}
This package contains the Boost::IOStreams Runtime libraries.


%package        -n libboost_math%{lib_appendix}
Summary:        Boost::Math Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_math%{lib_appendix}
This package contains the Boost::Math Runtime libraries.


%if %build_mpi

%package        -n libboost_mpi%{lib_appendix}
Summary:        Boost::MPI Runtime libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_mpi%{lib_appendix}
This package contains the Boost::MPI Runtime libraries.

%endif

%package        -n libboost_test%{lib_appendix}
Summary:        Boost::Test Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_test%{lib_appendix}
This package contains the Boost::Test runtime libraries.


%package        -n libboost_program_options%{lib_appendix}
Summary:        Boost::ProgramOptions Runtime libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_program_options%{lib_appendix}
This package contains the Boost::ProgramOptions Runtime libraries.


%package        -n libboost_python%{lib_appendix}
Summary:        Boost::Python Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_python%{lib_appendix}
This package contains the Boost::Python Runtime libraries.


%package        -n libboost_serialization%{lib_appendix}
Summary:        Boost::Serialization Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_serialization%{lib_appendix}
This package contains the Boost::Serialization Runtime libraries.


%package        -n libboost_signals%{lib_appendix}
Summary:        Boost::Signals Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_signals%{lib_appendix}
This package contains the Boost::Signals Runtime libraries.


%package        -n libboost_system%{lib_appendix}
Summary:        Boost::System Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_system%{lib_appendix}
This package contains the Boost::System runtime libraries.


%package        -n libboost_thread%{lib_appendix}
Summary:        Boost::Thread Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_thread%{lib_appendix}
This package contains the Boost::Thread runtime libraries.


%package        -n libboost_wave%{lib_appendix}
Summary:        Boost::Wave Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_wave%{lib_appendix}
This package contains the Boost::Wave runtime libraries.


%package        -n libboost_regex%{lib_appendix}
Summary:        The Boost::Regex runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_regex%{lib_appendix}
This package contains the Boost::Regex runtime library.

%package        -n libboost_random%{lib_appendix}
Summary:        The Boost::Random runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_random%{lib_appendix}
This package contains the Boost::Random runtime library.

%package        -n libboost_chrono%{lib_appendix}
Summary:        The Boost::Chrono runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_chrono%{lib_appendix}
This package contains the Boost::Chrono runtime library.

%package        -n libboost_locale%{lib_appendix}
Summary:        The Boost::Locale runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_locale%{lib_appendix}
This package contains the Boost::Locale runtime library.

%package        -n libboost_timer%{lib_appendix}
Summary:        The Boost::Timer runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_timer%{lib_appendix}
This package contains the Boost::Timer runtime library.


%prep
%if %build_docs
%setup -q -n %{name}_%{file_version} -b 3
%else
%setup -q -n %{name}_%{file_version} -a 2 -b 3
%endif
#everything in the tarball has the executable flag set ...
find -type f ! \( -name \*.sh -o -name \*.py -o -name \*.pl \) -exec chmod -x {} +
%patch1
%patch2
%patch8
%patch20
%patch50
%patch51
%patch60 -p1
#stupid build machinery copies .orig files
find . -name \*.orig -exec rm {} +

%build
find . -type f -exec chmod u+w {} +

# Create shared build instructions
cat > .build <<\EOF
# Now build it
J_P=%{jobs}
J_G=$(getconf _NPROCESSORS_ONLN)
[ $J_G -gt 64 ] && J_G=64

if test -z "$JOBS"; then
  JOBS=$J_G
else
  test 1 -gt "$JOBS" && JOBS=1
fi
if test "$JOBS" = 0; then
  JOBS=1
fi

# In case you want more parallel jobs than autobuild grants you
#if [ $J_P -gt $J_I ]; then
#  JOBS=$J_G
#fi

%if %{disable_long_double}
export LONG_DOUBLE_FLAGS="--disable-long-double"
%endif
BJAM_CONFIG="-d2 -j$JOBS -sICU_PATH=%{_prefix}"
PYTHON_VERSION=$(python -c 'import sys; print sys.version[:3]')
PYTHON_FLAGS="--with-python-root=/usr --with-python-version=$PYTHON_VERSION"
export REGEX_FLAGS="--with-icu"
export EXPAT_INCLUDE=/usr/include EXPAT_LIBPATH=%{_libdir}
export PYTHON_FLAGS
LIBRARIES_FLAGS=
%if !%build_context
LIBRARIES_FLAGS+=" --without-context"
%endif
EOF

cat << EOF >user-config.jam
# Boost.Build Configuration

# Compiler configuration
using gcc ;

# Python configuration
using python : ${PYTHON_VERSION} : %{_prefix} ;
EOF

%if %build_docs
cat << EOF >>user-config.jam
using xsltproc ;

using boostbook : /usr/share/xml/docbook/stylesheet/nwalsh/current ;

using doxygen ;
EOF
%endif

%if %build_mpi
cat << EOF >>user-config.jam
using mpi ;
EOF

cat >> .build <<\EOF
# Set PATH, MANPATH and LD_LIBRARY_PATH
source /var/mpi-selector/data/$(rpm --qf "%{NAME}-%{VERSION}" -q openmpi).sh
EOF
%endif

# Read shared build instructions
. ./.build

%{_bindir}/bjam ${BJAM_CONFIG} ${LONG_DOUBLE_FLAGS} ${LIBRARIES_FLAGS} \
	--user-config=user-config.jam \
	cflags="%{optflags}" cxxflags="%{optflags}" stage || \
	(echo "Not all Boost libraries built properly."; exit 1)

%if %build_docs
cd doc
%{_bindir}/bjam ${BJAM_CONFIG} --user-config=../user-config.jam --v2 man
%endif

%install
# Read shared build instructions
. ./.build

%{_bindir}/bjam ${BJAM_CONFIG} ${LONG_DOUBLE_FLAGS} ${LIBRARIES_FLAGS} \
	--user-config=user-config.jam \
	--prefix=%{buildroot}%{_prefix} \
	--exec-prefix=$%{buildroot}%{_prefix} \
	--libdir=%{buildroot}%{_libdir} \
	--includedir=%{buildroot}%{_includedir} \
	install || echo "Not all Boost libraries built properly."

mkdir -p %{buildroot}%{_docdir}

pushd %{buildroot}%{_libdir}
blibs=$(find . -name \*.so.%{version})
echo $blibs | xargs chrpath -d 

for lib in ${blibs}; do
  BASE=$(basename ${lib} .so.%{version})
  SONAME_MT="$BASE-mt.so"
  ln -sf ${lib} $SONAME_MT
done
popd

# install the man pages
rm -rf doc/man/man3/boost::units::operator
mv doc/man/man3/path.3 doc/man/man3/boost::property_tree::path.3
mv doc/man/man3/string.3 doc/man/man3/boost::container::string.3

for sec in 3 7 9; do
    install -d %buildroot/%{_mandir}/man${sec}
done
pushd doc/man
rm -f *.manifest
tar -cf - .| tar -C %{buildroot}/%{_mandir} -xvf -
popd

#install the pdf documentation
install -d %buildroot/%{_docdir}/pdf
install -p -m 644 ../%{name}_%{short_version}_pdf/*.pdf %{buildroot}/%{_docdir}/pdf/

#install doc files
dos2unix libs/ptr_container/doc/tutorial_example.html \
	libs/parameter/doc/html/reference.html \
	libs/parameter/doc/html/index.html \
	libs/iostreams/doc/tree/tree.js \
	libs/graph/doc/lengauer_tarjan_dominator.htm \
	libs/test/test/test_files/errors_handling_test.pattern \
	libs/test/test/test_files/result_report_test.pattern
find . -name \*.htm\* -o -name \*.gif -o -name \*.css -o -name \*.jpg -o -name \*.png -o -name \*.ico | \
	tar --files-from=%{S:4} -cf - --files-from=- | tar -C %{buildroot}%{_docdir} -xf -
rm -rf %{buildroot}%{_docdir}/boost
ln -s /usr/include/boost %{buildroot}%{_docdir}
ln -s ../LICENSE_1_0.txt %{buildroot}%{_docdir}/libs
#Copy the news file.
#cp %%{S:5} %%{buildroot}%%{_docdir}
#only for documentation, doesn't need to be executable
find %{buildroot}%{_docdir} -name \*.py -exec chmod -x {} +
rm -f %{buildroot}%{_libdir}/*.a
#symlink dupes
%if 0%suse_version > 1020
%fdupes %buildroot
%endif

%post -n libboost_atomic%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_context%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_date_time%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_filesystem%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_iostreams%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_test%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_program_options%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_python%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_regex%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_serialization%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_signals%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_thread%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_math%{lib_appendix} -p /sbin/ldconfig 

%if %build_mpi
%post -n libboost_mpi%{lib_appendix} -p /sbin/ldconfig       
%endif

%post -n libboost_graph%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_system%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_wave%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_random%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_chrono%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_locale%{lib_appendix} -p /sbin/ldconfig
%post -n libboost_timer%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_atomic%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_context%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_date_time%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_filesystem%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_iostreams%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_test%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_program_options%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_python%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_regex%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_serialization%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_signals%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_thread%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_math%{lib_appendix} -p /sbin/ldconfig

%if %build_mpi
%postun -n libboost_mpi%{lib_appendix} -p /sbin/ldconfig
%endif

%postun -n libboost_graph%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_system%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_wave%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_random%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_chrono%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_locale%{lib_appendix} -p /sbin/ldconfig
%postun -n libboost_timer%{lib_appendix} -p /sbin/ldconfig

%files -n boost-license%{lib_appendix}
%defattr(-, root, root, -)
%dir %{_docdir}
#%%doc %%{_docdir}/NEWS
%doc %{_docdir}/LICENSE_1_0.txt

%files -n libboost_atomic%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_atomic*.so.*

%if %build_context
%files -n libboost_context%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_context*.so.*
%endif

%files -n libboost_date_time%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_date_time*.so.*

%files -n libboost_filesystem%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_filesystem*.so.*

%files -n libboost_graph%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_graph*.so.*

%files -n libboost_iostreams%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_iostreams*.so.*

%files -n libboost_math%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_math_*.so.*

%if %build_mpi

%files -n libboost_mpi%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_mpi*.so.*
%{_libdir}/mpi.so
%endif

%files -n libboost_test%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_prg_exec_monitor*.so.*
%{_libdir}/libboost_unit_test_framework*.so.*

%files -n libboost_program_options%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_program_options*.so.*

%files -n libboost_python%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_python*.so.*

%files -n libboost_serialization%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_*serialization*.so.*

%files -n libboost_signals%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_signals*.so.*

%files -n libboost_system%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_system*.so.*

%files -n libboost_thread%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_thread*.so.*

%files -n libboost_wave%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_wave*.so.*

%files -n libboost_regex%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_regex*.so.*

%files -n libboost_random%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_random*.so.*

%files -n libboost_chrono%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_chrono*.so.*

%files -n libboost_locale%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_locale*.so.*

%files -n libboost_timer%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_timer*.so.*

%files devel
%defattr(-, root, root, -)
%{_includedir}/boost
%{_libdir}/*.so
%if %build_mpi
%exclude %{_libdir}/mpi.so
%endif
#%%{_datadir}/aclocal/*.m4

%files doc-html
%defattr(-, root, root, -)
%doc %{_docdir}/*
%exclude %{_docdir}/pdf
%exclude %{_docdir}/LICENSE_1_0.txt

%files doc-man
%defattr(644, root, root, -)
%doc %{_mandir}/man3/*.3.gz
%doc %{_mandir}/man7/*.7.gz
%doc %{_mandir}/man9/*.9.gz

%if %package_pdf

%files doc-pdf
%defattr(-, root, root, -)
%doc %{_docdir}/pdf
%endif

%changelog
