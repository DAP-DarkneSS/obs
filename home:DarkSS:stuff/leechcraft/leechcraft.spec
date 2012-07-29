#
# spec file for package leechcraft
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define qtversion %(rpm -q libqt4 --qf='%{VERSION}\n'|awk -F. '{print $1 * 10000 + $2 * 100 + $3}')
%define plugin_dir %{_libdir}/%{name}/plugins
%define translations_dir %{_datadir}/%{name}/translations
%define settings_dir %{_datadir}/%{name}/settings
%define azoth_dir %{_datadir}/%{name}/azoth

Name:           leechcraft
Version:        0.5.75
Release:        1
Summary:        Modular Internet Client
License:        GPL-3.0+
Group:          Productivity/Networking/Other
Url:            http://leechcraft.org
Source0:        http://netcologne.dl.sourceforge.net/project/%{name}/LeechCraft/%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.desktop
# Fixing path to php-cli
Patch2:         eiskaltdcpp-fix-php5-issue.patch
# Set AppQStyle to default from plastique
Patch3:         defaultstyle.patch
# Fixing compilation with the latest poppler version
%if 0%{suse_version} > 1210
Patch4:         monocle-factory.patch
%endif

BuildRequires:  hunspell-devel
BuildRequires:  boost-devel
BuildRequires:  cmake > 2.8
%if 0%{suse_version} <= 1210
BuildRequires:  doxygen
%endif
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  kdebase4-workspace-devel
BuildRequires:  libGeoIP-devel
BuildRequires:  libQtWebKit-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmsn-devel
BuildRequires:  libqca2-devel
BuildRequires:  libqjson-devel
BuildRequires:  libqscintilla-devel
BuildRequires:  libqt4-devel >= 4.6
BuildRequires:  libqt4-sql
BuildRequires:  libqxmpp-lc-devel >= 0.3.61
BuildRequires:  libqxt1-devel
BuildRequires:  libtorrent-rasterbar-devel >= 0.15.6
BuildRequires:  oxygen-icon-theme
BuildRequires:  phonon-devel
BuildRequires:  speex-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  file-devel
BuildRequires:  taglib-devel
%if %qtversion >= 40800
BuildRequires:  libpoppler-qt4-devel
%endif

Requires:       oxygen-icon-theme

Obsoletes:      %{name}-iconset-oxygen
Obsoletes:      %{name}-iconset-tango
Obsoletes:      %{name}-tabpp
Obsoletes:      %{name}-eiskaltdcpp

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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


%package devel
Summary:        LeechCraft Development Files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package provides files required for development for LeechCraft.

It contains header files required to develop new modules.


%if 0%{suse_version} <= 1210
%package doc
Summary:        LeechCraft Core Documentation
Group:          Development/Libraries/Other
BuildArch:      noarch

%description doc
This packages provides documentation of LeechCraft core API.
 
It contains description of core API used for developing first-level
LeechCraft plugins. For developing sub-plugins, please refer to
corresponding packages (like leechcraft-azoth-doc). This documentation
is also available online at http://doc.leechcraft.org/core/
%endif


%package aggregator
Summary:        LeechCraft RSS/Atom Aggregator Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
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

%description aggregator-bodyfetch
This package provides a body fetch plugin for LeechCraft Aggregator.

It allows to automatically fetch full bodies of news items and replace the
original teasers from RSS feeds with them, so that it appears like the full
news stories were originally there.

Fetching is done according to little scripts called recipes. For this to
work, a script provider like Qrosp should be installed. Please refer to the
guide to writing recipes if you are interested in writing your own ones.


%package auscrie
Summary:        LeechCraft Screenshoter Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description auscrie
This package provides a screenshooter plugin for LeechCraft.

It allows to make screenshots of LeechCraft and then either save them locally
or upload them to an imagebin.


%package popishu
Summary:        LeechCraft Text editor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

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
Provides:       %{name}-visualnotifications
Requires:       %{name} = %{version}

%description dbusmanager
This package provides a D-Bus implementation plugin for LeechCraft.

It allows to use D-Bus. Currently, this only means showing notifications
via implementations supporting FreeDesktop's notifications standard,
like KDE 4.4 (or higher), Gnome, XFCE and others.


%package deadlyrics
Summary:        LeechCraft Lyrics finder Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

%description deadlyrics
This package provides a lyrics finder plugin for LeechCraft.

It is a simple client for searching song lyrics on various sites.
The search interface is available via LeechCraft Summary.


