#
# spec file for package wavegain
#
# Copyright (c) 2014 Packman team: http://packman.links2linux.org/
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.links2linux.org/
#

Name:           wavegain
Version:        1.3.1
Release:        0
License:        LGPL-2.1+
Summary:        A command line tool to normalize sound files
Url:            http://rarewares.org/others.php
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Source:         http://www.rarewares.org/files/others/%{name}-%{version}srcs.zip

BuildRequires:  dos2unix
BuildRequires:  unzip
BuildRequires:  pkgconfig(sndfile)
# x86 asm, so
ExcludeArch:    %arm

%description
%{name} is a ReplayGain for wave files. It normalizes sound files.

%prep
%setup -q -n WaveGain-%{version}
dos2unix COPYING


%build
gcc %{optflags} -fno-strict-aliasing *.c -o wavegain -DHAVE_CONFIG_H -lm


%install
install -Dm755 \
        %{name} \
        %{buildroot}/%{_bindir}/%{name}


%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/%{name}

%changelog
