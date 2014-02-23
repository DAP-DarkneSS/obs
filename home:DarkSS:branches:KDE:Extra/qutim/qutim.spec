#
# spec file for package qutim
#
# Copyright (c) 2012 Sergei Lopatin <magist3r@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           qutim
Version:        0.3.1
Release:        1.0
License:        GPL-3.0+
Summary:        QutIM instant messenger
Url:            http://qutim.org/
Group:          Productivity/Networking/Instant Messenger
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM fix-compilation-on-new-versions-of-cmake.patch -- fixes build with cmake 2.8.12
Patch0:         fix-compilation-on-new-versions-of-cmake.patch
Requires:       libjreen1 >= 1.1.0
Requires:       libqca2-plugin-cyrus-sasl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	update-desktop-files
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  libQtWebKit-devel >= 4.6
BuildRequires:  libjreen-devel >= 1.1.0
BuildRequires:  libqca2-devel >= 2.0
BuildRequires:  libqt4-devel >= 4.6
BuildRequires:  phonon-devel
BuildRequires:  doxygen
BuildRequires:  libpurple-devel
%if 0%{?suse_version} >= 1230
BuildRequires:	libotr2-devel
%else
BuildRequires:  libotr-devel >= 3.2
%endif

%description
Multiprotocol instant messenger.

%package devel
Summary:        Development files for QutIM
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libjreen-devel >= 1.1.0
Requires:       libqca2-devel >= 2.0
Requires:       libqt4-devel >= 4.6

%description devel
Development files for QutIM

%package plugin-aspeller
Summary:        Aspeller plugin for QutIM
BuildRequires:  aspell
BuildRequires:  aspell-devel
Requires:       %{name} = %{version}
Supplements:    packageand(qutim:aspell)

%description plugin-aspeller
Spell checker plugin for QutIM based on aspell

%package plugin-hunspeller
Summary:        Hunspeller plugin for QutIM
Requires:       %{name} = %{version}

BuildRequires:  hunspell
BuildRequires:  hunspell-devel
Supplements:    packageand(qutim:hunspell)

%description plugin-hunspeller
Spell checker plugin for QutIM based on hunspell

%package plugin-kdeintegration
Summary:        KDE integration plugin for QutIM
BuildRequires:  libkde4-devel
Requires:       %{name} = %{version}
Supplements:    packageand(qutim:libkde4)
%kde4_runtime_requires

%description plugin-kdeintegration
Plugin that provides integration with KDE

%package plugin-sdlsound
Summary:        SDL sound plugin for QutIM
BuildRequires:  libSDL_mixer-devel
Requires:       %{name} = %{version}
Supplements:    packageand(qutim:libSDL_mixer-1_2-0)

%description plugin-sdlsound
Sound engine plugin based on SDL

%prep
%setup -q
%if %{suse_version} > 1310
%patch0 -p1
%endif

%build
LIBSUFFIX=$(echo "%{_lib}"|sed 's/^lib//')
mkdir build
pushd build
export CXXFLAGS="%{optflags}"
export QMAKE_CXXFLAGS="%{optflags}"
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DSYSTEM_JREEN=1 \
    -DLIB_SUFFIX="$LIBSUFFIX" \
    -DBEARERMANAGER=1 \
    -DMULTIMEDIABACKEND=0 \
    -DANTIBOSS=0 \
    -DPLUGMAN=0 \
    -DIMAGEPUB=0 \
    -DQMLCHAT=0 \
    -DSQLHISTORY=0 \
    -DWEBHISTORY=0 \
    -DDBUSAPI=0 \
    -DAWN=0 \
    -DMOBILEABOUT=0 \
    -DMOBILECONTACTINFO=0 \
    -DMOBILENOTIFICATIONSSETTINGS=1 \
    -DNOTIFICATIONSSETTINGS=0 \
    -DMOBILESETTINGSDIALOG=0 \
    -DQRCICONS=0 \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    ..

make %{?_smp_flags}
#make
popd #build

%install
pushd build
%make_install
%suse_update_desktop_file qutim
popd #build

# Link duplicate files
%fdupes %{buildroot}/%{_datadir}/apps

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_libdir}/qutim
%dir %{_libdir}/qutim/plugins
%{_datadir}/%{name}
%{_datadir}/apps
%doc AUTHORS ChangeLog COPYING README.mediawiki

%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

#lib
%{_libdir}/libqutim.so.*
%{_libdir}/libqutim-adiumwebview.so.*

