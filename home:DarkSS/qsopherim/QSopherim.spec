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
Version:        git
Release:        1
Summary:        Holy Bible reader

License:        GPL-3.0
Url:            http://warmonger72.blogspot.ru/search/label/QSopherim
Group:          Amusements/Teaching/Other
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  dos2unix
BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files

Requires:       enca

%description
QSopherim is a reader for various formats of Holy Bible texts.

%prep
%setup -q
dos2unix -q {} ';' LICENSE.GPL

%build
qmake \
QMAKE_STRIP="" \
QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} build/bin/%{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} desktop/%{name}_logo.png %{buildroot}%{_datadir}/pixmaps

%suse_update_desktop_file -i %{name}

%files
%defattr(-,root,root)
%doc *.md LICENSE.GPL
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.png

%changelog
