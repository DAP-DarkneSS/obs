#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           xmahjongg
Version:        3.7
Release:        7.1
License:        GPL
Summary:        Colorful X solitaire Mah Jongg game
Url:            http://www.lcdf.org/xmahjongg/
Group:          X11/Applications/Games
Source0:        http://www.lcdf.org/xmahjongg/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
BuildRequires:  gcc-c++,
BuildRequires:  libX11-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary(pl):	Komputerowy Mad¿ong
Vendor:		Little Cambridgeport Design Factory

%description
Real Mah Jongg is a social game that originated in China thousands of
years ago. Four players, named after the four winds, take tiles from a
wall in turn. The best tiles are made of ivory and wood; they click
pleasantly when you knock them together. Computer Solitaire Mah Jongg
(xmahjongg being one of the sillier examples) is nothing like that but
it's fun, or it must be, since there are like 300 shareware versions
available for Windows. This is for X11 and it's free.

%description -l pl
Stara, chiñska gra logiczna. Powsta³a ona w staro¿ytnym Pañstwie
Šrodka, a jej historia siêga chiñskiej dynastii Zachodniego Chou,
czyli ok. 720 roku n.e. Podobnie jak wiêkszo¶æ gier karcianych tak i
mad¿ong rozwija³ siê niezale¿nie w ró¿nych okrêgach i prowincjach
dawnych Chin, zyskuj±c niezliczone odmiany dla ró¿nej liczby
graj±cych. Ta wersja przeznaczona jest dla jednej osoby i zawiera
kilka ró¿nych zestawów klocków (dorothys, gnome, gnome2, real, thick,
dorwhite, small, thin). Wywo³uje siê je za pomoc± parametru '-t'.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/%{name}

%changelog
