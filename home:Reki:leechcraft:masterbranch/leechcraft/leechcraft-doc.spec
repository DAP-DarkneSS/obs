#
# spec file for package leechcraft-doc
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


Name:           leechcraft-doc
Version:        git
%define LEECHCRAFT_VERSION 0.6.60-1224-g628f02a
Release:        0
License:        BSL-1.0
Summary:        Modular Internet Client Documentation
Url:            http://leechcraft.org
Group:          Development/Libraries/Other
Source0:        leechcraft-%{version}.tar.xz

BuildRequires:  doxygen >= 1.8.3.1
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildArch:      noarch

%description
This packages provides documentation of LeechCraft core API.

It contains description of core API used for developing first-level
LeechCraft plugins. For developing sub-plugins, please refer to
corresponding packages (like leechcraft-azoth-doc). This documentation
is also available online at http://doc.leechcraft.org/core/

%package -n leechcraft-azoth-doc
Summary:        LeechCraft Azoth Documentation
Group:          Development/Libraries/Other
BuildArch:      noarch

%description -n leechcraft-azoth-doc
This packages provides documentation of LeechCraft Azoth API.

It contains description of Azoth API used for developing LeechCraft
Azoth sub-plugins. For developing first-lexel plugins, please refer
to corresponding packages (like leechcraft-doc). This documentation
is also available online at http://doc.leechcraft.org/azoth/

%package -n leechcraft-monocle-doc
Summary:        LeechCraft Monocle Documentation
Group:          Development/Libraries/Other
BuildArch:      noarch

%description -n leechcraft-monocle-doc
This packages provides documentation of LeechCraft Monocle API.

It contains description of Monocle API used for developing LeechCraft
Monocle sub-plugins. For developing first-lexel plugins, please refer
to corresponding packages (like leechcraft-doc). This documentation
is also available online at http://doc.leechcraft.org/monocle/

%prep
%setup -q -n leechcraft-%{version}

%build
cd doc/doxygen/core
sed -i Doxyfile \
-e "s/PROJECT_NUMBER .*/PROJECT_NUMBER         = %{LEECHCRAFT_VERSION}/"
doxygen Doxyfile

cd ../azoth
sed -i Doxyfile \
-e "s/PROJECT_NUMBER .*/PROJECT_NUMBER         = %{LEECHCRAFT_VERSION}/"
doxygen Doxyfile

cd ../monocle
sed -i Doxyfile \
-e "s/PROJECT_NUMBER .*/PROJECT_NUMBER         = %{LEECHCRAFT_VERSION}/"
doxygen Doxyfile

%install
cd doc/doxygen/core/out/html
mkdir -p %{buildroot}%{_docdir}/leechcraft-doc
cp -r * %{buildroot}%{_docdir}/leechcraft-doc

cd ../../../azoth/out/html
mkdir -p %{buildroot}%{_docdir}/leechcraft-azoth-doc
cp -r * %{buildroot}%{_docdir}/leechcraft-azoth-doc

cd ../../../monocle/out/html
mkdir -p %{buildroot}%{_docdir}/leechcraft-monocle-doc
cp -r * %{buildroot}%{_docdir}/leechcraft-monocle-doc

%fdupes -s %{buildroot}%{_docdir}/leechcraft-doc/
%fdupes -s %{buildroot}%{_docdir}/leechcraft-azoth-doc/
%fdupes -s %{buildroot}%{_docdir}/leechcraft-monocle-doc/

%files
%defattr(-,root,root)
%doc %{_docdir}/leechcraft-doc

%files -n leechcraft-azoth-doc
%defattr(-,root,root)
%doc %{_docdir}/leechcraft-azoth-doc

%files -n leechcraft-monocle-doc
%defattr(-,root,root)
%doc %{_docdir}/leechcraft-monocle-doc

%changelog
