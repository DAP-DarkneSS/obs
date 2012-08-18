Name:           testendian
Summary:        Check bytes order
Group:          Development/Tools/Other
Source0:        raw.cpp
Version:        0
Release:        1
License:        Unknown

BuildRequires:  gcc-c++

%description
Check your machine bytes order.

%prep
%{__install} %{SOURCE0} %{_builddir}

%build
g++ -o %{name} %{SOURCE0}

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} %{name} %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Sat Aug 18 2012 DA <dap.darkness@gmail.com> - 20120818-1
- Initial build.
