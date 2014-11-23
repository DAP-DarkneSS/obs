#
# spec file for package zeal
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define gittag 20141123

Name:           zeal
Summary:        Offline API documentation browser
Version:        0.0+git.2014.11.23
Release:        0
License:        GPL-3.0
URL:            http://zealdocs.org
Group:          Development/Tools/Other
Source0:        https://github.com/jkozera/zeal/archive/%{gittag}.tar.gz

BuildRequires:  fdupes
%if 0%{?suse_version} > 1310
BuildRequires:  libQt5Gui-private-headers-devel
%else
BuildRequires:  libqt5-qtbase-private-headers-devel
%endif
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Xml)
%if 0%{?suse_version} > 1310
BuildRequires:  pkgconfig(appindicator-0.1)
%endif
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(xcb-keysyms)

%description
Zeal is a simple offline API documentation browser inspired by Dash
(OS X app), available for Linux and Windows.
 * Quickly search documentation using Alt+Space (or customised)
   hotkey to display Zeal from any place in your workspace.
 * Search in multiple sets of documentation at once.
 * Don't be dependent on your internet connection.
 * Integrate Zeal with Emacs, Sublime Text, or Vim. See Usage »
   Editor plugins for details.

%prep
%setup -q -n %{name}-%{gittag}/%{name}

%build
qmake-qt5 \
%if 0%{?suse_version} <= 1310
            "CONFIG+=no_libappindicator" \
%endif
            QMAKE_STRIP="" \
            QMAKE_CFLAGS+="%{optflags}" \
            QMAKE_CXXFLAGS+="%{optflags}"

make V=1 %{?_smp_mflags}

%install
make V=1 INSTALL_ROOT=%{buildroot} install
%suse_update_desktop_file -r %{name} Office Viewer
%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%doc ../COPYING ../README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/pixmaps/%{name}

%changelog
