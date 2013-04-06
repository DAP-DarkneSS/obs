# norootforbuild

Name:				imwheel
Version:			1.0.0pre12
Release:			0
Summary:			Mouse Event to Key Event Mapper Daemon
Source:			http://prdownloads.sourceforge.net/imwheel/imwheel-%{version}.tar.gz
Patch1:			imwheel-intptr_t.patch
Patch2:			imwheel-fix_uninitialized_var.patch
Patch3:			imwheel-fix_destdir.patch
Patch4:			imwheel-config_file_path.patch
URL:				http://imwheel.sourceforge.net
Group:			Hardware/Other
License:			GNU General Public License version 2 (GPL v2)
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	make gcc glibc-devel xorg-x11-devel
BuildRequires:	autoconf automake libtool

%description
A daemon for X11, which watches for mouse wheel actions and outputs them as
keypresses. It can be configured separately for different windows. It also
allows input from it's own (included) gpm, or from jamd, or from XFree86 ZAxis
mouse wheel conversion.




Authors:
--------
    Jonathan Atkins <jcatki@home.com>

%debug_package
%prep
%setup -q
%patch1
%patch2
%patch3
%patch4

%build
autoreconf -fiv
%configure --with-x
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog COPYING EMACS FREEBSD
%doc M-BA47 NEWS README TODO
%config(noreplace) %{_sysconfdir}/imwheelrc
%{_bindir}/imwheel
%doc %{_mandir}/man1/imwheel.1*

%changelog
* Tue Jan  8 2008 Pascal Bleser <guru@unixtech.be> 1.0.0pre12
- new package

# Local Variables:
# mode: rpm-spec
# tab-width: 3
# End:
