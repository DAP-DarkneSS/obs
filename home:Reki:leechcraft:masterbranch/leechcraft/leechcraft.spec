#
# spec file for package leechcraft
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# %%define qtversion %%(rpm -q libqt4 --qf='%%{VERSION}\n'|awk -F. '{print $1 * 10000 + $2 * 100 + $3}')
%define plugin_dir %{_libdir}/%{name}/plugins
%define translations_dir %{_datadir}/%{name}/translations
%define settings_dir %{_datadir}/%{name}/settings
%define azoth_dir %{_datadir}/%{name}/azoth

%define so_ver 0_6_75

%if 0%{?suse_version} >= 1320
%define clang_compiler 0
%else
%define clang_compiler 0
%endif
%define fenet 1
%define lmp 1
%define mellonetray 1
%define poleemery 1
%define woodpecker 1
%define vangog 1

Name:           leechcraft
Version:        git
%define LEECHCRAFT_VERSION 0.6.70-2063-g359188b
Release:        0
License:        BSL-1.0
Summary:        Modular Internet Client
Url:            http://leechcraft.org
Group:          Productivity/Networking/Other
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.svg

BuildRequires:  Qross-devel
BuildRequires:  boost-devel >= 1.50
BuildRequires:  cmake > 2.8.10
BuildRequires:  fdupes
BuildRequires:  file-devel
%if %{clang_compiler}
BuildRequires:  gcc49-c++
# BuildConflicts: gcc-c++
# BuildConflicts: libgcc_s1
%else
BuildRequires:  gcc-c++ >= 4.7
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  jbig2dec-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblastfm-devel
BuildRequires:  libotr-devel
BuildRequires:  libqscintilla-devel
BuildRequires:  libqt4-sql
%if 0%{?suse_version} > 1310
BuildRequires:  libqxt-devel
%endif
BuildRequires:  libsensors4-devel
BuildRequires:  libtidy-devel
%if %{clang_compiler}
BuildRequires:  llvm-clang
%endif
%if 0%{?suse_version} == 1310
%ifarch %ix86 x86_64 %arm
BuildRequires:  mupdf-devel-static
%endif
%endif
BuildRequires:  qwt6-devel
%if 0%{?suse_version} > 1310
BuildRequires:  pkgconfig(TelepathyQt4)
%endif
BuildRequires:  pkgconfig(QJson) >= 0.8.1
BuildRequires:  pkgconfig(QtCore) >= 4.8
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  libGeoIP-devel
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libprojectM)
# BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(phonon)
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(taglib)
%if %{lmp}
%if 0%{?suse_version} > 1310
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildConflicts: gstreamer-0_10-devel
BuildConflicts: gstreamer-0_10-plugins-base-devel
BuildConflicts: libgstapp-0_10
BuildConflicts: libgstinterfaces-0_10
BuildConflicts: libgstreamer-0_10
%else
BuildRequires:  pkgconfig(gstreamer-interfaces-0.10)
BuildConflicts: libgstreamer-1_0-0
%endif
%endif
BuildRequires:  libqxmpp-devel >= 0.8.0.1398262192
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(kqoauth)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libguess)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libmsn)
%ifarch %ix86 x86_64 %arm
BuildRequires:  pkgconfig(libopenjpeg)
%endif
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 0.15.6
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(poppler-qt4)
BuildRequires:  pkgconfig(qca2)
BuildRequires:  pkgconfig(qtermwidget4) >= 0.5.1
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(vmime) >= 0.9.2
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrender)


BuildRequires:  boost-devel >= 1.50
BuildRequires:  jbig2dec-devel
# BuildRequires:  libchromaprint-devel
# BuildRequires:  libffmpeg-devel
BuildRequires:  liblaretz-devel
BuildRequires:  openjpeg-devel
BuildRequires:  telepathy-qt4-devel
BuildRequires:  wt-devel >= 3.3
%if 0%{?suse_version} <= 1310
BuildRequires:  pkgconfig(QtMultimediaKit)
%endif
BuildRequires:  pkgconfig(libguess)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libvlc)


Requires:       oxygen-icon-theme
Recommends:     %{name}-advancednotifications
Recommends:     %{name}-azoth-acetamide
Recommends:     %{name}-azoth-xoox
Recommends:     %{name}-bittorrent
Recommends:     %{name}-blogique
Recommends:     %{name}-dolozhee
Recommends:     %{name}-lackman
Recommends:     %{name}-scrobbler
Suggests:       %{name}-lastfmscrobble
Recommends:     %{name}-monocle
Recommends:     %{name}-netstoremanager
Recommends:     %{name}-newlife
Recommends:     %{name}-poshuku
Recommends:     %{name}-secman-simplestorage
Recommends:     %{name}-visualnotifications

%description
This package provides core executable of Leechcraft.
LeechCraft is a free modular "Internet client" application.

LeechCraft allows to browse the web, read RSS/Atom feeds, download
files via BitTorrent, HTTP, FTP and DC, automatically stream,
download or play podcasts and other media files and much more.

Features can be easily added via plugins that can be integrated with
each other with no effert while staying abstract from the exact
implementation.

This package contains the main LeechCraft executable, which connects
all the plugins with each other, routes requests between them, tracks
dependencies and performs several other housekeeping tasks.

#-------------------------patterns----------------------------#
%package meta_full
Summary:        Meta package for pattern leechcraft_full
Group:          Metapackages
Requires:       leechcraft-meta_browser
Requires:       leechcraft-meta_media
Requires:       leechcraft-meta_messenger
Requires:       leechcraft-meta_office
Requires:       leechcraft-meta_tools
Requires:       leechcraft-meta_websurf

%description meta_full
This package is installed if a pattern is selected to have a working update path

%package meta_browser
Summary:        Meta package for pattern leechcraft_browser
Group:          Metapackages
Requires:       %{name}-advancednotifications
Requires:       %{name}-historyholder
Requires:       %{name}-kinotify
Requires:       %{name}-lackman
Requires:       %{name}-newlife
Requires:       %{name}-pintab
Requires:       %{name}-pogooglue
Requires:       %{name}-poshuku
Requires:       %{name}-poshuku-cleanweb
Requires:       %{name}-poshuku-fatape
Requires:       %{name}-poshuku-filescheme
Requires:       %{name}-poshuku-fua
Requires:       %{name}-poshuku-keywords
Requires:       %{name}-poshuku-onlinebookmarks
Requires:       %{name}-poshuku-onlinebookmarks-delicious
Requires:       %{name}-poshuku-onlinebookmarks-readitlater
Requires:       %{name}-secman
Requires:       %{name}-secman-simplestorage
Requires:       %{name}-seekthru
Requires:       %{name}-summary
Requires:       %{name}-tabsessionmanager
Requires:       %{name}-xproxy
Recommends:     %{name}-meta_tools

%description meta_browser
This package is installed if a pattern is selected to have a working update path

%package meta_desktop
Summary:        Meta package for pattern leechcraft_browser
Group:          Metapackages
Requires:       %{name}-fenet
Requires:       %{name}-cpuload
Requires:       %{name}-kbswitch
Requires:       %{name}-krigstask
Requires:       %{name}-laughty
Requires:       %{name}-launchy
Requires:       %{name}-lemon
Requires:       %{name}-liznoo
Requires:       %{name}-mellonetray
Requires:       %{name}-ooronee
Requires:       %{name}-sb2
Requires:       %{name}-tpi
Requires:       %{name}-vrooby
Recommends:     %{name}-hotsensors
Recommends:     %{name}-meta_tools

%description meta_desktop
This package is installed if a pattern is selected to have a working update path

%package meta_messenger
Summary:        Meta package for pattern leechcraft_messenger
Group:          Metapackages
Requires:       %{name}-advancednotifications
Requires:       %{name}-azoth
Requires:       %{name}-azoth-acetamide
Requires:       %{name}-azoth-adiumstyles
Requires:       %{name}-azoth-astrality
Requires:       %{name}-azoth-autoidler
Requires:       %{name}-azoth-autopaste
Requires:       %{name}-azoth-birthdaynotifier
Requires:       %{name}-azoth-chathistory
Requires:       %{name}-azoth-depester
Requires:       %{name}-azoth-embedmedia
Requires:       %{name}-azoth-herbicide
Requires:       %{name}-azoth-hili
Requires:       %{name}-azoth-isterique
Requires:       %{name}-azoth-juick
Requires:       %{name}-azoth-keeso
Requires:       %{name}-azoth-lastseen
Requires:       %{name}-azoth-metacontacts
Requires:       %{name}-azoth-modnok
Requires:       %{name}-azoth-murm
Requires:       %{name}-azoth-nativeemoticons
Requires:       %{name}-azoth-otroid
Requires:       %{name}-azoth-rosenthal
Requires:       %{name}-azoth-shx
Requires:       %{name}-azoth-standardstyles
Requires:       %{name}-azoth-vader
Requires:       %{name}-azoth-velvetbird
Requires:       %{name}-azoth-woodpecker
Requires:       %{name}-azoth-xoox
Requires:       %{name}-azoth-xtazy
Requires:       %{name}-azoth-zheet
Requires:       %{name}-historyholder
Requires:       %{name}-lackman
Requires:       %{name}-newlife
Requires:       %{name}-secman
Requires:       %{name}-secman-simplestorage
Requires:       %{name}-soundnotifications
Requires:       %{name}-tabsessionmanager
Requires:       %{name}-visualnotifications
Recommends:     %{name}-meta_tools

%description meta_messenger
This package is installed if a pattern is selected to have a working update path

%package meta_media
Summary:        Meta package for pattern leechcraft_media
Group:          Metapackages
Requires:       %{name}-lyricsprovider
Requires:       %{name}-gacts
Requires:       %{name}-hotstreams
Requires:       %{name}-lmp
Requires:       %{name}-lmp-dumbsync
Requires:       %{name}-lmp-graffiti
Requires:       %{name}-lmp-mp3tunes
Requires:       %{name}-lmp-mtpsync
Requires:       %{name}-musiczombie
Requires:       %{name}-secman
Requires:       %{name}-secman-simplestorage
Requires:       %{name}-touchstreams
Requires:       %{name}-vgrabber
Requires:       %{name}-vtyulc
Recommends:     %{name}-scrobbler
Suggests:       %{name}-lastfmscrobble
Recommends:     %{name}-meta_tools

%description meta_media
This package is installed if a pattern is selected to have a working update path

%package meta_websurf
Summary:        Meta package for pattern leechcraft_websurf
Group:          Metapackages
Requires:       %{name}-advancednotifications
Requires:       %{name}-aggregator
Requires:       %{name}-aggregator-bodyfetch
Requires:       %{name}-auscrie
Requires:       %{name}-bittorrent
Requires:       %{name}-blasq
Requires:       %{name}-blasq-spegnersi
Requires:       %{name}-blasq-deathnote
Requires:       %{name}-blasq-rappor
Requires:       %{name}-blasq-vangog
Requires:       %{name}-blogique
Requires:       %{name}-blogique-hestia
Requires:       %{name}-blogique-metida
Requires:       %{name}-choroid
Requires:       %{name}-gmailnotifier
Requires:       %{name}-historyholder
Requires:       %{name}-kinotify
Requires:       %{name}-lhtr
Requires:       %{name}-netstoremanager
Requires:       %{name}-netstoremanager-googledrive
Requires:       %{name}-newlife
Requires:       %{name}-pintab
Requires:       %{name}-sb
Requires:       %{name}-secman
Requires:       %{name}-secman-simplestorage
Requires:       %{name}-summary
Requires:       %{name}-tabsessionmanager
Requires:       %{name}-xproxy
Recommends:     %{name}-meta_tools

%description meta_websurf
This package is installed if a pattern is selected to have a working update path

%package meta_office
Summary:        Meta package for pattern leechcraft_office
Group:          Metapackages
Requires:       %{name}-blogique
Requires:       %{name}-blogique-hestia
Requires:       %{name}-lhtr
Requires:       %{name}-monocle
Requires:       %{name}-monocle-dik
Requires:       %{name}-monocle-fxb
Requires:       %{name}-monocle-pdf
Requires:       %{name}-monocle-postrus
Requires:       %{name}-monocle-seen
Requires:       %{name}-popishu
Recommends:     %{name}-meta_tools
Recommends:     %{name}-monocle-mu
Recommends:     %{name}-otlozhu

%description meta_office
This package is installed if a pattern is selected to have a working update path

%package meta_tools
Summary:        Meta package for pattern leechcraft_websurf
Group:          Metapackages
Requires:       %{name}-advancednotifications
Requires:       %{name}-dolozhee
Requires:       %{name}-gacts
Requires:       %{name}-glance
Requires:       %{name}-kbswitch
Requires:       %{name}-kinotify
Requires:       %{name}-knowhow
Requires:       %{name}-lackman
Requires:       %{name}-networkmonitor
Requires:       %{name}-pogooglue
Requires:       %{name}-tabsessionmanager
Requires:       %{name}-tabslist
Requires:       %{name}-vrooby
Requires:       %{name}-xproxy
Requires:       %{name}-xtazy
Recommends:     %{name}-sb2

%description meta_tools
This package is installed if a pattern is selected to have a working update path
#-----------------------end-patterns--------------------------#

%package advancednotifications
Summary:        LeechCraft Notifications framework Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-visualnotifications = %{version}
Recommends:     %{name}-soundnotifications = %{version}
Provides:       %{name}-shellopen = %{version}
Obsoletes:      %{name}-shellopen < %{version}

