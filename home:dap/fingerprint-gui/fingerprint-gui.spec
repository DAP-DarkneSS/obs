#
# spec file for package fingerprint-gui
#
# Copyright (c) 2008-2013 Wolfgang Ullrich <w.ullrich@n-view.net>
# (source), (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via
# https://bugs.links2linux.org
#

Name:           fingerprint-gui
Version:        1.04.99.2
Release:        1
License:        GPL-2.0+
Summary:        A tool for fingerprint enrollment and verification
Url:            http://www.n-view.net/Appliance/fingerprint/
Group:          System/X11/Utilities
Source0:        http://www.n-view.net/Appliance/fingerprint/download/fingerprint-gui-1.05~pre2.tar.gz
Source1:        %{name}.svg

#PATCH-FIX-UPSTREAM to fix deprecated Qt includes.
Patch0:         fingerprint-gui-qtinclude.patch
#PATCH-FIX-OPENSUSE to prevent using ldconfig.
Patch1:         fingerprint-gui-noldconfig.patch
#PATCH-FIX-OPENSUSE to prevent "ERROR: Icon file not installed".
Patch2:         fingerprint-gui-icon.patch

BuildRequires:  libfakekey-devel
BuildRequires:  libfprint-devel >= 0.1.0
BuildRequires:  libpolkit-qt-1-devel
BuildRequires:  libqca2-devel
BuildRequires:  libqt4-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  pam-devel
BuildRequires:  pwdutils
BuildRequires:  update-desktop-files
Requires(pre):  permissions
Requires:       libbsapi

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fingerprint GUI is a set of GUI tools for the use of fingerprint scanners
on Linux systems. It enables the recording and checking of fingerprints
of users and allows login and authentication of users by their
fingerprint through its PAM module. An additional "fingerprintIdentifier"
application can be used for customized (shell) scripts when users have to
be identified or authenticated by their fingerprints. The system is based
on device drivers from the "libfprint" project.

%package -n libbsapi
Version:        4.0
License:        SUSE-NonFree
Summary:        SDK for most of UPEK fingerprint readers (shared libraries)
Url:            http://www.upek.com/solutions/pc_and_networking/sdks/linux/

%description -n  libbsapi
The Biometric Services API (BSAPI) is a mid-level SDK for application
developers, allowing them to use UPEK fingerprint readers from their
applications. The set of provided functions includes biometry (e.g. swiping
fingers, matching finger templates etc.), navigation (i.e. using the
fingerprint reader as a pointing device in similar way as touchpad) and
other functions (e.g. controling LEDs on the fingerprint reader).

%prep
%setup -q -n %{name}-1.05~pre2
%patch0
%patch1
%patch2

%build
qmake \
LIBPOLKIT_QT=LIBPOLKIT_QT_1_1 \
QMAKE_STRIP="" \
PREFIX=%{_prefix} \
LIB=%{_lib} \
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}" \
QMAKE_LFLAGS+="%{optflags}"

make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
install -D %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/scalable/%{name}.svg
%suse_update_desktop_file %{name}
# Add permissions file to allow packaging of suid file on SUSE.
mkdir -p %{buildroot}%{_sysconfdir}/permission.d/
echo "%{_libdir}/%{name}/fingerprint-suid                        root.root 4755" > %{buildroot}%{_sysconfdir}/permission.d/%{name}

make INSTALL_ROOT=%{buildroot} install-upek
# Upek directory is created.
mkdir -p %{buildroot}%{_localstatedir}/upek_data

%verifyscript
%verify_permissions -e %{_prefix}/lib/%{name}/fingerprint-suid

%post
%set_permissions %{_prefix}/lib/%{name}/fingerprint-suid

%if %{undefined suse_version}
%pre -n libbsapi
/usr/sbin/groupadd -f -r plugdev
%endif

%post -n libbsapi
/sbin/ldconfig
# Udevadm commands:
if command -v udevadm >/dev/null; then \
  for ID in 2015 2016; do \
      udevadm trigger --subsystem-match=usb --attr-match=idVendor=0483 --attr-match=idProduct=$ID; \
  done; \
  for ID in 2015 2016 1000 1001 1002 1003 3000 3001 5002 5003; do \
      udevadm trigger --subsystem-match=usb --attr-match=idVendor=147e --attr-match=idProduct=$ID; \
  done; \
fi

%postun -n libbsapi -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING Lubuntu-Readme.txt README
%dir %{_datadir}/pixmaps/scalable
%attr(644,root,root) %{_datadir}/pixmaps/scalable/%{name}.svg
%{_datadir}/doc/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/*fingerprint*.?.gz
/%{_lib}/security/pam_%{name}.so
%{_prefix}/lib/%{name}
%{_bindir}/fingerprint*
%dir %{_sysconfdir}/permission.d
%config %{_sysconfdir}/permission.d/%{name}
%{_sysconfdir}/xdg/autostart/fingerprint-polkit-agent.desktop
%config %{_sysconfdir}/udev/rules.d/92-%{name}-uinput.rules

%files -n libbsapi
%defattr(-,root,root)
%{_libdir}/libbsapi.so
%config %{_sysconfdir}/upek.cfg
%{_localstatedir}/upek_data
%config %{_sysconfdir}/udev/rules.d/91-%{name}-upek.rules

%changelog