%package historyholder
Summary:        LeechCraft History Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description historyholder
This package provides a history keeper plugin for LeechCraft.

It allows to store information about finished downloads and similar events
and allows to search it by text, wildcard, regular expressions or tags.


%package kinotify
Summary:        LeechCraft Kinetic notifications Module
Group:          Productivity/Networking/Other
Provides:       %{name}-visualnotifications
Requires:       %{name} = %{version}

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


%package lmp
Summary:        LeechCraft Media player Module
Group:          Productivity/Networking/Other
Provides:       %{name}-audioplayer
Requires:       %{name} = %{version}
Recommends:     ffmpeg
%if %qtversion >= 40800
Recommends:     %{name}-vrooby = %{version}
%endif

%description lmp
This package provides a audio player plugin for LeechCraft.

It allows to play audio and stream audio.
It uses Phonon as a backend thus supporting major codecs.

Features
 * Support for major audio formats.
 * Streaming media over Internet.
 * Play queue.
 * Support for automatic podcast playing (with a plugin like Aggregator).


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

%package poshuku
Summary:        LeechCraft Web Browser Module
Group:          Productivity/Networking/Other
Provides:       %{name}-webbrowser
Requires:       %{name} = %{version}
Obsoletes:      poshuku-wyfv

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


%package poshuku-cleanweb
Summary:        LeechCraft Poshuku - Ad Filter Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku

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


%package poshuku-pogooglue
Summary:        LeechCraft Poshuku - quick google search Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-pogooglue
This package provides an instant search plugin for LeechCraft Poshuku.

It allows to search instantly selected text in Google.


%package poshuku-keywords
Summary:        LeechCraft Poshuku - Support of url keywords Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-keywords
This package contains a plugin for supporting url keywords for LeechCraft
Poshuku browser


%package poshuku-onlinebookmarks
Summary:        LeechCraft Poshuku - Online Bookmarks Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}
Requires:       %{name}-securestorage

%description poshuku-onlinebookmarks
This package provides an online bookmarks plugin for LeechCraft Poshuku.

It allows to synchronize bookmarks with services like Read It Later
or Del.icio.us.


%package poshuku-delicious
Summary:        LeechCraft Poshuku - Onlinebookmarks Delicious Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}

%description poshuku-delicious
This package contains a plugin for LeechCraft Poshuku Online Bookmarks.

It provides support for the the Del.icio.us service.


%package poshuku-readitlater
Summary:        LeechCraft Poshuku - Onlinebookmarks ReadItLater Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}

%description poshuku-readitlater
This package contains a plugin for LeechCraft Poshuku Online Bookmarks.

It provides support for the Read it Later service.


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


%package summary
Summary:        LeechCraft Summary info Module
Group:          Productivity/Networking/Other
Provides:       %{name}-summaryrepresentation
Requires:       %{name} = %{version}

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


%package shellopen
Summary:        LeechCraft Shellopen Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description shellopen
This package provides an opening files with external apps for LeechCraft.

It allows to open files and handle entities with external applications.
For example, you may choose to open a video file with your favorite media
player instead of LC's one.


%package secman
Summary:        LeechCraft Security manager Module
Group:          Productivity/Networking/Other
Provides:       %{name}-securestorage
Requires:       %{name} = %{version}
Requires:       %{name}-secman-simplestorage = %{version}

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


%package azoth
Summary:        LeechCraft Instant messenger Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-azoth-chatstyler = %{version}
Requires:       %{name}-securestorage = %{version}

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

%if 0%{suse_version} <= 1210
%package azoth-doc
Summary:        LeechCraft Azoth Documentation
Group:          Development/Libraries/Other
BuildArch:      noarch

%description azoth-doc
This packages provides documentation of LeechCraft Azoth API.

It contains description of Azoth API used for developing LeechCraft
Azoth sub-plugins. For developing first-lexel plugins, please refer
to corresponding packages (like leechcraft-doc). This documentation
is also available online at http://doc.leechcraft.org/azoth/
%endif


%package azoth-acetamide
Summary:        LeechCraft Azoth - IRC Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-acetamine = %{version}
Obsoletes:      %{name}-acetamine < %{version}

%description azoth-acetamide
This package provides an IRC protocol plugin for LeechCraft Azoth.

Features:
 * Secure Sockets Layer (SSL) cryptographic protocol.
 * Channels bookmarks.
 * Automatic password entry.
 * Automatic logging on.


%package azoth-chathistory
Summary:        LeechCraft Azoth - Chat history Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

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


