#
# spec file for package whdd
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


Name:           whdd
Version:        1.0
Release:        0
Summary:        Diagnostic and recovery tool for block devices (near to replace MHDD for Linux)
License:        GPL-2.0+
Group:          Hardware/Other
Url:            https://github.com/krieger-od/whdd
# git clone https://github.com/krieger-od/whdd.git && cd whdd
# git archive f4ca537f80 --prefix=whdd-%%{version}/ | bzip2 > ../whdd-%%{version}.tar.bz2
Source0:        %{name}-%{version}.tar.bz2
Patch1:         whdd-link-libraries.patch

BuildRequires:  cmake
BuildRequires:  dialog-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
Functionality:
- List available block devices (HDD, Flash drives etc.)
- List SMART parameters
- Perform tests:
--- Read
--- Write zeros
- Visualize results of tests
- Low-level device copying (not implemented yet)
Program is designed for adding more complex tests or recovery procedures,
and different front-ends.

%prep
%setup -q
%patch1 -p1

%build
export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS
cmake \
       -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
       -DDIALOG_INCLUDE_DIR:PATH=%{_includedir}/dialog/ \
       -DMENU_INCLUDE_DIR:PATH=%{_includedir}/ncursesw/ \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
%doc README doc/README.developer
%{_sbindir}/whdd*

%changelog