%description advancednotifications
This package provides an advanced notifications plugin for Leechcraft.

It allows to customize notifications better.


%package aggregator
Summary:        LeechCraft RSS/Atom Aggregator Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       libqt4-sql-sqlite
Recommends:     %{name}-poshuku = %{version}

%description aggregator
This package provides a RSS/Atom feed reader plugin for LeechCraft.

It features:
 * RSS 0.92/0.93/1.0/2.0, Atom 0.3/1.0;
 * extensions like GeoRSS, MediaRSS, Comment API etc;
 * OPML support;
 * broadcatching and fetching arbitrary data with regexps;
 * tape mode for news display;
 * individual options for each channel like update interval;
 * storage either in SQLite or PostgreSQL;
 * exporting feeds to FB2 for further reading on handheld devices.

A web browser plugin is recommended to show the news in a fancy way.


%package aggregator-bodyfetch
Summary:        LeechCraft Aggregator - Bodyfetch Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-aggregator
Recommends:     %{name}-qrosp

%description aggregator-bodyfetch
This package provides a body fetch plugin for LeechCraft Aggregator.

It allows to automatically fetch full bodies of news items and replace the
original teasers from RSS feeds with them, so that it appears like the full
news stories were originally there.

Fetching is done according to little scripts called recipes. For this to
work, a script provider like Qrosp should be installed. Please refer to the
guide to writing recipes if you are interested in writing your own ones.


%package aggregator-webaccess
Summary:        LeechCraft Aggregator - Web Interface Module
Group:          Productivity/Networking/Other
Requires:       %{name}-aggregator = %{version}

%description aggregator-webaccess
WebAccess provides a basic web interface for the
Aggregator feed reader, so one can read news
articles from a mobile device or another machine.


%package anhero
Summary:        LeechCraft Crash handler Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       gdb
Recommends:     %{name}-dolozhee

%description anhero
This package provides a crash handler plugin for LeechCraft.

It shows backtraces and aids in sending bug reports.


%package auscrie
Summary:        LeechCraft Screenshoter Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-imgaste = %{version}

%description auscrie
This package provides a screenshooter plugin for LeechCraft.

It allows to make screenshots of LeechCraft and then either save them locally
or upload them to an imagebin.


%package azoth
Summary:        LeechCraft Instant messenger Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-azoth-chatstyler = %{version}
Requires:       %{name}-azoth-protocolplugin
Requires:       %{name}-securestorage = %{version}
Suggests:       %{name}-azoth-standardstyles
Obsoletes:      %{name}-azoth-p100q

%description azoth
This package provides a modular IM client for LeechCraft.

Totally in the spirit of LeechCraft, Azoth is modular itself. For example,
protocols are provided by corresponding plugins, so Azoth is a multiprotocol
client as well. Modularity also allows Azoth to be flexible, extensible and
enables the modules to use each other and avoid code and functionality
duplication.

Unlike other multiprotocol clients which tend to implement only those
features that are present in all the protocols, Azoth is modelled after the
XMPP protocol, aiming to provide extensive and full support for XMPP while
remaining usable for other protocols.


%package azoth-abbrev
Summary:        LeechCraft Azoth - Abbreviations Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth-protocolplugin = %{version}
Suggests:       %{name}-xoox
Recommends:     %{name}-acetamide
Recommends:     %{name}-xoox

%description azoth-abbrev
This package provides abbreviations via commands like /abbrev, /unabbrev
and /listabbrevs for LeechCraft Azoth.


%package azoth-acetamide
Summary:        LeechCraft Azoth - IRC Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin
Recommends:     %{name}-azoth-mucommands

%description azoth-acetamide
This package provides an IRC protocol plugin for LeechCraft Azoth.

Features:
 * Secure Sockets Layer (SSL) cryptographic protocol.
 * Channels bookmarks.
 * Automatic password entry.
 * Automatic logging on.


%package azoth-adiumstyles
Summary:        LeechCraft Azoth - Adium Styles Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-chatstyler

%description azoth-adiumstyles
This package provides an Adium styles support plugin for LeechCraft Azoth.


%package azoth-astrality
Summary:        LeechCraft Azoth - Telepathy Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       telepathy-haze
Requires:       telepathy-mission-control
Provides:       %{name}-azoth-protocolplugin

%description azoth-astrality
This package provides a telepathy plugin for LeechCraft Azoth.

It supportes various protocols provided by telepathy framework.

Features:
 * Telepathy account creation.
 * In-band account registration.
 * Standard one-to-one chats.
 * Nick resolution.


%package azoth-autoidler
Summary:        LeechCraft Azoth - Automatic Change of Status Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-autoidler
This package provides a status changing plugin for LeechCraft Azoth.

It allows to automatically change of status due to inactivity period.


%package azoth-autopaste
Summary:        LeechCraft Azoth - Autopaste Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-autopaste
This package provides an autopaste plugin for LeechCraft Azoth.

It allows to paste long messages to pastebins automatically.


%package azoth-birthdaynotifier
Summary:        LeechCraft Azoth - Birthday Notifier Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-birthdaynotifier
This package provides a Birthday Notifier plugin for LeechCraft Azoth.

So you will not miss your contacts' birthdays if there are ones in vCards.


%package azoth-chathistory
Summary:        LeechCraft Azoth - Chat history Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       libqt4-sql-sqlite

%description azoth-chathistory
This package provides a chat history plugin for LeechCraft Azoth.

Azoth ChatHistory, as the name implies, stores the history of chat sessions.
It supports storing history from normal one-to-one chats as well as from
multiuser conferences and private chats in conferences. It also allows to
search the logs by SQL's LIKE expressions. SQLite is used for storage.

Features:
 * Stores history from normal chats, multiuser conferences and private chats.
 * Supports searching logs.
 * SQLite-based.


%package azoth-depester
Summary:        LeechCraft Azoth - Ignore Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-depester
This package provides an ignoring plugin for LeechCraft Azoth.

It allows to ignore unwanted participants.


%package azoth-embedmedia
Summary:        LeechCraft Azoth - Media Objects Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-embedmedia
This package provides a embedding media plugin for LeechCraft Azoth.

It allows to enable embedding different media objects in chat tabs.


%package azoth-herbicide
Summary:        LeechCraft Azoth - Antispam Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-herbicide
This package provides a basic antispam plugin for LeechCraft Azoth.


%package azoth-hili
Summary:        LeechCraft Azoth - Conference highlights Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-hili
This package provides a highlights customizing plugin for LeechCraft Azoth.

It allows to customize conference highlights.


%package azoth-isterique
Summary:        LeechCraft Azoth - Isterique Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-isterique
This package provides a CAPS removing plugin for LeechCraft Azoth.

It allows to remove excessive CAPS usage from incoming messages.


%package azoth-juick
Summary:        LeechCraft Azoth - Juick.com service Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-juick
This package contains a juick.com plugin for LeechCraft Azoth.

It provides the enhanced experience with the juick.com microblogging service.


%package azoth-keeso
Summary:        LeechCraft Azoth - Text transform Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-keeso
This package provides a text transform plugin for LeechCraft Azoth.


%package azoth-lastseen
Summary:        LeechCraft Azoth - Contact last seen time Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-lastseen
This package provides a LastSeen plugin for LeechCraft Azoth.

It allows to record of contacts' last online and availability time at
client's side. It doesn't depend on the concrete protocol implementation.


%package azoth-metacontacts
Summary:        LeechCraft Azoth - Metacontacts Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-metacontacts
This package provides a metacontacts support plugin for LeechCraft Azoth.


%package azoth-modnok
Summary:        LeechCraft Azoth - LaTeX support Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-modnok
This package provides a LaTeX plugin for LeechCraft Azoth.

It allows to render and display LaTeX formulae directly in chat windows.

It doesn't depend on the underlying protocol, and if the protocol supports
rich text formatting in outgoing messages, it is able to replace the formulas
with corresponding images in outgoing messages as well, so your buddies would
see nice rendered formulas instead of raw LaTeX code, even if their client
doesn't have a LaTeX formatter.


%package azoth-mucommands
Summary:        LeechCraft Azoth - Conference-oriented Commands Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth-protocolplugin = %{version}
Suggests:       %{name}-xoox
Recommends:     %{name}-acetamide
Recommends:     %{name}-xoox

%description azoth-mucommands
This package provides some common conference-oriented commands like
/vcard, /time, /last, /subject, /kick, /ban and so on for LeechCraft Azoth.


%package azoth-murm
Summary:        LeechCraft Azoth - VKontakte Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin

%description azoth-murm
This package provides a special protocol subplugin for extensive VKontakte
messaging support plugin for LeechCraft Azoth.


%package azoth-nativeemoticons
Summary:        LeechCraft Azoth - Emoticons packs
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-nativeemoticons
This package provides an emoticons plugin for LeechCraft Azoth.

It allows to use emoticons packs in Psi+, Kopete and own format.


%package azoth-otroid
Summary:        LeechCraft Azoth - Off-the-Record Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-otroid
This package provides support Off-the-Record messaging for LeechCraft Azoth.


%package azoth-rosenthal
Summary:        LeechCraft Azoth - Spell Checker Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       %{name}-rosenthal = %{version}

%description azoth-rosenthal
This package provides a spell checker plugin for LeechCraft Azoth.

It is based on Hunspell or Myspell dictionaries.


%package azoth-shx
Summary:        LeechCraft Azoth - Shell command runner Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-shx
This package provides a shell command runner plugin for LeechCraft Azoth.


%package azoth-standardstyles
Summary:        LeechCraft Azoth - Standard chat styles Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-chatstyler

%description azoth-standardstyles
This package provides an standard styles support plugin for LeechCraft Azoth.

Standard styles are ones in LeechCraft's own format.


%package azoth-vader
Summary:        LeechCraft Azoth - MrIM Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin

%description azoth-vader
This package provides a MRIM protocol plugin for LeechCraft Azoth.

MRIM protocol is used in the Mail.Ru Agent IM service.

Vader is based on an own implementation of the MRIM protocol, partially based
on available (and outdated) official specs and partly reverse-engineered.

The following protocol features are supported:
 * Extended statuses.
 * Attention requests (alarms).
 * Publishing current tune and fetching others' tune.
 * Message delivery receipts.
 * Mailbox notifications.
 * Opening mailbox without login.
 * Authorization management.
 * Grouping contacts.


%package azoth-velvetbird
Summary:        LeechCraft Azoth - LibPurple Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin

%description azoth-velvetbird
This package provides a LibPurple plugin for LeechCraft Azoth.

It supportes various protocols provided by Purple library.


%if %{woodpecker}
%package azoth-woodpecker
Summary:        LeechCraft Twitter Client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     libkqoauth0 >= 0.98

%description azoth-woodpecker
This package provides a Twitter Client plugin for LeechCraft.
%endif


%package azoth-xoox
Summary:        LeechCraft Azoth - XMPP Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       libqxmpp0 >= 0.8.0.1398262192
Provides:       %{name}-azoth-protocolplugin
Recommends:     %{name}-azoth-mucommands

%description azoth-xoox
This package provides a XMPP protocol plugin for LeechCraft Azoth.

Feature highlights:
 * Media calls support (Jingle).
 * Support for PEP and current user activity, mood, tune and location.
 * Bookmarks with autojoin support.
 * Full support for MUCs.
 * Notifications about chat state participation.
 * Service discovery support.
 * Gateway support, with registration.
 * Support for various file transfer methods.
 * In-band registration of accounts (right from the client).
 * Privacy lists.
 * Encrypted and signed messages and presences.
 * Full CAPTCHA support.
 * Support for ad-hoc commands.
 * Support for exchanging roster items.
 * Search for contacts in Jabber.


%package azoth-xtazy
Summary:        LeechCraft Azoth - Publishing current user tune Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       %{name}-xtazy = %{version}

%description azoth-xtazy
This package provides a tune publishing plugin for LeechCraft Azoth.

It allows to publish current user tune.


%package azoth-zheet
Summary:        LeechCraft Azoth - MSN Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin

%description azoth-zheet
This package provides a MSN protocol plugin for LeechCraft Azoth.

MSN protocol is used in the Windows Live Messenger.

The following protocol features are currently supported:
 * Message delivery receipts.
 * Attention requests (nudges).
 * Notifications about messages in mailbox.
 * Announcing own current tune and fetching others' one.
 * Multiple groups for each contact.
 * Authorization management.
 * Blacklist management.


%package bittorrent
Summary:        LeechCraft BitTorrent client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-summaryrepresentation = %{version}

%description bittorrent
This package provides a bittorrent client for Leechcraft.

It is feature-rich, fast and efficient.

Features
 * Support for DHT.
 * Magnet links support.
 * Sequential download mode where torrent is download sequentially.
 * Torrents queue, limiting number of seeding/leeching torrents.
 * Ability to rename files and directories in the torrent.
 * Selective download: possibility to select specific files from torrent.
 * Continue downloads left by any other client.
 * Support for sparse files.
 * Tags for torrents.
 * Global and per-torrent speed limits.
 * Connection number limits.
 * Fast resume support to avoid long startup times.
 * IP filter to block/unblock unwanted peers.
 * Support for extension protocol
etc.


#%%package blackdash
#Summary:        LeechCraft Dashboard Module
#Group:          Productivity/Networking/Other
#Requires:       %%{name} = %%{version}

#%%description blackdash
#Dashboard


%package blasq
Summary:        LeechCraft Image storages Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blasq-subplugin = %{version}

%description blasq
This package provides a modular Image storages plugin for LeechCraft.

It supports different cloud image storages like Picasa or Flick.


