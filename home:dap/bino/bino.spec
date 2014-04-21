# vim: set sw=4 ts=4 et nu:
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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

Name:           bino
Version:        1.4.2
Release:        0
Summary:        Video Player with 3D and Multi-Display Video Support
Source:         http://download-mirror.savannah.gnu.org/releases/bino/bino-%{version}.tar.xz
Patch1:         bino-1.4.2-openal-fix.patch
URL:            http://www.nongnu.org/bino/
Group:          Productivity/Multimedia/Video/Players
License:        GPL-2.0+
BuildRoot:      %{_tmppath}/build-%{name}-%{version}
BuildRequires:  libqt4-devel
BuildRequires:  glew-devel >= 1.6.0
%if 0%{?suse_version} > 1220
BuildRequires:  pkgconfig(glu)
%endif
BuildRequires:  ffmpeg-devel
BuildRequires:  libass-devel
BuildRequires:  openal-devel
BuildRequires:  gcc-c++ make glibc-devel pkgconfig
BuildRequires:  autoconf automake libtool
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  equalizer-devel
BuildRequires:  xz
Requires:       %install_info_prereq

%description
Bino is a video player with two special features:
* support for 3D videos, with a wide variety of input and output formats.
* support for multi-display video, e.g. for powerwalls, Virtual Reality
  installations and other multi-projector setups.

%prep
%setup -q
%if 0%{?suse_version} < 1220
%patch1 -p1
%endif

%build
%if 0%{?suse_version} >= 1230
# hangle 'multiple definition of'
export LDFLAGS="%{optflags} -zmuldefs"
%endif
%configure \
    --with-equalizer \
    --disable-silent-rules 

%__make %{?_smp_flags}

%install
%makeinstall

%__rm -rf "%{buildroot}%{_datadir}/doc"

%suse_update_desktop_file -r "%{name}" AudioVideo Player
%find_lang "%{name}" || echo -n >"%{name}.lang"

%post
%install_info --info-dir="%{_infodir}" "%{_infodir}/bino".info*

%postun
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/bino".info*

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files -f "%{name}.lang"
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%doc doc/*.html doc/*.jpg doc/*.png
%{_bindir}/bino
%doc %{_mandir}/man1/bino.1%{ext_man}
%doc %{_infodir}/bino.info%{ext_info}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/apps/bino.*

%changelog

