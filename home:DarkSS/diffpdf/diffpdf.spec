#
# spec file for package diffpdf
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


Name:           diffpdf
Version:        2.1.3
Release:        0
License:        GPL-2.0+
Summary:        PDF files comparator
Url:            http://www.qtrac.eu/diffpdf.html
Group:          Productivity/Text/Utilities
Source0:        http://www.qtrac.eu/%{name}-%{version}.tar.gz
Source3:        %{name}.desktop

BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(poppler-qt4)

%description
DiffPDF is used to compare two PDF files. By default the comparison is
of the text on each pair of pages, but comparing the appearance of pages
is also supported (for example, if a diagram is changed or a paragraph
reformatted). It is also possible to compare particular pages or page
ranges.

%prep
%setup -q


%build
lrelease diffpdf.pro
qmake \
      QMAKE_STRIP="" \
      QMAKE_CFLAGS+="%{optflags}" \
      QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 diffpdf %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install images/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file -i %{name}


%post
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%postun
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files
%defattr(-,root,root,-)
%doc CHANGES gpl-2.0.txt help_cz.html help_de.html help_fr.html help.html README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
