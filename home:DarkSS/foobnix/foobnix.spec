#
# spec file for package foobnix
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           foobnix
Version:        2.6.10
Release:        1
License:        GPL-3.0+
Summary:        Light and functional music player
Url:            http://www.foobnix.com/
Group:          Productivity/Multimedia/Sound/Players
Source:         https://launchpad.net/~foobnix-team/+archive/foobnix-player/+files/foobnix_%{version}q.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version} > 1110
BuildRequires:  python-base
Requires:       python-base = %py_ver
# This works on newer version
# on older version it dies misserably if used
BuildArch:      noarch
%else
BuildRequires:  python
# Required way for older version of suse
Requires:       python = %py_ver
%endif

BuildRequires:  dos2unix
BuildRequires:  python-devel
BuildRequires:  python-gtk
BuildRequires:  update-desktop-files

Recommends:     gnome-settings-daemon
Recommends:     gstreamer-0_10-plugins-fluendo_mp3
Recommends:     python-notify
Recommends:     python-webkitgtk

Requires:       %{name}-python-google
Requires:       %{name}-python-lyricwiki
Requires:       %{name}-python-mutagen
Requires:       %{name}-python-pylast
Requires:       dbus-1-python
Requires:       python-chardet
Requires:       python-gstreamer010 >= 0.10.18
Requires:       python-gtk
Requires:       python-keybinder
Requires:       python-mutagen
Requires:       python-simplejson

%description
Main player features:
 * CUE support (also wv, iso.wv);
 * Formats MP3, MP4, AAC, CD Audio, WMA, Vorbis, FLAC, WavPack, WAV, AIFF,
   Musepack, Speex, AU, SND ...
 * Converter from any format to any (mp3, ogg, mp2, ac3, m4a, wav);
 * Scrobbler tags with music and radio;
 * Find and play music and videos;
 * Equalizer;
 * Online music download manager;
 * Shortcuts;
 * Displays the album cover, lyrics, photo artist;
 * Integration with VKontakte (displaying all the friends and their music;
   downloading music from the group vkontakte);
 * Integration with Last.FM (the best songs, favorite songs, artists).

%package lang
Summary:        FoobNix transtalions

%description lang
Provides FoobNix light and functional music player transtalions files.

%package python-google
License:        MIT
Summary:        FoobNix Python library for google search
Url:            http://www.catonmat.net/blog/python-library-for-google-search/

%description python-google
Provides FoobNix Python library for google search.

%package python-lyricwiki
License:        GPL-2.0+
Summary:        FoobNix Python interface to the http://lyrics.wikia.com
Url:            https://pypi.python.org/pypi/lyricwiki

%description python-lyricwiki
A Python interface which provides simple access to lyrics from
http://lyrics.wikia.com.

%package python-mutagen
License:        GPL-2.0
Summary:        FoobNix Python module to Handle Audio Metadata
Url:            http://code.google.com/p/mutagen/

%description python-mutagen
Mutagen is a Python module to handle audio metadata. It supports FLAC,
M4A, MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True Audio, and
WavPack audio files. All versions of ID3v2 are supported, and all
standard ID3v2.4 frames are parsed. It can read Xing headers to
accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags
can be edited regardless of their audio format. It can also manipulate
Ogg streams on an individual packet/page level.

%package python-pylast
License:        GPL-2.0+
Summary:        FoobNix Python interface to Last.fm
Url:            http://code.google.com/p/pylast/

%description python-pylast
A Python interface to Last.fm (and other API compatible social networks).

%prep
%setup -q -n %{name}_%{version}

find foobnix/ -name "*.py" -exec dos2unix {} ';'
# remove shebangs from library files
find foobnix/ -name "*.py" -exec sed -i -e  '/^#!\s\?\/usr\/bin\/\(env\s\)\?python$/d' {} ';'

%build
%{__python} setup.py build 

%install
%{__python} setup.py install \
        --prefix=%{_prefix} \
        --root=%{buildroot} \
        --record-rpm=%{name}_filelist.txt
%suse_update_desktop_file %{name}

# Check compress manual pages so fix it here..
sed -i 's/foobnix.1$/foobnix.1.gz/g' %{name}_filelist.txt
# fix folder names that should not exist in file list to start with...
sed -i -e "/\/usr\/share\/applications$/d" %{name}_filelist.txt
sed -i -e  "/\/usr\/share\/pixmaps$/d" %{name}_filelist.txt
sed -i -e  "/\.mo$/d" %{name}_filelist.txt
%find_lang %{name}

%files -f %{name}_filelist.txt
%defattr(-,root,root)
%doc CHANGELOG COPYING README
%exclude %{python_sitelib}/%{name}/thirdparty/google*
%exclude %{python_sitelib}/%{name}/thirdparty/lyr*
%exclude %{python_sitelib}/%{name}/thirdparty/mutagen*
%exclude %{python_sitelib}/%{name}/thirdparty/pylast*

%files lang -f %{name}.lang
%defattr(-,root,root)

%files python-google
%defattr(-,root,root)
%{python_sitelib}/%{name}/thirdparty/google*

%files python-lyricwiki
%defattr(-,root,root)
%{python_sitelib}/%{name}/thirdparty/lyr*

%files python-mutagen
%defattr(-,root,root)
%{python_sitelib}/%{name}/thirdparty/mutagen*

%files python-pylast
%defattr(-,root,root)
%{python_sitelib}/%{name}/thirdparty/pylast*

%changelog
