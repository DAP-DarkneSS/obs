#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           florence
Version:        0.5.0
Release:        6%{?dist}
Summary:        Extensible scalable on-screen virtual keyboard for GNOME

License:        GPLv2+ and GFDL
Url:            http://florence.sourceforge.net
Group:          User Interface/X Hardware Support
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         florence-0.5.0-glib.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  GConf2-devel
BuildRequires:  at-spi-devel
BuildRequires:  desktop-file-utils
#BuildRequires:    libpanelappletmm-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  intltool
BuildRequires:  libXtst-devel
BuildRequires:  libgnome-devel
BuildRequires:  librsvg2-devel
BuildRequires:  scrollkeeper
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       control-center
Requires:       gnome-doc-utils
Requires(pre):    GConf2
Requires(preun):  GConf2
Requires(post):   scrollkeeper
Requires(post):   GConf2
Requires(postun): scrollkeeper

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
