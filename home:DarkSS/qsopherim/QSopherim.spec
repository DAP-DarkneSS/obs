#
# spec file for package QSopherim
#
# Copyright (c) 2012-2013 Sapronov Alexander (source),
# (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# https://github.com/WarmongeR1/QSopherim/issues
#

Name:           QSopherim
Version:        git.alfa.pre.3.1362996819
Release:        1
Summary:        Holy Bible reader

License:        GPL-3.0
Url:            http://warmonger72.blogspot.ru/search/label/QSopherim
Group:          Amusements/Teaching/Other
Source0:        %{name}-%{version}.tar.bz2

Patch0:         data.patch

BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files

Requires:       enca
Requires:       %{name}-data = %{version}

%description
QSopherim is a reader for various formats of Holy Bible texts.

%package data
Summary:        QSopherim data
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Architecture independent data of QSopherim package.

%prep
%setup -q
%patch0

%build
qmake \
QMAKE_STRIP="" \
QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -R data/* %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_bindir}
%{__install} build/bin/%{name} %{buildroot}%{_bindir}/%{name}-bin
echo -e '#!/bin/sh'"\n\ncd %{_datadir}/%{name}\n%{name}-bin" > %{buildroot}%{_bindir}/%{name}
# The binary file must be run from the game data directory.

mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} resources/images/logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file -c %{name} %{name} "Holy Bible reader" %{name} %{name}.png "Office;Viewer;"

%files
%defattr(-,root,root)
%doc *.md LICENSE.GPL
%attr(755,root,root) %{_bindir}/%{name}*

%files data
%defattr(-,root,root)
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%attr(777,root,users) %{_datadir}/%{name}

%changelog
