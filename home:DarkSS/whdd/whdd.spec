#
# spec file for package whdd
#
# Copyright (c) 2011-2013 Andrey 'Krieger' Utkin
# <andrey.krieger.utkin@gmail.com>, (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# https://github.com/krieger-od/whdd/issues
#

Name:           whdd
Version:        1.0
Release:        1
Summary:        Diagnostic and recovery tool for block devices (near to replace MHDD for Linux)

License:        GPL
URL:            https://github.com/krieger-od/whdd
Source0:        %{name}-%{version}.tar.gz
Group:          System/Benchmark

BuildRequires:  cmake
BuildRequires:  dialog-devel
# BuildRequires:  update-desktop-files fdupes
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

%build
export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS
cmake . \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DDIALOG_INCLUDE_DIRS:PATH=%{_includedir}/dialog/
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# %%suse_update_desktop_file %{name}
# %%fdupes -s %{buildroot}%{_datadir}/games/%{name}/mods/

%files
%defattr(-,root,root)
%doc README doc/README.developer

%changelog
