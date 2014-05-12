#
# spec file for package syspeek
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


Name:           syspeek
Version:        0.2+bzr.12
Release:        0
Summary:        A system monitor indicator
License:        GPL-3.0+
Group:          System/GUI/GNOME
Url:            https://launchpad.net/syspeek

Source0:         https://launchpad.net/~nilarimogard/+archive/webupd8/+files/syspeek_0.3~bzr12~webupd8~trusty2.tar.gz
# PATCH-FIX-OPENSUSE to make settings openable.
Patch0:         syspeek-file-not-found.patch
# PATCH-FEATURE-OPENSUSE to make system monitor openable at KDE.
Patch1:         syspeek-kde.patch

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
# Not really needed but setup spams errors.
# BuildRequires:  python-appindicator
# BuildRequires:  python-gtk
# BuildRequires:  python-gobject
BuildRequires:  python-distutils-extra
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(python2)
Requires:       python-appindicator
Requires:       python-gobject
Requires:       python-gtk
Recommends:     %{name}-autostart
BuildArch:      noarch

%description
SysPeek is a system monitor indicator that displays CPU usage,
memory usage, swap usage, disk usage and network traffic.

%package        autostart
Summary:        SysPeek — autostart
Requires:       %{name}

%description    autostart
Run SysPeek automatically at system start.

%prep
%setup -q -n syspeek-bzr
%patch0
%patch1

%build
python \
       setup.py \
       build

%install
install -D -m 644 \
        data/icons/256x256/apps/%{name}.svg \
        %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}
%if 0%{?suse_version}
%suse_update_desktop_file -i %{name} -r "GNOME;Utility;DesktopUtility;"
%endif

python \
       setup.py \
       install \
       -O1 \
       --skip-build \
       --root=%{buildroot} \
       --prefix=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/22x22/status
cp data/icons/22x22/status/*.svg \
   %{buildroot}%{_datadir}/icons/hicolor/22x22/status

%fdupes -s %{buildroot}%{python_sitelib}

# Let's use %%doc macro.
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{python_sitelib}/%{name}*
%{_datadir}/%{name}
%if 0%{?suse_version}
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/scalable/apps/%{name}
%{_datadir}/icons/hicolor/22x22/status/%{name}*

%files autostart
%defattr(-,root,root)
%{_sysconfdir}/xdg/autostart/%{name}.desktop

%changelog
