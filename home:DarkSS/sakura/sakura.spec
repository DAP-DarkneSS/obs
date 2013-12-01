# norootforbuild

%define cmake_version %(rpm -q --qf='%{VERSION}' cmake || echo NOTFOUND)
%define cmake_major %(echo %cmake_version | cut -f1 -d.)
%define cmake_minor %(echo %cmake_version | cut -f2 -d.)

Name:			sakura
Version:		2.3.8
Release:		0
Summary:		Terminal Emulator based on the VTE Library
Source:			http://pleyades.net/david/projects/sakura/sakura-%{version}.tar.bz2
Patch1:			sakura-icon.patch
Patch2:			sakura-cmake-usepkgconfig.patch
Patch4:         sakura-fix_pod2man.patch
URL:			http://pleyades.net/david/sakura.php
Group:			System/X11/Utilities
License:		GNU General Public License version 2 (GPL 2)
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	gcc gcc-c++ libstdc++-devel glibc-devel make vte-devel >= 0.20
BuildRequires:	pkgconfig gtk2-devel >= 2.6.0
BuildRequires:	cmake
BuildRequires:	gettext gettext-devel intltool
BuildRequires:	update-desktop-files
# to convert SVG to PNG:
BuildRequires:  ImageMagick
# to fix an rpmlint/python bug on Factory:
BuildRequires:	python

%description
sakura is a vte-based terminal emulator. It aims to provide a terminal
emulator that only depends on GTK and VTE. It uses a notebook to allow
multiple tabs in the same window.




Authors:
--------
    David Gómez Espinosa <david@pleyades.net>

%prep
%setup -q
%patch1
%__mv terminal-tango.svg sakura.svg
convert sakura.svg sakura.png
%if %cmake_major == 2 && %cmake_minor < 6
%patch2
%endif
%patch4
# replace hard-coded ICON_DIR
%__sed -i -r 's|^(\s*#define\s*ICON_DIR\s+").+("\s*)$|\1%{_datadir}/pixmaps\2|g' src/sakura.c

%build
%__mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
      -DCMAKE_BUILD_TYPE:STRING="Release" \
      -DCMAKE_C_FLAGS:STRING="" \
      -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -DNDEBUG" \
      ..

%__make %{?jobs:-j%{jobs}} VERBOSE=1 V=1
popd #build

%install
pushd build
%makeinstall
popd #build
%__rm -rf "%{buildroot}%{_datadir}/doc"

%suse_update_desktop_file -r "%{name}" System TerminalEmulator

%find_lang "%{name}"

%clean
%__rm -rf "%{buildroot}"

%files -f "%{name}.lang"
%defattr(-,root,root)
%doc AUTHORS GPL INSTALL
%{_bindir}/sakura
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%doc %{_mandir}/man1/sakura.1%{ext_man}

%changelog
# Local Variables:
# mode: rpm-spec
# tab-width: 3
# End:
