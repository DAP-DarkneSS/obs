#
# spec file for package eidete
#
# Copyright (c) 2011-2012 elementary Team (source),
# (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via https://bugs.launchpad.net/eidete
#

%define descr Current Features: \
 - encoding to webm, \
 - selection of the area to be recorded, \
 - display of the pressed keys, \
 - audio recording.

Name:           eidete
Version:        0.1+bzr
Release:        1
Summary:        A simple screencasting app for the elementary project

License:        GPL-3.0+
Url:            https://launchpad.net/eidete
Group:          Productivity/Multimedia/Other
Source0:        eidete-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires:  pkg-config
%else
BuildRequires:  pkgconfig
%endif
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(granite) >= 0.2
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-interfaces-0.10)
BuildRequires:  pkgconfig(gstreamer-pbutils-0.10)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(xtst)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  vala >= 0.16
%if 0%{?suse_version}
Recommends:     %{name}-lang
Recommends:     gstreamer-plugins-ugly
%else
Requires:       %{name}-lang
Requires:       gstreamer-plugins-ugly
%endif

%description
%{descr}

%package lang
Group:          System/Localization
Summary:        Transtalions files for %{name}
BuildArch:      noarch

%description lang
%{descr}

%prep
%setup -q
mkdir build

%build
cd build

cmake .. \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

make VERBOSE=1 %{?_smp_mflags}

%install
mkdir -p %{buildroot}
cd build
%make_install INSTALL_ROOT=%{buildroot}

%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} 'Multimedia;Video;Recorder;'
%endif

%find_lang %{name}

%files
%defattr(-,root,root)
%{_bindir}/*
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%{_datadir}/contractor
%{_datadir}/icons/hicolor/*/apps/*.svg

%files lang -f build/%{name}.lang
%defattr(-,root,root)

%changelog