%package blasq-deathnote
Summary:        LeechCraft DeathNote - LiveJournal FotoBilder client Module
Group:          Productivity/Networking/Other
Requires:       %{name}-blasq = %{version}
Provides:       %{name}-blasq-subplugin = %{version}

%description blasq-deathnote
This package provides a LiveJournal FotoBilder image storage client subplugin
for LeechCraft Blasq.


%package blasq-rappor
Summary:        LeechCraft Blasq - VKontakte client Module
Group:          Productivity/Networking/Other
Requires:       %{name}-blasq = %{version}
Provides:       %{name}-blasq-subplugin = %{version}

%description blasq-rappor
This package provides a VKontakte image storage client subplugin
for LeechCraft Blasq.


%if %{vangog}
%package blasq-vangog
Summary:        LeechCraft Picasa - Flickr client Module
Group:          Productivity/Networking/Other
Requires:       %{name}-blasq = %{version}
Provides:       %{name}-blasq-subplugin = %{version}

%description blasq-vangog
This package provides a Picasa image storage client subplugin
for LeechCraft Blasq.
%endif


%package blasq-spegnersi
Summary:        LeechCraft Blasq - Flickr client Module
Group:          Productivity/Networking/Other
Requires:       %{name}-blasq = %{version}
Provides:       %{name}-blasq-subplugin = %{version}

%description blasq-spegnersi
This package provides a Flickr image storage client subplugin
for LeechCraft Blasq.


%package blogique
Summary:        LeechCraft Blogging client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blogique-subplugin = %{version}
Recommends:     %{name}-lhtr

%description blogique
This package provides a modular Blogging client plugin for LeechCraft.

It supports different blogging platforms via different submodules.


%package blogique-hestia
Summary:        LeechCraft Blogique - Local blogging Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blogique = %{version}
Provides:       %{name}-blogique-subplugin = %{version}

%description blogique-hestia
This package provides a local blogging subplugin for LeechCraft Blogique.


%package blogique-metida
Summary:        LeechCraft Blogique - LiveJournal Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blogique = %{version}
Recommends:     %{name}-xtazy = %{version}
Provides:       %{name}-blogique-subplugin = %{version}

%description blogique-metida
This package provides a LiveJournal subplugin for LeechCraft Blogique.

It provides LiveJournal support.


%package certmgr
Summary:        LeechCraft SSL certificates Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description certmgr
This package provides an SSL certificates manager plugin.


%package choroid
Summary:        LeechCraft Image viewer Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description choroid
This package provides an image viewer plugin for LeechCraft.


%package cpuload
Summary:        LeechCraft CPU Usage Monitoring Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description cpuload
This package provides a quark for monitoring the CPU usage
for LeechCraft SB2. Monitoring memory and swap will also
be probably added later. For now it uses /proc/stat.


%package cstp
Summary:        LeechCraft HTTP Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-http

%description cstp
This package provides HTTP implementation plugin for LeechCraft.

It is a clean and simple HTTP implementation. Mainly used by many other
plugins, like Aggregator or SeekThru or vGrabber.

Features:
 * Support for redirects.
 * Automatic downloads from other plugins.
 * Support for continuing of interrupted downloads.


%package dbusmanager
Summary:        LeechCraft D-Bus Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description dbusmanager
This package provides a D-Bus implementation plugin for LeechCraft.


%package deadlyrics
Summary:        LeechCraft Lyrics finder Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}
Provides:       %{name}-lyricsprovider

%description deadlyrics
This package provides a lyrics finder plugin for LeechCraft.

It is a simple client for searching song lyrics on various sites.
The search interface is available via LeechCraft Summary.


%package devel
Summary:        LeechCraft Development Files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       cmake
Requires:       lib%{name}-util-db%{so_ver}        = %{version}
Requires:       lib%{name}-util-gui%{so_ver}       = %{version}
Requires:       lib%{name}-util-models%{so_ver}    = %{version}
Requires:       lib%{name}-util-network%{so_ver}_1   = %{version}
Requires:       lib%{name}-util-qml%{so_ver}_1     = %{version}
Requires:       lib%{name}-util-shortcuts%{so_ver} = %{version}
Requires:       lib%{name}-util-sll%{so_ver}       = %{version}
Requires:       lib%{name}-util-svcauth%{so_ver}   = %{version}
Requires:       lib%{name}-util-sys%{so_ver}_1     = %{version}
Requires:       lib%{name}-util-tags%{so_ver}_1    = %{version}
Requires:       lib%{name}-util-x11-%{so_ver}      = %{version}
Requires:       lib%{name}-util-xdg%{so_ver}       = %{version}
Requires:       lib%{name}-util-xpc%{so_ver}_1     = %{version}
Requires:       lib%{name}-util-xsd%{so_ver}       = %{version}
Requires:       pkgconfig(QtWebKit)

%description devel
This package provides files required for development for LeechCraft.

It contains header files required to develop new modules.


%package devmon
Summary:        LeechCraft Device Monitor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-secman = %{version}

%description devmon
This package provides a devices monitor plugin for LeechCraft.


# %%package dlniwe
# Summary:        LeechCraft DLNA Module
# Group:          Productivity/Networking/Other
# Requires:       %%{name} = %%{version}
# 
# %%description dlniwe
# This package provides a DLNA server plugin for LeechCraft.


%package dolozhee
Summary:        LeechCraft Issue reporting Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-secman = %{version}

%description dolozhee
This package provides a Dolozhee plugin for LeechCraft.

It allows to quickly and easily submit bug reports
and feature requests to LeechCraft issues tracker.


%package dumbeep
Summary:        LeechCraft DumBeep Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     mplayer
Provides:       %{name}-soundnotifications = %{version}

%description dumbeep
This package provides a dumb sound notifier plugin for LeechCraft.

It also uses Phonon as a backend or something like aplay/mplayer.


%package eleeminator
Summary:        LeechCraft Eleeminator Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-shaitan = %{version}
Obsoletes:      %{name}-shaitan < %{version}

%description eleeminator
This package provides a terminal plugin for Leechcraft.


%if %{fenet}
%package fenet
Summary:        LeechCraft Window Manager Module
Group:          Productivity/Networking/Other
Recommends:     %{name}-cpuload
Recommends:     %{name}-hotsensors
Recommends:     %{name}-kbswitch
Recommends:     %{name}-krigstask
Recommends:     %{name}-laughty
Recommends:     %{name}-launchy
Recommends:     %{name}-lemon
Recommends:     %{name}-liznoo
Recommends:     %{name}-mellonetray
Recommends:     %{name}-ooronee
Recommends:     %{name}-sb2
Recommends:     %{name}-tpi
Recommends:     %{name}-vrooby
Requires:       %{name} = %{version}
Requires:       %{name}-fenet-wm = %{version}

%description fenet
This package provides a WM control plugin for Leechcraft.


%package fenet-awesome
Summary:        LeechCraft Fenet Awesome Stuff
Group:          Productivity/Networking/Other
BuildArch:      noarch
Provides:       %{name}-fenet-wm = %{version}
Requires:       %{name}-fenet = %{version}
Requires:       awesome

%description fenet-awesome
This package allows to start Leechcraft as a Desktop Environment with
the Awesome Window Manager.


%package fenet-compton
Summary:        LeechCraft Fenet Compton Stuff
Group:          Productivity/Networking/Other
BuildArch:      noarch
Provides:       %{name}-fenet-wm = %{version}
Requires:       %{name}-fenet = %{version}
Requires:       compton

%description fenet-compton
This package allows to start Leechcraft as a Desktop Environment with
the Compton Compositor.


%package fenet-kwin
Summary:        LeechCraft Fenet Kwin Stuff
Group:          Productivity/Networking/Other
BuildArch:      noarch
Provides:       %{name}-fenet-wm = %{version}
Requires:       %{name}-fenet = %{version}
Requires:       kwin

%description fenet-kwin
This package allows to start Leechcraft as a Desktop Environment with
the KDE Window Manager.


%package fenet-openbox
Summary:        LeechCraft Fenet Openbox Stuff
Group:          Productivity/Networking/Other
BuildArch:      noarch
Provides:       %{name}-fenet-wm = %{version}
Requires:       %{name}-fenet = %{version}
Requires:       openbox

%description fenet-openbox
This package allows to start Leechcraft as a Desktop Environment with
the Openbox Window Manager.
%endif


%package gacts
License:        BSL-1.0 and (LGPL-2.1 or CPL-1.0)
Summary:        LeechCraft Global actions Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description gacts
This package provides a global shortcut manager for LeechCraft.

It allows to set and use global hotkeys.


%package glance
Summary:        LeechCraft Opened tabs overview Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description glance
This package provides a tabs overview plugin for Leechcraft.

It allows to show the thumbnailed grid overview of tabs.


%package gmailnotifier
Summary:        LeechCraft GMail notifier Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Recommends:     %{name}-sb = %{version}

%description gmailnotifier
This package provides a GMail notifications plugin for Leechcraft.

It allows to get notifications about new mail in your GMail account.

It has configurable frequency of the updates and the number of last unread
messages shown.


%package harbinger
Summary:        LeechCraft Collections Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description harbinger
This package provides a collections manager plugin for LeechCraft.


%package historyholder
Summary:        LeechCraft History Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description historyholder
This package provides a history keeper plugin for LeechCraft.

It allows to store information about finished downloads and similar events
and allows to search it by text, wildcard, regular expressions or tags.


%package hotsensors
Summary:        LeechCraft Temperature Sensors Module
Group:          Productivity/Networking/Other
Requires:       %{name}-sb = %{version}

%description hotsensors
This package provides a temperature sensors subplugin (a quark)
for LeechCraft SideBar.


%package hotstreams
Summary:        LeechCraft Radio streams Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description hotstreams
This package provides a radio streams provider plugin for LeechCraft.


%package htthare
Summary:        LeechCraft Http Server Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description htthare
This package provides content from local filesystem over LANs (and
possibly WANs, but by default only LAN interfaces are listened on).


%package imgaste
Summary:        LeechCraft Image Paster Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description imgaste
This module provides a simple image paster plugin from LeechCraft


%package kbswitch
Summary:        LeechCraft keyboard switcher Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       setxkbmap

%description kbswitch
This module allow change keyboard layouts from LeechCraft


%package kinotify
Summary:        LeechCraft Kinetic notifications Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-visualnotifications
Recommends:     %{name}-poshuku

%description kinotify
This package contains a fancy notifications plugin for LeechCraft.

It provides fancy kinetic notifications LeechCraft-wide instead of old-style
tray-based ones. It supports notifications with HTML markup, notification
actions (for example, "Open chat" action in a notification about incoming IM
message) and is fully themable.

Features:
 * Supports HTML markup.
 * Supports notification actions.
 * Themable.
 * Platform-independent.


%package knowhow
Summary:        LeechCraft Tips of the day Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description knowhow
This package provides a tips plugin for LeechCraft.

It allows to display tips of the day window after launch LeechCraft.


%package krigstask
Summary:        LeechCraft Applications Switcher Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description krigstask
This package provides an applications switcher quark for LeechCraft SB2.


%package lackman
Summary:        LeechCraft Package manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       xz
Recommends:     %{name}-poshuku = %{version}

%description lackman
This package provides a package manager plugin for Leechcraft.

It allows to install script plugins, iconsets, translations, additional data
and other similar packages.

It also supports dependencies between packages as well as versioning and
automatic updates of the packages. LackMan works completely in userspace and
is crossplatform by its nature.

Features:
 * Allows installation of script plugins, icons and various other data.
 * Supports versioning and automatic updates of packages.
 * Supports dependencies between packages.
 * Works entirely in userspace, operating in user's home directory.
 * Is a crossplatform package manager.


%package lastfmscrobble
Summary:        LeechCraft Last.FM Scrobble Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-lmp = %{version}
Provides:       %{name}-scrobbler

%description lastfmscrobble
This package contains a LastFMScrobble plugin for LeechCraft.

It provides support for the Last.FM service. For example, it scrobble tracks
from other players, requests similar artists (on demand by other players as
well), supports fetching album art, etc.

Features:
 * Scrobbling listened tracks from other players like LMP to Last.FM.
 * "Loving" listened tracks.
 * Support for requesting artists that are similar to a given artist.
 * Automatic fetching of album art.
 * Support for Last.FM radio.
 * Fetching personalized recommendations.
 * Fetching recent releases of artists that are in the user's collection.
 * Fetching artists biography.
 * Configurable language of the fetched information.


%package laughty
Summary:        LeechCraft Notifications Server Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      %{name}-sysnotify

%description laughty
This package provides a desktop notifications server plugin for Leechcraft.


%package launchy
Summary:        LeechCraft Launcher Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb = %{version}

%description launchy
This package provides a third-party application launcher plugin for Leechcraft.


#%%package lcftp
#Summary:        LeechCraft FTP Client Module
#Group:          Productivity/Networking/Other
#Requires:       %%{name} = %%{version}

#%%description lcftp
#FTP client with recursive downloads, uploads and two-panel interface.


%package lemon
Summary:        LeechCraft Network Monitor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb = %{version}

%description lemon
This package provides another Network Monitor plugin for Leechcraft.


%package lhtr
Summary:        LeechCraft HTML WYSIWYG editor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-poshuku

%description lhtr
This package provides a HTML WYSIWYG editor plugin for Leechcraft.

It can be usable with mail and blog modules.


%package liznoo
Summary:        LeechCraft Power managment module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       upower
Recommends:     %{name}-sb = %{version}

%description liznoo
This package provides a power manager plugin for Leechcraft.

