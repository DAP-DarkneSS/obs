#
# spec file for package gnome-commander
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gnome-commander
Version:        1.4.0
Release:        0
Summary:        Nice and Fast File Manager for the GNOME Desktop
License:        GPL-2.0+
Group:          Productivity/File utilities
Url:            http://www.nongnu.org/gcmd/
Source:         http://download.gnome.org/sources/gnome-commander/1.4/%{name}-%{version}.tar.xz
BuildRequires:  chmlib-devel
# BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  intltool
BuildRequires:  libexiv2-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  libgsf-devel
BuildRequires:  libpoppler-devel
BuildRequires:  libxslt
BuildRequires:  python-devel
BuildRequires:  taglib-devel
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(unique-1.0)
BuildConflicts: brp-check-suse
BuildConflicts: post-build-checks
Recommends:     %{name}-lang
# For xdg-su
Recommends:     xdg-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GNOME Commander is a nice and fast file manager for the GNOME desktop.
In addition to basic file manager functions, the program is also an FTP
client and can browse SMB networks.

%lang_package
Requires:       %{name}

%prep
%setup -q
# translation-update-upstream

%build
%configure\
	--disable-static\
	--disable-scrollkeeper
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print
%suse_update_desktop_file gnome-commander
# Change sr@Latn to sr@latin
mv %{buildroot}%{_datadir}/locale/sr@Latn %{buildroot}%{_datadir}/locale/sr@latin
%find_lang %{name} %{?no_lang_C}
# calling /usr/lib/rpm/brp-suse.d/brp-25-symlink
# ERROR: link target doesn't exist
# (neither in build root nor in installed system):
# /usr/share/gnome/help/gnome-commander/de/figures/gnome-
# commander_options_network.png -> /usr/share/gnome/help/gnome
# -commander/C/figures/gnome-commander_options_network.png
# %%fdupes %%{buildroot}
# calling /usr/lib/rpm/brp-suse.d/brp-25-symlink
# ERROR: /usr/share/gnome/help/gnome-commander/C/figures/
# gnome-commander_options_network.png points to itself
# (as ../../C/figures/gnome-commander_options_network.png)
rm %{buildroot}%{_datadir}/gnome/help/gnome-commander/C/figures/gnome-commander_options_network.png

%if 0%{?suse_version} > 1130

%post
%desktop_database_post
%endif

%if 0%{?suse_version} > 1130

%postun
%desktop_database_postun
%endif

%files
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/%{name}/
%doc %{_datadir}/gnome/help/%{name}/C/
%dir %{_datadir}/omf/
%dir %{_datadir}/omf/%{name}/
%doc %{_datadir}/omf/%{name}/%{name}-C.omf
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/gnome-commander
%{_libdir}/gnome-commander
%doc %{_mandir}/man1/gnome-commander.1.gz

%files lang -f %{name}.lang

%changelog
