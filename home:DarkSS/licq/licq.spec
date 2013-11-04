#
# spec file for package licq
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


Name:           licq
BuildRequires:  boost-devel
BuildRequires:  cdk-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
BuildRequires:  libkde4-devel
BuildRequires:  xosd-devel
BuildRequires:  pkgconfig(QtGui) >= 4.7
Version:        1.8.1
Release:        0
Summary:        Linux ICQ Client
License:        GPL-2.0+
Group:          Productivity/Networking/ICQ
Source:         http://switch.dl.sourceforge.net/project/licq/licq/%{version}/licq-%{version}.tar.bz2
Source2:        licq.png
Recommends:     sox
Patch2:         licq-1.5.0-remove_desktop_file.patch
# TODO: please drop it after the next subj update!
# PATCH-FIX-UPSTREAM to prevent compiling error.
Patch3:         licq-1.8.1-65026d6.patch
Url:            http://www.licq.org/

%description
Licq includes all the basic features of ICQ, like sending and receiving
messages, chat, file transfer, contact list with pixmaps and user
status, basic and extended user information, adding and editing users
from within the GUI, user history, user groups, and new user
registration. All commands and information are available through a
simple and convenient tab dialog. Licq also has a completely
configurable user interface with Skin and Icon pack support. It is
written in C++ and comes with a GUI plug-in using the Qt widget set.
Other plug-ins are also available.



%package qt4-gui-data
Summary:        Qt4 data files for Licq
Group:          Productivity/Networking/ICQ
BuildArch:      noarch

%description qt4-gui-data
Data files for the Qt4 Licq plug-in.


%package qt4-gui
Summary:        Qt4 plug-in for Licq
Group:          Productivity/Networking/ICQ
Requires:       %{name} = %{version}
Requires:       %{name}-qt4-gui-data = %{version}
Supplements:    %{name}

%description qt4-gui
This plug-in uses the Qt4 libraries to provide Licq GUI.


%package kde4-gui
Summary:        KDE4 plug-in for Licq
Group:          Productivity/Networking/ICQ
Requires:       %{name} = %{version}
Requires:       %{name}-qt4-gui-data = %{version}
Supplements:    packageand(kdebase4-workspace:licq)
%kde4_runtime_requires

%description kde4-gui
This plug-in uses the KDE4 libraries to provide Licq GUI.


%package devel
Summary:        Development files of Licq
Group:          Development/Sources
Requires:       %{name} = %{version}

%description devel
Header files of Licq program.



%prep
%setup
%patch2 -p1
%patch3

# disabled for now (deps missing)
rm -r plugins/aosd plugins/jabber

%build
# seems to be needed for whatever reason
LDFLAGS="$LDFLAGS -pthread"

# the KDE4 rpm macros are more convenient, so simply use them for everything
%cmake_kde4 -d build -- -DBUILD_TESTS=OFF -DBUILD_PLUGINS=ON
%make_jobs
cd ..

# build the qt4-gui plugin also with KDE integration
cp -a plugins/qt4-gui plugins/kde4-gui
pushd plugins/kde4-gui
sed -i -e 's/WITH_KDE\(.*\)OFF/WITH_KDE\1ON/' CMakeLists.txt
sed -i -e 's#\${CMAKE_MODULE_PATH}#${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/../../cmake#' CMakeLists.txt
%cmake_kde4 -d build -- -DWITH_KDE=ON
%make_jobs
popd

%install 
%kde4_makeinstall -C build
%kde4_makeinstall -C plugins/kde4-gui/build
# docs
mkdir -p $RPM_BUILD_ROOT%{_docdir}/licq
install -m 644 doc/*  $RPM_BUILD_ROOT%{_docdir}/licq
%suse_update_desktop_file -i -G "ICQ Client" licq Network InstantMessaging
%find_lang %{name} %{name}.lang
%find_lang licq_osd_plugin %{name}.lang
%fdupes -s $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,755)
%doc %{_docdir}/licq/
%{_bindir}/licq
%{_libdir}/licq/
%{_datadir}/licq/
/usr/share/applications/licq.desktop
/usr/share/pixmaps/licq.png
%exclude %{_includedir}/licq/
%exclude %{_libdir}/licq/licq_qt4-gui.so
%exclude %{_libdir}/licq/licq_kde4-gui.so
%exclude %{_datadir}/licq/qt4-gui
%exclude %{_datadir}/licq/cmake

%files devel
%defattr(-,root,root,755)
%{_includedir}/licq/
%{_datadir}/licq/cmake

%files qt4-gui-data
%defattr(-,root,root,755)
%{_datadir}/licq/qt4-gui

%files qt4-gui
%defattr(-,root,root,755)
%{_libdir}/licq/licq_qt4-gui.so

%files kde4-gui
%defattr(-,root,root,755)
%{_libdir}/licq/licq_kde4-gui.so

%changelog
