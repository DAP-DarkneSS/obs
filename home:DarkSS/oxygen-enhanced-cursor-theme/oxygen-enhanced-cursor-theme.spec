#
# spec file for package oxygen-enhanced-cursor-theme
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         oname +OxygenE

Name:           oxygen-enhanced-cursor-theme
Version:        0.2
Release:        0
Summary:        +OxygenE X11 Mouse Theme
License:        LGPL-2.1 or LGPL-3.0
Group:          System/GUI/KDE
Url:            http://kde-look.org/content/show.php/?content=159354
Source0:        http://kde-look.org/CONTENT/content-files/159354-%{oname}.tar.gz

BuildRequires:  kde4-filesystem
BuildArch:      noarch

%description
+OxygenEnhanced is a +1Multisized X11 Mouse Theme; +1Multisized is my
concept for cursor themes with colorful pointers or pointer with colored
backgrounds, and is accomplished by defining the colors that we will use
in our cursor theme and set the initial size of the cursor, increasing
one pixel between each of the colors. This is my original idea.

For this X11 mouse theme, I defined six colors for pointers, and the
initial cursor size is 32 pixels. Therefore we have cursors of Green 32,
Yellow 33, Red 34, Blue 35, Aqua 36 and Fuchsia 37 pixels. There is a
5-pixel difference between the initial size and the final size of the
cursor. Simply imperceptible difference, and will be less if we choose
4 colors, or a larger initial size of the cursor.

%prep
%setup -q -n %{oname}

%build

%install
mkdir -p %{buildroot}%{_kde4_iconsdir}/%{oname}
cp -rf ./* %{buildroot}%{_kde4_iconsdir}/%{oname}

%files
%defattr(-,root,root)
%{_kde4_iconsdir}/%{oname}

%changelog
