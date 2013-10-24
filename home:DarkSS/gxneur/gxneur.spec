#
# spec file for package gxneur
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gxneur
Version:        0.16.0
Release:        0
License:        GPL-2.0+
Summary:        GTK Front-end for XNeur
Url:            http://www.xneur.ru
Group:          System/X11/Utilities
Source0:        http://dists.xneur.ru/release-%{version}/tgz/%{name}-%{version}.tar.bz2
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(xneur) = %{version}
BuildRequires:  pkgconfig(xnconfig) = %{version}
Requires:       xneur = %{version}
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
gXNeur is a GTK front-end for XNeur keyboard layout switcher.

%lang_package

%prep
%setup -q

%build
%configure \
    --without-appindicator \
    --without-gconf
make %{?_smp_mflags}

%install
%make_install
# Create desktop-file.
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=gXNeur
GenericName=Keyboard Layout Switcher
GenericName[ru]=Переключатель раскладки клавиатуры
Type=Application
Exec=gxneur
Icon=gxneur
Categories=Utility;X-SuSE-DesktopUtility;GTK;
Comment=Keyboard Layout Switcher
Comment[ru]=Переключатель раскладки клавиатуры
StartupNotify=false
Terminal=false
EOF
%find_lang %{name}
%suse_update_desktop_file -i %{name}

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}*
%doc %{_mandir}/man?/*

%files lang -f %{name}.lang

%changelog
