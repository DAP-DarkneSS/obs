#
# spec file for package anki
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

%bcond_with tests

Name:           anki
Version:        2.0.33
Release:        0
License:        AGPL-3.0
Summary:        Intelligent Spaced-Repetition Memory Training Program
Url:            http://ankisrs.net
Group:          Productivity/Text/Utilities
Source0:        http://ankisrs.net/download/mirror/%{name}-%{version}.tgz
Source1:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE - anki-Makefile.patch -- Fix installation
Patch0:         %{name}-Makefile.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
%if %{with tests}
BuildRequires:  python-nose
BuildRequires:  python-beautifulsoup
BuildRequires:  python-sqlalchemy
%endif
BuildRequires:  python-devel
BuildRequires:  python-httplib2
BuildRequires:  python-qt4-devel
BuildRequires:  python-PyAudio
BuildRequires:  python-setuptools
BuildRequires:  python-simplejson
BuildRequires:  shared-mime-info
Requires:       python-send2trash
Requires:       python-sip
Requires:       python-qt4
Requires:       python-beautifulsoup
Requires:       python-httplib2
Suggests:       MPlayer
Suggests:       lame
Suggests:       sox
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Anki is a spaced repetition system (SRS). It helps you remember things by
intelligently scheduling reviews, so that you can learn a lot of information
with the minimum amount of effort.

Anki is a program which makes remembering things easy. Because it's a
lot more efficient than traditional study methods, you can either
greatly decrease your time spent studying, or greatly increase
the amount you learn.

Anyone who needs to remember things in their daily life can benefit
from Anki. Since it is content-agnostic and supports images, audio,
videos and scientific markup (via LaTeX), the possibilities are
endless.
For example:

    Learning a language
    Studying for medical and law exams
    Memorizing people's names and faces
    Brushing up on geography
    Mastering long poems
    Even practicing guitar chords!

Anki store all Settings default in

    ~/Documents/Anki/

If you wish to change Anki Language, sync and quit Anki

    cd ~/Documents/Anki

    mv prefs.db prefsold.db

Start Anki, say which Language you wish to use and
import your old Profile.

%prep
%setup -q
%patch0

# SED-FIX-OPENSUSE -- Don't check for new updates.
sed -i -e 's|updates=True|updates=False|;
           s|suppressUpdate=False|suppressUpdate=True|' aqt/profiles.py

# Use dependencies instead of bundled stuff
rm -rf thirdparty

# Remove not needed files
rm -f anki/anki

%build
./tools/build_ui.sh
python -m compileall .
python -O -m compileall .

%install
%make_install

# install appdata
mkdir -p %{buildroot}%{_datadir}/appdata
install -m 0644 %{S:1} %{buildroot}%{_datadir}/appdata

%find_lang %{name} %{name}.lang

%if 0%{?suse_version}
    %suse_update_desktop_file -r %{name} Education Languages
    %fdupes -s %{buildroot}%{_prefix}
%endif

%check
%if %{with tests}
# to prevent Exception("Anki requires a UTF-8 locale.")
export LC_ALL=en_US.UTF-8
# tests expecting remote connection can't be run inside OBS
rm tests/test_sync.py tests/test_remote_sync.py tests/test_media.py
./tools/tests.sh
%endif

%post
update-mime-database %{_datadir}/mime

%postun
update-mime-database %{_datadir}/mime

%files -f %{name}.lang
%defattr(-,root,root)
%doc LICENSE LICENSE.logo README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/%{name}

%changelog
