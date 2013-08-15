#
# spec file for package python-nbxmpp
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


# To buid at SLE <= 11 SP2.
%if 0%{?suse_version} < 1140
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           python-nbxmpp
Version:        0.1
Release:        0
Summary:        XMPP library by Gajim team
License:        GPL-3.0
Group:          Development/Libraries/Python
Url:            http://python-nbxmpp.gajim.org/
Source0:        nbxmpp-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  python-devel

# To buid at SLE <= 11 SP2.
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1140
BuildArch:      noarch
%endif

%description
Python-nbxmpp is a Python library that provides a way for Python
applications to use Jabber/XMPP networks in a non-blocking way. This
library is initialy a fork of xmpppy one, but using non-blocking sockets.

%package doc
Summary:        Nbxmpp Documentation
Group:          Development/Libraries/Python
# ^ To buid at SLE <= 11 SP2.

%description doc
This packages provides documentation of Nbxmpp API.

%prep
%setup -q -n nbxmpp-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot} --prefix=%{_prefix}
%fdupes %{buildroot}%{python_sitelib}

%files
%defattr(-,root,root)
%{python_sitelib}/nbxmpp-*.egg-info
%{python_sitelib}/nbxmpp/

%files doc
%defattr(-,root,root)
%doc ChangeLog COPYING README doc/*

%changelog
