#
# spec file for package italc
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#


Name:           italc
Version:        2.0.0
Release:        5.1
License:        GPL-2.0+
Summary:        Didactical monitoring software for Linux-networks
Url:            http://italc.sourceforge.net/
Group:          Productivity/Networking/Other
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libstdc++-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
#
# CentOS
#
%if 0%{?centos_version}
BuildRequires:  libXtst-devel
BuildRequires:  qt4-devel
%endif
#
# Mandriva
#
%if 0%{?mandriva_version}
BuildRequires:  libxtst6-devel
BuildRequires:  qt4-devel
%endif
#
# Fedora
#
%if 0%{?fedora_version}
BuildRequires:  libXtst-devel
BuildRequires:  qt4-devel
%endif
#
# openSUSE
#
%if 0%{?suse_version}
Requires:       gpg2
%if 0%{?suse_version} <= 1110
Requires:       avahi
%else
Requires:       avahi-utils
%endif
BuildRequires:  update-desktop-files
Requires(pre):  pwdutils
%if 0%{?suse_version} > 1010
BuildRequires:  libqt4-devel
BuildRequires:  libqt4-qt3support
BuildRequires:  libqt4-sql
BuildRequires:  libqt4-x11
BuildRequires:  wvstreams-devel
%else
BuildRequires:  libqt4-qt3support
BuildRequires:  libqt4-sql
BuildRequires:  qt-devel
BuildRequires:  qt-x11
%endif
%if 0%{?suse_version} > 1100
BuildRequires:  pkgconfig(glib-2.0)
%endif
%if 0%{?suse_version} > 1120
BuildRequires:  gcc43
BuildRequires:  gcc43-c++
%endif
%if 0%{?suse_version} > 1020
Source4:        italc.firewall2
%endif
Source7:        italc-README.SuSE
%endif
#
# standard source and patch files
#
Source:         %{name}-%{version}.tar.bz2
Source2:        italc-start_ica
Source3:        italc.sysconfig
Source5:        ica-autostart.desktop
Source6:        italc-launcher
Source8:        italc.desktop
Source9:        italc-rpmlintrc
Source10:       italc-imc.1.gz

# PATCH-FIX-UPSTREAM Building error with gcc >= 4.7 is fixed.
Patch0:         %{name}-gcc47.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         italcgrp italc

%description
iTALC is a powerful software for Linux-networks, which was especially developed
for working with computers in school. But it can be also used in other
learning-environments. iTALC is a software for teachers using the computer
as didactical tool in their lessons. It aims to be a complete replacement for
expensive commercial software like MasterEye (tm).

iTALC makes it possible, to access and influence the pupils activities from the
computer of the teacher. This way iTALC supports the work with modern
equipment in school.
For example the teacher is able to see the content of the pupils screens on his
screen. If a student needs help, the teacher can access his desktop and
give support while sitting in front of his computer. The pupil can watch all
activities, the teacher is doing on his desktop. So the he can learn new
processes.

If you want to teach the pupils completely new stuff, you can switch into
demo-mode. Then all pupils see what the teacher is doing/demonstrating.
It's also possible to let a pupil demonstrate something by redirecting his
screen to all screens of the other pupils.
iTALC provides even more features for controlling the pupils computers.
For example you can lock all screens, so that the pupils can't continue their
work and are forced to turn their attention to the teacher. You can also kill
games or internet-browsers, if these things are not part of the lesson.

But there are also some nice features for administrators, making the
administration of the computers much easier and more comfortable. For example
you can execute one or more commands on every computer without sitting in front
of every computer and typing these comands. The execution of X-applications
(e.g. Star/OpenOffice-Setup) on all clients with redirection to the local
admin-computer is also part of iTALC's featurelist. Furthermore you can
shutdown and restart the computers per remote control. If the computers support
Wake-on-LAN, it's also possible to turn on all computers from a central place.


Author:
-------
    Tobias Doerfel


%package        client
Summary:        Software for iTALC-clients
Group:          Productivity/Networking/Other
Requires(pre):  perl
Requires(pre):  xorg-x11
Requires:       italc = %{version}
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
Requires(pre):  permissions
%endif

