Name:           meshmagick
Version:        0.6.0
Release:        30.svn2898%{?dist}
Summary:        Command line manipulation tool for Ogre meshes

Group:          Applications/Multimedia
License:        MIT
URL:            http://www.ogre3d.org/tikiwiki/MeshMagick
# The source for this package was pulled from upstream's svn.  Use the
# following commands to generate the tarball:
#  svn export -r 2898 https://svn.code.sf.net/p/ogreaddons/code/trunk/meshmagick meshmagick
#  tar cjf meshmagick-0.6.0-r2898.tar.bz2 meshmagick
Source0:        %{name}-%{version}-r2898.tar.bz2
Patch0:         meshmagick-version.patch
Patch1:         meshmagick-multilib.patch
# Based on http://www.ogre3d.org/forums/download/file.php?id=5869&sid=127fa0b4be759e78d23b8a5f264a197f
# I needed to strip CRs out of the file to get patch to take it
# Since src/MmOptimiseTool.cpp had CRLF line endings and was affected 
# by this patch, I needed to change them to LF during setup.
Patch2:         meshmagick-ogre19.patch
Patch3:         meshmagick-boost-DSO.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ogre-devel
BuildRequires:  cmake

%description
MeshMagick is a manipulation tool for Ogre meshes (and skeletons). It
allows the user to query interesting information and to transform binary
meshes (and skeletons) in many ways.


%package        libs
Summary:        Libraries for %{name}
Group:          System Environment/Libraries

%description    libs
The %{name}-libs package contains libraries that are needed for
running applications that use %{name}.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release} pkgconfig ogre-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
sed -i "s|\r||g" src/MmOptimiseTool.cpp
%patch0
%patch1
%patch2
%patch3


%build
%cmake . -DSTATIC_BUILD=FALSE -DLIB:STRING=%{_lib} -DCMAKE_SKIP_RPATH=TRUE
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}.la


%clean
rm -rf $RPM_BUILD_ROOT


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS README LICENSE.txt
%{_bindir}/%{name}

%files libs
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc


%changelog
