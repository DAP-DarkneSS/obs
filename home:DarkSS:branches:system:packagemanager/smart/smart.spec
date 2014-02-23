#
# spec file for package smart
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           smart
BuildRequires:  deb kdelibs3-devel python python-devel python-xml rpm-python update-desktop-files
%if %{suse_version} < 1010
BuildRequires:  rpm-devel
%endif
%if %{suse_version} <= 1010
BuildRequires:  python-elementtree
%endif
Summary:        Smart Package Manager
Version:        1.4.1
Release:        1
Source:         http://launchpad.net/smart/trunk/%{version}/+download/smart-%{version}.tar.bz2
Source1:        distro.py
Source2:        smart-gtk.desktop
Source3:        smart-qt.desktop
Source4:        smart-ksmarttray.desktop
Source5:        channels.tar.bz2
Source99:       smart-rpmlintrc
# https://bugs.launchpad.net/smart/+bug/592503
Patch0:         smart-gtk-progress-nothread.diff
Patch4:         smart-ksmarttray.patch
Patch9:         smart-no-strict-aliasing.patch
Url:            https://launchpad.net/smart
Group:          System/Packages
License:        GPL v2 or later
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{suse_version} <= 1010
Requires:       python-elementtree
%endif
Requires:       python-xml
Requires:       rpm-python
Provides:       smart-addons = %{version}-%{release}
%py_requires

%description 
The Smart Package Manager project has the ambitious objective of
creating smart and portable algorithms for solving adequately the
problem of managing software upgrading and installation. This tool
works in all major distributions, and will bring notable advantages
over native tools currently in use (APT, APT-RPM, YUM, URPMI, etc).



Authors:
--------
    Gustavo Niemeyer <gustavo@niemeyer.net>

%package gui-gtk
License:        GPL v2 or later
Summary:        GTK2 Graphical User Interface for smart
Group:          System/Packages
Requires:       %{name} = %{version}-%{release}
Requires:       python-gtk
Requires:       xdg-utils
Provides:       smart-gui = %{version}
Obsoletes:      smart-gui < %{version}

%description gui-gtk
GTK2 Graphical User Interface for the smart package manager.



Authors:
--------
    Gustavo Niemeyer <gustavo@niemeyer.net>

%package gui-qt3
License:        GPL v2 or later
Summary:        QT3 Graphical User Interface for smart
Group:          System/Packages
Requires:       %{name} = %{version}-%{release}
Requires:       python-qt3
Requires:       xdg-utils
Provides:       smart-gui-qt = %{version}
Obsoletes:      smart-gui-qt

%description gui-qt3
QT3 Graphical User Interface for the smart package manager.



Authors:
--------
    Gustavo Niemeyer <gustavo@niemeyer.net>

%if %{suse_version} > 1010
%package ksmarttray
License:        GPL v2 or later
Summary:        KDE System Tray for the Smart Package Manager
Group:          System/Packages
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-gui = %{version}-%{release}

%description ksmarttray
KDE System Tray for the Smart Package Manager.




Authors:
--------
    Gustavo Niemeyer <gustavo@niemeyer.net>

%endif

%prep
%setup -q -n %{name}-%{version} -b 5
%patch0
%patch4
%patch9
%if %{suse_version} < 1010
echo '    sysconf.set("no-rpm-readHeaderFromFD", 3)' >> "%{SOURCE1}"
%endif

%build
export CFLAGS="%{optflags}"
%if %suse_version >= 1010
CFLAGS="$CFLAGS -fstack-protector"
%endif
export CXXFLAGS="$CFLAGS"
%__python ./setup.py build
%__make CC="%__cc $CFLAGS" -C contrib/smart-update
# only build rpmhelper on < 10.1, see #208534
%if %{suse_version} < 1010
pushd contrib/rpmhelper
%__python ./setup.py build
popd #contrib/rpmhelper
%endif
%if %{suse_version} > 1010
pushd contrib/ksmarttray
# add missing files or autotools will fail:
touch INSTALL NEWS README AUTHORS ChangeLog COPYING
. /etc/opt/kde3/common_options  
update_admin
./configure $configkde --disable-final
make %{?jobs:-j%{jobs}}
popd #contrib/ksmarttray
%endif

%install
%__python ./setup.py install --prefix="%{_prefix}" --root="%{buildroot}"
%__install -m0755 -D contrib/smart-update/smart-update \
    "%{buildroot}%{_sbindir}/smart-update"
