#
# spec file for package salutatoi
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


%define pack_desc Salut à Toi (French for "hello you") is a multi- \
frontends, multi-purposes communication tool, based on the XMPP \
standard. It features: \
 * instant messaging, \
 * microblogging, \
 * file sharing, \
 * games, \
 * group permissions (share what you want \
   with the people you choose), \
 * interaction with other networks \
   (IRC, StatusNet, other XMPP networks), \
 * email client access (use your favorite mail user agent \
   (MUA) to communicate on the supported networks), \
 * extensible design.

Name:           salutatoi
Version:        0.4.1
Release:        0
Summary:        Salut à Toi XMPP-based communication and sharing tool
License:        AGPL-3.0+
Group:          Productivity/Networking/Instant Messenger
Url:            http://www.salut-a-toi.org
Source0:        ftp://ftp.goffi.org/sat/sat-%{version}.tar.bz2

BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-setuptools >= 0.6.49
BuildRequires:  python-wxWidgets
BuildRequires:  pkgconfig(pygobject-2.0)
BuildRequires:  pkgconfig(python2)
BuildArch:      noarch

%description
%{pack_desc}


%lang_package


%package        -n sat-xmpp-core
Summary:        Salut à Toi XMPP — Core
Requires:       python-Twisted
Requires:       python-dateutil
Requires:       python-wokkel
Recommends:     %{name}-lang
Recommends:     sat-xmpp-jp
Recommends:     sat-xmpp-wix

%description    -n sat-xmpp-core
%{pack_desc}


%package        -n sat-xmpp-jp
Summary:        Salut à Toi XMPP — Command-line interface
Requires:       sat-xmpp-core = %{version}

%description    -n sat-xmpp-jp
%{pack_desc}


%package        -n sat-xmpp-wix
Summary:        Salut à Toi XMPP — WxPython graphical user interface
Requires:       sat-xmpp-core = %{version}
Requires:       python-wxWidgets

%description    -n sat-xmpp-wix
%{pack_desc}

%prep
%setup -q -n sat-%{version}
dos2unix README*


%build
python \
       setup.py \
       build

%install
python \
       setup.py \
       install \
       -O1 \
       --skip-build \
       --root=%{buildroot} \
       --prefix=%{_prefix}

%find_lang sat %{?no_lang_C}

# No required python-urwid-satext package.
rm %{buildroot}%{_bindir}/primitivus
rm -rf %{buildroot}%{python_sitelib}/sat_frontends/primitivus

%fdupes -s %{buildroot}%{python_sitelib}

# W: non-executable-script / W: script-without-shebang.
chmod +x %{buildroot}%{python_sitelib}/sat*/*.py
chmod +x %{buildroot}%{python_sitelib}/sat*/*/*.py
chmod +x %{buildroot}%{python_sitelib}/sat/sat.tac
chmod -x %{buildroot}%{python_sitelib}/sat*/__init__.py
chmod -x %{buildroot}%{python_sitelib}/sat*/*/__init__.py

# Let's use %%doc macro.
rm -rf %{buildroot}%{_datadir}/doc

# Symlink points to BuildRoot.
rm %{buildroot}%{_bindir}/sat
ln -s %{python_sitelib}/sat/sat.sh %{buildroot}%{_bindir}/sat

# E: file-contains-buildroot.
sed -i \
    '/^TAP_PATH/c TAP_PATH="%{python_sitelib}/sat/"' \
    "%{buildroot}%{python_sitelib}/sat/sat.sh"


%files -n sat-xmpp-core
%defattr(-,root,root)
%doc CHANGELOG CONTRAT_SOCIAL* COPYING README*
%{_bindir}/sat
%{python_sitelib}/sat*


%files -n sat-xmpp-jp
%defattr(-,root,root)
%{_bindir}/jp


%files -n sat-xmpp-wix
%defattr(-,root,root)
%{_bindir}/wix


%files lang -f sat.lang

%changelog