It uses UPower on Linux.

Features:
 * Displays battery status in LeechCraft tray.
 * Displays battery charge and power consumption history.
 * Notifies other plugins about sleep and resume events. This way plugins
like Azoth can disconnect from servers gracefully on hibernation and
reconnect properly on startup.
 * Allows user to easily sleep/hibernate the system.
 * Notifies user when device starts discharging or charging.
 * Notifies user on low power level.


%if %{lmp}
%package lmp
Summary:        LeechCraft Media player Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-lyricsprovider
Recommends:     %{name}-gacts = %{version}
Recommends:     %{name}-scrobbler
Suggests:       %{name}-lastfmscrobble
Recommends:     %{name}-musiczombie = %{version}
Recommends:     ffmpeg
%if 0%{?suse_version} > 1310
Requires:       gstreamer-plugins-base >= 1.0
Requires:       gstreamer-plugins-good >= 1.0
Recommends:     gstreamer-plugins-bad >= 1.0
%else
Requires:       gstreamer-0_10-plugins-base
Requires:       gstreamer-0_10-plugins-good
Recommends:     gstreamer-0_10-plugins-bad
Recommends:     gstreamer-0_10-plugins-fluendo_mp3
%endif
Provides:       %{name}-audioplayer
Provides:       %{name}-soundnotifications = %{version}

%description lmp
This package provides a audio player plugin for LeechCraft.

It allows to play audio and stream audio.
It uses Gstreamer as a backend thus supporting major codecs.

Features:
 * Support for major audio formats.
 * Streaming media over Internet.
 * Play queue.
 * Support for automatic podcast playing (with a plugin like Aggregator).


%package lmp-brainslugz
Summary:        LeechCraft Collection Checker Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lastfmscrobble = %{version}
Requires:       %{name}-lmp = %{version}
Requires:       %{name}-musiczombie = %{version}

%description lmp-brainslugz
This package provides a collection checker plugin for LeechCraft.

It allows to check collection completeness.


%package lmp-dumbsync
Summary:        LeechCraft Media syncing Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}
Recommends:     %{name}-hotstreams = %{version}
Recommends:     %{name}-vrooby = %{version}

%description lmp-dumbsync
This package provides a audio syncing plugin for LeechCraft.

It allows to sync with Flash-like media players.


%package lmp-fradj
Summary:        LeechCraft FrAdj Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-fradj
This package provides a 10-band equalizer for now.

n-band (with configurable n) equalizer is planned
in somewhat near future.


%package lmp-graffiti
Summary:        LeechCraft Tags Manipulating Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-graffiti
This package provides a tags editor plugin for LeechCraft.

It allows to manipulate audio file tags.


%package lmp-httstream
Summary:        LeechCraft Tags Manipulating Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-httstream
This package provides a streamer plugin for LeechCraft player.

It allows to stream music from LMP via HTTP.


%package lmp-mp3tunes
Summary:        LeechCraft mp3tunes.com Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-mp3tunes
This package provides a mp3tunes.com plugin for LeechCraft.

It allows to sync and use the mp3tunes.com service.

Features:
 * Using many accounts.
 * Getting playlists.


%package lmp-mtpsync
Summary:        LeechCraft MtpSync Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}
Requires:       %{name}-devmon = %{version}

%description lmp-mtpsync
This package allows to sync with MTP devices via LeechCraft.


%package lmp-potorchu
Summary:        LeechCraft Visualization Effects Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-potorchu
This package provides visualization effects for LeechCraft audio player.
%endif


%if %{mellonetray}
%package mellonetray
Summary:        LeechCraft Tray Area Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description mellonetray
This package provides a tray area quark for third-party apps
for LeechCraft SB2.
%endif


%package monocle
Summary:        LeechCraft Document viewer Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle-subplugin

%description monocle
This package provides a modular Document viewer plugin for LeechCraft.

It will support different formats via different backends.


%package monocle-fxb
Summary:        LeechCraft Monocle - FictionBook Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-fxb
This package contains a FictionBook subplugin for LeechCraft Monocle.

This package provides FB2 documents support for Document viewer Module.


%package monocle-dik
Summary:        LeechCraft Monocle - MOBI Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-dik
This package contains a MOBI subplugin for LeechCraft Monocle.

This package provides MOBI documents support for Document viewer Module.


%if 0%{?suse_version} == 1310
%package monocle-mu
Summary:        LeechCraft Monocle - Another PDF Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Requires:       mupdf
Provides:       %{name}-monocle-subplugin

%description monocle-mu
This package contains another pdf subplugin for LeechCraft Monocle.

This package provides PDF documents support for Document viewer Module
via the mupdf backend.
%endif


%package monocle-pdf
Summary:        LeechCraft Monocle - PDF Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-pdf
This package contains a pdf subplugin for LeechCraft Monocle.

This package provides PDF documents support for Document viewer Module
via the Poppler backend.


%package monocle-postrus
Summary:        LeechCraft Monocle - PostScript Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle-pdf = %{version}
Requires:       ghostscript
Provides:       %{name}-monocle-subplugin

%description monocle-postrus
This package contains a PostRus subplugin for LeechCraft Monocle.

This package provides PostScript documents support for Document viewer Module
via the ghostscript utils and Pdf plugin.


%package monocle-seen
Summary:        LeechCraft Monocle - Djvu Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-seen
This package contains a Djvu subplugin for LeechCraft Monocle.

This package provides Djvu documents support for Document viewer Module
via the DjvuLibre backend.
%endif


%package musiczombie
Summary:        LeechCraft Azoth - MusicBrainz.org client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-lmp = %{version}

%description musiczombie
This package provides a MusicBrainz.org client plugin for LeechCraft.


# %%package nacheku
# Summary:        LeechCraft Link watcher Module
# Group:          Productivity/Networking/Other
# Requires:       %%{name} = %%{version}
# 
# %%description nacheku
# This package provides a Nacheku plugin for LeechCraft.
# 
# It allows to watch clipboard and directory in order to
# get links and download files.


%package netstoremanager
Summary:        LeechCraft Network file storages Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-netstoremanager-subplugin

%description netstoremanager
This package provides a network storage plugin for Leechcraft.

It allows to manage network storages like Google Drive.
It is modular, so different storages can be added to it
without modifying the plugin itself.

Features:
 * Upload files easily from LeechCraft.
 * Maintain the list of uploaded files.
 * Delete the uploaded files (if supported by service).
 * Support for prolongating uploaded files (if supported by service).

Supported services:
 * Google Drive


%package netstoremanager-dropbox
Summary:        LeechCraft DropBox storage Module
Group:          Productivity/Networking/Other
Requires:       %{name}-cstp = %{version}
Requires:       %{name}-netstoremanager = %{version}
Provides:       %{name}-netstoremanager-subplugin

%description netstoremanager-dropbox
This package provides a DropBox subplugin for Leechcraft NetStoreManager.


%package netstoremanager-googledrive
Summary:        LeechCraft Google Drive storage Module
Group:          Productivity/Networking/Other
Requires:       %{name}-netstoremanager = %{version}
Provides:       %{name}-netstoremanager-subplugin

%description netstoremanager-googledrive
This package provides a Google Drive subplugin for Leechcraft NetStoreManager.


#%%package netstoremanager-yandexdisk
#Summary:        LeechCraft Network file storages Module
#Group:          Productivity/Networking/Other
#Requires:       %%{name}-netstoremanager = %%{version}
#Provides:       %%{name}-netstoremanager-subplugin
#
#%%description netstoremanager-yandexdisk
#This package provides a Yandex.Disk subplugin for Leechcraft NetStoreManager.


%package networkmonitor
Summary:        LeechCraft Network Monitor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description networkmonitor
This package provides a network monitor plugin for LeechCraft.

It allows to watch for HTTP requests and allows to inspect them and search
through the list.


%package newlife
Summary:        LeechCraft Importer Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description newlife
This package provides a settings importer plugin for LeechCraft.

It allows to import settings, preferences etc. from various applications.

Currently it supports
 * Kopete: chat history.
 * Psi+: account settings, chat history.
 * Vacuum IM: account settings, chat history.
 * Akregator: feeds list, individual settings for each feed, like
update interval and custom storage parameters, Akregator's settings.
 * Firefox: history, bookmarks, RSS feeds (aka Live bookmarks).
 * Liferea: feeds list.


%package ooronee
Summary:        LeechCraft Text and Images Handler Module
Group:          Productivity/Networking/Other
Requires:       %{name}-sb2 = %{version}
Recommends:     %{name}-blasq
Recommends:     %{name}-imgaste
Recommends:     %{name}-pogooglue
Recommends:     %{name}-seekthru

%description ooronee
This package provides a quark handling text and images
dropped on it for Leechcraft.

The dropped data is then sent to a data filter chosen by the user.
See more at http://leechcraft.org/concepts-data-filters


%package otlozhu
Summary:        LeechCraft ToDo manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description otlozhu
This package provides a ToDo manager plugin for LeechCraft.

It is a GTD-inspired ToDo manager.


%package pintab
Summary:        LeechCraft Pinning tabs Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description pintab
This package provides a pinning tab module for LeechCraft.

It allows to pin important tabs so that they occupy less space.


%package pogooglue
Summary:        LeechCraft Poshuku - quick google search Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-poshuku = %{version}

%description pogooglue
This package provides an instant search plugin for LeechCraft.

It allows to search instantly selected text in Google.


%if %{poleemery}
%package poleemery
Summary:        LeechCraft Poleemery - Finances manager Module
Group:          Productivity/Networking/Other
BuildRequires:  qwt6-devel >= 6.1
Requires:       %{name} = %{version}

%description poleemery
This package provides a personal finances manager plugin for LeechCraft.
%endif


%package popishu
Summary:        LeechCraft Text editor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-rosenthal

%description popishu
This package provides a text editor plugin for LeechCraft.

It is a simple QScintilla2-based text editor. It supports basic syntax
highlighting for some common file types, folding, automatic identation, and
such. It also could be used as enhanced source view plugin for the Poshuku
browser module, for example.

Features:
 * Basic syntax highlighting.
 * Line folding.
 * Basic automatic identation.
 * Support for multiple documents at once.


%package poshuku
Summary:        LeechCraft Web Browser Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-webbrowser
Recommends:     %{name}-imgaste = %{version}

%description poshuku
This package provides a web browser plugin for LeechCraft.

It is an full-featured web browser based on WebKit.
Poshuku is fully extensible with plugins.

Currently it features:
 * support for all major web-standards;
 * integration with other plugins;
 * autodiscovery;
 * tagging bookmarks;
 * support for SQLite or PostgreSQL storage.


%package poshuku-autosearch
Summary:        LeechCraft Poshuku - Autosearch Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-autosearch
This package provides an autosearch plugin for LeechCraft Poshuku.


%package poshuku-cleanweb
Summary:        LeechCraft Poshuku - Ad Filter Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-cleanweb
This package provides an ads filter compatibility for LeechCraft Poshuku.

It allows to use ads filter compatible with block lists.

Features:
 * Support for Firefox AdBlock+ block lists.
 * Support for detection and subscription to such lists.
 * Automatic updates of block lists.
 * User filters: blocking arbitrary images.
 * Support for replacing Adobe Flash objects with a "Load flash" button.
 * Whitelists for Flash blocker.


%package poshuku-dcac
Summary:        LeechCraft Poshuku - DC/AC Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-dcac
This package provides DC/AC plugin for LeechCraft Poshuku.

It allows to invert colors on web pages.


%package poshuku-fatape
Summary:        LeechCraft Poshuku - Greasemonkey Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-fatape
This package provides greasemonkey scripts plugin for LeechCraft Poshuku.

It allows to use GreaseMonkey userscripts. These scripts could be used for
adding new features to web pages (for example, embedding price comparisons
within shopping sites), fixing rendering bugs, combining data from multiple
webpages, and numerous other purposes.

This plugin supports almost whole API of GreaseMonkey and is compatible
with most userscripts present "in the wild".

FatApe usage is documented on the corresponding user guide page.


%package poshuku-filescheme
Summary:        LeechCraft Poshuku - Schemes Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-filescheme
This package provides a file://-schemes support for LeechCraft Poshuku.

It allows to navigate local resource via the file:// scheme. Of course,
FileScheme supports "downloading" files from local resources.


%package poshuku-fua
Summary:        LeechCraft Poshuku - Change user agent Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-fua
This package provides a fake user agent plugin for LeechCraft Poshuku.

It allows to set different User-Agent strings for different URLs.

Features:
 * URLs are defined either by their substring or by regular expression.
 * Several popular predefined user agents are present.
 * Support for custom user-defined strings.
 * Support automatic insertion of current platform, language, WebKit's
version etc. into the User-Agent string in arbitrary places.


%package poshuku-keywords
Summary:        LeechCraft Poshuku - Support of url keywords Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-keywords
This package provides an url keywords plugin for LeechCraft Poshuku.


%package poshuku-onlinebookmarks
Summary:        LeechCraft Poshuku - Online Bookmarks Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}
Requires:       %{name}-securestorage

%description poshuku-onlinebookmarks
This package provides an online bookmarks plugin for LeechCraft Poshuku.

It allows to synchronize bookmarks with services like Read It Later
or Del.icio.us.


%package poshuku-onlinebookmarks-delicious
Summary:        LeechCraft Poshuku - Onlinebookmarks Delicious Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}

%description poshuku-onlinebookmarks-delicious
This package contains a plugin for LeechCraft Poshuku Online Bookmarks.

It provides support for the the Del.icio.us service.


