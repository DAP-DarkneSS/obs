Summary:	GNOME screen ruler
Name:		screenruler
Version:	0.96
Release:	3%{?dist}
License:	GPLv2+
Group:		Applications/Engineering
URL:		https://launchpad.net/screenruler/
Source0:	http://launchpad.net/screenruler/trunk/0.9.6/+download/%{name}-0.9.6.tar.gz
Source1:	screenruler.desktop
Patch0:		screenruler-ruby19.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	desktop-file-utils
Requires:	ruby
Requires:	rubygem-gtk2 rubygem-cairo rubygem-gettext
Obsoletes:	gruler < 0.85
Provides:	gruler = %{version}-%{release}

BuildArch:	noarch

%description
Screenruler is a small GNOME based utility that allows you to measure objects 
on your desktop. It can be used to take both horizontal and vertical
measurement in 6 different metrics: pixels, centimeters, inches, picas, points,
and as a percentage of the ruler’s length.

%prep
%setup -q -n %{name}
%patch0 -p0 -b ruby19

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}

cat << EOF > screenruler
#!/bin/bash

cd %{_datadir}/%{name}
ruby ./screenruler.rb
EOF
chmod 0755 screenruler

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p screenruler %{buildroot}%{_bindir}/
cp -p screenruler-icon*.png %{buildroot}%{_datadir}/pixmaps/
cp -pr utils *.rb screenruler*.* *.glade %{buildroot}%{_datadir}/%{name}/
cd %{buildroot}%{_datadir}/pixmaps
 ln -s ./screenruler-icon-32x32.png screenruler-icon.png

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
	--vendor="fedora"				\
%endif
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications		\
	%{SOURCE1}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING 
%{_bindir}/screenruler
%{_datadir}/screenruler/
%{_datadir}/pixmaps/screenruler-icon*.png
%{_datadir}/applications/*.desktop

%changelog
