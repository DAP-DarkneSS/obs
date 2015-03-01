#
# spec file for package dontwaitup
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           dontwaitup
Version:        14.08.12
Release:        0
Summary:        Do something else while your PC is completing a job
License:        GPL-3.0
Group:          Productivity/Other
Url:            https://launchpad.net/dontwaitup
Source0:        http://sourceforge.net/projects/dontwaitup/files/%{version}/dontwaitup_%{version}.tar.gz
Patch0:         patch.diff

BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libgio-2_0-0
BuildRequires:  python-distutils-extra
BuildRequires:  pkgconfig(python2)
BuildRequires:  gobject-introspection
Requires:       python-gtk
BuildArch:      noarch
Requires(post):   glib2-tools
Requires(postun): glib2-tools
%glib2_gsettings_schema_requires

%description
DontWaitUp catches windows which close, change name or are resized in
order to understand when a process has completed and then do an action
like shut down, restart, sleep, hibernate, play an alarm sound, show a
notification or run whatever command you need to run.

%prep
%setup -q -n %{name}
%patch0

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

%fdupes -s %{buildroot}%{python_sitelib}

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING debian/changelog
%{_bindir}/%{name}
%{python_sitelib}/%{name}*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml

%changelog