%package poshuku-onlinebookmarks-readitlater
Summary:        LeechCraft Poshuku - Onlinebookmarks ReadItLater Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}

%description poshuku-onlinebookmarks-readitlater
This package contains a plugin for LeechCraft Poshuku Online Bookmarks.

It provides support for the Read it Later service.


%package poshuku-qrd
Summary:        LeechCraft Poshuku - QR coDe Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-qrd
This package provides a QR coDe support plugin for LeechCraft Poshuku.

It shows the URL of a web page as a QR code.


%package poshuku-speeddial
Summary:        LeechCraft Poshuku - Speed Dial Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-speeddial
This package provides a Speed Dial support plugin for LeechCraft Poshuku.


%package qrosp
Summary:        LeechCraft Qross Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       libqrosspython1

%description qrosp
This package contains a scripting support plugin for Leechcraft.


%package rosenthal
Summary:        LeechCraft - Spell Checker Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description rosenthal
This package provides a spell checker plugin for LeechCraft.

It is based on Hunspell or Myspell dictionaries.


%package sb2
Summary:        LeechCraft SideBar2 Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sb = %{version}

%description sb2
This package provides another side bar plugin for Leechcraft.

It is a next-gen fluid sidebar with quick launch, tabs and tray areas.


%package scroblibre
Summary:        LeechCraft Submissions Protocol Scrobble Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}
Provides:       %{name}-scrobbler

%description scroblibre
This package contains a Scroblibre plugin for LeechCraft.

It is an implementation of the submissions protocol 1.2 with
support ( http://www.audioscrobbler.net/development/protocol )
for sites other than last.fm (libre.fm for now). It can
potentially handle arbitrary scrobbling URLs implementing the
submissions protocol, but it is not exposed in the GUI (yet).
 
Scroblibre is a supplement for LastFMScrobble module, and the
latter is still the recommended one because of all the social
features it offers which Scroblibre lacks.


%package secman
Summary:        LeechCraft Security manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-secman-simplestorage = %{version}
Provides:       %{name}-securestorage

%description secman
This package provides a security manager plugin for LeechCraft.

It is the base module for secure storage and such stuff.
Particular storage backends are implemented by plugins for this plugin.


%package secman-simplestorage
Summary:        LeechCraft Simple storage Module
Group:          Productivity/Networking/Other
Requires:       %{name}-secman = %{version}

%description secman-simplestorage
This package provides a simple backend for LeechCraft SecMan.

It is a simple, unencrypted storage backend.


%package seekthru
Summary:        LeechCraft OpenSearch Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

%description seekthru
This package contains an OpenSearch plugin for LeechCraft.

It provides a search client for OpenSearch-enabled web sites and engines.

Features:
 * Support for autodiscovery of OpenSearch-capable web sites.
 * Tagging of search engines.
 * Support for queries to several search engines at once.
 * Support search results in RSS/Atom format and subscribe to them
with a suitable plugin like Aggregator.
 * Show results in HTML format with a suitable plugin like Poshuku.


# %%package shaitan
# Summary:        LeechCraft Shaitan Module
# Group:          Productivity/Networking/Other
# Requires:       %%{name} = %%{version}
# Requires:       xterm
# 
# %%description shaitan
# This package provides a terminal plugin for Leechcraft.


%if %{clang_compiler}
%package snails
Summary:        LeechCraft Email client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description snails
This package contains a Email client plugin for LeechCraft.

It provides basic Email client functionality and supports SMTP and IMAP4.
%endif


%package summary
Summary:        LeechCraft Summary info Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-summaryrepresentation

%description summary
This package provides a summary plugin for LeechCraft.

It allows to show a quick overview of LeechCraft's state. It shows current
tasks like leeching or seeding torrents and downloading files with context-
dependent actions and views. It also can collect status information from
other plugins like unread channels.

Summary also allows to perform searches via the installed plugins
like SeekThru, HistoryHolder or vGrabber.

Features:
 * List of current tasks and events with context-dependent actions
and views for selected items.
 * Support for gathering status information from other plugins.
 * Category-based search query support via other plugins.


%package syncer
Summary:        LeechCraft Sync setting Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description syncer
This package provides a synchronizing plugin for Leechcraft.

It allows to synchronize data and settings between LeechCraft instances
running on different machines.


%package sysnotify
Summary:        LeechCraft System notifications Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-visualnotifications
Conflicts:      %{name}-laughty

%description sysnotify
This package contains a system notifications plugin for LeechCraft.

It provides notifications via implementations supporting FreeDesktop's
notifications standard, like KDE 4.4 (or higher), Gnome, XFCE and others.


%package tabsessionmanager
Summary:        LeechCraft Tab Session Manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description tabsessionmanager
This package provides a Tab Session Manager plugin for Leechcraft.

TabSessManager allows to restore automatically last session and allows
to create named sessions.

Features:
 * Automatically restores last session on LeechCraft startup.
 * Allows one to save named sessions for restoring them later.


%package tabslist
Summary:        LeechCraft TabsList Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description tabslist
This package provides a tabs list plugin for Leechcraft.

It allows to show the list of currently opened tabs
and allows to quickly navigate between them.


%package textogroose
Summary:        LeechCraft Script-Based Lyrics Module
Group:          Productivity/Networking/Other
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}
Requires:       %{name}-qrosp
Provides:       %{name}-lyricsprovider

%description textogroose
This package provides a lyrics finder plugin for LeechCraft.

Textogroose is a kind of supplement to DeadLyrics for sites
too complex to be described by DeadLyrics rules.


%package touchstreams
Summary:        LeechCraft VK.com Streaming Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-lmp = %{version}
Requires:       %{name}-musiczombie = %{version}

%description touchstreams
This package provides a VK.com music streaming plugin for Leechcraft.


%package tpi
Summary:        LeechCraft Task Progress Indicator Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description tpi
This package provides a Task Progress Indicator quark plugin for Leechcraft.


%package vgrabber
Summary:        LeechCraft Vkontakte grabber Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

%description vgrabber
This package provides a Vkontakte.ru plugin for LeechCraft.

It allows to grab and play audio and video from the russian
social network Vkontakte.

Features:
 * Download or stream audios and videos from Vkontakte.
 * Search for audios and videos.


%package vtyulc
Summary:        LeechCraft Video player Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-liznoo
Recommends:     vlc-codecs

%description vtyulc
This package provides a video player plugin for LeechCraft.

It allows to play video (local files, web, DVD etc).
It uses vlc library as a backend thus supporting major codecs.


%package vrooby
Summary:        LeechCraft Removable storage devices Manager
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb = %{version}
Recommends:     udisks2

%description vrooby
This package provides a Vrooby plugin for LeechCraft.

It allows to watch removable storage devices via d-bus and udisks.


%package xproxy
Summary:        LeechCraft Proxy manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description xproxy
This package provides an advanced proxy manager for LeechCraft.

It allows to configure and use proxy servers.


%package xtazy
Summary:        LeechCraft Current user tune Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description xtazy
This package provides a tune wrapper plugin for LeechCraft.

It allows to get current user tune via mpris protocol.


%package zalil
Summary:        LeechCraft Files Uploader Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}


%description zalil
This package provides a file uploader plugin for LeechCraft.

It allows to upload files to accountless filebin services.


%package -n lib%{name}-util-db%{so_ver}
Summary:        Database utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-db%{so_ver}
A library providing some useful and commonly used database-related
classes and functions.


%package -n lib%{name}-util-gui%{so_ver}
Summary:        GUI utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-gui%{so_ver}
A library providing some useful and commonly used GUI-related
widgets, classes and functions.


%package -n lib%{name}-util-models%{so_ver}
Summary:        MVC utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-models%{so_ver}
A library providing some useful and commonly used models (as in MVC),
as well as model-related classes and functions.


%package -n lib%{name}-util-network%{so_ver}_1
Summary:        Network utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-network%{so_ver}_1
A library providing some useful and commonly used
network classes and functions.


%package -n lib%{name}-util-qml%{so_ver}_1
Summary:        QML utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-qml%{so_ver}_1
A library providing some useful and commonly used QML items as well as
QML-related classes and functions.


%package -n lib%{name}-util-shortcuts%{so_ver}
Summary:        Shortcuts utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-shortcuts%{so_ver}
A library easing shortcuts usage in LeechCraft, particularly the
configurable shortcuts subsystem.


%package -n lib%{name}-util-sll%{so_ver}
Summary:        Standard LeechCraft Library
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-sll%{so_ver}
A library providing some useful classes and algorithms, not directly
related to any other library.


%package -n lib%{name}-util-svcauth%{so_ver}
Summary:        Authenticators library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-svcauth%{so_ver}
A library providing authenticators for various services like VKontakte.


%package -n lib%{name}-util-sys%{so_ver}_1
Summary:        System utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-sys%{so_ver}_1
A library providing some useful and commonly used system-related
classes and functions, like OS version parser, paths utilities or MIME
detector.


%package -n lib%{name}-util-tags%{so_ver}_1
Summary:        Tags utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-tags%{so_ver}_1
A library providing some useful classes and functions commonly used
with the LeechCraft tags subsystem.


%package -n lib%{name}-util-x11-%{so_ver}
Summary:        X11 utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-x11-%{so_ver}
A library providing X11 wrappers for LeechCraft.


%package -n lib%{name}-util-xdg%{so_ver}
Summary:        XDG utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-xdg%{so_ver}
A library providing XDG parsers and other support methods and classes
for LeechCraft.


%package -n lib%{name}-util-xpc%{so_ver}_1
Summary:        Cross-plugin communication utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-xpc%{so_ver}_1
A library providing some useful and commonly used primitives for
communications between different plugins in LeechCraft.


%package -n lib%{name}-util-xsd%{so_ver}
Summary:        XSD utility library for LeechCraft
Group:          Productivity/Networking/Other

%description -n lib%{name}-util-xsd%{so_ver}
A library providing some useful classes to be used with the
XmlSettingsDialog LeechCraft subsystem.


%prep
%setup -q -n %{name}-%{version}

#removing non-free icons
rm -rf src/plugins/azoth/share/azoth/iconsets/clients/default

#removing hidden files
find src/plugins/azoth/plugins/adiumstyles/share/azoth/styles/adium/ -name ".?*" -delete

#setup permissions correctly to avoid false duplicates reported by rpmlint (bnc#784670)
find src -name '*.png' -or -name '*.css' -or -name '*.gif' -exec chmod 0644 {} +

mkdir build && cd build

%if %{clang_compiler}
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
%endif

cmake ../src \
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_CXX_FLAGS="%{optflags} -Doverride=" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DSTRICT_LICENSING=True \
        -DWITH_DBUS_LOADERS=True \
        -DWITH_PCRE=True \
        -DWITH_QWT=True \
        -DENABLE_ADVANCEDNOTIFICATIONS=True \
        -DENABLE_AGGREGATOR=True \
                -DENABLE_AGGREGATOR_WEBACCESS=True \
        -DENABLE_AUSCRIE=True \
        -DENABLE_AZOTH=True \
                -DENABLE_AZOTH_ABBREV=True \
                -DENABLE_AZOTH_ACETAMIDE=True \
                -DENABLE_AZOTH_ASTRALITY=True \
                -DENABLE_AZOTH_AUTOPASTE=True \
                -DENABLE_AZOTH_MUCOMMANDS=True \
                -DENABLE_AZOTH_MURM=True \
                -DENABLE_AZOTH_OTROID=True \
                -DENABLE_AZOTH_SARIN=False \
                -DENABLE_AZOTH_SHX=True \
                -DENABLE_AZOTH_TRACOLOR=False \
                -DENABLE_AZOTH_VELVETBIRD=True \
%if %{woodpecker}
                -DENABLE_AZOTH_WOODPECKER=True \
%else
                -DENABLE_AZOTH_WOODPECKER=False \
%endif
                -DENABLE_AZOTH_ZHEET=True \
%if 0%{?suse_version} <= 1310
                -DENABLE_MEDIACALLS=True \
%else
                -DENABLE_MEDIACALLS=False \
%endif
        -DENABLE_BLACKDASH=False \
        -DENABLE_BLASQ=True \
%if %{vangog}
                -DENABLE_BLASQ_VANGOG=True \
%else
                -DENABLE_BLASQ_VANGOG=False \
%endif
        -DENABLE_BLOGIQUE=True \
        -DENABLE_CERTMGR=True \
        -DENABLE_CHOROID=True \
        -DENABLE_CPULOAD=True \
        -DENABLE_DEVMON=True \
        -DENABLE_DLNIWE=False \
        -DENABLE_DOLOZHEE=True \
        -DENABLE_DUMBEEP=True \
                -DDUMBEEP_WITH_PHONON=True \
        -DENABLE_ELEEMINATOR=True \
%if %{fenet}
        -DENABLE_FENET=True \
%else
        -DENABLE_FENET=False \
%endif
        -DENABLE_GACTS=True \
%if 0%{?suse_version} > 1310
                -DWITH_GACTS_BUNDLED_QXT=False \
%else
                -DWITH_GACTS_BUNDLED_QXT=True \
%endif
        -DENABLE_GLANCE=True \
        -DENABLE_GMAILNOTIFIER=True \
        -DENABLE_HARBINGER=True \
        -DENABLE_HOTSENSORS=True \
        -DENABLE_HOTSTREAMS=True \
        -DENABLE_HTTHARE=True \
        -DENABLE_IMGASTE=True \
        -DENABLE_KBSWITCH=True \
        -DENABLE_KNOWHOW=True \
        -DENABLE_KRIGSTASK=True \
        -DENABLE_LACKMAN=True \
        -DENABLE_LADS=False \
        -DENABLE_LASTFMSCROBBLE=True \
        -DENABLE_LAUGHTY=True \
        -DENABLE_LAUNCHY=True \
        -DENABLE_LEMON=True \
        -DENABLE_LHTR=True \
                -DWITH_LHTR_HTML=True \
        -DENABLE_LIZNOO=True \
