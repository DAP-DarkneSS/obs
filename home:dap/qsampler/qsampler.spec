%define rev	2546
%define rel	3

%if %{rev}
%define release	%mkrel -c %{rev} %{rel}
%else
%define release	%mkrel %{rel}
%endif

Name:		qsampler
Summary:	LinuxSampler GUI front-end application
Version:	0.2.2
Release:	%{release}
License:	GPLv2
Group:		Sound/Midi
# Create tarball from svn in SOURCES using:
# ./mk_svn_tar qsampler https://svn.linuxsampler.org/svn/qsampler/trunk tar.gz
Source0:	%{name}-%{rev}.tar.gz
Source1:	mk_svn_tar
URL:		http://qsampler.sourceforge.net/
BuildRequires:	pkgconfig(lscp)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(gig)
Requires:	linuxsampler

%description
QSampler is a LinuxSampler GUI front-end application written in 
C++ around the Qt4 toolkit using Qt Designer. At the moment it 
just wraps as a client reference interface for the LinuxSampler 
Control Protocol (LSCP).

%files
%{_bindir}/qsampler
%{_datadir}/applications/qsampler.desktop
%{_datadir}/icons/hicolor/32x32/apps/qsampler.png
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-qsampler-session.png
%{_datadir}/icons/hicolor/scalable/apps/qsampler.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-qsampler-session.svg
%{_datadir}/locale/*.qm
%{_datadir}/mime/packages/qsampler.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}
[ -f Makefile.svn ] && make -f Makefile.svn

%build
export PATH=$QTDIR/bin:$PATH
%configure2_5x
%make 

%install
%makeinstall_std


%changelog
* Tue May 13 2014 barjac <barjac> 0.2.2-0.2546.3.mga5
+ Revision: 622399
- new snapshot 2546
- fix files list

* Sat Oct 19 2013 umeabot <umeabot> 0.2.2-0.2459.2.mga4
+ Revision: 531790
- Mageia 4 Mass Rebuild

* Sun Aug 11 2013 barjac <barjac> 0.2.2-0.2459.1.mga4
+ Revision: 465353
- new snapshot 2459
- use makeinstall_std
- fix files

* Sun Jan 13 2013 umeabot <umeabot> 0.2.2-0.2379.2.mga3
+ Revision: 379911
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Fri Jan 11 2013 barjac <barjac> 0.2.2-0.2379.1.mga3
+ Revision: 349433
- correct release format

* Wed Nov 14 2012 barjac <barjac> 0.2.2-0.2379.mga3
+ Revision: 317573
- imported package qsampler

