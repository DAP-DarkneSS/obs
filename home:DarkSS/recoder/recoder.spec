#
# spec file for package recoder
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


%define bitbucket_hash 61d3315a38f0

Name:           recoder
Version:        0.2.0
Release:        0
Summary:        A tool to decode from mojibakes to Cyrillic text
License:        SUSE-Freeware
# Group:          Productivity/Networking/Instant Messenger
Url:            https://bitbucket.org/dkuryakin/recoder
Source0:        https://bitbucket.org/dkuryakin/recoder/get/v%{version}.tar.bz2
Source1:        %{name}.sh

BuildRequires:  fdupes
BuildRequires:  python-setuptools
BuildRequires:  python-devel
BuildArch:      noarch

%description
When downloaded, html pages are often incorrectly
decoded. For example, CP1251 page can be interpreted
as ISO8859 page. Supports only Cyrillic at the moment.
echo "Îñíîâíàÿ Îëèìïèéñêàÿ äåðåâíÿ â" | recoder
http://habrahabr.ru/post/216969


%prep
%setup -q -n dkuryakin-recoder-%{bitbucket_hash}


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
install -D %{SOURCE1} %{buildroot}%{_bindir}/%{name}


%check
# `python setup.py test` requires Internet access.
echo "Îñíîâíàÿ Îëèìïèéñêàÿ äåðåâíÿ â" | \
                      %{buildroot}%{_bindir}/%{name}


%files
%defattr(-,root,root)
%doc README.rst
%{python_sitelib}/%{name}*
%{_bindir}/%{name}


%changelog
