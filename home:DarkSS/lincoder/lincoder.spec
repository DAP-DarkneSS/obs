#
# spec file for package rexloader
#
# Copyright (c) 2009-2010 Gabriela Steren & Guillermo Steren (source), (c) 2012 Perlow Dmitriy A. (patches & spec file)
#
# Please submit bugfixes or comments via http://sourceforge.net/tracker/?group_id=260327&atid=1210261
#

Name:           lincoder
Version:        0.70c
Release:        0
Summary:        A Java frontend for MEncoder

Group:          Productivity/Multimedia/Video/Editors and Convertors
License:        GPL
URL:            http://lincoder.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Patch1:         q2templates.patch
Patch2:         jardir.patch

BuildRequires:  update-desktop-files
Requires:       MPlayer java-1_6_0-openjdk
BuildArch:      noarch

%description
Simple GUI plus support for custom command lines and templates, to batch encode files.
It can use srt subs and provides WinAVI-like features. Now with support for PSP encoding.

Features:
- Conversion to and from different video and audio formats.
- Customizable templates and command-line options.
- Video and audio filters to facilitate edition.
- Support for cutting and merging videos.
- Batch processing with multi-thread support.
- SRT subtitle hardcoding.

%prep
%setup -q
%patch1
%patch2

%build

%install
mkdir -p %{buildroot}%{_javadir}/%{name}/lib
cp -r ./dist/*.jar %{buildroot}%{_javadir}/%{name}/
cp -r ./dist/lib/*.jar %{buildroot}%{_javadir}/%{name}/lib/
%{__install} templates.properties %{buildroot}%{_javadir}/%{name}/
chmod -x %{buildroot}%{_javadir}/%{name}/templates.properties
mkdir -p %{buildroot}%{_bindir}
%{__install} ./dist_resources/LinCoder.sh %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} ./dist_resources/LinCoderIcon48.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name} %{name} LinCoder %{name} %{name}.png "Audiovideo;AudioVideoEditing;"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ./dist/README.TXT
%{_bindir}/%{name}
%{_javadir}/%{name}
%{_javadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Mar 05 2012 DA <dap.darkness@gmail.com> - 20120305-1
- Initial build is done with templates for Digma© Q2.

* Tue Oct 05 2010 DA <dap.darkness@gmail.com> - 20101005-1
- Version 0.70c was released.