#app icons
%{_datadir}/icons/*
%{_datadir}/pixmaps/qutim.xpm

#protocols
%{_libdir}/qutim/plugins/libirc.so
%{_libdir}/qutim/plugins/libjabber.so
%{_libdir}/qutim/plugins/libmrim.so
%{_libdir}/qutim/plugins/liboscar.so
%{_libdir}/qutim/plugins/liboscaridentify.so
%{_libdir}/qutim/plugins/liboscarxstatus.so
%{_libdir}/qutim/plugins/libvkontakte.so
%{_libdir}/qutim/plugins/libvkontaktewall.so
%{_libdir}/qutim/plugins/libvphotoalbum.so
%{_libdir}/qutim/plugins/libquetzal.so

#plugins
%{_libdir}/qutim/plugins/libadiumwebview.so
%{_libdir}/qutim/plugins/libaccountcreator.so
%{_libdir}/qutim/plugins/libaddcontactdlg.so
%{_libdir}/qutim/plugins/libadiumchat.so
%{_libdir}/qutim/plugins/libadiumsrvicons.so
%{_libdir}/qutim/plugins/libauthdialog.so
%{_libdir}/qutim/plugins/libbearermanager.so
%{_libdir}/qutim/plugins/libchatnotificationsbackend.so
%{_libdir}/qutim/plugins/libchatspellchecker.so
%{_libdir}/qutim/plugins/libcontactinfo.so
%{_libdir}/qutim/plugins/libdataformsbackend.so
%{_libdir}/qutim/plugins/libemoticonssettings.so
%{_libdir}/qutim/plugins/libfiletransfer.so
%{_libdir}/qutim/plugins/libfiletransfersettings.so
%{_libdir}/qutim/plugins/libidledetector.so
%{_libdir}/qutim/plugins/libidlestatuschanger.so
%{_libdir}/qutim/plugins/libjoinchatdialog.so
%{_libdir}/qutim/plugins/libjoingroupchatdlg.so
%{_libdir}/qutim/plugins/libjsonconfig.so
%{_libdir}/qutim/plugins/libjsonhistory.so
%{_libdir}/qutim/plugins/libkineticscroller.so
%{_libdir}/qutim/plugins/libkopeteemoticonsbackend.so
%{_libdir}/qutim/plugins/liblocalization.so
%{_libdir}/qutim/plugins/libmetacontacts.so
%{_libdir}/qutim/plugins/libmigration02x03.so
%{_libdir}/qutim/plugins/libnocryptoservice.so
%{_libdir}/qutim/plugins/libnotificationfilter.so
%{_libdir}/qutim/plugins/libmobilenotificationssettings.so
%{_libdir}/qutim/plugins/liboldsoundtheme.so
%{_libdir}/qutim/plugins/libpassword.so
%{_libdir}/qutim/plugins/libplaincontactsmodel.so
%{_libdir}/qutim/plugins/libplistconfig.so
%{_libdir}/qutim/plugins/libproxysettings.so
%{_libdir}/qutim/plugins/libqticons.so
%{_libdir}/qutim/plugins/libsearchdialog.so
%{_libdir}/qutim/plugins/libservicechooser.so
%{_libdir}/qutim/plugins/libsessionhelper.so
%{_libdir}/qutim/plugins/libseparatedcontactsmodel.so
%{_libdir}/qutim/plugins/libshortcutsettings.so
%{_libdir}/qutim/plugins/libsimpleaboutdialog.so
%{_libdir}/qutim/plugins/libsimpleactionbox.so
%{_libdir}/qutim/plugins/libsimpleactions.so
%{_libdir}/qutim/plugins/libsimplecontactlist.so
%{_libdir}/qutim/plugins/libsimplecontactlistwidget.so
%{_libdir}/qutim/plugins/libsimplecontactdelegate.so
%{_libdir}/qutim/plugins/libsimplerosterstorage.so
%{_libdir}/qutim/plugins/libsoundthemeselector.so
%{_libdir}/qutim/plugins/libstackedchatform.so
%{_libdir}/qutim/plugins/libtabbedchatform.so
%{_libdir}/qutim/plugins/libtextchat.so
%{_libdir}/qutim/plugins/libtorycontactlistwidget.so
%{_libdir}/qutim/plugins/libtrayicon.so
%{_libdir}/qutim/plugins/libtreecontactsmodel.so
%{_libdir}/qutim/plugins/libxsettingsdialog.so
%{_libdir}/qutim/plugins/liblinuxintegration.so
%{_libdir}/qutim/plugins/libphononsound.so

%{_libdir}/qutim/plugins/libaescrypto.so
%{_libdir}/qutim/plugins/libantispam.so
%{_libdir}/qutim/plugins/libbirthdayreminder.so
%{_libdir}/qutim/plugins/libclconf.so
%{_libdir}/qutim/plugins/libemoedit.so
%{_libdir}/qutim/plugins/libfloaties.so
%{_libdir}/qutim/plugins/libhistman.so
%{_libdir}/qutim/plugins/libkineticpopups.so
%{_libdir}/qutim/plugins/libmassmessaging.so
%{_libdir}/qutim/plugins/liboldcontactdelegate.so
%{_libdir}/qutim/plugins/libscriptapi.so
%{_libdir}/qutim/plugins/libunreadmessageskeeper.so
%{_libdir}/qutim/plugins/libweather.so
%{_libdir}/qutim/plugins/liblogger.so
%{_libdir}/qutim/plugins/liburlpreview.so
%{_libdir}/qutim/plugins/libyandexnarod.so
%{_libdir}/qutim/plugins/libdbusnotifications.so
%{_libdir}/qutim/plugins/libnowplaying.so
%{_libdir}/qutim/plugins/libhighlighter.so
%{_libdir}/qutim/plugins/libblogimprover.so
%{_libdir}/qutim/plugins/libupdater.so
%{_libdir}/qutim/plugins/libofftherecord.so

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libqutim.so
%{_libdir}/libqutim-adiumwebview.so
%{_datadir}/cmake/Modules

%files plugin-aspeller
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libaspeller.so

%files plugin-hunspeller
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libhunspeller.so

%files plugin-kdeintegration
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libkdeintegration.so
%dir %{_datadir}/kde4/apps/desktoptheme/
%dir %{_datadir}/kde4/apps/desktoptheme/default
%dir %{_datadir}/kde4/apps/desktoptheme/default/icons
%{_datadir}/kde4/apps/desktoptheme/default/icons/qutim.svg

%files plugin-sdlsound
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libsdlsound.so

%changelog