%package azoth-autopaste
Summary:        LeechCraft Azoth - Autopaste Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-autopaste
This package provides an autopaste plugin for LeechCraft Azoth.

It allows to paste long messages to pastebins automatically.


%package azoth-embedmedia
Summary:        LeechCraft Azoth - Media Objects Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-embedmedia
This package provides a embedding media plugin for LeechCraft Azoth.

It allows to enable embedding different media objects in chat tabs.


%package azoth-hili
Summary:        LeechCraft Azoth - Conference highlights Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-hili
This package provides a highlights customizing plugin for LeechCraft Azoth.

It allows to customize conference highlights.


%package azoth-juick
Summary:        LeechCraft Azoth - Juick.com service Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-juick
This package contains a juick.com plugin for LeechCraft Azoth.

It provides the enhanced experience with the juick.com microblogging service.


%package azoth-nativeemoticons
Summary:        LeechCraft Azoth - Emoticons packs
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-nativeemoticons
This package provides an emoticons plugin for LeechCraft Azoth.

It allows to use emoticons packs in Psi+, Kopete and own format.


%package azoth-p100q
Summary:        LeechCraft Azoth - Psto.net service Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-p100q
This package contains a psto.net plugin for LeechCraft Azoth.

It provides the enhanced experience with the psto.net microblogging service.


%package azoth-standardstyles
Summary:        LeechCraft Azoth - Standard chat styles Module
Group:          Productivity/Networking/Other
Provides:       %{name}-azoth-chatstyler
Requires:       %{name}-azoth = %{version}

%description azoth-standardstyles
This package provides an standard styles support plugin for LeechCraft Azoth.

Standard styles are ones in LeechCraft's own format.


%package azoth-xoox
Summary:        LeechCraft Azoth - XMPP Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

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


%package azoth-keeso
Summary:        LeechCraft Azoth - Text transform Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-keeso
This package contains text transform plugin for LeechCraft Azoth Module.


%package azoth-zheet
Summary:        LeechCraft Azoth - MSN Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

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


%package azoth-vader
Summary:        LeechCraft Azoth - MrIM Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

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


%package azoth-xtazy
Summary:        LeechCraft Azoth - Publishing current user tune Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-xtazy
This package provides a tune publishing plugin for LeechCraft Azoth.

It allows to publish current user tune.


%package azoth-depester
Summary:        LeechCraft Azoth - Ignore Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-depester
This package provides an ignoring plugin for LeechCraft Azoth.

It allows to ignore unwanted participants.


%package azoth-herbicide
Summary:        LeechCraft Azoth - Antispam Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-herbicide
This package contains a basic antispam plugin for LeechCraft Azoth.


%package azoth-rosenthal
Summary:        LeechCraft Azoth - Spell Checker Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-rosenthal
This package provides a spell checker plugin for LeechCraft Azoth.

It is based on Hunspell or Myspell dictionaries.


%package azoth-lastseen
Summary:        LeechCraft Azoth - Contact last seen time Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-lastseen
This package provides a LastSeen plugin for LeechCraft Azoth.

It allows to record of contacts' last online and availability time at
client's side. It doesn't depend on the concrete protocol implementation.


%package azoth-adiumstyles
Summary:        LeechCraft Azoth - Adium Styles Module
Group:          Productivity/Networking/Other
Provides:       %{name}-azoth-chatstyler
Requires:       %{name}-azoth = %{version}

%description azoth-adiumstyles
Azoth AdiumStyles for, well, support Adium styles for LeechCraft Azoth.


%package azoth-autoidler
Summary:        LeechCraft Azoth - Automatic Change of Status Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-autoidler
This package provides a status changing plugin for LeechCraft Azoth.

It allows to automatically change of status due to inactivity period.


%package azoth-metacontacts
Summary:        LeechCraft Azoth - Metacontacts Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-metacontacts
This package provides a metacontacts support plugin for LeechCraft Azoth.


%package azoth-isterique
Summary:        LeechCraft Azoth - Isterique Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-isterique
This package provides a CAPS removing plugin for LeechCraft Azoth.

It allows to remove excessive CAPS usage from incoming messages.


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


%package bittorrent
Summary:        LeechCraft BitTorrent client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

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


%package advancednotifications
Summary:        LeechCraft Notifications framework Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-visualnotifications = %{version}

%description advancednotifications
This package provides an advanced notifications plugin for Leechcraft.

It allows to customize notifications better.


%package glance
Summary:        LeechCraft Opened tabs overview Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description glance
This package provides a tabs overview plugin for Leechcraft.

