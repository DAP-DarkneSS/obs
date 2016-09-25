#
# spec file for package zeal
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


Name:           zeal
Version:        0.2.1
Release:        0
Summary:        Offline API documentation browser
License:        GPL-3.0
Group:          Development/Tools/Other
Url:            http://zealdocs.org
Source0:        https://github.com/zealdocs/zeal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE vs. file-contains-current-date WARNING:
Patch0:         zeal-no-date-and-time.diff
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel >= 5.2.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2.0
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.2.0
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2.0
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(xcb-keysyms)
Requires:       libQt5Sql5-sqlite >= 5.2.0
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

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
%setup -q
%patch0 -p1

%build
%qmake5 
make %{?_smp_mflags} V=1

%install
%qmake5_install
%suse_update_desktop_file -r %{name} Office Viewer
%fdupes -s %{buildroot}%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*

%changelog
