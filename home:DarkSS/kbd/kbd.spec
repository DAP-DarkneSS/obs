#
# spec file for package kbd
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


Name:           kbd
Version:        2.0.1
Release:        0
Summary:        Keyboard and Font Utilities
License:        GPL-2.0+
Group:          System/Console
# git: git://git.altlinux.org/people/legion/packages/kbd.git
Url:            ftp://ftp.altlinux.org/pub/people/legion/kbd/
%if 0
Source:         ftp://ftp.kernel.org/pub/linux/utils/kbd/kbd-%{version}.tar.xz
%else
Source:         %{name}-%{version}-repack.tar.bz2
%endif
Source1:        kbd_fonts.tar.bz2
Source2:        suse-add.tar.bz2
Source3:        README.SuSE
Source5:        kbd.fillup
Source6:        kbd.fillup.nonpc
Source8:        sysconfig.console
Source9:        sysconfig.keyboard
Source10:       testutf8
Source11:       fbtest.c
Source12:       fbtest.8
Source13:       guess_encoding.pl
Source42:       convert-kbd-mac.sed
Source43:       repack_kbd.sh
Patch0:         kbd-1.15.2-prtscr_no_sigquit.patch
Patch2:         kbd-1.15.2-unicode_scripts.patch
Patch3:         kbd-1.15.2-docu-X11R6-xorg.patch
Patch4:         kbd-1.15.2-sv-latin1-keycode10.patch
Patch5:         kbd-1.15.2-setfont-no-cruft.patch
# TODO: no ideas how to port it.
Patch6:         kbd-1.15.2-dumpkeys-C-opt.patch
Patch8:         kbd-1.15.2-chvt-userwait.patch

BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  check-devel
BuildRequires:  flex
BuildRequires:  gcc >= 4.6
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  xz

Requires(pre):  %fillup_prereq
Recommends:     fbset

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Load and save keyboard mappings. This is needed if you are not using
the US keyboard map. This package also contains utilities for changing
your console fonts. If you install this package, YaST includes an extra
menu to allow you to choose between the different fonts. This package
also includes fonts from the kbd_fonts.tar.gz package (by Paul
Gortmaker) on Sunsite.



Authors:
--------
    Andries Brouwer <aeb@cwi.nl>
    Alexey Gladkov <gladkov.alexey@gmail.com>

%define kbd /usr/share/kbd

%prep
%setup -q -a 1 -a 2 -n kbd-%{version}
%patch0 -p1
%patch2
%patch3
%patch4 -p1
%patch5 -p1
# TODO: no ideas how to port it.
# %%patch6
%patch8 -p1

%build
for i in `find data/keymaps/mac -type f` ; do
sed -i -f %{SOURCE42} $i
done
# workaround ambiguous keymap names
pushd data/keymaps/i386
	# bnc#48301
	test -f qwerty/se-latin1.map || cp qwerty/sv-latin1.map qwerty/se-latin1.map
	# bnc#435121
	test -f olpc/es-olpc.map || mv olpc/es.map olpc/es-olpc.map
popd
%configure \
	--datadir=%{kbd} \
	--enable-nls \
	--localedir=/usr/share/locale \
	--enable-optional-progs \
	--disable-vlock
make CFLAGS="%{optflags}"
gcc %{optflags} -o fbtest   $RPM_SOURCE_DIR/fbtest.c
# fix lat2-16.psfu (bnc#340579)
font=data/consolefonts/lat2a-16.psfu
./src/psfxtable -i $font -it  data/unimaps/lat2u.uni \
	-o t.psfu
mv t.psfu $font
make

