#
# spec file for package kkedit
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.2.7
Release:        0
Summary:        Source code text editor
License:        GPL-3.0
Group:          Productivity/Text/Editors
Url:            http://keithhedger.hostingsiteforfree.com/pages/kkedit/help.html
Source0:        http://keithhedger.hostingsiteforfree.com/zips/kkedit/KKEdit-%{version}.tar.gz

BuildRequires:  aspell-devel
BuildRequires:  ctags
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.32.4
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(unique-1.0)
BuildRequires:  pkgconfig(webkit-1.0)
Recommends:     %{name}-lang
Recommends:     ctags

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

%build
%configure \
           --enable-aspell \
           --enable-docviewer

make %{?_smp_mflags}

%install
%make_install
# A workaround for "WARNING: absolute path in Icon line".
sed -i %{buildroot}%{_datadir}/applications/KKEdit.desktop \
    -e "s/\/usr\/share\/KKEdit\/pixmaps\/KKEdit.png/KKEdit/"
%suse_update_desktop_file -r KKEdit 'Utility;TextEditor;GTK;'
%suse_update_desktop_file -r KKEditRoot 'Utility;TextEditor;GTK;'
# Let's use %%doc macro.
rm -rf %{buildroot}%{_datadir}/KKEdit
%fdupes -s %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}


%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun


%files
%defattr(-,root,root)
%doc ChangeLog
%doc KKEdit/resources/docs/* KKEdit/resources/help
%{_bindir}/%{name}
%{_bindir}/KKEdit*
%{_datadir}/applications/KKEdit*.desktop
%{_datadir}/pixmaps/KKEdit*.png
%{_datadir}/icons/hicolor/*/apps/KKEdit*.png

%files          devel
%defattr(-,root,root)
%doc KKEdit/resources/Exampl*
%{_includedir}/%{name}*

%files lang -f %{name}.lang

%changelog
