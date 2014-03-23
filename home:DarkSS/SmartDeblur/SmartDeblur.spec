#
# spec file for package SmartDeblur
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


Name:           SmartDeblur
Version:        1.27+git.2013.01.10
Release:        0
License:        GPL-3.0
Summary:        A smart deblur program
Url:            http://smartdeblur.net
Group:          Productivity/Graphics/Bitmap Editors
# git@github.com:Y-Vladimir/SmartDeblur.git
Source0:        %{name}-%{version}.tar.xz
Patch0:         SmartDeblur-nonoss-updates.patch

BuildRequires:  fftw3-threads-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(QtCore) >= 4.7

%description
SmartDeblur is a user friendly and useful tool for restoring
blurry and defocused images. Blurry images are universal in
our life. There are many causes of that: camera shakes,
defocussing, artificial blur via photo editors like Photoshop
or Gimp. Many people think that blurring is an irreversible
operation and the information in this case is lost for good.
But it is not quite true - now you can restore your blurry
images using SmartDeblur. New release features a blind deblurring
module which can automatically identify and remove complicated
blur patterns in an image. Just load your image and click on the
"Analyze Blur" button - the rest will be done automatically!


%prep
%setup -q
%patch0


%build
%{_libdir}/qt4/bin/qmake \
                         src/%{name}.pro \
                         QMAKE_STRIP="" \
                         QMAKE_CFLAGS+="%{optflags}" \
                         QMAKE_CXXFLAGS+="%{optflags}"
%{__make} V=1 %{?_smp_mflags}


%install
install -m0755 -D \
        %{name} \
        %{buildroot}%{_bindir}/%{name}
%if 0%{?suse_version}
install -m0644 -D \
        src/Icons/Logo1.png \
        %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name} %{name} "A smart deblur program" %{name} %{name} "Graphics;RasterGraphics;Qt;"
%endif


%post
%if 0%{?suse_version} >= 1140
%desktop_database_post
%else
update-desktop-database &> /dev/null || :
%endif

%postun
%if 0%{?suse_version} >= 1140
%desktop_database_postun
%else
update-desktop-database &> /dev/null || :
%endif


%files
%defattr(-,root,root)
%doc README.md www/updates.xml
%{_bindir}/%{name}
%if 0%{?suse_version}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%endif

%changelog
