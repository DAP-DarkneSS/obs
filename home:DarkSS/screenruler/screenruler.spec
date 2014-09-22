#
# spec file for package screenruler
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


Name:           screenruler
Version:        0.9.6
Release:        0
Summary:        GNOME screen ruler
License:        GPL-2.0+
Group:          Applications/Engineering
Url:            https://launchpad.net/screenruler/
Source0:        http://launchpad.net/screenruler/trunk/0.9.6/+download/%{name}-0.9.6.tar.gz
Source1:        screenruler.desktop
#PATCH-FIX-UNKNOWN for ruby 1.9 users.
Patch0:         screenruler-ruby19.patch

BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       ruby
Requires:       rubygem-atk
Requires:       rubygem-cairo
Requires:       rubygem-gettext
Requires:       rubygem-glib2
Requires:       rubygem-gtk2
Requires:       rubygem-pango
Provides:       gruler
BuildArch:      noarch

%description
Screenruler is a small GNOME based utility that allows you to measure objects
on your desktop. It can be used to take both horizontal and vertical
measurement in 6 different metrics: pixels, centimeters, inches, picas, points,
and as a percentage of the ruler’s length.

%prep
%setup -q -n %{name}
%patch0 -p0 -b ruby19

%build

%install

mkdir -p %{buildroot}

cat << EOF > screenruler
#!/bin/bash

cd %{_datadir}/%{name}
ruby ./screenruler.rb
EOF
chmod 0755 screenruler

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p screenruler %{buildroot}%{_bindir}/
cp -p screenruler-icon*.png %{buildroot}%{_datadir}/pixmaps/
cp -pr utils *.rb screenruler*.* *.glade %{buildroot}%{_datadir}/%{name}/
cd %{buildroot}%{_datadir}/pixmaps
 ln -s ./screenruler-icon-32x32.png screenruler-icon.png

%suse_update_desktop_file -i %{name}
%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING
%{_bindir}/screenruler
%{_datadir}/screenruler/
%{_datadir}/pixmaps/screenruler-icon*.png
%{_datadir}/applications/*.desktop

%changelog