It allows to show the thumbnailed grid overview of tabs.


%package tabslist
Summary:        LeechCraft TabsList Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description tabslist
This package provides a tabs list plugin for Leechcraft.

It allows to show the list of currently opened tabs
and allows to quickly navigate between them.


%package gmailnotifier
Summary:        LeechCraft GMail notifier Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}

%description gmailnotifier
This package provides a GMail notifications plugin for Leechcraft.

It allows to get notifications about new mail in your GMail account.

It has configurable frequency of the updates and the number of last unread
messages shown.


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


%package syncer
Summary:        LeechCraft Sync setting Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description syncer
This package provides a synchronizing plugin for Leechcraft.

It allows to synchronize data and settings between LeechCraft instances
running on different machines.


%package lhtr
Summary:        LeechCraft HTML WYSIWYG editor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description lhtr
This package provides a HTML WYSIWYG editor plugin for Leechcraft.

It can be usable with mail and blog modules.


%package knowhow
Summary:        LeechCraft Tips of the day Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description knowhow
This package provides a tips plugin for LeechCraft.
 
It allows to display tips of the day window after launch LeechCraft.


%package choroid
Summary:        LeechCraft Image viewer Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description choroid
This package provides an image viewer plugin for LeechCraft.


%package anhero
Summary:        LeechCraft Crash handler Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       kdebase4-runtime

%description anhero
This package provides a crash handler plugin for LeechCraft.
 
It uses KDE utils to handle crashes, show backtraces and aid
in sending bug reports.

KDE should not be running for AnHero to work.

%package netstoremanager
Summary:        LeechCraft Network file storages Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description netstoremanager
This package provides a network storage plugin for Leechcraft.

It allows to manage network storages like Yandex.Disk.
It is modular, so different storages can be added to it
without modifying the plugin itself.

Features:
 * Upload files easily from LeechCraft.
 * Maintain the list of uploaded files.
 * Delete the uploaded files (if supported by service).
 * Support for prolongating uploaded files (if supported by service).

Supported services:
 * Yandex.Disk


%package dolozhee
Summary:        LeechCraft Issue reporting Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-secman = %{version}

%description dolozhee
This package provides a Dolozhee plugin for LeechCraft.

It allows to quickly and easily submit bug reports
and feature requests to LeechCraft issues tracker.


%package kbswitch
Summary:        LeechCraft keyboard switcher Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-keyboardcraft = %{version}
Obsoletes:      %{name}-keyboardcraft < %{version}

%description kbswitch
This module allow change keyboard layouts from LeechCraft


%package xproxy
Summary:        LeechCraft Proxy manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description xproxy
This package provides an advanced proxy manager for LeechCraft.

It allows to configure and use proxy servers.


%package gacts
Summary:        LeechCraft Global actions Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description gacts
This package provides a global shortcut manager for LeechCraft.

It allows to set and use global hotkeys.


%package pintab
Summary:        LeechCraft Pinning tabs Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-poshuku-pintab = %{version}
Obsoletes:      %{name}-poshuku-pintab < %{version}

%description pintab
This package provides a pinning tab module for LeechCraft.


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


%package sidebar
Summary:        LeechCraft Sidebar Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description sidebar
This package provides a side bar plugin for Leechcraft.

It is a nice side bar with quick launch, tabs and tray areas.


%if %qtversion >= 40800
%package otlozhu
Summary:        LeechCraft ToDo manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description otlozhu
This package provides a ToDo manager plugin for LeechCraft.

It is a GTD-inspired ToDo manager.


%package monocle
Summary:        LeechCraft Document viewer Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description monocle
This package provides a modular Document viewer plugin for LeechCraft.

It will support different formats via different backends.


%package monocle-pdf
Summary:        LeechCraft Monocle - PDF Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}

%description monocle-pdf
This package contains a pdf subplugin for LeechCraft Monocle.

This package provides PDF documents support for Document viewer Module
via the Poppler backend.

%package monocle-fxb
Summary:        LeechCraft Monocle - FictionBook Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}

%description monocle-fxb
This package contains a FictionBook subplugin for LeechCraft Monocle.

This package provides FB2 documents support for Document viewer Module.


%package vrooby
Summary:        LeechCraft Removable storage devices Manager
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       udisks

%description vrooby
This package provides a Vrooby plugin for LeechCraft.

It allows to watch removable storage devices via d-bus and udisks.
%endif


%package nacheku
Summary:        LeechCraft Link watcher Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description nacheku
This package provides a Nacheku plugin for LeechCraft.