%description    client
This package contains the software, needed by iTALC-clients.

See /usr/share/doc/packages/italc/README.SuSE for details on how to install
and setup iTALC in your network.


Author:
-------
    Tobias Doerfel


%package        master
Summary:        Software for iTALC-masters
Group:          Productivity/Networking/Other
Requires(pre):  coreutils
Requires(pre):  italc = %{version}
Requires(pre):  italc-client = %{version}

%description    master
This package contains the software, needed by iTALC-master-computers.

See /usr/share/italc/doc/INSTALL for details on how to install and setup iTALC
in your network.


Author:
-------
    Tobias Doerfel


%prep
%setup -q
%patch0

%build
##export SUSE_ASNEEDED=0
mkdir build
cd build
cmake ../ \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
        -DCMAKE_C_FLAGS="%{optflags} -fpic -fPIC" \
        -DCMAKE_CXX_FLAGS="%{optflags} -fpic -fPIC"

%install
cd build
%make_install
cd ..
# create the directories containing the auth-keys
mkdir -p %{buildroot}%{_sysconfdir}/italc/keys/{private,public}/{teacher,admin,supporter,other}
# create pseudo key files so RPM can own them (ghost files)
for role in admin supporter teacher; do
	touch %{buildroot}%{_sysconfdir}/italc/keys/{private,public}/$role/key
done
# create the initial config
mkdir -p "%{buildroot}/%{_sysconfdir}/settings/iTALC Solutions"
cat > "%{buildroot}/%{_sysconfdir}/settings/iTALC Solutions/iTALC.conf" << EOF
[Authentication]
LogonAuthenticationEnabled=0
KeyAuthenticationEnabled=1
PublicKeyBaseDir=%{_sysconfdir}/italc/keys/public
PrivateKeyBaseDir=%{_sysconfdir}/italc/keys/private
LogonGroups=
PermissionRequiredWithKeyAuthentication=0
PermissionRequiredWithLogonAuthentication=0
SameUserConfirmationDisabled=0

[DemoServer]
Backend=0
Multithreaded=1

[Logging]
LimittedLogFileSize=0
LogFileDirectory=\$TEMP
LogFileSizeLimit=-1
LogLevel=4
LogToStdErr=1
LogToWindowsEventLog=0

[Network]
CoreServerPort=11100
DemoServerPort=11400
FirewallExceptionEnabled=1
HttpServerEnabled=0
HttpServerPort=5800

[Service]
Arguments=
Autostart=1
HideTrayIcon=0

[VNC]
CaptureLayeredWindows=0
LowAccuracy=1
PollFullScreen=1

[Paths]
PersonalConfiguration=\$APPDATA/PersonalConfig.xml
GlobalConfiguration=\$APPDATA/GlobalConfig.xml
SnapshotDirectory=\$APPDATA/Snapshots

EOF
# install manpages
mkdir -p %{buildroot}%{_mandir}/man1
install -m644 ./ica/ica.1 %{buildroot}%{_mandir}/man1/
install -m644 ./ima/italc.1 %{buildroot}%{_mandir}/man1/
install -m644 %{SOURCE10} %{buildroot}%{_mandir}/man1/imc.1.gz
# install start script for ica client
install -D -m755 %{SOURCE2} %{buildroot}/%{_bindir}/start-ica
install -D -m644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/xdg/autostart/ica-autostart.desktop
install -D -m755 %{SOURCE6} %{buildroot}/%{_bindir}/italc-launcher
# icon for the desktop file
install -Dm644 ima/data/italc.png %{buildroot}/%{_datadir}/pixmaps/italc.png
#
# Distribution specific
#
# configuration for ica
%if 0%{?suse_version}
install -D -m644 %{SOURCE3} %{buildroot}%{_localstatedir}/adm/fillup-templates/sysconfig.ica
%else
install -D -m644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig/ica
%endif
%if 0%{?suse_version}
%if 0%{?suse_version} > 1020
# install firewall definitions
# see http://en.opensuse.org/SuSEfirewall2/Service_Definitions_Added_via_Packages
# for details
install -D -m644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/italc
%endif
#
# install desktop file
#
install -Dm644 %{SOURCE8} %{buildroot}/%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name}
#
# install README.SuSE
#
install -m644 %{SOURCE7} README.SuSE
%endif

