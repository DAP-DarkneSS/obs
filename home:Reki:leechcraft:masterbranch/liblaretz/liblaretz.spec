#
# spec file for package liblaretz
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


%define pack_summ Next-gen sync server for LC library

%define pack_desc Next-gen synchronization server for LeechCraft library.


Name:           liblaretz
Version:        git
Release:        0
License:        BSL-1.0
Summary:        %{pack_summ}
Group:          System/Libraries

Url:            https://github.com/0xd34df00d/laretz
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  boost-devel >= 1.52
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 4.7

%description
%{pack_desc}


%package        -n %{name}_ops
Summary:        %{pack_summ}

%description    -n %{name}_ops
%{pack_desc}


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}_ops = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
cmake src/lib \
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_CXX_FLAGS="%{optflags} -Doverride=" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags}


%install
%make_install


%post -n %{name}_ops -p /sbin/ldconfig

%postun -n %{name}_ops -p /sbin/ldconfig


%files -n %{name}_ops
%defattr(-,root,root)
# %%doc README*
%{_prefix}/lib/%{name}_ops.so

%files devel
%defattr(-,root,root)
%{_includedir}/laretz
%dir %{_datadir}/apps
%dir %{_datadir}/apps/cmake
%dir %{_datadir}/apps/cmake/modules
%{_datadir}/apps/cmake/modules/FindLibLaretz.cmake

%changelog
