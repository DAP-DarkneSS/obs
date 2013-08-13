#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           plee-the-bear
Version:        0.6.0
Release:        13%{?dist}
# Code and artwork respectively
License:        GPLv2+ and CC-BY-SA
Summary:        2D platform game
Url:            http://plee-the-bear.sourceforge.net/
Group:          Amusements/Games
Source0:        http://downloads.sourceforge.net/project/plee-the-bear/Plee%20the%20Bear/0.5/%{name}-%{version}-light.tar.gz

# There is probably a more appropriate C++ fix instead of using -fpermissive, but I don't know it.
Patch1:         plee-the-bear-0.6.0-fpermissive.patch
# Disable stupid & broken SVN revision checking
Patch2:         plee-the-bear-0.6.0-svnclawfix.patch
# Initial work taken from Debian, thanks to Konstantinos Margaritis <markos@genesi-usa.com>
Patch3:         plee-the-bear-boost-1.50-patch

BuildRequires:  SDL_mixer-devel
BuildRequires:  boost-devel
# There has to be a saner way to remove rpath via cmake...
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  wxGTK-devel

%description
Plee the Bear is a 2D platform game like those we found on consoles in the
beginning of the 90's. The basis of the scenario fit in few lines:

4 PM or so, Plee wakes up, tired. He has dreamed again about that awesome
period when he went across the entire world together with his belle. He
puts his leg in the honey pot... empty! Moreover every single honey pot in
the house is empty. "One more trick of that kid", he thinks. "I'm going to
give him such a wallop of which he sure will remember".

Following honey drops on the ground, Plee reaches the edge of the forest.
Beginning of the game.

The game is led by Julien Jorge and Sebastien Angibaud. Nevertheless, the
game counts several contributions from external people.


%prep
%setup -q
%patch1 -p1 -b .fpermissive
%patch2 -p1 -b .svnclawfix
%patch3 -p1 -b .boost150

%build
%cmake  . \
        -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib} \
        -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} \
        -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib}
make %{?_smp_mflags} VERBOSE=1


%install
make install DESTDIR=%{buildroot} VERBOSE=1 INSTALL="install -p"

# Translations
%find_lang %{name}
%find_lang bear-factory
cat bear-factory.lang >>%{name}.lang
%find_lang bear-engine
cat bear-engine.lang >>%{name}.lang

# Menu entries
for F in %{buildroot}%{_datadir}/applications/*.desktop
do
        desktop-file-validate $F
done

# Nuke the rpaths.
for i in %{buildroot}%{_libdir}/*.so %{buildroot}%{_bindir}/bf-* %{buildroot}%{_bindir}/running-bear; do
	chrpath --delete $i
done


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
/sbin/ldconfig
[ $1 = 0 ] || exit 0
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%{_libdir}/*.so
%{_bindir}/*
%{_datadir}/plee-the-bear
%{_datadir}/bear-factory
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*
%doc CCPL COPYING GPL


%changelog
