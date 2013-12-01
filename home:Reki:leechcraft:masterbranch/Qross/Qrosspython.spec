#
# spec file for package Qrosspython
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


%define pack_summ A Qt-only fork of Kross

%define pack_desc Kross is the new scripting framework \
for KDE SC 4, the latest version of the KDE SC. Originally \
Kross was designed for use in KOffice but eventually became the \
official scripting framework in KDE SC 4. Kross is designed to \
provide full scripting power for users of KDE applications, \
with a language of their own choice; and make it easy for \
developers targeting the KDE platform to enable their \
application with support for multiple scripting languages \
(without themselves needing to be proficient in any of them). \
\
The Kross scripting framework is not a scripting language \
itself. It merely serves to plug into KDE the support for \
other, already existing scripting languages.


Name:           Qrosspython
Version:        0.3.0
Release:        0
License:        LGPL-2.0+
Summary:        %{pack_summ}, python2 engine
Url:            https://github.com/0xd34df00d/Qross
Group:          System/Libraries
Source0:        https://github.com/0xd34df00d/Qross/archive/%{version}.tar.gz

BuildRequires:  Qross-devel
BuildRequires:  python-sip-devel
BuildRequires:  pkgconfig(python2)

%description
%{pack_desc}


%package        -n libqrosspython1
Summary:        %{pack_summ}

%description    -n libqrosspython1
%{pack_desc}


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libqrosspython1 = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n Qross-%{version}


%build
cd src/bindings/python/qrosspython
cmake \
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_CXX_FLAGS="%{optflags} -Doverride=" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags}

%install
cd src/bindings/python/qrosspython
%make_install


%post   -n libqrosspython1 -p /sbin/ldconfig

%postun -n libqrosspython1 -p /sbin/ldconfig


%files -n libqrosspython1
%defattr(-,root,root)
%{_libdir}/*qrosspython*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*qrosspython*.so

%changelog
