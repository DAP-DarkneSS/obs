#
# spec file for package plasma-wallpaper-dreamdesktop
#
# Copyright (c) 2013 Buschmann <buschmann23@opensuse.org>
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

Name:           plasma-wallpaper-dreamdesktop
Version:        0.3.0
Release:        1
License:        GPL-3.0+
Summary:        Animated Wallpapers for KDE
Url:            http://www.jarzebski.pl/projekty/dreamdesktop.html
Group:          System/GUI/KDE
Source0:        http://www.jarzebski.pl/dreamdesktop/%{name}-%{version}.tar.bz2
Source1:        copyright
# Could be found in the ubuntu package from ppa:
# https://launchpad.net/~blueleaflinux/+archive/ppa/+sourcepub/2802609/+listing-archive-extra

BuildRequires:  kdebase4-workspace-devel >= 4.8.0
BuildRequires:  libffmpeg-devel
BuildRequires:  update-desktop-files

%kde4_runtime_requires

%description
DreamDesktop is an animated video wallpaper plugin for KDE4 plasma desktop.

Be sure that you have enough RAM and powerful CPU to run it!

Videos could be found at http://www.dreamsceneseven.com/animatedwallpapers.htm
or at http://www.dreamscene.org/gallery.php?Cmd=Show&site=all#downloadgallery

%prep
%setup -q -n %{name}
%{__install} %{SOURCE1} .

%build
%cmake_kde4 -d builddir
%make_jobs

%install
cd builddir
%make_install
cd ..
%suse_update_desktop_file -n %{buildroot}%{_datadir}/kde4/services/dreamdesktop.desktop
%kde_post_install


%files
%defattr(644,root,root,755)
%doc CHANGELOG README.ENGLISH README.POLSKI copyright
%_kde4_modulesdir/*.so
%_kde4_servicesdir/*.desktop
%_kde4_appsdir/dreamdesktop

%changelog
