#
# spec file for package gxneur
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


Name:           gxneur
Version:        0.19.0
Release:        0
Summary:        GTK Front-end for XNeur
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://www.xneur.ru
Source0:        Source0:        https://github.com/AndrewCrewKuznetsov/xneur-devel/blob/master/dists/%{version}/%{name}_%{version}.orig.tar.gz?raw=true#/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(xnconfig) = %{version}
BuildRequires:  pkgconfig(xneur) = %{version}
Requires:       xneur = %{version}
Recommends:     %{name}-lang
Provides:       xneur-gui

%description
gXNeur is a GTK front-end for XNeur keyboard layout switcher.

%lang_package

%prep
%setup -q

%build
# NOTE: remove at version bump this workaround vs. utils.c:46:18: error:
# 'total_mod_keys' defined but not used [-Werror=unused-const-variable=]
%if 0%{?suse_version} > 1320
export CPPFLAGS="%{optflags} -Wno-misleading-indentation -Wno-unused-variable"
%endif
%configure \
    --without-appindicator \
    --without-gconf
make V=1 %{?_smp_mflags}

%install
%make_install V=1
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
%{_mandir}/man?/*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
