#
# spec file for package smillaenlarger
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


Name:           smillaenlarger
Version:        0.9.0
Release:        0
License:        GPL-3.0+
Summary:        A graphical tool to resize bitmaps in high quality
Url:            http://sourceforge.net/projects/imageenlarger/
Group:          Productivity/Graphics/Bitmap Editors
Source0:        http://kent.dl.sourceforge.net/project/imageenlarger/imageenlarger/SmillaEnlarger%20Release%20%{version}/SmillaEnlarger_%{version}_source.zip
Source1:        smillaenlarger.desktop

BuildRequires:  gcc-c++
BuildRequires:  qt-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SmillaEnlarger is a small graphical tool ( based on Qt ) to resize,
especially magnify bitmaps in high quality.

%prep
%setup -q -n SmillaEnlarger_%{version}_source/SmillaEnlargerSrc
sed \
    -i -e \
    's|0.8.9|%{version}|g' \
    EnlargerDialog.cpp

%build
%{_libdir}/qt4/bin/qmake \
                         ImageEnlarger.pro \
                         QMAKE_STRIP="" \
                         QMAKE_CFLAGS+="%{optflags}" \
                         QMAKE_CXXFLAGS+="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__install} -m0755 -D SmillaEnlarger %{buildroot}%{_bindir}/smillaenlarger
%{__install} -m0644 -D smilla.png %{buildroot}%{_datadir}/pixmaps/smillaenlarger.png
%suse_update_desktop_file -i %{name}

%post
%if 0%{?suse_version} >= 1140
%desktop_database_post
%else
update-desktop-database &> /dev/null || :
%endif

%postun
%if 0%{?suse_version} >= 1140
%desktop_database_postun
%else
update-desktop-database &> /dev/null || :
%endif

%files
%defattr(-,root,root)
%doc docs/* help/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
