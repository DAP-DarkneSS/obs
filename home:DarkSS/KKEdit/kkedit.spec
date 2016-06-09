#
# spec file for package kkedit
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


Name:           kkedit
Version:        0.3.3
Release:        0
Summary:        Source code text editor
License:        GPL-3.0
Group:          Productivity/Text/Editors
Url:            http://gtk-apps.org/content/show.php?content=158161
Source0:        http://khapplications.darktech.org/zips/kkedit/KKEdit-%{version}.tar.gz
Source8:        KKEditProgressBar.1
Source9:        %{name}.1
# PATCH-FIX-OPENSUSE vs. various errors & warnings about desktop files.
Patch0:         kkedit-desktop-warnings.diff

BuildRequires:  aspell-devel
BuildRequires:  ctags
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.32.4
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(unique-1.0)
BuildRequires:  pkgconfig(vte) >= 0.28.2
BuildRequires:  pkgconfig(webkit-1.0)
Requires(post): update-desktop-files
Requires(pre):  update-desktop-files
Recommends:     %{name}-lang
Recommends:     ctags
Recommends:     doxygen
Recommends:     manpageeditor

%description
KKEdit is NOT a word processor or a web page editor, it is NOT
and IDE! It won't right code for you, it wont insist on inserting
brackets ( REALLY annoying! ), it wont force you to use any
particular style, it doesn't need you to break all your fingers
trying to hit weird and wonderful key combo's and it is not tied
to one particular distro, oh yes and it won't cost you a penny!

KKEdit is a deceptively simple text editor with syntax colouring.
It also has a function menu which allows you to jump instantly to
a function definition, a navigation menu which will look in all
open files for a function definition and then switch to that tab
and go to the relevant line if it can't find a definition in any
open files it will do a recursive search from the folder of the
currently selected document, you can also highlight a #include
directive and it will search for and try to open the file,
include files surrounded by <> will be looked for in /usr/include,
files surrounded by "" will be looked for in the current folder.
External tools can be added either globally or locally and when
run can either replace the currently select text with their
output, replace all the files text, be run in a terminal or you
can choose to ignore the output form the script, BASH, python and
perl can be used for the script language or any interpretor that
uses '#' as a comment marker.

You can drag and drop a file onto the main toolbar/menu to open a
file. Session can be saved and reloaded. Any amount of bookmarks can
be added anywhere, selecting a bookmark from the menu will switch to
that tab and move to the appropriate line. Just type a line number
into the edit box on the toolbar to jump straight to that line.

%lang_package


%package        devel
Summary:        KKEdit development files
Group:          Development/Libraries/C and C++

%description    devel
KKEdit include headers and example external tools.


%prep
%setup -q -n KKEdit-%{version}
%patch0

%build
%configure \
           --enable-aspell \
           --enable-docviewer

make %{?_smp_mflags}

%install
%make_install

# Let's use %%doc macro.
rm %{buildroot}%{_datadir}/KKEdit/docs/gpl-3.0.txt

# E: spurious-executable-perm
cd %{buildroot}%{_datadir}/KKEdit/tools
chmod -x Re-Open-As-Root Open-Man-Page Open-Xterm-Here
chmod -x %{buildroot}%{_includedir}/kkedit-plugins.h

# Don't package binary modules in datadir.
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}/%{_datadir}/KKEdit/plugins-gtk/*.so %{buildroot}%{_libdir}/%{name}
rm -rf %{buildroot}/%{_datadir}/KKEdit/plugins-gtk
ln -s %{_libdir}/%{name} %{buildroot}/%{_datadir}/KKEdit/plugins-gtk

# Man pages:
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c9 %{SOURCE8} | tee -a %{buildroot}%{_mandir}/man1/KKEditProgressBar.1.gz
gzip -c9 %{SOURCE9} | tee -a %{buildroot}%{_mandir}/man1/%{name}.1.gz

%fdupes -s %{buildroot}


%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun


%files
%defattr(-,root,root)
%doc BUGS-ETC ChangeLog COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/KKEdit*
%{_mandir}/man1/KKEdit*.1.gz
%attr(644,root,root) %{_datadir}/applications/KKEdit*.desktop
%{_datadir}/pixmaps/KKEdit*.png
%{_datadir}/icons/hicolor/*/apps/KKEdit*.png
%{_datadir}/KKEdit
%{_libdir}/%{name}

%files          devel
%defattr(-,root,root)
%{_includedir}/%{name}*

%files lang
%defattr(-,root,root)
%lang(fr) %{_datadir}/locale/fr_FR/LC_MESSAGES/*.mo

%changelog
