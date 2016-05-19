#
# spec file for package yang
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yang
Version:        0.0+git
Release:        0
Summary:        Yet Another NonoGrams
License:        MIT
Group:          Games
Url:            https://github.com/RPG-18/yang
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  cmake >= 3
%if 0%{?suse_version} <= 1320
BuildRequires:  gcc49-c++
BuildRequires:  llvm-clang >= 3.4
%else
BuildRequires:  gcc-c++ >= 5
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.6

%description
Yang is the prototype for the client nanograms.org.

%prep
%setup -q

%build
mkdir build && cd build
%if 0%{?suse_version} <= 1320
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
%endif
cmake ../src \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -k V=1 %{?_smp_mflags}


%install
cd build
%make_install


%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
