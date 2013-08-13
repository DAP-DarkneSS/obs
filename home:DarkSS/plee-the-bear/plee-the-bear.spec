Name:           plee-the-bear
Version:        0.6.0
Release:        13%{?dist}
Summary:        2D platform game
Group:          Amusements/Games
# Code and artwork respectively
License:        GPLv2+ and CC-BY-SA
URL:            http://plee-the-bear.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/plee-the-bear/Plee%20the%20Bear/0.5/%{name}-%{version}-light.tar.gz

# There is probably a more appropriate C++ fix instead of using -fpermissive, but I don't know it.
Patch1:         plee-the-bear-0.6.0-fpermissive.patch
# Disable stupid & broken SVN revision checking
Patch2:         plee-the-bear-0.6.0-svnclawfix.patch
# Initial work taken from Debian, thanks to Konstantinos Margaritis <markos@genesi-usa.com>
Patch3:		plee-the-bear-boost-1.50-patch

BuildRequires:  desktop-file-utils
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  boost-devel
BuildRequires:  wxGTK-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  gettext
BuildRequires:  cmake
# There has to be a saner way to remove rpath via cmake...
BuildRequires:	chrpath

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
make install DESTDIR=$RPM_BUILD_ROOT VERBOSE=1 INSTALL="install -p"

# Translations
%find_lang %{name}
%find_lang bear-factory
cat bear-factory.lang >>%{name}.lang
%find_lang bear-engine
cat bear-engine.lang >>%{name}.lang

# Menu entries
for F in $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
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
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.6.0-12
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.0-11
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.0-10
- Rebuild for Boost-1.53.0

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.6.0-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.6.0-8
- rebuild against new libjpeg

* Tue Aug 21 2012 Tom Callaway <spot@fedoraproject.org> - 0.6.0-7
- fix compile with current boost (thanks to Konstantinos Margaritis)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for c++ ABI breakage

* Sun Feb  5 2012 Tom Callaway <spot@fedoraproject.org> - 0.6.0-4
- rebuild against fixed libclaw

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.0-2
- Rebuild for new libpng

* Thu Aug 25 2011 Tom Callaway <spot@fedoraproject.org> - 0.6.0-1
- update to 0.6.0

* Mon Apr 18 2011 Tom Callaway <spot@fedoraproject.org> - 0.5.1-1
- update to 0.5.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.4.1-9
- rebuild for new boost

* Wed Sep 29 2010 jkeating - 0.4.1-8
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.1-7
- fix incorrect return type

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.4.1-6
- rebuilt against wxGTK-2.8.11-2

* Wed Feb 17 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-5
- Fix build

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4.1-4
- Rebuild for Boost soname bump

* Sun Nov 29 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-3
- Fix libdir for 64-bit archs

* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-2
- Incorporate suggestions from review (#524283#c2, Simon Wesp)
- Fix license tag
- Preserve timestamps
- Regenerate icon cache

* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-1
- Initial packaging
