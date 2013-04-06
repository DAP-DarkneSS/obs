#
# spec file for package [spectemplate]
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

#%{!?python_sitelib: %global python_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%define python3_sitelib %(python3 -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib())')

Name:           python3-nbxmpp
Version:        0.1
Release:        1
Summary:        XMPP library by Gajim team
Group:          Development/Libraries/Python

License:        GPL-3.0
URL:            http://python-nbxmpp.gajim.org/
Source0:        nbxmpp-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3

BuildRequires:  fdupes

%description
python-nbxmpp is a Python library that provides a way for Python applications to use Jabber/XMPP networks in a non-blocking way. This library is initialy a fork of xmpppy one, but using non-blocking sockets. 

%prep
%setup -q -n nbxmpp-%{version}


%build
python3 setup.py build

%install
python3 setup.py install -O1 --skip-build --root %{buildroot} --prefix=/usr
%fdupes %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{python3_sitelib}/nbxmpp-*.egg-info
%dir %{python3_sitelib}/nbxmpp/
%{python3_sitelib}/nbxmpp/*


%changelog