%if %{lmp}
        -DENABLE_LMP=True \
%if 0%{?suse_version} > 1310
        -DUSE_GSTREAMER_10=True \
%endif
                -DENABLE_LMP_BRAINSLUGZ=True \
                -DENABLE_LMP_FRADJ=True \
                -DENABLE_LMP_GRAFFITI=True \
                -DENABLE_LMP_HTTSTREAM=True \
                -DENABLE_LMP_LIBGUESS=True \
                -DENABLE_LMP_MPRIS=True \
                -DENABLE_LMP_MTPSYNC=True \
                -DENABLE_LMP_POTORCHU=True \
%else
        -DENABLE_LMP=False \
%endif
%if %{mellonetray}
        -DENABLE_MELLONETRAY=True \
%else
        -DENABLE_MELLONETRAY=False \
%endif
        -DENABLE_MONOCLE=True \
%if 0%{?suse_version} == 1310
        -DENABLE_MONOCLE_MU=True \
                -DMUPDF_VERSION=0x0102 \
%else
        -DENABLE_MONOCLE_MU=False \
%endif
        -DENABLE_MONOCLE_PDF=True \
        -DENABLE_MONOCLE_POSTRUS=True \
        -DENABLE_MUSICZOMBIE=True \
                -DWITH_MUSICZOMBIE_CHROMAPRINT=False \
        -DENABLE_NACHEKU=False \
        -DENABLE_NETSTOREMANAGER=True \
                -DENABLE_NETSTOREMANAGER_DROPBOX=True \
                -DENABLE_NETSTOREMANAGER_GOOGLEDRIVE=True \
        -DENABLE_NEWLIFE=True \
        -DENABLE_OORONEE=True \
        -DENABLE_OTLOZHU=True \
        -DENABLE_PINTAB=True \
        -DENABLE_POGOOGLUE=True \
%if %{poleemery}
        -DENABLE_POLEEMERY=True \
%else
        -DENABLE_POLEEMERY=False \
%endif
        -DENABLE_POPISHU=True \
        -DENABLE_POSHUKU=True \
                -DENABLE_IDN=True \
                -DENABLE_POSHUKU_AUTOSEARCH=True \
                -DENABLE_POSHUKU_DCAC=True \
                -DENABLE_POSHUKU_QRD=True \
                -DENABLE_POSHUKU_SPEEDDIAL=True \
        -DENABLE_QROSP=True \
        -DENABLE_SB2=True \
        -DENABLE_SCROBLIBRE=True \
        -DENABLE_SECMAN=True \
        -DENABLE_SHAITAN=False \
        -DENABLE_SHELLOPEN=False \
%if %{clang_compiler}
        -DENABLE_SNAILS=True \
%else
        -DENABLE_SNAILS=False \
%endif
        -DENABLE_SYNCER=True \
        -DENABLE_TABSESSMANAGER=True \
        -DENABLE_TABSLIST=True \
        -DENABLE_TEXTOGROOSE=True \
        -DENABLE_TORRENT=True \
                -DENABLE_BITTORRENT_GEOIP=True \
        -DENABLE_TOUCHSTREAMS=True \
        -DENABLE_TPI=True \
        -DENABLE_TWIFEE=False \
        -DENABLE_VTYULC=True \
        -DENABLE_VROOBY=True \
        -DENABLE_WKPLUGINS=False \
        -DENABLE_ZALIL=True \
        -DLEECHCRAFT_VERSION=%{LEECHCRAFT_VERSION}

%build
cd build
make %{?_smp_mflags} VERBOSE=1

%install
cd build
%make_install

# Unneeded here Qt5 build' files:
rm -rf %{buildroot}%{_datadir}/leechcraft/qml5

#-------------------------patterns----------------------------#
%__install -d %{buildroot}%{_docdir}/%{name}

cat <<EOF >> %{buildroot}%{_docdir}/%{name}/meta_browser
This file marks the pattern meta_browser to be installed.
EOF

cat <<EOF >> %{buildroot}%{_docdir}/%{name}/meta_desktop
This file marks the pattern meta_desktop to be installed.
EOF

cat <<EOF >> %{buildroot}%{_docdir}/%{name}/meta_media
This file marks the pattern meta_browser to be installed.
EOF

cat <<EOF >> %{buildroot}%{_docdir}/%{name}/meta_messenger
This file marks the pattern meta_messenger to be installed.
EOF

cat <<EOF >> %{buildroot}%{_docdir}/%{name}/meta_office
This file marks the pattern meta_office to be installed.
EOF

cat <<EOF >> %{buildroot}%{_docdir}/%{name}/meta_tools
This file marks the pattern meta_tools to be installed.
EOF

cat <<EOF >> %{buildroot}%{_docdir}/%{name}/meta_websurf
This file marks the pattern meta_websurf to be installed.
EOF

cat <<EOF >> %{buildroot}%{_docdir}/%{name}/meta_full
This file marks the pattern meta_full to be installed.
EOF
#-----------------------end-patterns--------------------------#


%fdupes -s %{buildroot}%{_datadir}/%{name}/translations
%fdupes -s %{buildroot}%{_datadir}/%{name}/azoth
%fdupes -s %{buildroot}%{_datadir}/%{name}/global_icons/flags
%fdupes -s %{buildroot}%{_datadir}/%{name}/themes

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n lib%{name}-util-db%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-db%{so_ver}
/sbin/ldconfig

%post -n lib%{name}-util-gui%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-gui%{so_ver}
/sbin/ldconfig

%post -n lib%{name}-util-models%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-models%{so_ver}
/sbin/ldconfig

%post -n lib%{name}-util-network%{so_ver}_1
/sbin/ldconfig

%postun -n lib%{name}-util-network%{so_ver}_1
/sbin/ldconfig

%post -n lib%{name}-util-qml%{so_ver}_1
/sbin/ldconfig

%postun -n lib%{name}-util-qml%{so_ver}_1
/sbin/ldconfig

%post -n lib%{name}-util-shortcuts%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-shortcuts%{so_ver}
/sbin/ldconfig

%post -n lib%{name}-util-sll%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-sll%{so_ver}
/sbin/ldconfig

%post -n lib%{name}-util-svcauth%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-svcauth%{so_ver}
/sbin/ldconfig

%post -n lib%{name}-util-sys%{so_ver}_1
/sbin/ldconfig

%postun -n lib%{name}-util-sys%{so_ver}_1
/sbin/ldconfig

%post -n lib%{name}-util-tags%{so_ver}_1
/sbin/ldconfig

%postun -n lib%{name}-util-tags%{so_ver}_1
/sbin/ldconfig

%post -n lib%{name}-util-x11-%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-x11-%{so_ver}
/sbin/ldconfig

%post -n lib%{name}-util-xdg%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-xdg%{so_ver}
/sbin/ldconfig

%post -n lib%{name}-util-xpc%{so_ver}_1
/sbin/ldconfig

%postun -n lib%{name}-util-xpc%{so_ver}_1
/sbin/ldconfig

%post -n lib%{name}-util-xsd%{so_ver}
/sbin/ldconfig

%postun -n lib%{name}-util-xsd%{so_ver}
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE README
%{_bindir}/%{name}
%{_bindir}/%{name}-add-file
%{_bindir}/%{name}-handle-file
%{_bindir}/lc_plugin_wrapper
%{settings_dir}/coresettings.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%dir %{_datadir}/icons/hicolor/14x14
%dir %{_datadir}/icons/hicolor/14x14/apps
%dir %{_datadir}/%{name}
%dir %{settings_dir}
%dir %{translations_dir}
%dir %{_datadir}/%{name}/qml
%{translations_dir}/leechcraft_??.qm
%{translations_dir}/leechcraft_??_??.qm
%dir %{_libdir}/%{name}
%dir %{plugin_dir}
%{_libdir}/lib%{name}-util.so.*
%{_libdir}/lib%{name}-xsd.so.*
%doc %{_mandir}/man1/%{name}*.1.gz
%{_datadir}/%{name}/global_icons/
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/*
%{_datadir}/%{name}/themes/*/*.rc
%exclude %{_datadir}/cmake/Modules/InitLCPlugin.cmake
%{_datadir}/%{name}/qml/org/
%{_datadir}/%{name}/qml/common/
%exclude %{_docdir}/%{name}/meta_*

%files advancednotifications
%defattr(-,root,root)
%{plugin_dir}/*%{name}_advancednotifications.so
%{translations_dir}/leechcraft_advancednotifications*
%{settings_dir}/advancednotificationssettings.xml
%{_datadir}/%{name}/qml/advancednotifications
%{_datadir}/%{name}/sounds

%files aggregator
%defattr(-,root,root)
%{settings_dir}/aggregatorsettings.xml
%{translations_dir}/%{name}_aggregator_??.qm
%{translations_dir}/%{name}_aggregator_??_??.qm
%{plugin_dir}/*%{name}_aggregator.so

%files aggregator-bodyfetch
%defattr(-,root,root)
%{plugin_dir}/*%{name}_aggregator_bodyfetch.so
%dir %{_datadir}/%{name}/scripts
%{_datadir}/%{name}/scripts/aggregator/

%files aggregator-webaccess
%defattr(-,root,root)
%{plugin_dir}/*%{name}_aggregator_webaccess.so
%{settings_dir}/aggregatorwebaccesssettings.xml
%{translations_dir}/%{name}_aggregator_webaccess*.qm

%files anhero
%defattr(-,root,root)
%{_bindir}/lc_anhero_crashprocess
%{plugin_dir}/*%{name}_anhero.so
%{translations_dir}/leechcraft_anhero*
%doc %{_mandir}/man*/lc_anhero_crashprocess*

%files auscrie
%defattr(-,root,root)
%{translations_dir}/%{name}_auscrie_*.qm
%{plugin_dir}/lib%{name}_auscrie.so

