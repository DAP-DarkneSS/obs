#
# spec file for package mcrypt-shell
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


Name:           mcrypt-shell
Version:        1.1.01
Release:        0
License:        GPL-3.0+
Summary:        Gui shell for linux mcrypt util written on Qt
Url:            http://sourceforge.net/projects/mcrypt-shell/
Group:          Productivity/File utilities
Source0:        http://surfnet.dl.sourceforge.net/project/mcrypt-shell/source/mcrypt-shell-source-v%{version}.7z

BuildRequires:  p7zip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(QtGui)

%description
Gui shell for linux mcrypt util written on Qt with integrated
file-manager, hex and text editor, compress function.
It uses symmetric encryption provided by mcrypt, with no
signature and crc writen to file (--no-openpgp --bare). No list
of encrypted files or logs are created, no temp files writed on
disk during process of encryption/decryption.
Included Manage keys dialog for storing used keys (it will
encrypted by password), or you can type "one-time" key.

%prep
7z x %{SOURCE0} -o%{_builddir}
%setup -DT -n %{name}

%build
qmake \
      QMAKE_STRIP="" \
      QMAKE_CFLAGS+="%{optflags}" \
      QMAKE_CXXFLAGS+="%{optflags}"

make V=1 %{?_smp_mflags}
lrelease %{name}.pro


%install
install -D %{name} %{buildroot}/%{_bindir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}/bin/translations/
cp translations/%{name}_*.qm %{buildroot}/%{_datadir}/%{name}/bin/translations/
install -D %{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -i %{name}


%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG GPLv3 README TODO
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop  
%{_datadir}/pixmaps/%{name}.png  
%{_bindir}/%{name}


%changelog