%install
mkdir -p %{buildroot}%{_sbindir}
DOC=%{buildroot}%{_defaultdocdir}/kbd
KBD=%{kbd}
K=%{buildroot}$KBD
mkdir -p $K/consolefonts
# First install the fonts from the vfont package 
# (allowing kbd to overwrite some of them)
mkdir -p $DOC/fonts
install -m 644 fonts/README $DOC/fonts/README.fonts
install -m 644 fonts/vfont-4.36/README $DOC/fonts/README.vfont-4.36
install -m 644 fonts/vfont-5.10/README $DOC/fonts/README.vfont-5.10
install -m 644 fonts/vfont-5.10/SCRIPT $DOC/fonts/SCRIPT.vfont-5.10
rm -f fonts/vfont-5.10/SCRIPT fonts/*/README
install -m 644 fonts/*/* $K/consolefonts/
# Now call kbd install
echo "# Now call kbd install DESTDIR=%{buildroot} DATA_DIR=%{kbd} MAN_DIR=%{_mandir}"
make DESTDIR=%{buildroot} DATA_DIR=%{kbd} MAN_DIR=%{_mandir} install
# ln -s iso01-12x22.psfu $K/consolefonts/suse12x22.psfu
install -m 644 data/consolefonts/README* $DOC/fonts/
mkdir -p $DOC/doc/
install -m 644 docs/doc/keysyms.h.info docs/doc/kbd.FAQ.txt docs/doc/kbd.FAQ*.html docs/doc/README* docs/doc/TODO $DOC/doc/
install -m 644 docs/doc/as400.kbd docs/doc/console.docs docs/doc/repeat/set_kbd_repeat-2 $DOC/doc/
echo "See /usr/share/i18/charmaps for a description of char maps" >$DOC/doc/README.charmaps
install -m 644 COPYING ChangeLog CREDITS README $DOC/
install -m 644 %{SOURCE3} $DOC/
rm -f $K/consolefonts/README* $K/consolefonts/ERRORS.gz
if ls $K/consolefonts/Agafari-* > /dev/null 2>&1; then
  echo "";
  echo "ERROR: Ethiopian Agafari fonts are for noncommercial distribution only."
  echo "please run repack_kbd.sh";
  echo "";
  exit 1
