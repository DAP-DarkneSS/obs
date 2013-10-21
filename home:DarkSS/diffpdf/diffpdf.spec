Name:           diffpdf
Version:        2.1.2
Release:        3%{?dist}
Summary:        PDF files comparator

Group:          Applications/Text
License:        GPLv2+
URL:            http://www.qtrac.eu/diffpdf.html
Source0:        http://www.qtrac.eu/%{name}-%{version}.tar.gz
Source3:        %{name}.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  poppler-qt4-devel, desktop-file-utils, ImageMagick
# /usr/include/poppler/cpp/poppler-version.h
BuildRequires:  poppler-cpp-devel
Requires:       hicolor-icon-theme

%description
DiffPDF is used to compare two PDF files. By default the comparison is
of the text on each pair of pages, but comparing the appearance of pages
is also supported (for example, if a diagram is changed or a paragraph
reformatted). It is also possible to compare particular pages or page
ranges.

%prep
%setup -q


%build
lrelease-qt4 diffpdf.pro
qmake-qt4
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 diffpdf $RPM_BUILD_ROOT%{_bindir}

for f in 32 16; do
   mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/"$f"x$f/apps
   convert images/icon.png -size "$f"x$f diffpdf-$f.png
   install -p diffpdf-$f.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/"$f"x$f/apps/diffpdf.png
done

desktop-file-install                                    \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE3}

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES gpl-2.0.txt help_cz.html help_de.html help_fr.html help.html README
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/??x??/apps/*.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Till Maas <opensource@till.name> - 2.1.2-1
- Update to new release

* Tue Oct 02 2012 Till Maas <opensource@till.name> - 2.1.1-1
- Update to new release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 1.2.2-4
- Rebuild (poppler-0.20.0)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 1.2.2-2
- Rebuild (poppler-0.17.3)

* Mon Jul 25 2011 Till Maas <opensource@till.name> - 1.2.2-1
- Update to new release

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 1.0.0-3
- Rebuild (poppler-0.17.0)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 19 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0.0-1
- diffpdf 1.0.0 new/improved algorithm

* Sat May 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.6.0-1
- diffpdf 0.6.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 14 2008 Rafał Psota <rafalzaq@gmail.com> - 0.3.8-4
- forgot about ImageMagick
* Fri Dec 12 2008 Rafał Psota <rafalzaq@gmail.com> - 0.3.8-3
- drop vendor for desktop file
* Thu Nov 27 2008 Rafał Psota <rafalzaq@gmail.com> - 0.3.8-2
- forgot about desktop file
* Tue Nov 11 2008 Rafał Psota <rafalzaq@gmail.com> - 0.3.8-1
- Initial release
