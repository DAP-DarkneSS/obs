#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           diffpdf
Version:        2.1.2
Release:        3%{?dist}
Summary:        PDF files comparator

License:        GPLv2+
Url:            http://www.qtrac.eu/diffpdf.html
Group:          Applications/Text
Source0:        http://www.qtrac.eu/%{name}-%{version}.tar.gz
Source3:        %{name}.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils,
# /usr/include/poppler/cpp/poppler-version.h
BuildRequires:  poppler-cpp-devel
BuildRequires:  poppler-qt4-devel,
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
mkdir -p %{buildroot}%{_bindir}
install -m 755 diffpdf %{buildroot}%{_bindir}

for f in 32 16; do
   mkdir -p %{buildroot}%{_datadir}/icons/hicolor/"$f"x$f/apps
   convert images/icon.png -size "$f"x$f diffpdf-$f.png
   install -p diffpdf-$f.png %{buildroot}%{_datadir}/icons/hicolor/"$f"x$f/apps/diffpdf.png
done

desktop-file-install                                    \
  --dir=%{buildroot}%{_datadir}/applications         \
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