fi
ln -sf us.map.gz $K/keymaps/i386/qwerty/khmer.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/korean.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/arabic.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/chinese.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/taiwanese.map.gz
# Compatability links; don't know what the first three are good for.
# The others are for yast/langselection and should be removed as soon as
# yast knows about it.
#ln -sf de-latin1-nodeadkeys.map.gz \
#  $K/keymaps/i386/qwertz/de-lat1-nd.map.gz
#ln -sf ru1.map.gz $K/keymaps/i386/qwerty/russian.map.gz
#ln -sf sg-latin1-lk450.map.gz \
#  $K/keymaps/i386/qwertz/sg-l1-lk450.map.gz
# The next two links are for yast-language choise; should be obsolete
# with the next yast version (on 6.1)
#ln -sf lat1-16.psfu.gz $K/consolefonts/lat1u-16.psf.gz
#ln -sf lat2-16.psfu.gz $K/consolefonts/lat2u-16.psf.gz
#
# This is for stupid default font search
rm -f $K/consolefonts/default8x16.gz
ln -sf default8x16.psfu.gz $K/consolefonts/default8x16.gz
#
rm -f $K/keymaps/i386/qwerty/*~ $K/keymaps/i386/qwerty/*,v
#
# this is until the Cyr* font are not part of the package
rm -f $K/consolefonts/Cyr_a8x14.gz
ln -sf Cyr_a8x14.psfu.gz $K/consolefonts/Cyr_a8x14.gz
rm -f $K/consolefonts/Cyr_a8x16.gz
ln -sf Cyr_a8x16.psfu.gz $K/consolefonts/Cyr_a8x16.gz
rm -f $K/consolefonts/Cyr_a8x8.gz
ln -sf Cyr_a8x8.psfu.gz $K/consolefonts/Cyr_a8x8.gz
#
find $K -name \*.orig | xargs -r rm -vf
# add some missing maps to mac and remap french board
(
cd $K/keymaps/mac/all
pwd
#ln -s mac-fr-latin1.map.gz mac-fr_CH-latin1.map.gz
#ln -s mac-fr-latin1.map.gz mac-fr.map.gz
for i in \
	mac-es.map.gz \
	mac-it.map.gz \
	mac-pt-latin1.map.gz \
	mac-br-abnt2.map.gz \
	mac-gr.map.gz \
	mac-dk-latin1.map.gz \
	mac-no-latin1.map.gz \
	mac-fi-latin1.map.gz \
	mac-cz-us-qwertz.map.gz \
	mac-hu.map.gz \
	mac-Pl02.map.gz \
	mac-ru1.map.gz \
	mac-jp106.map.gz
do test -f $i || ln -sv mac-us.map.gz $i
done
)
FILLUP_DIR=%{buildroot}%{_localstatedir}/adm/fillup-templates
mkdir -p $FILLUP_DIR
install -m 644 %{SOURCE8} $FILLUP_DIR/sysconfig.console
install -m 644 %{SOURCE9} $FILLUP_DIR/sysconfig.keyboard
%ifarch %ix86 alpha ia64 x86_64
cat %{SOURCE5} >> $FILLUP_DIR/sysconfig.keyboard
%else
cat %{SOURCE6} >> $FILLUP_DIR/sysconfig.keyboard
%endif
#mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
#touch $RPM_BUILD_ROOT/etc/sysconfig/console
%ifnarch %ix86
%ifnarch x86_64
   rm -f %{buildroot}/%{_mandir}/man8/resizecons.8*
%endif
%endif
%ifarch %sparc m68k
rm -f %{buildroot}/%{_mandir}/man8/getkeycodes.8*
rm -f %{buildroot}/%{_mandir}/man8/setkeycodes.8*
%endif
install -m 755 %_sourcedir/testutf8  %{buildroot}/%{_bindir}
install -m 755 fbtest    %{buildroot}/%{_sbindir}
install -m 644 %{SOURCE12} %{buildroot}/%{_mandir}/man8/
install -m 755 %{SOURCE13} %{buildroot}/%{_bindir}/guess_encoding
#UsrMerge
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/sbin
ln -s %{_bindir}/chvt %{buildroot}/bin
ln -s %{_bindir}/clrunimap %{buildroot}/bin
ln -s %{_bindir}/deallocvt %{buildroot}/bin
ln -s %{_bindir}/dumpkeys %{buildroot}/bin
ln -s %{_bindir}/fgconsole %{buildroot}/bin
ln -s %{_bindir}/getunimap %{buildroot}/bin
ln -s %{_bindir}/guess_encoding %{buildroot}/bin
ln -s %{_bindir}/kbd_mode %{buildroot}/bin
ln -s %{_bindir}/kbdinfo %{buildroot}/bin
ln -s %{_bindir}/kbdrate %{buildroot}/bin
ln -s %{_bindir}/loadkeys %{buildroot}/bin
ln -s %{_bindir}/loadunimap %{buildroot}/bin
ln -s %{_bindir}/mapscrn %{buildroot}/bin
ln -s %{_bindir}/openvt %{buildroot}/bin
ln -s %{_bindir}/outpsfheader %{buildroot}/bin
ln -s %{_bindir}/psfaddtable %{buildroot}/bin
ln -s %{_bindir}/psfgettable %{buildroot}/bin
ln -s %{_bindir}/psfstriptable %{buildroot}/bin
ln -s %{_bindir}/psfxtable %{buildroot}/bin
ln -s %{_bindir}/screendump %{buildroot}/bin
ln -s %{_bindir}/setfont %{buildroot}/bin
ln -s %{_bindir}/setleds %{buildroot}/bin
ln -s %{_bindir}/setlogcons %{buildroot}/bin
ln -s %{_bindir}/setmetamode %{buildroot}/bin
ln -s %{_bindir}/setpalette %{buildroot}/bin
ln -s %{_bindir}/setvesablank %{buildroot}/bin
ln -s %{_bindir}/setvtrgb %{buildroot}/bin
ln -s %{_bindir}/showconsolefont %{buildroot}/bin
ln -s %{_bindir}/showkey %{buildroot}/bin
ln -s %{_bindir}/spawn_console %{buildroot}/bin
ln -s %{_bindir}/spawn_login %{buildroot}/bin
ln -s %{_bindir}/testutf8 %{buildroot}/bin
ln -s %{_bindir}/unicode_start %{buildroot}/bin
ln -s %{_bindir}/unicode_stop %{buildroot}/bin
ln -s %{_sbindir}/fbtest %{buildroot}/sbin
%ifnarch %sparc m68k
ln -s %{_bindir}/getkeycodes %{buildroot}/bin
ln -s %{_bindir}/setkeycodes %{buildroot}/bin
%endif
%ifarch %ix86
ln -s %{_bindir}/resizecons %{buildroot}/bin
%endif
%ifarch x86_64
ln -s %{_bindir}/resizecons %{buildroot}/bin
%endif
#EndUsrMerge
%find_lang %{name}

%post
%{fillup_only -n console}
%{fillup_only -n keyboard}
#echo "Please read the docu about the new COMPOSETABLE rc.config variable."
#echo "See /etc/sysconfig/console, /etc/sysconfig/keyboard"
#echo "and {_docdir}/kbd/README.SuSE."

%files -f %{name}.lang
%defattr(-,root,root)
#config(noreplace) /etc/sysconfig/console
%doc %{_defaultdocdir}/kbd
#doc COPYING CHANGES README CREDITS
%{_localstatedir}/adm/fillup-templates/sysconfig.console
%{_localstatedir}/adm/fillup-templates/sysconfig.keyboard
%{kbd}
#UsrMerge
/sbin/fbtest
/bin/chvt
/bin/openvt
/bin/deallocvt
/bin/dumpkeys
%ifnarch %sparc m68k
/bin/getkeycodes
/bin/setkeycodes
%endif
/bin/fgconsole
/bin/kbd_mode
/bin/kbdinfo
/bin/loadkeys
/bin/loadunimap
/bin/mapscrn
/bin/psfaddtable
/bin/psfgettable
/bin/psfstriptable
/bin/psfxtable
%ifarch %ix86
/bin/resizecons
%endif
%ifarch x86_64
/bin/resizecons
%endif
/bin/setfont
/bin/setleds
/bin/setmetamode
/bin/setvtrgb
/bin/showconsolefont
/bin/showkey
/bin/unicode_start
/bin/unicode_stop
/bin/kbdrate
/bin/testutf8
/bin/guess_encoding
/bin/clrunimap
/bin/getunimap
/bin/outpsfheader
/bin/screendump
/bin/setlogcons
/bin/setpalette
/bin/setvesablank
/bin/spawn_console
/bin/spawn_login
#EndUsrMerge
%{_sbindir}/fbtest
%{_bindir}/chvt
%{_bindir}/openvt
%{_bindir}/deallocvt
%{_bindir}/dumpkeys
%ifnarch %sparc m68k
%{_bindir}/getkeycodes
%{_bindir}/setkeycodes
%endif
%{_bindir}/fgconsole
%{_bindir}/kbd_mode
%{_bindir}/kbdinfo
%{_bindir}/loadkeys
%{_bindir}/loadunimap
%{_bindir}/mapscrn
%{_bindir}/psfaddtable
%{_bindir}/psfgettable
%{_bindir}/psfstriptable
%{_bindir}/psfxtable
%ifarch %ix86
%{_bindir}/resizecons
%endif
%ifarch x86_64
%{_bindir}/resizecons
%endif
%{_bindir}/setfont
%{_bindir}/setleds
%{_bindir}/setmetamode
%{_bindir}/setvtrgb
%{_bindir}/showconsolefont
%{_bindir}/showkey
%{_bindir}/unicode_start
%{_bindir}/unicode_stop
%{_bindir}/kbdrate
%{_bindir}/testutf8
%{_bindir}/guess_encoding
%{_bindir}/clrunimap
%{_bindir}/getunimap
%{_bindir}/outpsfheader
%{_bindir}/screendump
%{_bindir}/setlogcons
%{_bindir}/setpalette
%{_bindir}/setvesablank
%{_bindir}/spawn_console
%{_bindir}/spawn_login
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/keymaps.5.gz
%ifnarch %sparc m68k
%doc %{_mandir}/man8/getkeycodes.8.gz
%doc %{_mandir}/man8/setkeycodes.8.gz
%endif
%doc %{_mandir}/man8/showconsolefont.8.gz
%doc %{_mandir}/man8/loadunimap.8.gz
%doc %{_mandir}/man8/mapscrn.8.gz
%ifarch %ix86
%doc %{_mandir}/man8/resizecons.8.gz
%endif
%ifarch x86_64
%doc %{_mandir}/man8/resizecons.8.gz
%endif
%doc %{_mandir}/man8/setfont.8.gz
%doc %{_mandir}/man8/fbtest.8.gz
%doc %{_mandir}/man8/kbdrate.8.gz
%doc %{_mandir}/man8/clrunimap.8.gz
%doc %{_mandir}/man8/getunimap.8.gz
%doc %{_mandir}/man8/mk_modmap.8.gz
%doc %{_mandir}/man8/setlogcons.8.gz
%doc %{_mandir}/man8/setvesablank.8.gz
%doc %{_mandir}/man8/setvtrgb.8.gz
%doc %{_mandir}/man8/vcstime.8.gz

%changelog
