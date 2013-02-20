#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:           foobnix
Version:	2.6.09
Release:	1
Summary:	Player for any music from the internet
Group:		Productivity/Multimedia/Sound/Players
License:	GPL-3.0
Url:		http://www.foobnix.com/
Source:		https://launchpad.net/~foobnix-team/+archive/foobnix-player/+files/%{name}_%{version}q.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version} > 1110  
Requires:       python-base = %py_ver  
BuildRequires:  python-base  
# This works on newer version  
# on older version it dies misserably if used  
BuildArch:      noarch  
%else  
# Required way for older version of suse  
Requires:       python = %py_ver  
BuildRequires:  python  
%endif

Requires:	dbus-1-python
Requires:	python-mutagen python-chardet python-keybinder
Requires:	python-gtk python-gstreamer010 >= 0.10.18
Requires:	python-simplejson

BuildRequires:	python-devel
BuildRequires:	python-gtk
BuildRequires:	update-desktop-files
BuildRequires:	dos2unix

AutoReqProv:    on

%description
Player written in Python, GTK +, Glade
The idea of creating the player was such that now almost all the music is 
on the internet (videos, facebook, last.fm and other sites), 
but she or is not structured or an existing directory, but you can not listen to or paid.

Authors:
--------
    Name Surname 
    Ivan Ivanenko

%prep
%setup -q -n %{name}_%{version}

find foobnix/ -name "*.py" -exec dos2unix {} ';'
# remove shebangs from library files  
find foobnix/ -name "*.py" -exec sed -i -e  '/^#!\s\?\/usr\/bin\/\(env\s\)\?python$/d' {} ';'

%build
%{__python} setup.py build 

%install
%{__python} setup.py install \
        --prefix=%{_prefix} \
        --root=%{buildroot} \
        --record-rpm=%{name}_filelist.txt
%suse_update_desktop_file -r %{name}
%suse_update_desktop_file -i %{name} Music Player

# Check compress manual pages so fix it here..
sed -i 's/foobnix.1$/foobnix.1.gz/g' %{name}_filelist.txt
# fix folder names that should not exist in file list to start with... 
sed -i -e "/\/usr\/share\/applications$/d" %{name}_filelist.txt
sed -i -e  "/\/usr\/share\/pixmaps$/d" %{name}_filelist.txt
sed -i -e  "/\.mo$/d" %{name}_filelist.txt
%find_lang %{name}
cat  %{name}_filelist.txt  %{name}.lang > all_files.list

%files -f all_files.list
%defattr(-,root,root)

%changelog
