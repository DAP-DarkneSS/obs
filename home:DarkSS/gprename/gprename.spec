#
# spec file for package gprename
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


Name:           gprename
Version:        5
Release:        0
License:        GPL-3.0+
Summary:        A GTK2 batch renamer for files and directories
Url:            http://gprename.sourceforge.net/
Group:          Productivity/File utilities

Source0:        http://kent.dl.sourceforge.net/project/gprename/gprename/%{version}/gprename-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE to prevent "W: invalid-desktopfile; unknown value."
Patch0:         validate-desktopfile.patch

BuildRequires:  update-desktop-files
Requires:       perl-Gtk2
Requires:       perl-gettext
Recommends:     %{name}-lang
Recommends:     nautilus-actions
BuildArch:      noarch
# SLE 11 requires it to build:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GPRename is a complete GTK2/perl batch renamer for files and directories.

%lang_package

%prep
%setup -q
%patch0


%build


%install
make \
     PREFIX=%{_prefix} \
     DESTDIR=%{buildroot}%{_prefix} \
     install
%suse_update_desktop_file -r %{name} 'Utility;System;FileManager;'
%find_lang %{name}


%files
%defattr(-,root,root)
# SLE complains: "directories are not even executable by their owner."
%if 0%{?suse_version} >= 1140
%attr(644,root,root) %doc *.TXT
%endif
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*
%doc %{_mandir}/man*/%{name}*
%{_datadir}/pixmaps/%{name}


%files lang -f %{name}.lang


%changelog
