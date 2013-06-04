%define name soundz
%define version 3.6.1
%define release %mkrel 1

Summary: Soundz audio player
Name:	 %{name}
Version: %{version}
Release: %{release}
URL:	 http://code.google.com/p/coverz/
Source0: %{name}-%{version}.tar.xz
License: GPLv3
Group:   Sound
BuildRoot: %{_tmppath}/%{version}-%{release}-buildroot
Patch:     %{name}-%{version}-desktop.patch
BuildArch: noarch
Requires: gettext  
Requires: gstreamer0.10-plugins-base
Requires: gstreamer0.10-pulse
Requires: fonts-ttf-droid
Requires: python-dbus
Requires: gstreamer0.10-python
Requires: pygtk2.0-libglade
Requires: pygtk2.0
Requires: mutagen
Requires: pyxdg


%description
A PyGTK audio player designed for XFCE

%prep
%setup -q -n %{name}-%{version}
%patch -p1

%build
#nobuild

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 %{buildroot}%{_bindir}
install -m 755 bin %{buildroot}%{_bindir}/soundz
install -dm 755 %{buildroot}/%{_datadir}/%{name}
cp -af {pix,gui,soundz,utils,mods} %{buildroot}/%{_datadir}/%{name}
install -dm 755 %{buildroot}/%{_datadir}/applications
install -m 755 desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -dm 755 %{buildroot}/%{_datadir}/pixmaps
install -m 644 pix/48.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png




%clean
rm -rf $RPM_BUILD_ROOT



%post
%{update_menus}


%postun
%{clean_menus}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Feb 06 2013 Ken <lxgator@gmail.com> 3.6.1-1pclos2013
- initial build
