#
# spec file for package granite
#
# Copyright (c) 2011-2012 elementary Team (source),
# (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via https://code.launchpad.net/granite
#

%define descr Granite is an extension of GTK. Among other things, \
it provides the commonly-used widgets such as modeswitchers, \
welcome screens, AppMenus, search bars, and more found in elementary apps.

Name:           granite
Version:        0.1.0
Release:        1
Summary:        A development library for elementary development

License:        GPL-2.0+
Url:            https://launchpad.net/granite
Group:          System/Libraries
Source0:        https://launchpad.net/granite/0.1/0.1/+download/granite-%{version}.tar.gz

%if 0%{?suse_version}
BuildRequires:  -post-build-checks
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:  pkg-config
%else
BuildRequires:  pkgconfig
%endif
BuildRequires:  pkgconfig(gee-1.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.3.14
BuildRequires:  vala >= 0.16

%description
%{descr}

%package devel
Group:          Development/Libraries/GNOME
Summary:        Development files for lib%{name}0
Requires:       lib%{name}0 = %{version}

%description devel
%{descr}

%package lang
Group:          System/Localization
Summary:        Transtalions files for %{name}
BuildArch:      noarch

%description lang
%{descr}

%package -n lib%{name}0
Summary:        %{summary}

%description -n lib%{name}0
%{descr}

%prep
%setup -q
mkdir build

%build
cd build

cmake .. \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

make VERBOSE=1 %{?_smp_mflags}

%install
mkdir -p %{buildroot}
cd build

%if 0%{?fedora} == 18
touch lib/Granite-0.1.gir
touch lib/Granite-0.1.typelib
%endif

%make_install INSTALL_ROOT=%{buildroot}

%ifarch x86_64 ppc64
%__mv %{buildroot}/usr/{lib,lib64}
%endif

%find_lang %{name}

%post -n lib%{name}0 -p /sbin/ldconfig

%postun -n lib%{name}0 -p /sbin/ldconfig

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_datadir}/gir-1.0
%{_datadir}/vala
%{_bindir}/%{name}-demo
%{_libdir}/girepository-1.0

%files lang -f build/%{name}.lang
%defattr(-,root,root)

%files -n lib%{name}0
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/lib%{name}.so.*

%changelog
