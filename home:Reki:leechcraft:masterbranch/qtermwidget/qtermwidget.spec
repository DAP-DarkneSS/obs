
Name:		qtermwidget
Summary:	Qt4 terminal widget
Version:	0.5.0
Release:	0
License:	GPL-2.0+
Source:		%{name}-%{version}.tar.bz2
Group:		Development/Libraries/C and C++
Url:		https://github.com/qterminal/qtermwidget
Vendor:         Petr Vanek <petr@yarpen.cz>
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	pkg-config
BuildRequires:	pkgconfig(QtGui)
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
QTermWidget is an opensource project based on KDE4 Konsole application. The main goal of this project is to provide unicode-enabled, embeddable QT4 widget for using as a built-in console (or terminal emulation widget). 
Of course I`m aware about embedding abilities of original Konsole, but once I had Qt without KDE, and it was a serious problem. I decided not to rely on a chance. I could not find any interesting related project, so I had to write it. 
The original Konsole`s code was rewritten entirely with QT4 only; also I have to include in the project some parts of code from kde core library. All code dealing with user interface parts and session management was removed (maybe later I bring it back somehow), and the result is quite useful, I suppose. 

%package -n libqtermwidget4-0
Summary:	Qt4 terminal widget
Group:		Development/Libraries/C and C++

%description -n libqtermwidget4-0
QTermWidget is an opensource project based on KDE4 Konsole application. The main goal of this project is to provide unicode-enabled, embeddable QT4 widget for using as a built-in console (or terminal emulation widget). 
Of course I`m aware about embedding abilities of original Konsole, but once I had Qt without KDE, and it was a serious problem. I decided not to rely on a chance. I could not find any interesting related project, so I had to write it. 
The original Konsole`s code was rewritten entirely with QT4 only; also I have to include in the project some parts of code from kde core library. All code dealing with user interface parts and session management was removed (maybe later I bring it back somehow), and the result is quite useful, I suppose. 


%package devel
Summary:	Qt4 terminal widget - devel package
Group:          Development/Libraries/C and C++
Requires:       libqtermwidget4-0 = %{version}
Requires:	pkg-config

%description devel
Development environment for qtermwidget library

%prep
%setup -q

%build
%cmake
%__make

%install
%cmake_install

%clean
%{__rm} -rf %{buildroot}

%post -n libqtermwidget4-0 -p /sbin/ldconfig

%postun -n libqtermwidget4-0 -p /sbin/ldconfig

%files -n libqtermwidget4-0
%defattr(-,root,root,-)
%doc AUTHORS COPYING Changelog README 
%{_libdir}/lib%{name}4.so.*
%{_libdir}/qt4/plugins/designer/lib%{name}4plugin.so
%{_datadir}/%{name}4/

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}4
%{_libdir}/lib%{name}4.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/cmake/%{name}4


%changelog
