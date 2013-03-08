#
# spec file for package pyload
#
# Copyright (c) 2009-2012 pyLoad Team (source),
# (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# https://github.com/pyload/pyload/issues
#

Name:           pyload
Version:        0.4.9
Release:        1
Summary:        Downloadtool for One-Click-Hoster written in python

License:        GPL-3.0+
Url:            http://pyload.org/
Group:          Productivity/Networking/Other
# Source0:        pyload-src-v0.4.9.zip
Source0:        http://get.pyload.org/get/src/%{version}
Source1:        http://bitbucket.org/ranan/pyload-dist/raw/bf705af8f412/debian/pyload/usr/share/applications/pyload-gui.desktop
Source2:        http://bitbucket.org/ranan/pyload-dist/raw/bf705af8f412/debian/pyload/usr/share/applications/pyload.desktop
Source3:        http://bitbucket.org/ranan/pyload-dist/raw/bf705af8f412/debian/pyload/usr/share/pixmaps/pyload-gui.png
Source4:        http://bitbucket.org/ranan/pyload-dist/raw/bf705af8f412/debian/pyload/usr/share/pixmaps/pyload.svg

Patch0:         recursion.patch

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files

Requires:       python
Requires:       python-pycurl

Recommends:     js
Recommends:     python-Beaker
Recommends:     python-Jinja2
Recommends:     python-flup
Recommends:     python-imaging
Recommends:     python-pyOpenSSL
Recommends:     python-pycrypto
Recommends:     tesseract

%description
pyLoad is a fast, lightweight and full featured download manager for many
One-Click-Hoster, container formats like DLC, video sites or just plain
http/ftp links. It aims for low hardware requirements and platform independence
to be runnable on all kind of systems (desktop pc, netbook, NAS, router).

Despite its strict restriction it is packed full of features just like
webinterface, captcha recognition, unrar and much more.

pyLoad is divided into core and clients, to make it easily remote accessible.
Currently there are a webinterface, command line interface, a GUI written in
Qt and an Android client.

Some main advantages at a glance:
 * low hardware requirements;
 * features many One-Click-Hoster;
 * including premium support, captcha recognition, reconnect feature;
 * DLC, CCF, RSDF support;
 * easily remote accessible via webinterface or GUI.

%package gui
Summary:        PyQt4 GUI for pyLoad
Requires:       %{name}
Requires:       python-qt4
Recommends:     python-notify

%description gui
pyLoad python-Qt4 Graphical User Interface.

%prep
unzip -q %{SOURCE0} -d %{_builddir}
%patch0

# This python bytecode file (.pyo/.pyc) is not accompanied by its original
# source file (.py)
rm %{_builddir}/pyload/module/plugins/container/DLC_*.pyc

# This script has wrong end-of-line encoding, usually caused by creation or
# modification on a non-Unix system. It will prevent its execution.
find %{name}/ -name "*.py" -exec dos2unix -q {} ';'

# This text file contains a shebang or is located in a path dedicated for
# executables, but lacks the executable bits and cannot thus be executed.  If
# the file is meant to be an executable script, add the executable bits,
# otherwise remove the shebang or move the file elsewhere.
find %{name}/module/ -name "*.py" -exec sed -i -e  '/^#!\s\?\/usr\/bin\/\(env\s\)\?python$/d' {} ';'

%build

%install
mkdir -p %{buildroot}/opt/%{name}
cp -r pyload/* %{buildroot}/opt/%{name}

mkdir -p %{buildroot}%{_datadir}/pixmaps
%{__install} %{SOURCE3} %{buildroot}%{_datadir}/pixmaps
%{__install} %{SOURCE4} %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{_bindir}
ln -s /opt/pyload/pyLoadCore.py %{buildroot}%{_bindir}/pyLoadCore
ln -s /opt/pyload/pyLoadCli.py %{buildroot}%{_bindir}/pyLoadCli
ln -s /opt/pyload/pyLoadGui.py %{buildroot}%{_bindir}/pyLoadGui

%suse_update_desktop_file -i %{name}
%suse_update_desktop_file -i %{name}-gui

%fdupes -s %{buildroot}/opt/%{name}

%files
%defattr(-,root,root)
%doc %{name}/README %{name}/LICENSE
/opt/%{name}
%attr(755,root,root) %{_bindir}/pyLoadC*
%attr(644,root,root) %{_datadir}/pixmaps/%{name}*
%{_datadir}/applications/%{name}.desktop
%exclude /opt/%{name}/pyLoadGui.py
%exclude /opt/%{name}/module/gui

%files gui
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/pyLoadGui
/opt/%{name}/pyLoadGui.py
/opt/%{name}/module/gui
%{_datadir}/applications/%{name}-gui.desktop

%changelog
