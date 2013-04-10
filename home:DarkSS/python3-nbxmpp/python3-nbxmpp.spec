#
# spec file for package python3-nbxmpp
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

%define python3_sitelib %(python3 -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib())')

Name:           python3-nbxmpp
Version:        0.1
Release:        1
License:        GPL-3.0
Summary:        XMPP library by Gajim team
Url:            http://python-nbxmpp.gajim.org/
Group:          Development/Libraries/Python
Source0:        nbxmpp-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  python3
BuildRequires:  python3-devel
BuildArch:      noarch
Requires:       python3

%description
Python-nbxmpp is a Python library that provides a way for Python
applications to use Jabber/XMPP networks in a non-blocking way. This
library is initialy a fork of xmpppy one, but using non-blocking sockets.

%package doc
Summary:        Nbxmpp Documentation

%description doc
This packages provides documentation of Nbxmpp API.

%prep
%setup -q -n nbxmpp-%{version}

%build
python3 setup.py build

%install
python3 setup.py install -O1 --skip-build --root=%{buildroot} --prefix=%{_prefix}
%fdupes %{buildroot}%{python3_sitelib}

mkdir -p %{buildroot}%{_docdir}/%{name}-doc
cp -r doc/* %{buildroot}%{_docdir}/%{name}-doc
%fdupes %{buildroot}%{_docdir}

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{python3_sitelib}/nbxmpp-*.egg-info
%{python3_sitelib}/nbxmpp/

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}-doc