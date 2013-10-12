#
# spec file for package Checksum
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


Name:           Checksum
Version:        1.1.7
Release:        0
License:        SUSE-WTFPL-2.0
Summary:        An easy-to-use tool for hashing files and validating checksums
Url:            http://qt-apps.org/content/show.php/Checksum?content=161033
Group:          Productivity/Other
Source0:        Checksum_%{version}.tar.gz

BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(QtGui)

%description
Features:
 * Beautiful and intuitive design;
 * JIT generation of checksums;
 * Supports drap-and-drop.

%prep
%setup -q -n %{name}


%build
qmake \
      QMAKE_STRIP="" \
      QMAKE_CFLAGS+="%{optflags}" \
      QMAKE_CXXFLAGS+="%{optflags}"

make VERBOSE=1 %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
install %{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install checksum.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file -c %{name} %{name} "An easy-to-use tool for hashing files and validating checksums" %{name} %{name} "Utility;Accessibility;"


%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
