#
# spec file for package [spectemplate]
#
# Copyright (c) 2010-2012 Rudoy Georg aka 0xd34df00d (source), (c) 2012 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via https://github.com/0xd34df00d/lcpackgen/issues
#

%define _commit 1327077336

Name:           leechcraft-lcpackgen
Version:        1.1.git.%{_commit}
Release:        0
Summary:        Package description file generator for LeechCraft repos

License:        BSD
URL:            https://github.com/0xd34df00d/lcpackgen
Source0:        %{name}-%{version}.tar.bz2
Group:          Development/Tools/Other

BuildRequires:  make cmake
BuildRequires:  update-desktop-files
BuildRequires:  gcc gcc-c++
BuildRequires:  qt qt-devel libQtWebKit-devel libqt4-devel
Recommends:     leechcraft-lackman

%description
Package description file generator for packages for LeechCraft repos:
script plugins, iconsets, additional data and other similar packages.

%prep
%setup -q

%build
cd ./src/
cmake .
make

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} ./src/lcpackgen %{buildroot}%{_bindir}
%suse_update_desktop_file -c lcpackgen lcpackgen "LeechCraft packages generator" lcpackgen "" "Development;Design;"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/lcpackgen
%{_datadir}/applications/lcpackgen.desktop

%changelog
* Fri Jan 20 2012 DA <dap.darkness@gmail.com> - 20120120-1
- Commit 1327077336:
"Save as" action was added.
Autodetect archiver type was added (gz, bz2, lzma and hz are allowed).
Uppercase in filenames is allowed.

- Commit 1327070763:
If you open file in file manager with lcpackgen, selected xml will be loaded.

* Wed Jan 18 2012 DA <dap.darkness@gmail.com> - 20120118-1
- Commit 1319978478.