%post
if
    getent group %italcgrp >/dev/null
then
    : OK group %italcgrp already present
else
    groupadd -r %italcgrp 2>/dev/null || :
fi

%if 0%{?suse_version}
%post client
%{fillup_only -n ica}
# remove old entries (italc-client < 1.0.8.992
if grep -qw /etc/init.d/italc /etc/X11/xdm/Xsetup 2>/dev/null; then
  sed -i "s@.*/etc/init.d/italc start.*@@g" /etc/X11/xdm/Xsetup
fi
if grep -qw /etc/init.d/ica /etc/X11/xdm/Xsetup 2>/dev/null; then
  sed -i "s@.*/etc/init.d/ica start.*@@g" /etc/X11/xdm/Xsetup
fi
%endif # suse_version

%post master
# dont run scripts on update
if [ ${1:-0} -lt 2 ]; then
  for role in admin supporter teacher; do
	if [ ! -f "%{_sysconfdir}/italc/keys/private/$role/key" ]; then
		/usr/bin/imc -role $role -createkeypair "%{_sysconfdir}/italc/keys" >/dev/null
		chgrp %italcgrp "%{_sysconfdir}/italc/keys/private/$role/key"
		chmod 0440 "%{_sysconfdir}/italc/keys/private/$role/key"
	fi
  done
fi


%files
%defattr(-,root,root)
%doc contrib doc/* AUTHORS ChangeLog COPYING README* TODO
%{_datadir}/italc/
%dir %{_sysconfdir}/italc
%dir %{_sysconfdir}/italc/keys
%dir %{_sysconfdir}/italc/keys/public
%dir %{_sysconfdir}/italc/keys/public/teacher
%dir %{_sysconfdir}/italc/keys/public/admin
%dir %{_sysconfdir}/italc/keys/public/supporter
%dir %{_sysconfdir}/italc/keys/public/other
%dir %{_sysconfdir}/settings
%dir "%{_sysconfdir}/settings/iTALC Solutions"
%ghost %config(missingok,noreplace) %{_sysconfdir}/italc/keys/public/*/key
%config(missingok,noreplace) "%{_sysconfdir}/settings/iTALC Solutions/iTALC.conf"
%if 0%{?suse_version} > 1020
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/italc
%endif

%files client
%defattr(-,root,root)
%doc %{_mandir}/man1/ica.1*
%doc %{_mandir}/man1/imc.1*
%{_bindir}/ica
%{_bindir}/start-ica
%{_bindir}/imc
%attr(755,root,root) %{_bindir}/italc_auth_helper
%{_libdir}/libItalcCore.so
%if 0%{?suse_version} <= 1010
%dir %{_sysconfdir}/xdg/autostart
%endif
%config %{_sysconfdir}/xdg/autostart/ica-autostart.desktop
%if 0%{?suse_version}
%doc README.SuSE
%{_localstatedir}/adm/fillup-templates/sysconfig.ica
%else
%config(noreplace) %{_sysconfdir}/sysconfig/ica
%endif

