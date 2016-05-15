#
# spec file for package manpageeditor
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


%define oname ManPageEditor
Name:           manpageeditor
Version:        0.0.15
Release:        0
Summary:        Manual pages editor
License:        GPL-3.0
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Books/Howtos
Url:            http://keithhedger.hostingsiteforfree.com/
Source0:        http://keithhedger.hostingsiteforfree.com/zips/manpageeditor/%{oname}-%{version}.tar.gz
BuildRequires:  aspell-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(gtksourceview-2.0)

%description
Create,edit,import,preview man-pages.

%prep
%setup -q -n %{oname}-%{version}
cp -r ManPageEditor/resources/docs/gpl-3.0.txt gpl-3.0.txt

%build
# FIXME: you should use the %%configure macro
./configure --prefix=%{_prefix} --enable-aspell
sed -i "s|update-mime-database %{_datadir}/mime||" Makefile
sed -i "/gtk-update-icon-cache/d" Makefile %{oname}/app/Makefile
sed -i "s|xdg-mime install ManPageEditor/resources/documenticons/maneditdoc-mime.xml||" Makefile
sed -i "s|-Wall|-Wall -fPIC|" Makefile %{oname}/app/Makefile

%install
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
%make_install
desktop-file-install %{buildroot}%{_datadir}/applications/%{oname}.desktop
rm -fr %{buildroot}%{_datadir}/%{oname}/docs

%files
%defattr(-,root,root)
%doc ChangeLog gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}/examples/*
%{_datadir}/%{oname}/help/*
%{_mandir}/man1/manpageeditor.1*
%{_datadir}/pixmaps/%{oname}.png
%{_datadir}/icons/hicolor/256x256/apps/%{oname}.png

%changelog
%changelog