It allows to watch clipboard and directory in order to
get links and download files.


%prep
%setup -q -n %{name}-%{version}

#%%patch1
%if 0%{suse_version} > 1140
%patch2
%endif
%patch3
%if 0%{suse_version} > 1210
%patch4
%endif

#removing non-free icons
rm -rf src/plugins/azoth/share/azoth/iconsets/clients/default

#removing hidden files
find src/plugins/azoth/plugins/adiumstyles/share/azoth/styles/adium/ -name ".?*" -delete

mkdir build && cd build

cmake ../src \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DENABLE_ADVANCEDNOTIFICATIONS=True \
        -DENABLE_AZOTH=True \
        -DENABLE_EISKALTDCPP=False \
        -DENABLE_GLANCE=True \
        -DENABLE_GMAILNOTIFIER=True \
        -DENABLE_LACKMAN=True \
        -DENABLE_POPISHU=True \
        -DENABLE_SECMAN=True \
        -DENABLE_SHELLOPEN=True \
        -DENABLE_SYNCER=True \
        -DENABLE_TABSLIST=True \
        -DENABLE_VFSCORE=False \
        -DENABLE_QROSP=False \
        -DENABLE_KNOWHOW=True \
        -DENABLE_MEDIACALLS=False \
        -DENABLE_BLACKDASH=False \
        -DENABLE_FTP=False \
        -DENABLE_CHOROID=True \
        -DENABLE_SIDEBAR=True \
        -DENABLE_SNAILS=False \
        -DENABLE_TABSESSMANAGER=True \
        -DENABLE_AZOTH_ZHEET=True \
        -DENABLE_AZOTH_ASTRALITY=False \
        -DENABLE_LIZNOO=False \
        -DENABLE_NETSTOREMANAGER=True \
        -DENABLE_PINTAB=True \
        -DENABLE_GACTS=True \
        -DENABLE_KBSWITCH=True \
        -DENABLE_BLOGIQUE=False \
        -DENABLE_DOLOZHEE=True \
        -DENABLE_LMP=True \
        -DENABLE_NEWLIFE=True \
        -DENABLE_NACHEKU=True \
        -DENABLE_LADS=False \
        -DENABLE_LEMON=False \
        -DENABLE_TWIFEE=False \
%if %qtversion >= 40800
        -DENABLE_OTLOZHU=True \
        -DENABLE_MONOCLE=True \
        -DENABLE_VROOBY=True \
%else
        -DENABLE_OTLOZHU=False \
        -DENABLE_MONOCLE=False \
        -DENABLE_VROOBY=False \
%endif
        -DLEECHCRAFT_VERSION=%{version}

%build
cd build
make %{?_smp_mflags}

%if 0%{suse_version} <= 1210
cd ../doc/doxygen/core
sed -i Doxyfile \
-e "s/PROJECT_NUMBER .*/PROJECT_NUMBER         = %{LEECHCRAFT_VERSION}/"
doxygen Doxyfile

cd ../azoth
sed -i Doxyfile \
-e "s/PROJECT_NUMBER .*/PROJECT_NUMBER         = %{LEECHCRAFT_VERSION}/"
doxygen Doxyfile
%endif

%install
cd build
%makeinstall

%if 0%{suse_version} <= 1210
cd ../doc/doxygen/core/out/html
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
cp -r * %{buildroot}%{_docdir}/%{name}-doc

cd ../../../azoth/out/html
mkdir -p %{buildroot}%{_docdir}/%{name}-azoth-doc
cp -r * %{buildroot}%{_docdir}/%{name}-azoth-doc
%endif

%suse_update_desktop_file -i %{name}

