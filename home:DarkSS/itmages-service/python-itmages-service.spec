#
# spec file for package python-itmages-service
#
# Copyright (c) 2009-2012 ITmages: https://launchpad.net/itmages
#
# Please submit bugfixes or comments via https://bugs.launchpad.net/itmages
#

Name:           python-itmages-service
Version:        0.38
Release:        6
Summary:        ITmages service requests on DBus, offers to work with image hosting ITmages

License:        GPL-3.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/itmages/itmages-service
Source0:        %{name}-%{version}.tar.bz2
Patch1:         x-desktop.patch

Provides:       itmages-service python-itmages
BuildRequires:  python-base python
BuildRequires:  update-desktop-files fdupes
%if 0%{?suse_version} >= 1210
BuildRequires:  python-distribute
%else
BuildRequires:  python-setuptools
%endif
Requires:       python-base python-pycurl dbus-1-python python-gobject python-lxml python
BuildArch:      noarch

%description
ITmages service is a service that runs all the time in the system, and
service requests on bus DBus, offering to work with image hosting ITmages.
Using ITmages service you no longer need to write a uploader,
and deal with a hosting API. Just use DBus.

%prep
%setup -q
%patch1

%build
%{__python} setup.py build

%install
export PYTHONDONTWRITEBYTECODE=
%{__python} setup.py install -O1 --root=%{buildroot}
%fdupes -s %{buildroot}%{python_sitelib}/itmagesd
%suse_update_desktop_file itmagesd

%files
%defattr(-,root,root)
%doc README
%{_bindir}/itmagesd
%{python_sitelib}/*
%{_datadir}/itmages/testwindow.ui
%{_datadir}/doc/itmages/example/dbustestwin.py_
%{_datadir}/applications/itmagesd.desktop
%{_datadir}/dbus-1/services/org.freedesktop.ITmagesEngine.service
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/itmages/
%dir %{_datadir}/doc/itmages/
%dir %{_datadir}/dbus-1/services/
%dir %{python_sitelib}/itmagesd/
%dir %{_datadir}/doc/itmages/example/

%changelog