%__install -m0644 -D "%{SOURCE2}" "%{buildroot}/usr/share/applications/%{name}-gtk.desktop"
%__install -m0644 -D "%{SOURCE3}" "%{buildroot}/usr/share/applications/%{name}-qt.desktop"
%if %{suse_version} > 1010
%__install -m0644 -D "%{SOURCE4}" "%{buildroot}/usr/share/applications/%{name}-ksmarttray.desktop"
%endif
%__install -m0644 -D smart/interfaces/images/smart.png "%{buildroot}/usr/share/pixmaps/smart.png"
%if %{suse_version} < 1010
pushd contrib/rpmhelper
%__python ./setup.py install --prefix="%{_prefix}" --root="%{buildroot}"
%__cp README ../../README.rpmhelper
popd
%endif
%__install -d "%{buildroot}%{_localstatedir}/lib/smart" \
    "%{buildroot}%{_prefix}/lib/smart" \
    "%{buildroot}%{_prefix}/lib/smart/plugins" \
    "%{buildroot}%{_sysconfdir}/smart/channels"
%__install -m0644 "%{SOURCE1}" "%{buildroot}%{_prefix}/lib/smart/distro.py"
%if %{suse_version} >= 1110 && %{suse_version} <= 1130 && %sles_version == 0
%__install -m0644 "$RPM_BUILD_DIR/channels"/%{suse_version}* "%{buildroot}%{_sysconfdir}/smart/channels/"
rename %{suse_version} opensuse "%{buildroot}%{_sysconfdir}/smart/channels"/*.channel
%endif
%if %{suse_version} > 1130 && %sles_version == 0
%__install -m0644 "$RPM_BUILD_DIR/channels"/factory* "%{buildroot}%{_sysconfdir}/smart/channels/"
rename factory opensuse "%{buildroot}%{_sysconfdir}/smart/channels"/*.channel
%endif

%if %{suse_version} > 1010 
%__install -D -m0755 contrib/servicemenus/kde_add_smart_channel.sh \
        "%{buildroot}/opt/kde3/bin/kde_add_smart_channel.sh"
%__install -D -m0644 contrib/servicemenus/add_smart_channel.desktop \
        "%{buildroot}/opt/kde3/share/apps/konqueror/servicemenus/add_smart_channel.desktop"
pushd contrib/ksmarttray
. /etc/opt/kde3/common_options
%makeinstall
popd #contrib/ksmarttray

for f in smart-gtk smart-qt smart-ksmarttray; do
    %suse_update_desktop_file "$f" System PackageManager
done

kde_post_install
%endif

%__install -D -m0644 contrib/bash-completion/smart-completion.sh \
    "%{buildroot}%{_sysconfdir}/bash_completion.d/%{name}.sh"

%find_lang %name

%if !%{opensuse_bs:1}0
%check
%__make test
%endif

%clean
%__rm -rf "%{buildroot}"

%files -f %{name}.lang
%defattr(-,root,root)
%doc HACKING IDEAS LICENSE README TODO
%if %{suse_version} < 1010
%doc README.rpmhelper
%endif
%doc doc/*
%{_mandir}/man8/*
%config %{_sysconfdir}/bash_completion.d/%{name}.sh
%dir %{_localstatedir}/lib/smart
%dir %{_prefix}/lib/smart
%dir %{_prefix}/lib/smart/plugins
%dir %{_sysconfdir}/smart
%if %sles_version == 0 && %{suse_version} >= 1110
%dir %{_sysconfdir}/smart/channels
%config %{_sysconfdir}/smart/channels/*.channel
%endif
%{_bindir}/%{name}
%{_sbindir}/%{name}-update
%config %{_prefix}/lib/smart/distro.py
%if %{suse_version} < 1010
%{py_sitedir}/rpmhelper.so
%endif
%{py_sitedir}/smart
%if %{suse_version} > 1010
%{py_sitedir}/*egg-info
%endif
%exclude %{py_sitedir}/smart/interfaces/gtk
%exclude %{py_sitedir}/smart/interfaces/qt
%{_datadir}/pixmaps/smart.png

%files gui-gtk
%defattr(-,root,root)
%{py_sitedir}/smart/interfaces/gtk
%{_datadir}/applications/smart-gtk.desktop

%files gui-qt3
%defattr(-,root,root)
%{py_sitedir}/smart/interfaces/qt
%{_datadir}/applications/smart-qt.desktop

%if %{suse_version} > 1010 
%files ksmarttray
%defattr(-,root,root)
%{_datadir}/applications/smart-ksmarttray.desktop
/opt/kde3/bin/ksmarttray
/opt/kde3/share/apps/ksmarttray
/opt/kde3/bin/kde_add_smart_channel.sh
/opt/kde3/share/apps/konqueror
/opt/kde3/share/icons/hicolor/48x48/apps/ksmarttray.png
%endif

%changelog