%fdupes -s %{buildroot}%{_datadir}/%{name}/translations
%fdupes -s %{buildroot}%{_datadir}/%{name}/azoth
%if 0%{suse_version} <= 1210
%fdupes -s %{buildroot}%{_docdir}/%{name}-doc/
%fdupes -s %{buildroot}%{_docdir}/%{name}-azoth-doc/
%endif
#%%fdupes -s %%{buildroot}%%{_datadir}/icons/oxygen

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-add-file
%{settings_dir}/coresettings.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%dir %{_datadir}/icons/hicolor/14x14
%dir %{_datadir}/icons/hicolor/14x14/apps
%dir %{_datadir}/%{name}
#%%dir %%{_datadir}/%%{name}/icons
%dir %{_datadir}/%{name}/installed
%dir %{settings_dir}
%dir %{translations_dir}
%dir %{_datadir}/%{name}/scripts
%dir %{_datadir}/%{name}/qml
%{translations_dir}/leechcraft_??.qm
%{translations_dir}/leechcraft_??_??.qm
%dir %{_libdir}/%{name}
%dir %{plugin_dir}
%{_libdir}/*lcutil.so.*
%{_libdir}/*xmlsettingsdialog.so.*
%doc %{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}/sounds
%exclude %{_datadir}/cmake/Modules/InitLCPlugin.cmake

%if 0%{suse_version} <= 1210
%files doc
%defattr(-,root,root)
%dir %{_docdir}/%{name}-doc
%doc %{_docdir}/%{name}-doc/*
%exclude %{_docdir}/%{name}-doc/installdox

%files azoth-doc
%defattr(-,root,root)
%dir %{_docdir}/%{name}-azoth-doc
%doc %{_docdir}/%{name}-azoth-doc/*
%exclude %{_docdir}/%{name}-azoth-doc/installdox
%endif

%files advancednotifications
%defattr(-,root,root)
%{plugin_dir}/*%{name}_advancednotifications.so
%{translations_dir}/leechcraft_advancednotifications*
%{settings_dir}/advancednotificationssettings.xml
%{_datadir}/%{name}/qml/advancednotifications

%files bittorrent
%defattr(-,root,root)
%{settings_dir}/torrentsettings.xml
%{translations_dir}/%{name}_bittorrent_*.qm
%{plugin_dir}/*%{name}_bittorrent.so

%files aggregator
%defattr(-,root,root)
%{settings_dir}/aggregatorsettings.xml
%{translations_dir}/%{name}_aggregator*.qm
%{plugin_dir}/*%{name}_aggregator.so
%{_datadir}/%{name}/scripts/aggregator/

%files aggregator-bodyfetch
%defattr(-,root,root)
%{plugin_dir}/*%{name}_aggregator_bodyfetch.so

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

%files azoth-acetamide
%defattr(-,root,root)
%{settings_dir}/azothacetamidesettings.xml
%{translations_dir}/%{name}_azoth_acetamide*
%{plugin_dir}/*%{name}_azoth_acetamide.so

%files azoth-autopaste
%defattr(-,root,root)
%{settings_dir}/azothautopastesettings.xml
%{translations_dir}/%{name}_azoth_autopaste*
%{plugin_dir}/*%{name}_azoth_autopaste.so

%files azoth-chathistory
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_chathistory*
%{plugin_dir}/*%{name}_azoth_chathistory.so

%files azoth-embedmedia
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_embedmedia.so

%files azoth-hili
%defattr(-,root,root)
%{settings_dir}/azothhilisettings.xml
%{translations_dir}/%{name}_azoth_hili*
%{plugin_dir}/*%{name}_azoth_hili.so

%files azoth-juick
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_juick.so

%files azoth-nativeemoticons
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_nativeemoticons.so

%files azoth-p100q
%defattr(-,root,root)
%{settings_dir}/azothp100qsettings.xml
%{plugin_dir}/*%{name}_azoth_p100q.so
%{translations_dir}/leechcraft_azoth_p100q*

%files azoth-standardstyles
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_standardstyles.so
%{_datadir}/%{name}/azoth/styles/standard/

%files azoth-xoox
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_xoox*
%{plugin_dir}/*%{name}_azoth_xoox.so

%files azoth-xtazy
%defattr(-,root,root)
%{settings_dir}/azothxtazysettings.xml
%{plugin_dir}/*%{name}_azoth_xtazy.so
%{translations_dir}/%{name}_azoth_xtazy*

%files azoth-depester
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_depester.so
%{translations_dir}/%{name}_azoth_depester*

%files azoth-herbicide
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_herbicide.so
%{translations_dir}/%{name}_azoth_herbicide*
%{settings_dir}/azothherbicidesettings.xml

%files azoth-rosenthal
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_rosenthal.so
%{translations_dir}/%{name}_azoth_rosenthal*
%{settings_dir}/azothrosenthalsettings.xml

%files azoth-adiumstyles
%defattr(644,root,root,755)
%{plugin_dir}/*%{name}_azoth_adiumstyles*
%{_datadir}/%{name}/azoth/styles/adium

%files azoth-autoidler
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_autoidler*
%{settings_dir}/azothautoidlersettings.xml
%{translations_dir}/leechcraft_azoth_autoidler*

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

%files azoth-isterique
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_isterique*
%{settings_dir}/azothisteriquesettings.xml
%{translations_dir}/leechcraft_azoth_isterique*

%files azoth-zheet
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_zheet*
%{plugin_dir}/*%{name}_azoth_zheet.so

%files azoth-vader
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_vader*
%{_datadir}/%{name}/settings/azothvadersettings.xml
%{plugin_dir}/*%{name}_azoth_vader.so

%files azoth-keeso
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_keeso.so

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
%{settings_dir}/deadlyricssettings.xml
%{translations_dir}/%{name}_deadlyrics*.qm
%{plugin_dir}/*%{name}_deadlyrics.so

%files devel
%defattr(-,root,root)
%{_datadir}/%{name}/cmake
%{_includedir}/%{name}
%{_libdir}/*lcutil.so
%{_libdir}/*xmlsettingsdialog.so
%{_datadir}/cmake/Modules/InitLCPlugin.cmake

%files historyholder
%defattr(-,root,root)
%{plugin_dir}/*leechcraft_historyholder.so
%{translations_dir}/leechcraft_historyholder*.qm

%files kinotify
%defattr(-,root,root)
%{_datadir}/%{name}/kinotify
%{settings_dir}/kinotifysettings.xml
%{plugin_dir}/*%{name}_kinotify.so

%files lmp
%defattr(-,root,root)
%{settings_dir}/lmpsettings.xml
%{translations_dir}/%{name}_lmp*
%{plugin_dir}/*%{name}_lmp.so
%{plugin_dir}/*%{name}_lmp_dumbsync.so

%files networkmonitor
%defattr(-,root,root)
%{translations_dir}/%{name}_networkmonitor*.qm
%{plugin_dir}/*%{name}_networkmonitor.so

%files newlife
%defattr(-,root,root)
%{translations_dir}/%{name}_newlife*.qm
%{plugin_dir}/*%{name}_newlife.so

%files poshuku-cleanweb
%defattr(-,root,root)
%{settings_dir}/poshukucleanwebsettings.xml
%{translations_dir}/%{name}_poshuku_cleanweb*.qm
%{plugin_dir}/*%{name}_poshuku_cleanweb.so

%files poshuku-filescheme
%defattr(-,root,root)
%{translations_dir}/%{name}_poshuku_filescheme_*.qm
%{plugin_dir}/*%{name}_poshuku_filescheme.so

%files poshuku-keywords
%defattr(-,root,root,-)
%{plugin_dir}/*%{name}_poshuku_keywords.so
%{settings_dir}/poshukukeywordssettings.xml

%files poshuku-fua
%defattr(-,root,root)
%{settings_dir}/poshukufuasettings.xml
%{translations_dir}/%{name}_poshuku_fua*.qm
%{plugin_dir}/*%{name}_poshuku_fua.so

%files popishu
%defattr(-,root,root)
%{settings_dir}/popishusettings.xml
%{translations_dir}/%{name}_popishu_*.qm
%{plugin_dir}/*%{name}_popishu.so

%files poshuku
%defattr(-,root,root)
%{_datadir}/%{name}/installed/poshuku/
%{settings_dir}/poshukusettings.xml
%{translations_dir}/%{name}_poshuku_??.qm
%{translations_dir}/%{name}_poshuku_??_??.qm
%{plugin_dir}/*%{name}_poshuku.so

%files poshuku-fatape
%defattr(-,root,root)
%{settings_dir}/poshukufatapesettings.xml
%{plugin_dir}/*%{name}_poshuku_fatape.so
%{translations_dir}/leechcraft_poshuku_fatape_*.qm

%files poshuku-pogooglue
%defattr(-,root,root)
%{plugin_dir}/*%{name}_poshuku_pogooglue*
%{translations_dir}/leechcraft_poshuku_pogooglue*

%files poshuku-onlinebookmarks
%defattr(-,root,root)
%{settings_dir}/poshukuonlinebookmarkssettings.xml
%{translations_dir}/%{name}_poshuku_onlinebookmarks*.qm
%{plugin_dir}/*%{name}_poshuku_onlinebookmarks.so

%files poshuku-delicious
%defattr(-,root,root)
%{plugin_dir}/*%{name}_poshuku_onlinebookmarks_delicious*

%files poshuku-readitlater
%defattr(-,root,root)
%{plugin_dir}/*%{name}_poshuku_onlinebookmarks_readitlater.*

%files secman
%defattr(-,root,root)
%{plugin_dir}/*%{name}_secman.so

%files secman-simplestorage
%defattr(-,root,root)
%{plugin_dir}/*%{name}_secman_simplestorage.so

%files seekthru
%defattr(-,root,root)
%{settings_dir}/seekthrusettings.xml
%{translations_dir}/%{name}_seekthru*.qm
%{plugin_dir}/*%{name}_seekthru.so

%files shellopen
%defattr(-,root,root)
%{translations_dir}/%{name}_shellopen*.qm
%{plugin_dir}/*%{name}_shellopen.so

%files summary
%defattr(-,root,root)
%{translations_dir}/%{name}_summary*.qm
%{plugin_dir}/*%{name}_summary.so

#%%files tabpp
#%%defattr(-,root,root)
#%%{settings_dir}/tabppsettings.xml
#%%{translations_dir}/%%{name}_tabpp_*.qm
#%%{plugin_dir}/*%%{name}_tabpp.so

%files vgrabber
%defattr(-,root,root)
%{settings_dir}/vgrabbersettings.xml
%{translations_dir}/%{name}_vgrabber*.qm
%{plugin_dir}/*%{name}_vgrabber.so

%files glance
%defattr(-,root,root)
%{plugin_dir}/*%{name}_glance.so
%{translations_dir}/leechcraft_glance*

%files tabslist
%defattr(-,root,root)
%{plugin_dir}/*%{name}_tabslist.so
%{translations_dir}/leechcraft_tabslist*

%files anhero
%defattr(-,root,root)
%{plugin_dir}/*%{name}_anhero.so
%{translations_dir}/leechcraft_anhero*

%files gmailnotifier
%defattr(-,root,root)
%{plugin_dir}/*%{name}_gmailnotifier.so
%{settings_dir}/gmailnotifiersettings.xml
%{translations_dir}/leechcraft_gmailnotifier*

%files lackman
%defattr(-,root,root)
%{plugin_dir}/*%{name}_lackman.so
%{settings_dir}/lackmansettings.xml
%{translations_dir}/leechcraft_lackman*

%files syncer
%defattr(-,root,root)
%{plugin_dir}/*%{name}_syncer.so
%{settings_dir}/syncersettings.xml
%{translations_dir}/leechcraft_syncer*

%files knowhow
%defattr(-,root,root)
%{_datadir}/%{name}/knowhow
%{plugin_dir}/*%{name}_knowhow.so
%{settings_dir}/knowhowsettings.xml

%files tabsessionmanager
%defattr(-,root,root)
%{plugin_dir}/*%{name}_tabsessmanager.so
%{_datadir}/%{name}/translations/%{name}_tabsessmanager_*.qm

%files sidebar
%defattr(-,root,root)
%{plugin_dir}/*%{name}_sidebar.so

%files choroid
%defattr(-,root,root)
%{plugin_dir}/*%{name}_choroid.so
%{_datadir}/%{name}/qml/choroid

%files netstoremanager
%defattr(-,root,root)
%{plugin_dir}/*%{name}_netstoremanager.so
%{_libdir}/%{name}/plugins/lib%{name}_netstoremanager_yandexdisk.so
%{_datadir}/%{name}/settings/netstoremanagersettings.xml
%{_datadir}/%{name}/translations/%{name}_netstoremanager_*.qm

%files lhtr
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_lhtr.so
%{_datadir}/%{name}/translations/%{name}_lhtr_*.qm

%files pintab
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_pintab.so
%{_datadir}/%{name}/translations/%{name}_pintab_*.qm

%files gacts
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_gacts.so

%files dolozhee
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_dolozhee.so
%{_datadir}/%{name}/translations/%{name}_dolozhee_*.qm

%files kbswitch
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_kbswitch.so
%{_datadir}/%{name}/settings/kbswitchsettings.xml

%files xproxy
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_xproxy.so
%{_datadir}/%{name}/settings/xproxysettings.xml
%{_datadir}/%{name}/translations/%{name}_xproxy_*.qm

%if %qtversion >= 40800
%files otlozhu
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_otlozhu.so
%{_datadir}/%{name}/translations/%{name}_otlozhu_*.qm

%files monocle
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle.so
%{_datadir}/%{name}/translations/%{name}_monocle_*.qm
%{_datadir}/%{name}/settings/monoclesettings.xml

%files monocle-pdf
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_pdf.so

%files monocle-fxb
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_fxb.so

%files vrooby
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_vrooby.so
%{_datadir}/%{name}/translations/%{name}_vrooby_*.qm
%endif

%files nacheku
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_nacheku.so
%{_datadir}/%{name}/settings/nachekusettings.xml

%changelog