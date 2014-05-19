%define ver      2.7.4
%define rel      0
%define prefix   /usr

Summary: transparent applications suite
Name: transparency
Version: %{ver}
Release: %{rel}
License: GPL
Group: User Interface/X
Source: %{name}-%{ver}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot

Requires: qt4-common, libqtcore4, libqtgui4, aspell >= 0.60.4, libaspell15 >= 0.60.4

%description
transparent applications suite:
- transparent clock;
- transparent calendar;
- transparent cpu load meter;
- transparent memory load meter;
- transparent disk usage meter;
- transparent network load meter;
- transparent temperature meter.
- transparent pictures display.

%prep
%setup -q -n %{name}-%{ver} %{rel}

%build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} .
make -j4

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING INSTALL
%{prefix}/bin/transparency
%{prefix}/bin/transparency-settings
%{prefix}/bin/transparent-clock
%{prefix}/bin/transparent-calendar
%{prefix}/bin/transparent-pictures

%changelog