%files master
%defattr(-,root,root)
%{_bindir}/italc
%{_bindir}/italc-launcher
%doc %{_mandir}/man1/italc.1*
%{_datadir}/applications/italc.desktop
#{_datadir}/icons/italc.*
%{_datadir}/pixmaps/italc.*
%dir %{_sysconfdir}/italc/keys/private
%defattr(0440,root,%italcgrp,0750)
%dir %{_sysconfdir}/italc/keys/private/teacher
%dir %{_sysconfdir}/italc/keys/private/admin
%dir %{_sysconfdir}/italc/keys/private/supporter
%dir %{_sysconfdir}/italc/keys/private/other
%ghost %config(missingok,noreplace) %{_sysconfdir}/italc/keys/private/*/key

%changelog
* Mon Dec 17 2012 dap.darkness@gmail.com
- italc-gcc47.patch was added to build via gcc >= 4.7.
- fpie flag was replaced by fpic to build under x32.
- Build type was switched to RelWithDebInfo to get debug info.
- Fixed up via spec-cleaner.
- Clean-section was removed.
- Licence was replaced by GPL-2.0+ to fix an invalid-license warning.
- italc_auth_helper attributes were set to 755 to fix another warning.
* Fri Dec 16 2011 fschuett@gymnasium-himmelsthuer.de
- reverted qt4 -> settings because of openSUSE qt4 defaults (see libqt4)
- changed ports to 11100,11400
- adapted italc-launcher, start_ica
* Tue Aug 30 2011 lars@linux-schulserver.de
- update to 2.0.0
- removed unneeded patches
- moved generic iTALC.conf from '/etc/settings/iTALC Solutions'
  to '/etc/qt4/iTALC Solutions' according to the wiki documentation
  for version 2
* Mon Aug  1 2011 lars@linux-schulserver.de
- just require avahi on SLED 11 (fix bnc #709338)
* Wed Mar 30 2011 lars@linux-schulserver.de
- update to 1.0.13:
  + fixes serious memory leak when running iTALC master
* Sat Jul 31 2010 lars@linux-schulserver.de
- update to 1.0.10:
  * Added NSIS script for building an iTALC installer
  * Added support for languages written right-to-left
  * IMA: rewrote top level UI and added new toolbar style
  * IMA: updated and improved splash screen
  * IMA: Implemented Toggle Autoview
  * IMA/ClassroomManager: sort items numerically where appropriate
  * ICA/Linux/x11vnc: synced with libvncserver Git repository
  * Updated localization files:
  - Czech
  - French
  - German
  - Norwegian
  - Slovakian
  - Ukrainian
  - Spanish
  * Added localization files
  - Catalan
  - Hebrew
  - Turkish
  * Localization files: merged all translations of each language
    into one file
  + Bugfixes:
  * Allow remote login without password
  * Include stdint.h for compiling with GCC >= 4.4
  * Setup/Makefile.am: do not fail linking when using
  - -as-needed linker flag
  * IsdServer: fixed running multiple program
  * IMA/Client: do not paint screen if window is too small
- added patch from Frank Schuett to italc-launcher, so the keys
  mentioned in /etc/settings/iTALC Solutions/iTALC.conf are
  honored
- fixed deprecated md5 module usage in italc-launcher
* Sat Jun 26 2010 cyberorg@opensuse.org
- use gcc43 to enable building on 11.3
* Fri Nov 20 2009 cyberorg@opensuse.org
- add export SUSE_ASNEEDED=0 to enable building on 11.2
* Thu Oct  1 2009 cyberorg@opensuse.org
- Fix source6 defined twice
- add italc-add-missing-include-gcc4.4.patch to fix build on new gcc
* Mon Mar 30 2009 lars@linux-schulserver.de
- fix italc-launcher again to save/re-use system lang for ifconfig
  (thanks again to Ciro Iriarte for the patch)
* Tue Mar 24 2009 lars@linux-schulserver.de
- fix italc-launcher not finding ifconfig
  (thanks to Ciro Iriarte for the patch)
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Thu Sep 18 2008 lrupp@suse.de
- write logfiles to /var/tmp as files in this directory are stored
  longer than in /tmp
* Mon Sep  1 2008 lars@linux-schulserver.de
- fix ica launch script
* Fri Aug 15 2008 lars@linux-schulserver.de
- added wvstreams-devel to BuildRequires
* Mon Aug 11 2008 cyberorg@opensuse.org
- Add italc-launcher and new ica launch scripts from stgraber@ubuntu.com
  +Autodetection of all the clients using avahi
* Thu Jul 24 2008 lars@linux-schulserver.de
- update to 1.0.9:
  + switched back to Qt 4.3.5 - finally "fixes" demo-crash
  + fixed endless loop when initializing keys
  + add date and time to logfiles
  + updated miniLZO-library to version 2.03
  + increased timeouts in socket-read-function in order to minimize
    lost connections
  + made Linux-version compile with libc 2.8
  + Linux: integrated latest x11vnc-version which fixes
    ICA-crashes when isconnecting during internal speed-estimations
  + added option for making toolbar buttons only display icon
  + fixed tooltip flicker issue
  + made visibility of individual sidebar-buttons configurable
    via context-menu
  + when selecting multiple clients (<ctrl>+left click) perform
    context-menu action on all selected clients
  + added support for controlling master-application via
    system-tray-icon
* Mon Jul  7 2008 lars@linux-schulserver.de
- update to 1.0.9-rc4:
  + integrated latest x11vnc-version which fixes ICA-crahes when
    disconnecting in certain situations
  + do not update GUI outside GUI-thread - fixes crashes of master
* Fri Jun 13 2008 lars@linux-schulserver.de
- update to 1.0.9-rc3:
  + made visibility of individual sidebar-buttons configurable
    via context-menu
  + when selecting multiple clients (<ctrl>+left click) process
    selected action in context menu on all clients
  + fixed possibility to escape locked mode
  + finally fixed huge-logfile problem under win32
  + made Linux-version compile on latest systems
  + in case of failed connections, sleep longer for not immediately
    hitting WinXP SP2 connection limit
* Thu Jun 12 2008 lars@linux-schulserver.de
- prefix ICA variables to aviod name clashes
- package the script and desktop file in other distributions, too
- enable post script for italc and italc-master on other dists
- new pathname: Applications/iTALC in sysconfig
* Wed Jun 11 2008 lars@linux-schulserver.de
- allow additional options in /etc/sysconfig/ica for ica
- allow really to disable ica in /etc/sysconfig/ica
* Tue Jun 10 2008 lars@linux-schulserver.de
- enhanced documentation in README and sysconfig
- firewall settings should be in the italc package
* Mon Jun  9 2008 lars@linux-schulserver.de
- /etc/X11/xinit/xinitrc.d/ is to early
  use /etc/xdg/autostart now
* Thu Jun  5 2008 lars@linux-schulserver.de
- the sysconfig script is called italc not ica (set manually)
- complete reconstruction of the ica start. Using an adapted script
  from Skolelinux now
- start ica using /etc/X11/xinit/xinitrc.d/
* Mon May 26 2008 lars@linux-schulserver.de
- update to 1.0.9-rc2 (1.0.8.992):
  + Qt 4.4-compatibility fixes
  + fixed mode-buttons in toolbar (demo, locked ...)
  + fixed tray-menu-actions when main-window is minimized
  + updated localizations
* Tue May 20 2008 lars@linux-schulserver.de
- the private keys and directories should belong to the
  italc-master package
- don't pay attention for 'other' role
* Fri May 16 2008 lars@linux-schulserver.de
- fix renamed italc init script in activation code
* Sun May 11 2008 lars@linux-schulserver.de
- update to 1.0.9-rc1 (1.0.8.99 to make updates easier):
  + fixed demo-mode on Linux
  + fixed endless loop when initializing keys
  + add date and time to logfiles
    (italc-1.0.8-logging.patch removed)
  + added option for making toolbar buttons only display icon
  + fixed tooltip flicker issue
  + updated miniLZO-library to version 2.03
  + added support for controlling master-application via
    system-tray-icon
  + increased timeouts in socket-read-function in order to minimize
    lost connections
* Wed Apr 23 2008 lars@linux-schulserver.de
- added italc-1.0.8-logging.patch
- don't call --with-qtdir on fedora and centos
* Mon Apr 21 2008 lars@linux-schulserver.de
- update to 1.0.8:
  - disabled MMX-optimized image-scaler on x86_64 as
    it's currently buggy
  - added zoom-feature: holding mouse-button on a client-window
    makes it zoom
  - display hostname in client-windows when "show user" is
    not checked
  - removed support-tab and added a button in toolbar instead
  - improved sidebar
  - visibility of individual toolbar-buttons can be configured
    via the toolbar-contextmenu
  - fixed several issues with scaling in remote-control-window
  - always try to run demo-server on default-port 5858 to allow
    easier and more secure firewall-configuration
  - drag'n drop support in classroom manager
  - fixed confirmation-dialog when closing setup-window
    via Alt+F4/close-button
  - added timeout-recognition in isdConnection::readFromServer()-function
    which makes iTALC-master not hang when quitting if a connection
    is somehow blocked
  - the name-field of a client is now optional - if you do not
    specify it, the hostname/IP is used for displaying
    the client's name
  - network-interface for demo-modes doesn't need to be configured
    anymore - it's auto-detected by clients
  - improved stability of demo-server
- added Port 5858 to the SuSEfirewall2
- removed upstreamed italc-1.0.7-fix-x64_64-compilation.patch
- fix some duplicated buildrequires
- prereq pwdutils
* Mon Mar 10 2008 lars@linux-schulserver.de
- update to 1.0.7:
  - improved overall usability by adding new icons and reworking
    look of overview-mode
  - added new image-scaling algorithm with (optional)
    MMX-optimizations in order to use less CPU-time on master-computer
    when monitoring a lot of clients with short update-intervals
  - thanks to fast image-scaler, remote-control and demo-mode now
    scale screen in real-time instead of having the user to scroll
  - removed user-list and added ability to display user-name instead
    of IP-address in classroom-manager instead
  - removed remote-IP-property as not used anymore
  - fixed logon-feature from classroom-action-menu
  - in case user accidently changed role but no keys exist for this
    role try teacher-role as fallback in order to make iTALC still
    usable in such cases (Closes #1866440)
  - added Polish localization-files
  - made power-down, reboot and logoff work under Linux
    if no user is logged in
  - fixed various crashes
- use the rcitalc script in /etc/X11/xdm/Xsetup (italc-setup.sh)
- rcitalc just starts, if third parameter is given
* Fri Mar  7 2008 lars@linux-schulserver.de
- created italc-setup.sh to be able to stop and start italc even
  if the package is not (de-)installed
- added README.SuSE for italc-client
* Tue Mar  4 2008 lars@linux-schulserver.de
- added service definition for SuSEfirewall2 (> 1020)
* Fri Feb 22 2008 lars@linux-schulserver.de
- update to 1.0.6:
  + many 64bit fixes
  + added possibility to set parameters such as -ivsport and -isdport
    using settings in /etc/settings/iTALC Solutions/iTALC.conf
  + added setting for client-double-click-action
  + added "-v" and "--version"-parameter
  + added support for trapping Alt+Space (closes italc#1704091)
  + also print log-messages to stdout
  + correct titlebar caption (closes italc#1700553)
  + set widget-cursor for vncView to according remote-cursor
    instead of drawing it - speeds thing a bit up
  + complete redesign of toolbar and buttons
  + made all code in common-dir a shared library which all
    components are linked against
  + do not reload clients if remote-control is active
  + do not resize to desktop-geometry in window-mode
  + lot of cleanups
  + use "halt" rather than "poweroff" for halting Linux-systems
  + when copying file add absolute paths to source-file-names
    (closes italc#1704173)
  + display user-name in toolbar (closes italc#1711333)
  + updated localizations
  + implemented "lock student"-functionality in remote-control
  + highlight current classroom in classroom-menu
  + added "hide teacher-clients"-feature
  + added key for loglevel: 0 silent, 2 fatal, 4 critical,
    6 warning, 9 debug, default is 6
  + changed log-directory to /tmp
  + added fullscreen-functionality via F11
  + stop demo on clients after student showed demo
  + also accepting keys that were generated using ssh-keygen
  + added "-screen"-argument which makes it possible to specify
    which screen the remote-control-window should be displayed on
  + fixed host-based authentication in such a way that it works for
    ThinClient-environments as well as when ports other than 5900
    are used for IVS (i.e. -ivsport has been used) - fixes
    non-working-demo in these scenarios
  + make Backtab (i.e. Shift+Tab) work properly in remote-control
    (closes italc#1889307)
- fix permissions of the generated keys
- added sysconfig file and init script
- start ica automatically via /etc/X11/xdm/Xsetup for clients
* Tue Jan 15 2008 lars@linux-schulserver.de
- add italc group automatically
- generate italc keys automatically
* Wed May  2 2007 lars@linux-schulserver.de
- update to 1.0.2
* Tue Dec 12 2006 lars@linux-schulserver.de
- initial package 1.0.0.0-rc2
