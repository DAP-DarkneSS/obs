#
# spec file for package bundle-lang-kde-be
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


%define pack_summ Belarusian translations for a group of KDE applications

%define pack_desc This package groups translations for a dozen of KDE \
programs into Belarusian language, not split out into extra packages.

Name:           bundle-lang-kde-be
Version:        4.svn

Release:        0
License:        MIT
Summary:        %{pack_summ}
Url:            http://mova.org/lists/listinfo/i18n
Group:          System/Localization
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
Requires:       kde4-l10n-be
Provides:       locale(kdebase4-openSUSE:be)
BuildArch:      noarch

%description
%{pack_desc}

%package -n kde4-l10n-be
Summary:        %{pack_summ}
Requires:       bundle-lang-kde-be
Provides:       locale(kdelibs4:be)

%description -n kde4-l10n-be
%{pack_desc}

%prep
%setup -q
rm -rf messages/*office*

%build
find messages/ -name "*.po" -exec msgfmt -o {}.mo {} ';'
find messages/ -name "*.mo" -exec sh -c 'mv "$0" "${0%.po.mo}.mo"' {} \;

%install
mkdir -p %{buildroot}%{_datadir}/locale-bundle/be/LC_MESSAGES
%{__install} messages/*/*.mo %{buildroot}%{_datadir}/locale-bundle/be/LC_MESSAGES

mkdir -p %{buildroot}%{_datadir}/locale/be
%{__install} messages/entry.desktop %{buildroot}%{_datadir}/locale/be
%{__install} messages/flag.png %{buildroot}%{_datadir}/locale/be

%fdupes -s %{buildroot}%{_datadir}/locale-bundle/be

%files
%defattr(-,root,root)
%dir %{_datadir}/locale-bundle
%dir %{_datadir}/locale-bundle/be
%dir %{_datadir}/locale-bundle/be/LC_MESSAGES
%lang(be) %{_datadir}/locale-bundle/be/LC_MESSAGES/*.mo

%files -n kde4-l10n-be
%defattr(-,root,root)
%attr(644,root,root) %{_datadir}/locale/be/entry.desktop
%{_datadir}/locale/be/flag.png

%changelog