%files azoth
%defattr(-,root,root)
%dir %{azoth_dir}
%dir %{azoth_dir}/styles
%{azoth_dir}/emoticons
%{azoth_dir}/iconsets
%{settings_dir}/azothsettings.xml
%{translations_dir}/%{name}_azoth_??.qm
%{translations_dir}/%{name}_azoth_??_??.qm
%{plugin_dir}/*%{name}_azoth.so

%files azoth-abbrev
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_abbrev.so
%{_datadir}/%{name}/translations/%{name}_azoth_abbrev_??.qm
%{_datadir}/%{name}/translations/%{name}_azoth_abbrev_??_??.qm

%files azoth-acetamide
%defattr(-,root,root)
%{settings_dir}/azothacetamidesettings.xml
%{translations_dir}/%{name}_azoth_acetamide*
%{plugin_dir}/*%{name}_azoth_acetamide.so
%{_datadir}/applications/%{name}-azoth-acetamide.desktop

%files azoth-adiumstyles
%defattr(644,root,root,755)
%{plugin_dir}/*%{name}_azoth_adiumstyles*
%{_datadir}/%{name}/azoth/styles/adium
%{_datadir}/%{name}/translations/%{name}_azoth_adiumstyles_*.qm

%files azoth-astrality
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_azoth_astrality.so
%{_datadir}/%{name}/translations/%{name}_azoth_astrality_*.qm

%files azoth-autoidler
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_autoidler*
%{settings_dir}/azothautoidlersettings.xml
%{translations_dir}/leechcraft_azoth_autoidler*

%files azoth-autopaste
%defattr(-,root,root)
%{settings_dir}/azothautopastesettings.xml
%{translations_dir}/%{name}_azoth_autopaste*
%{plugin_dir}/*%{name}_azoth_autopaste.so

%files azoth-birthdaynotifier
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_birthdaynotifier.so
%{_datadir}/%{name}/settings/azothbirthdaynotifiersettings.xml
%{translations_dir}/%{name}_azoth_birthdaynotifier*

%files azoth-chathistory
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_chathistory*
%{plugin_dir}/*%{name}_azoth_chathistory.so
%{settings_dir}/azothchathistorysettings.xml

%files azoth-depester
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_depester.so
%{translations_dir}/%{name}_azoth_depester*

%files azoth-embedmedia
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_embedmedia.so

%files azoth-herbicide
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_herbicide.so
%{translations_dir}/%{name}_azoth_herbicide*
%{settings_dir}/azothherbicidesettings.xml

%files azoth-hili
%defattr(-,root,root)
%{settings_dir}/azothhilisettings.xml
%{translations_dir}/%{name}_azoth_hili*
%{plugin_dir}/*%{name}_azoth_hili.so

%files azoth-isterique
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_isterique*
%{settings_dir}/azothisteriquesettings.xml
%{translations_dir}/leechcraft_azoth_isterique*

%files azoth-juick
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_juick.so
%{_datadir}/%{name}/translations/%{name}_azoth_juick_*.qm

%files azoth-keeso
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_keeso.so

%files azoth-lastseen
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_lastseen*
%{translations_dir}/leechcraft_azoth_lastseen*

%files azoth-metacontacts
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_metacontacts*
%{translations_dir}/%{name}_azoth_metacontacts*

%files azoth-modnok
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_modnok*
%{settings_dir}/azothmodnoksettings.xml
%{translations_dir}/leechcraft_azoth_modnok*
%{azoth_dir}/lc_azoth_modnok_latexconvert.sh

%files azoth-mucommands
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_mucommands.so
%{_datadir}/%{name}/translations/%{name}_azoth_mucommands_??.qm
%{_datadir}/%{name}/translations/%{name}_azoth_mucommands_??_??.qm

%files azoth-murm
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_murm.so
%{_datadir}/%{name}/translations/%{name}_azoth_murm*.qm
%{settings_dir}/azothmurmsettings.xml

%files azoth-nativeemoticons
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_nativeemoticons.so
%{_datadir}/%{name}/translations/%{name}_azoth_nativeemoticons_*.qm

%files azoth-otroid
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_otroid.so
%{_datadir}/%{name}/translations/%{name}_azoth_otroid*.qm
%{_datadir}/%{name}/settings/azothotroidsettings.xml

%files azoth-rosenthal
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_rosenthal.so
%{translations_dir}/%{name}_azoth_rosenthal*
# %%{settings_dir}/azothrosenthalsettings.xml

%files azoth-shx
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_shx.so
%{_datadir}/%{name}/settings/azothshxsettings.xml
%{_datadir}/%{name}/translations/%{name}_azoth_shx_*.qm

%files azoth-standardstyles
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_standardstyles.so
%{_datadir}/%{name}/azoth/styles/standard/
%{_datadir}/%{name}/translations/%{name}_azoth_standardstyles_*.qm

%files azoth-vader
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_vader*
%{_datadir}/%{name}/settings/azothvadersettings.xml
%{plugin_dir}/*%{name}_azoth_vader.so

%files azoth-velvetbird
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_velvetbird.so

%if %{woodpecker}
%files azoth-woodpecker
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_azoth_woodpecker.so
%{_datadir}/%{name}/settings/azothwoodpeckersettings.xml
%{_datadir}/%{name}/translations/%{name}_azoth_woodpecker_*.qm
%endif

%files azoth-xoox
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_xoox*
%{plugin_dir}/*%{name}_azoth_xoox.so
%{_datadir}/applications/%{name}-azoth-xoox.desktop
%{_datadir}/%{name}/settings/azothxooxsettings.xml

%files azoth-xtazy
%defattr(-,root,root)
%{settings_dir}/azothxtazysettings.xml
%{plugin_dir}/*%{name}_azoth_xtazy.so
%{translations_dir}/%{name}_azoth_xtazy*

%files azoth-zheet
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_zheet*
%{plugin_dir}/*%{name}_azoth_zheet.so

%files bittorrent
%defattr(-,root,root)
%{settings_dir}/torrentsettings.xml
%{translations_dir}/%{name}_bittorrent_*.qm
%{plugin_dir}/*%{name}_bittorrent.so
%{_datadir}/applications/%{name}-bittorrent.desktop

#%%files blackdash
#%%defattr(-,root,root)
#%%{plugin_dir}/*%%{name}_blackdash.so

%files blasq
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blasq.so
%{_datadir}/%{name}/settings/blasqsettings.xml
%{_datadir}/%{name}/qml/blasq
%{_datadir}/%{name}/translations/%{name}_blasq_??.qm
%{_datadir}/%{name}/translations/%{name}_blasq_??_??.qm

%files blasq-spegnersi
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blasq_spegnersi.so
%{_datadir}/%{name}/translations/%{name}_blasq_spegnersi*.qm

%files blasq-deathnote
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blasq_deathnote.so
%{_datadir}/%{name}/translations/%{name}_blasq_deathnote*.qm

%files blasq-rappor
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blasq_rappor.so
%{_datadir}/%{name}/translations/%{name}_blasq_rappor*.qm

%if %{vangog}
%files blasq-vangog
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blasq_vangog.so
%{_datadir}/%{name}/translations/%{name}_blasq_vangog*.qm
%endif

%files blogique
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blogique.so
%{_datadir}/%{name}/settings/blogiquesettings.xml
%{_datadir}/%{name}/translations/%{name}_blogique_??.qm
%{_datadir}/%{name}/translations/%{name}_blogique_??_??.qm
%dir %{_datadir}/%{name}/qml/blogique
%{_datadir}/%{name}/qml/blogique/*.qml
%{_datadir}/%{name}/qml/blogique/*.js

%files blogique-hestia
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blogique_hestia.so
%{_datadir}/%{name}/settings/blogiquehestiasettings.xml
%{_datadir}/%{name}/translations/%{name}_blogique_hestia*.qm

%files blogique-metida
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blogique_metida.so
%{_datadir}/%{name}/settings/blogiquemetidasettings.xml
%{_datadir}/%{name}/translations/%{name}_blogique_metida*.qm
# %%{_datadir}/%%{name}/qml/blogique/metida/

%files certmgr
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_certmgr.so
%{_datadir}/%{name}/settings/certmgrsettings.xml
%{_datadir}/%{name}/translations/%{name}_certmgr*.qm

%files choroid
%defattr(-,root,root)
%{plugin_dir}/*%{name}_choroid.so
%{_datadir}/%{name}/qml/choroid

%files cpuload
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_cpuload.so
%{_datadir}/%{name}/qml/cpuload

%files cstp
%defattr(-,root,root)
%{settings_dir}/cstpsettings.xml
%{translations_dir}/leechcraft_cstp*.qm
%{plugin_dir}/*leechcraft_cstp.so

%files dbusmanager
%defattr(-,root,root)
%{translations_dir}/%{name}_dbusmanager*.qm
%{plugin_dir}/*leechcraft_dbusmanager.so
%{settings_dir}/dbusmanagersettings.xml

%files deadlyrics
%defattr(-,root,root)
# %%{settings_dir}/deadlyricssettings.xml
%{translations_dir}/%{name}_deadlyrics*.qm
%{plugin_dir}/*%{name}_deadlyrics.so

%files devel
%defattr(-,root,root)
%{_datadir}/%{name}/cmake
%{_includedir}/%{name}
%{_libdir}/lib%{name}-util*.so
%{_libdir}/lib%{name}-xsd.so
%{_datadir}/cmake/Modules/InitLCPlugin.cmake

%files devmon
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_devmon.so
%{_datadir}/%{name}/translations/%{name}_devmon_*.qm

# %%files dlniwe
# %%defattr(-,root,root)
# %%{_libdir}/%%{name}/plugins/lib%%{name}_dlniwe.so

%files dolozhee
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_dolozhee.so
%{_datadir}/%{name}/translations/%{name}_dolozhee_*.qm

%files dumbeep
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_dumbeep.so
%{_datadir}/%{name}/settings/dumbeepsettings.xml

%files eleeminator
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_eleeminator.so
%{_datadir}/%{name}/translations/%{name}_eleeminator_??.qm
%{_datadir}/%{name}/translations/%{name}_eleeminator_??_??.qm
%{_datadir}/%{name}/settings/eleeminatorsettings.xml

%if %{fenet}
%files fenet
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_fenet.so
%{_datadir}/%{name}/settings/fenetsettings.xml
%{_bindir}/%{name}-session
%dir %{_datadir}/%{name}/fenet
%dir %{_datadir}/%{name}/fenet/compositing
%dir %{_datadir}/%{name}/fenet/wms
%{_datadir}/xsessions/LCDE.desktop
%{_datadir}/%{name}/translations/%{name}_fenet_*.qm

%files fenet-awesome
%defattr(-,root,root)
%dir %{_datadir}/%{name}/fenet
%dir %{_datadir}/%{name}/fenet/wms
%{_datadir}/%{name}/fenet/wms/*awesome*

%files fenet-compton
%defattr(-,root,root)
%dir %{_datadir}/%{name}/fenet
%dir %{_datadir}/%{name}/fenet/compositing
%{_datadir}/%{name}/fenet/compositing/*compton*

%files fenet-kwin
%defattr(-,root,root)
%dir %{_datadir}/%{name}/fenet
%dir %{_datadir}/%{name}/fenet/wms
%{_datadir}/%{name}/fenet/wms/*kwin*

%files fenet-openbox
%defattr(-,root,root)
%dir %{_datadir}/%{name}/fenet
%dir %{_datadir}/%{name}/fenet/wms
%{_datadir}/%{name}/fenet/wms/*openbox*
%endif

%files gacts
%defattr(-,root,root)
%doc src/plugins/gacts/3rdparty/qxt/LICENSE
%{_libdir}/%{name}/plugins/*%{name}_gacts.so
%{_datadir}/%{name}/translations/%{name}_gacts_*.qm

%files glance
%defattr(-,root,root)
%{plugin_dir}/*%{name}_glance.so
%{translations_dir}/leechcraft_glance*

%files gmailnotifier
%defattr(-,root,root)
%{plugin_dir}/*%{name}_gmailnotifier.so
%{settings_dir}/gmailnotifiersettings.xml
%{translations_dir}/leechcraft_gmailnotifier*
%{_datadir}/%{name}/qml/gmailnotifier/

%files harbinger
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/libleechcraft_harbinger.so

%files historyholder
%defattr(-,root,root)
%{plugin_dir}/*leechcraft_historyholder.so
%{translations_dir}/leechcraft_historyholder*.qm

%files hotsensors
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_hotsensors.so
%{_datadir}/%{name}/qml/hotsensors
%{_datadir}/%{name}/translations/%{name}_hotsensors_*.qm

%files hotstreams
%defattr(-,root,root)
%{plugin_dir}/*%{name}_hotstreams.so
%{_datadir}/%{name}/translations/%{name}_hotstreams_*.qm

%files htthare
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_htthare.so
%{_datadir}/%{name}/settings/httharesettings.xml
%{_datadir}/%{name}/translations/%{name}_htthare_*.qm

%files imgaste
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_imgaste.so
%{_datadir}/%{name}/translations/%{name}_imgaste_*.qm

%files kbswitch
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_kbswitch.so
%{_datadir}/%{name}/settings/kbswitchsettings.xml
%{_datadir}/%{name}/translations/%{name}_kbswitch_*.qm
%{_datadir}/%{name}/qml/kbswitch

%files kinotify
%defattr(-,root,root)
%{_datadir}/%{name}/kinotify
%{settings_dir}/kinotifysettings.xml
%{plugin_dir}/*%{name}_kinotify.so
%{_datadir}/%{name}/translations/%{name}_kinotify_*.qm

%files knowhow
%defattr(-,root,root)
%{_datadir}/%{name}/knowhow
%{plugin_dir}/*%{name}_knowhow.so
%{settings_dir}/knowhowsettings.xml

%files krigstask
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_krigstask.so
%{_datadir}/%{name}/qml/krigstask
%{_datadir}/%{name}/translations/%{name}_krigstask_*.qm

%files lackman
%defattr(-,root,root)
%{plugin_dir}/*%{name}_lackman.so
%{settings_dir}/lackmansettings.xml
%{translations_dir}/leechcraft_lackman*

%files lastfmscrobble
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_lastfmscrobble.so
%{_datadir}/%{name}/settings/lastfmscrobblesettings.xml
%{_datadir}/%{name}/translations/%{name}_lastfmscrobble_*.qm

%files laughty
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_laughty.so
%{_datadir}/%{name}/translations/%{name}_laughty_*.qm

%files launchy
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_launchy.so
%{_datadir}/%{name}/translations/%{name}_launchy_*.qm
%{_datadir}/%{name}/qml/launchy/

#%%files lcftp
#%%defattr(-,root,root)
#%%{plugin_dir}/*%%{name}_lcftp.so
#%%{settings_dir}/lcftpsettings.xml
#%%{translations_dir}/leechcraft_lcftp*

%files lemon
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_lemon.so
%{_datadir}/%{name}/qml/lemon/
%{_datadir}/%{name}/translations/%{name}_lemon_*.qm
%{_datadir}/%{name}/settings/lemonsettings.xml

%files lhtr
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_lhtr.so
%{_datadir}/%{name}/translations/%{name}_lhtr_*.qm
%{_datadir}/%{name}/settings/lhtrsettings.xml

%files liznoo
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_liznoo.so
%{_datadir}/%{name}/settings/liznoosettings.xml
%{_datadir}/%{name}/translations/%{name}_liznoo_*.qm

%if %{lmp}
%files lmp
%defattr(-,root,root)
%{settings_dir}/lmpsettings.xml
%{settings_dir}/lmpfilterrgsettings.xml
%{_datadir}/%{name}/translations/%{name}_lmp_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_??_??.qm
%{plugin_dir}/*%{name}_lmp.so
%{_datadir}/applications/%{name}-lmp*.desktop
%dir %{_datadir}/%{name}/qml/lmp
%{_datadir}/%{name}/qml/lmp/*.qml
%exclude %{_datadir}/%{name}/qml/lmp/brainslugz

%files lmp-brainslugz
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_lmp_brainslugz.so
%dir %{_datadir}/%{name}/qml/lmp
%{_datadir}/%{name}/qml/lmp/brainslugz
%{_datadir}/%{name}/translations/%{name}_lmp_brainslugz_*.qm

%files lmp-dumbsync
%defattr(-,root,root)
%{plugin_dir}/*%{name}_lmp_dumbsync.so
%{_datadir}/%{name}/settings/lmpdumbsyncsettings.xml
%{_datadir}/%{name}/translations/%{name}_lmp_dumbsync_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_dumbsync_??_??.qm

%files lmp-fradj
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_lmp_fradj.so
%{_datadir}/%{name}/translations/%{name}_lmp_fradj_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_fradj_??_??.qm

%files lmp-graffiti
%defattr(-,root,root)
%{plugin_dir}/*%{name}_lmp_graffiti.so
%{_datadir}/%{name}/translations/%{name}_lmp_graffiti_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_graffiti_??_??.qm

%files lmp-httstream
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_lmp_httstream.so
%{_datadir}/%{name}/settings/lmphttstreamfiltersettings.xml
%{_datadir}/%{name}/translations/%{name}_lmp_httstream_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_httstream_??_??.qm

%files lmp-mp3tunes
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_lmp_mp3tunes.so
%{_datadir}/%{name}/settings/lmpmp3tunessettings.xml

%files lmp-mtpsync
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_lmp_mtpsync.so

%files lmp-potorchu
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_lmp_potorchu.so
%{_datadir}/%{name}/translations/%{name}_lmp_potorchu_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_potorchu_??_??.qm
%endif

%if %{mellonetray}
%files mellonetray
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_mellonetray.so
%{_datadir}/%{name}/qml/mellonetray/
%{_datadir}/%{name}/translations/%{name}_mellonetray_*.qm
%endif

%files monocle
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle.so
%{_datadir}/%{name}/translations/%{name}_monocle_*.qm
%{_datadir}/%{name}/settings/monoclesettings.xml

%files monocle-dik
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_dik.so

%files monocle-fxb
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_fxb.so
%{_datadir}/applications/%{name}-monocle-fxb.desktop
%{_datadir}/%{name}/settings/monoclefxbsettings.xml

%if 0%{?suse_version} == 1310
%files monocle-mu
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_mu.so
%endif

%files monocle-pdf
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_pdf.so
%{_datadir}/applications/%{name}-monocle-pdf.desktop
%{_datadir}/%{name}/settings/monoclepdfsettings.xml

%files monocle-postrus
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_postrus.so
%{_datadir}/applications/%{name}-monocle-postrus.desktop

%files monocle-seen
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_seen.so
%{_datadir}/applications/%{name}-monocle-seen.desktop

%files musiczombie
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_musiczombie.so
%{_datadir}/%{name}/translations/%{name}_musiczombie_*.qm

# %%files nacheku
# %%defattr(-,root,root)
# %%{_libdir}/%%{name}/plugins/lib%%{name}_nacheku.so
# %%{_datadir}/%%{name}/settings/nachekusettings.xml
# %%{_datadir}/%%{name}/translations/%%{name}_nacheku_*.qm

%files netstoremanager
%defattr(-,root,root)
%{plugin_dir}/*%{name}_netstoremanager.so
%{_datadir}/%{name}/settings/netstoremanagersettings.xml
%{_datadir}/%{name}/translations/%{name}_netstoremanager_??.qm
%{_datadir}/%{name}/translations/%{name}_netstoremanager_??_??.qm

%files netstoremanager-dropbox
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_netstoremanager_dbox.so
%{_datadir}/%{name}/settings/nsmdropboxsettings.xml

%files netstoremanager-googledrive
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_netstoremanager_googledrive.so
%{_datadir}/%{name}/settings/nsmgoogledrivesettings.xml
%{_datadir}/%{name}/translations/%{name}_netstoremanager_googledrive_*.qm

#%%if %%qtversion >= 40800
#%%files netstoremanager-yandexdisk
#%%defattr(-,root,root)
#%%{_libdir}/%%{name}/plugins/*%%{name}_netstoremanager_yandexdisk.so
#%%{_datadir}/%%{name}/translations/%%{name}_netstoremanager_yandexdisk_*.qm
#%%endif

%files networkmonitor
%defattr(-,root,root)
%{translations_dir}/%{name}_networkmonitor*.qm
%{plugin_dir}/*%{name}_networkmonitor.so

%files newlife
%defattr(-,root,root)
%{translations_dir}/%{name}_newlife*.qm
%{plugin_dir}/*%{name}_newlife.so

%files ooronee
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_ooronee.so
%{_datadir}/%{name}/settings/ooroneesettings.xml
%{_datadir}/%{name}/qml/ooronee

%files otlozhu
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_otlozhu.so
%{_datadir}/%{name}/translations/%{name}_otlozhu_*.qm
%{_datadir}/%{name}/settings/otlozhusettings.xml

%files pintab
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_pintab.so
%{_datadir}/%{name}/translations/%{name}_pintab_*.qm

%files pogooglue
%defattr(-,root,root)
%{plugin_dir}/*%{name}_pogooglue*
%{translations_dir}/leechcraft_pogooglue*

%if %{poleemery}
%files poleemery
%defattr(-,root,root)
%{_datadir}/%{name}/settings/poleemerysettings.xml
%{_datadir}/%{name}/translations/%{name}_poleemery_*.qm
%{_libdir}/%{name}/plugins/*%{name}_poleemery*
%endif

%files popishu
%defattr(-,root,root)
%{settings_dir}/popishusettings.xml
%{translations_dir}/%{name}_popishu_*.qm
%{plugin_dir}/*%{name}_popishu.so

%files poshuku
%defattr(-,root,root)
%dir %{_datadir}/%{name}/installed
%{_datadir}/%{name}/installed/poshuku/
%{settings_dir}/poshukusettings.xml
%{translations_dir}/%{name}_poshuku_??.qm
%{translations_dir}/%{name}_poshuku_??_??.qm
%{plugin_dir}/*%{name}_poshuku.so

%files poshuku-autosearch
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_poshuku_autosearch.so
%{_datadir}/%{name}/translations/%{name}_poshuku_autosearch_*.qm

%files poshuku-cleanweb
%defattr(-,root,root)
%{settings_dir}/poshukucleanwebsettings.xml
%{translations_dir}/%{name}_poshuku_cleanweb*.qm
%{plugin_dir}/*%{name}_poshuku_cleanweb.so

%files poshuku-dcac
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_poshuku_dcac.so
%{_datadir}/%{name}/translations/%{name}_poshuku_dcac_??.qm
%{_datadir}/%{name}/translations/%{name}_poshuku_dcac_??_??.qm
%{_datadir}/%{name}/settings/poshukudcacsettings.xml

%files poshuku-fatape
%defattr(-,root,root)
%{settings_dir}/poshukufatapesettings.xml
%{plugin_dir}/*%{name}_poshuku_fatape.so
%{translations_dir}/leechcraft_poshuku_fatape_*.qm

%files poshuku-filescheme
%defattr(-,root,root)
%{translations_dir}/%{name}_poshuku_filescheme_*.qm
%{plugin_dir}/*%{name}_poshuku_filescheme.so

%files poshuku-fua
%defattr(-,root,root)
%{settings_dir}/poshukufuasettings.xml
%{translations_dir}/%{name}_poshuku_fua*.qm
%{plugin_dir}/*%{name}_poshuku_fua.so

%files poshuku-keywords
%defattr(-,root,root,-)
%{plugin_dir}/*%{name}_poshuku_keywords.so
%{settings_dir}/poshukukeywordssettings.xml
%{_datadir}/%{name}/translations/%{name}_poshuku_keywords_*.qm

%files poshuku-onlinebookmarks
%defattr(-,root,root)
%{settings_dir}/poshukuonlinebookmarkssettings.xml
%{translations_dir}/%{name}_poshuku_onlinebookmarks*.qm
%{plugin_dir}/*%{name}_poshuku_onlinebookmarks.so

%files poshuku-onlinebookmarks-delicious
%defattr(-,root,root)
%{plugin_dir}/*%{name}_poshuku_onlinebookmarks_delicious*

%files poshuku-onlinebookmarks-readitlater
%defattr(-,root,root)
%{plugin_dir}/*%{name}_poshuku_onlinebookmarks_readitlater.*

%files poshuku-qrd
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_poshuku_qrd.so
%{_datadir}/%{name}/translations/%{name}_poshuku_qrd_??.qm
%{_datadir}/%{name}/translations/%{name}_poshuku_qrd_??_??.qm

%files poshuku-speeddial
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_poshuku_speeddial.so
%{_datadir}/%{name}/settings/poshukuspeeddialsettings.xml
%{_datadir}/%{name}/translations/%{name}_poshuku_speeddial_??.qm
%{_datadir}/%{name}/translations/%{name}_poshuku_speeddial_??_??.qm

%files qrosp
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_qrosp.so

%files rosenthal
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_rosenthal.so
%{_datadir}/%{name}/translations/%{name}_rosenthal*
%{_datadir}/%{name}/settings/rosenthalsettings.xml

%files sb2
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_sb2.so
%{_datadir}/%{name}/qml/sb2/
%{_datadir}/%{name}/settings/sb2panelsettings.xml
%{_datadir}/%{name}/translations/%{name}_sb2_*.qm

%files scroblibre
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_scroblibre.so
%{_datadir}/%{name}/settings/scroblibresettings.xml
%{_datadir}/%{name}/translations/%{name}_scroblibre_*.qm

%files secman
%defattr(-,root,root)
%{plugin_dir}/*%{name}_secman.so
%{_datadir}/%{name}/translations/%{name}_secman_*.qm

%files secman-simplestorage
%defattr(-,root,root)
%{plugin_dir}/*%{name}_secman_simplestorage.so

%files seekthru
%defattr(-,root,root)
%{settings_dir}/seekthrusettings.xml
%{translations_dir}/%{name}_seekthru*.qm
%{plugin_dir}/*%{name}_seekthru.so

# %%files shaitan
# %%defattr(-,root,root)
# %%{_libdir}/%%{name}/plugins/lib%%{name}_shaitan.so

%if %{clang_compiler}
%files snails
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_snails.so
%{_datadir}/%{name}/settings/snailssettings.xml
%{_datadir}/%{name}/translations/%{name}_snails_??.qm
%{_datadir}/%{name}/translations/%{name}_snails_??_??.qm
%{_datadir}/%{name}/snails
%endif

%files summary
%defattr(-,root,root)
%{translations_dir}/%{name}_summary*.qm
%{plugin_dir}/*%{name}_summary.so

%files syncer
%defattr(-,root,root)
%{plugin_dir}/*%{name}_syncer.so
%{settings_dir}/syncersettings.xml
%{translations_dir}/leechcraft_syncer*

%files sysnotify
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_sysnotify.so
%{_datadir}/%{name}/translations/%{name}_sysnotify_*.qm

%files tabsessionmanager
%defattr(-,root,root)
%{plugin_dir}/*%{name}_tabsessmanager.so
%{_datadir}/%{name}/translations/%{name}_tabsessmanager_*.qm

%files tabslist
%defattr(-,root,root)
%{plugin_dir}/*%{name}_tabslist.so
%{translations_dir}/leechcraft_tabslist*

%files textogroose
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_textogroose.so

%files touchstreams
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_touchstreams.so
%{_datadir}/%{name}/translations/%{name}_touchstreams*.qm
%{_datadir}/%{name}/settings/touchstreamssettings.xml

%files tpi
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_tpi.so
%{_datadir}/%{name}/qml/tpi/

%files vgrabber
%defattr(-,root,root)
%{settings_dir}/vgrabbersettings.xml
%{translations_dir}/%{name}_vgrabber*.qm
%{plugin_dir}/*%{name}_vgrabber.so

%files vtyulc
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_vtyulc.so
%{_datadir}/%{name}/settings/vtyulcsettings.xml
%{_datadir}/%{name}/translations/%{name}_vtyulc_*.qm

%files vrooby
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_vrooby.so
%{_datadir}/%{name}/translations/%{name}_vrooby_*.qm
%{_datadir}/%{name}/qml/vrooby

%files xproxy
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_xproxy.so
%{_datadir}/%{name}/settings/xproxysettings.xml
%{_datadir}/%{name}/translations/%{name}_xproxy_*.qm
%{_datadir}/%{name}/scripts/xproxy

%files xtazy
%defattr(-,root,root)
%{_datadir}/%{name}/settings/xtazysettings.xml
%{_libdir}/%{name}/plugins/*%{name}_xtazy.so
%{_datadir}/%{name}/translations/%{name}_xtazy*

%files zalil
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_zalil.so
%{_datadir}/%{name}/translations/%{name}_zalil_*.qm

%files -n lib%{name}-util-db%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-db*.so.*

%files -n lib%{name}-util-gui%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-gui*.so.*

%files -n lib%{name}-util-models%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-models*.so.*

%files -n lib%{name}-util-network%{so_ver}_1
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-network*.so.*

%files -n lib%{name}-util-qml%{so_ver}_1
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-qml*.so.*

%files -n lib%{name}-util-shortcuts%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-shortcuts*.so.*

%files -n lib%{name}-util-sll%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-sll*.so.*

%files -n lib%{name}-util-svcauth%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-svcauth*.so.*

%files -n lib%{name}-util-sys%{so_ver}_1
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-sys*.so.*

%files -n lib%{name}-util-tags%{so_ver}_1
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-tags*.so.*

%files -n lib%{name}-util-x11-%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-x11*.so.*

%files -n lib%{name}-util-xdg%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-xdg*.so.*

%files -n lib%{name}-util-xpc%{so_ver}_1
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-xpc*.so.*

%files -n lib%{name}-util-xsd%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}-util-xsd*.so.*

#-------------------------patterns----------------------------#
%files meta_browser
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/meta_browser

%files meta_desktop
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/meta_desktop

%files meta_media
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/meta_media

%files meta_messenger
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/meta_messenger

%files meta_office
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/meta_office

%files meta_tools
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/meta_tools

%files meta_websurf
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/meta_websurf

%files meta_full
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/meta_full
#-----------------------end-patterns--------------------------#

%changelog
