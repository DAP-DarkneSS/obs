Name:           florence
Version:        0.5.0
Release:        6%{?dist}
Summary:        Extensible scalable on-screen virtual keyboard for GNOME 

Group:          User Interface/X Hardware Support
License:        GPLv2+ and GFDL
URL:            http://florence.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         florence-0.5.0-glib.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:    gtk2-devel
BuildRequires:    libxml2-devel
BuildRequires:    libglade2-devel
BuildRequires:    at-spi-devel
BuildRequires:    librsvg2-devel
BuildRequires:    cairo-devel
BuildRequires:    libgnome-devel
BuildRequires:    GConf2-devel
BuildRequires:    desktop-file-utils
BuildRequires:    scrollkeeper
BuildRequires:    intltool
BuildRequires:    libnotify-devel
#BuildRequires:    libpanelappletmm-devel
BuildRequires:    gnome-doc-utils
BuildRequires:    libXtst-devel
Requires(pre):    GConf2
Requires(preun):  GConf2
Requires(post):   scrollkeeper
Requires(post):   GConf2
Requires(postun): scrollkeeper
Requires:         control-center
Requires:         gnome-doc-utils


%description
Florence is an extensible scalable virtual keyboard for GNOME. 
You need it if you can't use a real hardware keyboard, for 
example because you are disabled, your keyboard is broken or 
because you use a tablet PC, but you must be able to use a pointing 
device (as a mouse, a trackball or a touchscreen).

Florence stays out of your way when you don't need it: 
it appears on the screen only when you need it. 
A Timer-based auto-click functionality is available 
to help disabled people having difficulties to click.


%prep
%setup -q
%patch0 -p1 -b .glib

rm -f gconf-refresh
ln -sf /bin/true gconf-refresh

sed -i 's|Icon=%{name}.svg|Icon=%{name}|g' data/%{name}.desktop.in.in


%build
#without panelapplet for gnome3
%configure \
      --without-panelapplet \
      --without-xrecord 

make %{?_smp_mflags} 


%install
rm -rf %{buildroot}

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

make install \
     DESTDIR=%{buildroot} \
     INSTALL="install -p"

desktop-file-install \
        --delete-original \
        --remove-category="Application" \
        --add-category="Utility" \
        --dir=%{buildroot}%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/pixmaps/ 

install -p -m 0644 data/%{name}.svg \
    %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%find_lang %{name}


%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi


%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi


%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :


%postun
scrollkeeper-update -q || :


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING-DOCS NEWS README 
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.*
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/pixmaps/%{name}.svg


%changelog
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.0-3
- Rebuild for new libpng

* Tue Aug 02 2011 Simon Wesp <cassmodiah@fedoraproject.org> - 0.5.0-2
- Fixing RHBZ#690475

* Fri Jan 28 2011 Simon Wesp <cassmodiah@fedoraproject.org> - 0.5.0-1
- New upstream release

* Fri Nov 12 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.7-2
- Build without libnotify

* Wed Jun 23 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.7-1
- New Upstream Release

* Sat Mar 27 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.6-2
- Patch DSO

* Thu Jan 28 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.6-1
- New upstream release
- Fixed RHBZ #550165

* Fri Dec 11 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.5-1
- New upstream release

* Thu Oct 22 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.4-1
- New upstream release

* Thu Aug 20 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.3-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.2-1
- New upstream release

* Sat Jun 13 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.2-0.1
- Update to an unofficial prerelease (upstream sent it via email)

* Tue Jun 02 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.1-1
- New upstream release

* Mon Mar 23 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.0-1
- New upstream release

* Sun Feb 22 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3.3-1
- New upstream release

* Mon Jan 26 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3.2-1
- New upstream release

* Wed Dec 18 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3.1-1
- New upstream release
- Move installation of icon from highcolortheme to DATADIR/pixmaps

* Wed Nov 19 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3.0-2
- Correct URL
- Correct categories of desktop-file (Bug #472174)

* Tue Sep 16 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3.0-1
- New upstream release 

* Wed Jul 30 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2.3-2
- Create and add patch0 

* Tue Jul 29 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2.3-1
- New upstream release
- Delete warning-patch by Robert Scheck - included in new release
- Delete sed command to edit schemas file - included in new release
- Add sed command to delete file-extension in .desktop-file

* Sun Jul 27 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2.2-5
- Edit specfile bug #454208 C14 C15

* Sun Jul 27 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2.2-4
- Edit specfile bug #454208 C8
- Edit files section
- Add warning-patch by Robert Scheck

* Thu Jul 24 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2.2-3
- Edit specfile bug #454208 C4 C5 C6
- Add scrollkeeper 

* Fri Jul 11 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2.2-2
- Add .desktop file
- Add script to correct dirty gconf-settings

* Sun Jul 06 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2.2-1
- Initial Release
