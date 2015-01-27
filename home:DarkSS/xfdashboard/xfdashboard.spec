Name:           xfdashboard
Version:        0.3.8
Release:        0
Summary:        GNOME shell like dashboard for Xfce
License:        GPL-2.0+
Url:            http://xfdashboard.froevel.de
Source0:        https://github.com/gmc-holle/xfdashboard/archive/%{version}.tar.gz
BuildRequires:  clutter-devel
BuildRequires:  desktop-file-utils
BuildRequires:  garcon-devel
BuildRequires:  libICE-devel
BuildRequires:  libtool
BuildRequires:  libwnck-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  xfconf-devel

%description
Xfdashboard provides a GNOME shell dashboard like interface for use with Xfce
desktop. It can be configured to run to any keyboard shortcut and when executed
provides an overview of applications currently open enabling the user to switch
between different applications. The search feature works like Xfce's app finder
which makes it convenient to search for and start applications.

%package themes
Summary:        Themes for Xfdashboard
Requires:       %{name}

%description themes
Additional themes for use with Xfdashboard

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
./autogen.sh --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-settings.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}
%{_bindir}/%{name}-settings
%{_datadir}/%{name}/bindings.xml
%{_datadir}/%{name}/preferences.ui
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_datadir}/themes/%{name}/*

%files themes
%defattr(-,root,root)
%{_datadir}/themes/%{name}-*

%changelog
