#
# spec file for package gecrit
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


Name:           gecrit
Version:        2.8.4
Release:        0
Summary:        Source code text editor
License:        GPL-3.0+
Group:          Productivity/Text/Editors
Url:            http://sourceforge.net/projects/gecrit
Source0:        http://downloads.sourceforge.net/project/gecrit/SOURCE/gecrit-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  pkgconfig(python2)
BuildArch:      noarch

%description
gEcrit is a Python orientated source code editor. It tries to keep
the interface as clean as possible and keep the menus simple.
It features all the common features a Python programmer might need,
including an interactive Python shell.

%prep
%setup -q

%build
python \
       setup.py \
       build

%install
python \
       setup.py \
       install \
       -O1 \
       --skip-build \
       --root %{buildroot} \
       --prefix=%{_prefix} \
       --install-lib=%{_datadir}

%fdupes %{buildroot}%{_datadir}/gEcrit

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/gEcrit-*.egg-info
%{_datadir}/gEcrit

%changelog
