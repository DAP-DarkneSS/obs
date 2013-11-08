%ifarch %{ix86}
BuildArchitectures: i686
%endif

# %{?rhel} %{?centos} %{?centos_ver}
%if 0%{?centos_version} >= 600
%define dist .el%(echo %{?centos_version} | cut -b 1)
%endif


Name: smillaenlarger
Summary: graphical tool to resize bitmaps in high quality
Version: 0.9.0
Release: 0%{?dist}.1.<B_CNT>
License: GPLv3+
Group: Amusements/Graphics
URL: http://sourceforge.net/projects/imageenlarger/
Source0: smillaenlarger_%{version}.orig.tar.bz2
Source1: smillaenlarger_%{version}-0.2~ppa3.debian.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: Sawa <http://linux.ikoinoba.net/>
BuildRequires: qt-devel gcc-c++ desktop-file-utils

%description
SmillaEnlarger is a small graphical tool ( based on Qt ) to resize,
especially magnify bitmaps in high quality.

%prep
%setup -q -a 1
patch -p1 < debian/patches/fix_version.diff
cd SmillaEnlargerSrc
%{_libdir}/qt4/bin/qmake ImageEnlarger.pro

%build
cd SmillaEnlargerSrc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -m0755 -D -s SmillaEnlargerSrc/SmillaEnlarger %{buildroot}%{_libexecdir}/SmillaEnlarger
%{__install} -m0644 -D SmillaEnlargerSrc/smilla.png %{buildroot}%{_datadir}/pixmaps/smillaenlarger.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications debian/etc/smillaenlarger.desktop

#%{__install} -m0755 -D debian/etc/smillaenlarger %{buildroot}%{_bindir}/smillaenlarger
# (^^;
sed -i -e 's|/usr/share/doc/smillaenlarger|%{_docdir}/%{name}-%{version}|g' \
       -e 's|/usr/lib/smillaenlarger|%{_libexecdir}|g' debian/etc/smillaenlarger
%{__install} -m0755 -D debian/etc/smillaenlarger %{buildroot}%{_bindir}/smillaenlarger

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ReadMe.rtf WhatsNew.rtf changelog.txt gpl-3.0.txt
%doc debian/etc/smillaenlarger.ini
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Wed Apr 11 2012 Sawa <sawa@ikoinoba.net> - 0.9.0
- Initial package
