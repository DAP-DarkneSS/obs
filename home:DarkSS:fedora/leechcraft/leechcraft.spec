#
# spec file for package leechcraft
#
# Copyright (c) 2013 LeechCraft Team.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://dev.leechcraft.org/
#

%define plugin_dir %{_libdir}/%{name}/plugins
%define translations_dir %{_datadir}/%{name}/translations
%define settings_dir %{_datadir}/%{name}/settings
%define azoth_dir %{_datadir}/%{name}/azoth

Name:           leechcraft
Version:        git
%define LEECHCRAFT_VERSION 0.5.95-917-g6de7c63
Release:        0
License:        BSL-1.0
Summary:        Modular Internet Client
Url:            http://leechcraft.org
Group:          Productivity/Networking/Other
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  cmake > 2.8
BuildRequires:  file-devel
BuildRequires:  gcc-c++ >= 4.6
BuildRequires:  hicolor-icon-theme
BuildRequires:  hunspell-devel
BuildRequires:  GeoIP-devel
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  bzip2-devel
BuildRequires:  libcurl-devel
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  liblastfm-devel
BuildRequires:  libmsn-devel
BuildRequires:  libnl3-devel
BuildRequires:  libotr
BuildRequires:  libotr-devel
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(poppler-qt4)
BuildRequires:  libpurple-devel
BuildRequires:  libtidy-devel
BuildRequires:  pkgconfig(qca2)
BuildRequires:  pkgconfig(QJson)
BuildRequires:  qscintilla-devel
BuildRequires:  pkgconfig(QtCore) >= 4.8
BuildRequires:  pkgconfig(qxmpp) >= 0.7.4
BuildRequires:  lm_sensors-devel
BuildRequires:  libspectre-devel
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 0.15.6
%ifarch i586 i686
BuildRequires:  mupdf-devel
%endif
BuildRequires:  pcre-devel
BuildRequires:  phonon-devel
BuildRequires:  qwt-devel
BuildRequires:  speex-devel
BuildRequires:  taglib-devel
BuildRequires:  xz
BuildRequires:  telepathy-qt4-devel

BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrender-devel
BuildRequires:  libjpeg-devel

Requires:       oxygen-icon-theme

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


%package advancednotifications
Summary:        LeechCraft Notifications framework Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-visualnotifications = %{version}

%description advancednotifications
This package provides an advanced notifications plugin for Leechcraft.

It allows to customize notifications better.


%package aggregator
Summary:        LeechCraft RSS/Atom Aggregator Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}

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


%package anhero
Summary:        LeechCraft Crash handler Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       gdb

%description anhero
This package provides a crash handler plugin for LeechCraft.


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


%package azoth-acetamide
Summary:        LeechCraft Azoth - IRC Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-acetamine = %{version}
Obsoletes:      %{name}-acetamine < %{version}
Provides:       %{name}-azoth-protocolplugin

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


%package azoth-p100q
Summary:        LeechCraft Azoth - Psto.net service Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-p100q
This package contains a psto.net plugin for LeechCraft Azoth.

It provides the enhanced experience with the psto.net microblogging service.


%package azoth-rosenthal
Summary:        LeechCraft Azoth - Spell Checker Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

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


%package azoth-xoox
Summary:        LeechCraft Azoth - XMPP Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin

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


%package blogique
Summary:        LeechCraft Blogging client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blogique-subplugin = %{version}
Requires:       %{name}-lhtr = %{version}

%description blogique
This package provides a modular Blogging client plugin for LeechCraft.

It will support different blogging platforms via different submodules.


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
Provides:       %{name}-blogique-subplugin = %{version}

%description blogique-metida
This package provides a LiveJournal subplugin for LeechCraft Blogique.

It provides LiveJournal support.


%package choroid
Summary:        LeechCraft Image viewer Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description choroid
This package provides an image viewer plugin for LeechCraft.


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

%description deadlyrics
This package provides a lyrics finder plugin for LeechCraft.

It is a simple client for searching song lyrics on various sites.
The search interface is available via LeechCraft Summary.


%package devel
Summary:        LeechCraft Development Files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package provides files required for development for LeechCraft.

It contains header files required to develop new modules.


%package dolozhee
Summary:        LeechCraft Issue reporting Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description dolozhee
This package provides a Dolozhee plugin for LeechCraft.

It allows to quickly and easily submit bug reports
and feature requests to LeechCraft issues tracker.


%package dumbeep
Summary:        LeechCraft DumBeep Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-soundnotifications = %{version}

%description dumbeep
This package provides a dumb sound notifier plugin for LeechCraft.

It also uses Phonon as a backend or something like aplay/mplayer.


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

%description gmailnotifier
This package provides a GMail notifications plugin for Leechcraft.

It allows to get notifications about new mail in your GMail account.

It has configurable frequency of the updates and the number of last unread
messages shown.


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
Provides:       %{name}-keyboardcraft = %{version}
Obsoletes:      %{name}-keyboardcraft < %{version}

%description kbswitch
This module allow change keyboard layouts from LeechCraft


%package kinotify
Summary:        LeechCraft Kinetic notifications Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-visualnotifications

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

%description lhtr
This package provides a HTML WYSIWYG editor plugin for Leechcraft.

It can be usable with mail and blog modules.


%package liznoo
Summary:        LeechCraft Power managment module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       upower

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


%package lmp
Summary:        LeechCraft Media player Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-audioplayer
Provides:       %{name}-soundnotifications = %{version}

%description lmp
This package provides a audio player plugin for LeechCraft.

It allows to play audio and stream audio.
It uses Phonon as a backend thus supporting major codecs.

Features:
 * Support for major audio formats.
 * Streaming media over Internet.
 * Play queue.
 * Support for automatic podcast playing (with a plugin like Aggregator).


%package lmp-dumbsync
Summary:        LeechCraft Media syncing Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-dumbsync
This package provides a audio syncing plugin for LeechCraft.

It allows to sync with Flash-like media players.


%package lmp-graffiti
Summary:        LeechCraft Tags Manipulating Module
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-graffiti
This package provides a tags editor plugin for LeechCraft.

It allows to manipulate audio file tags.


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


%package mellonetray
Summary:        LeechCraft Tray Area Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description mellonetray
This package provides a tray area quark for third-party apps
for LeechCraft SB2.


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


%ifarch i586 i686
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
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-postrus
This package contains a PostRus subplugin for LeechCraft Monocle.

This package provides PostScript documents support for Document viewer Module
via the libSpectre backend.


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


%package musiczombie
Summary:        LeechCraft Azoth - MusicBrainz.org client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-lmp = %{version}

%description musiczombie
This package provides a MusicBrainz.org client plugin for LeechCraft.


%package nacheku
Summary:        LeechCraft Link watcher Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description nacheku
This package provides a Nacheku plugin for LeechCraft.

It allows to watch clipboard and directory in order to
get links and download files.


%package netstoremanager
Summary:        LeechCraft Network file storages Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-netstoremanager-subplugin
Obsoletes:      %{name}-netstoremanager-yandexdisk

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


%package netstoremanager-googledrive
Summary:        LeechCraft Network file storages Module
Group:          Productivity/Networking/Other
Requires:       %{name}-netstoremanager = %{version}
Provides:       %{name}-netstoremanager-subplugin

%description netstoremanager-googledrive
This package provides a Google Drive sunplugin for Leechcraft NetStoreManager.


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
Provides:       %{name}-poshuku-pintab = %{version}
Obsoletes:      %{name}-poshuku-pintab < %{version}

%description pintab
This package provides a pinning tab module for LeechCraft.

It allows to pin important tabs so that they occupy less space.


%package pogooglue
Summary:        LeechCraft Poshuku - quick google search Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Obsoletes:      %{name}-poshuku-pogooglue < %{version}
Provides:       %{name}-poshuku-pogooglue = %{version}

%description pogooglue
This package provides an instant search plugin for LeechCraft.

It allows to search instantly selected text in Google.


%package poleemery
Summary:        LeechCraft Poleemery - Finances manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description poleemery
This package provides a personal finances manager plugin for LeechCraft.


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


%package poshuku
Summary:        LeechCraft Web Browser Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-webbrowser

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
Requires:       %{name}-poshuku

%description poshuku-autosearch
This package provides an autosearch plugin for LeechCraft Poshuku.


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
Obsoletes:      %{name}-delicious < %{version}
Provides:       %{name}-delicious = %{version}

%description poshuku-onlinebookmarks-delicious
This package contains a plugin for LeechCraft Poshuku Online Bookmarks.

It provides support for the the Del.icio.us service.


%package poshuku-onlinebookmarks-readitlater
Summary:        LeechCraft Poshuku - Onlinebookmarks ReadItLater Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}
Obsoletes:      %{name}-readitlater < %{version}
Provides:       %{name}-readitlater = %{version}

%description poshuku-onlinebookmarks-readitlater
This package contains a plugin for LeechCraft Poshuku Online Bookmarks.

It provides support for the Read it Later service.


%package sb2
Summary:        LeechCraft SideBar2 Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sb = %{version}
Obsoletes:      %{name}-sidebar < %{version}
Provides:       %{name}-sidebar = %{version}

%description sb2
This package provides another side bar plugin for Leechcraft.

It is a next-gen fluid sidebar with quick launch, tabs and tray areas.


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


%package shaitan
Summary:        LeechCraft Shaitan Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       xterm

%description shaitan
This package provides a terminal plugin for Leechcraft.


%package shellopen
Summary:        LeechCraft Shellopen Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description shellopen
This package provides an opening files with external apps for LeechCraft.

It allows to open files and handle entities with external applications.
For example, you may choose to open a video file with your favorite media
player instead of LC's one.


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


%package vrooby
Summary:        LeechCraft Removable storage devices Manager
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb = %{version}

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
Summary:        LeechCraft - Current user tune Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}


%description xtazy
This package provides a tune wrapper plugin for LeechCraft.

It allows to get current user tune via mpris protocol.


%prep
%setup -q -n %{name}-%{version}

#removing non-free icons
rm -rf src/plugins/azoth/share/azoth/iconsets/clients/default

#removing hidden files
find src/plugins/azoth/plugins/adiumstyles/share/azoth/styles/adium/ -name ".?*" -delete

#setup permissions correctly to avoid false duplicates reported by rpmlint (bnc#784670)
find src -name '*.png' -or -name '*.css' -or -name '*.gif' -exec chmod 0644 {} +

mkdir build && cd build

cmake ../src \
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_CXX_FLAGS="%{optflags} -Doverride=" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DENABLE_ADVANCEDNOTIFICATIONS=True \
        -DENABLE_AUSCRIE=True \
        -DENABLE_AZOTH=True \
        -DENABLE_AZOTH_ACETAMIDE=True \
        -DENABLE_AZOTH_ASTRALITY=True \
        -DENABLE_AZOTH_OTROID=True \
        -DENABLE_AZOTH_SHX=True \
        -DENABLE_AZOTH_VELVETBIRD=True \
        -DENABLE_AZOTH_ZHEET=True \
        -DENABLE_BLACKDASH=False \
        -DENABLE_BLOGIQUE=True \
        -DENABLE_CHOROID=True \
        -DENABLE_DOLOZHEE=True \
        -DENABLE_DUMBEEP=True \
        -DDUMBEEP_WITH_PHONON=True \
        -DENABLE_GACTS=True \
        -DWITH_GACTS_BUNDLED_QXT=True \
        -DENABLE_GLANCE=True \
        -DENABLE_GMAILNOTIFIER=True \
        -DENABLE_HOTSENSORS=True \
        -DENABLE_HOTSTREAMS=True \
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
        -DENABLE_LIZNOO=True \
        -DENABLE_LMP=True \
        -DENABLE_LMP_GRAFFITI=True \
        -DENABLE_LMP_MPRIS=True \
        -DENABLE_MEDIACALLS=False \
        -DENABLE_MELLONETRAY=True \
        -DENABLE_MONOCLE=True \
%ifarch x86_64
        -DENABLE_MONOCLE_MU=False \
%else
        -DENABLE_MONOCLE_MU=True \
        -DMUPDF_VERSION=0x0100 \
%endif
        -DENABLE_MUSICZOMBIE=True \
        -DWITH_MUSICZOMBIE_CHROMAPRINT=False \
        -DENABLE_NACHEKU=True \
        -DENABLE_NEWLIFE=True \
        -DENABLE_NETSTOREMANAGER=True \
        -DENABLE_OTLOZHU=True \
        -DENABLE_PINTAB=True \
        -DENABLE_POLEEMERY=True \
        -DENABLE_POGOOGLUE=True \
        -DENABLE_POPISHU=True \
        -DENABLE_POSHUKU_AUTOSEARCH=True \
        -DUSE_POSHUKU_CLEANWEB_PCRE=True \
        -DENABLE_QROSP=False \
        -DENABLE_SB2=True \
        -DENABLE_SECMAN=True \
        -DENABLE_SHAITAN=True \
        -DENABLE_SHELLOPEN=True \
        -DENABLE_SNAILS=False \
        -DENABLE_SYNCER=True \
        -DENABLE_TABSESSMANAGER=True \
        -DENABLE_TABSLIST=True \
        -DENABLE_TORRENT=True \
        -DENABLE_TOUCHSTREAMS=True \
        -DENABLE_TPI=True \
        -DENABLE_TWIFEE=False \
        -DENABLE_VROOBY=True \
        -DENABLE_WOODPECKER=False \
        -DLEECHCRAFT_VERSION=%{LEECHCRAFT_VERSION}

# gcc 4.7 optimization.
# Disabled because of https://bugzilla.novell.com/show_bug.cgi?id=774180
#
# %%if %%{?suse_version} > 1230
#         -DCMAKE_CXX_FLAGS="%%{optflags} -flto" \
#         -DCMAKE_SHARED_LINKER_FLAGS="%%{optflags} -flto" \
#         -DCMAKE_EXE_LINKER_FLAGS="%%{optflags} -flto" \
# %%endif

%build
cd build
make %{?_smp_mflags}

%install
cd build
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

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
%{_libdir}/*lcutil.so.*
%{_libdir}/*xmlsettingsdialog.so.*
%doc %{_mandir}/man1/%{name}*.1.gz
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/global_icons/
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/*
%{_datadir}/%{name}/themes/*/*.rc
%exclude %{_datadir}/cmake/Modules/InitLCPlugin.cmake
%{_datadir}/%{name}/qml/org/
%{_datadir}/%{name}/qml/common/

%files advancednotifications
%defattr(-,root,root)
%{plugin_dir}/*%{name}_advancednotifications.so
%{translations_dir}/leechcraft_advancednotifications*
%{settings_dir}/advancednotificationssettings.xml
%{_datadir}/%{name}/qml/advancednotifications

%files aggregator
%defattr(-,root,root)
%{settings_dir}/aggregatorsettings.xml
%{translations_dir}/%{name}_aggregator*.qm
%{plugin_dir}/*%{name}_aggregator.so

%files aggregator-bodyfetch
%defattr(-,root,root)
%{plugin_dir}/*%{name}_aggregator_bodyfetch.so
%dir %{_datadir}/%{name}/scripts
%{_datadir}/%{name}/scripts/aggregator/

%files anhero
%defattr(-,root,root)
%{_bindir}/lc_anhero_crashprocess
%{plugin_dir}/*%{name}_anhero.so
%{translations_dir}/leechcraft_anhero*

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
%{_datadir}/applications/%{name}-azoth-acetamide.desktop

%files azoth-adiumstyles
%defattr(644,root,root,755)
%{plugin_dir}/*%{name}_azoth_adiumstyles*
%{_datadir}/%{name}/azoth/styles/adium

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

%files azoth-nativeemoticons
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_nativeemoticons.so

%files azoth-otroid
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_otroid.so
%{_datadir}/%{name}/translations/%{name}_azoth_otroid*.qm

%files azoth-p100q
%defattr(-,root,root)
%{settings_dir}/azothp100qsettings.xml
%{plugin_dir}/*%{name}_azoth_p100q.so
%{translations_dir}/leechcraft_azoth_p100q*

%files azoth-rosenthal
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_rosenthal.so
%{translations_dir}/%{name}_azoth_rosenthal*
%{settings_dir}/azothrosenthalsettings.xml

%files azoth-shx
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_shx.so
%{_datadir}/%{name}/settings/azothshxsettings.xml

%files azoth-standardstyles
%defattr(-,root,root)
%{plugin_dir}/*%{name}_azoth_standardstyles.so
%{_datadir}/%{name}/azoth/styles/standard/

%files azoth-vader
%defattr(-,root,root)
%{translations_dir}/%{name}_azoth_vader*
%{_datadir}/%{name}/settings/azothvadersettings.xml
%{plugin_dir}/*%{name}_azoth_vader.so

%files azoth-velvetbird
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_azoth_velvetbird.so

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

%files blogique-metida
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_blogique_metida.so
%{_datadir}/%{name}/settings/blogiquemetidasettings.xml
%{_datadir}/%{name}/qml/blogique/metida/

%files choroid
%defattr(-,root,root)
%{plugin_dir}/*%{name}_choroid.so
%{_datadir}/%{name}/qml/choroid

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
%{_libdir}/*lcutil.so
%{_libdir}/*xmlsettingsdialog.so
%{_datadir}/cmake/Modules/InitLCPlugin.cmake

%files dolozhee
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_dolozhee.so
%{_datadir}/%{name}/translations/%{name}_dolozhee_*.qm

%files dumbeep
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_dumbeep.so
%{_datadir}/%{name}/settings/dumbeepsettings.xml

%files gacts
%defattr(-,root,root)
%doc src/plugins/gacts/3rdparty/qxt/LICENSE
%{_libdir}/%{name}/plugins/*%{name}_gacts.so

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

%files historyholder
%defattr(-,root,root)
%{plugin_dir}/*leechcraft_historyholder.so
%{translations_dir}/leechcraft_historyholder*.qm

%files hotsensors
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_hotsensors.so
%{_datadir}/%{name}/qml/hotsensors

%files hotstreams
%defattr(-,root,root)
%{plugin_dir}/*%{name}_hotstreams.so

%files imgaste
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_imgaste.so

%files kbswitch
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_kbswitch.so
%{_datadir}/%{name}/settings/kbswitchsettings.xml

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

%files lmp
%defattr(-,root,root)
%{settings_dir}/lmpsettings.xml
%{_datadir}/%{name}/translations/%{name}_lmp_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_??_??.qm
%{plugin_dir}/*%{name}_lmp.so

%files lmp-dumbsync
%defattr(-,root,root)
%{plugin_dir}/*%{name}_lmp_dumbsync.so
%{_datadir}/%{name}/settings/lmpdumbsyncsettings.xml
%{_datadir}/%{name}/translations/%{name}_lmp_dumbsync_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_dumbsync_??_??.qm

%files lmp-graffiti
%defattr(-,root,root)
%{plugin_dir}/*%{name}_lmp_graffiti.so
%{_datadir}/%{name}/translations/%{name}_lmp_graffiti_??.qm
%{_datadir}/%{name}/translations/%{name}_lmp_graffiti_??_??.qm

%files lmp-mp3tunes
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_lmp_mp3tunes.so
%{_datadir}/%{name}/settings/lmpmp3tunessettings.xml

%files mellonetray
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_mellonetray.so
%{_datadir}/%{name}/qml/mellonetray/

%files monocle
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle.so
%{_datadir}/%{name}/translations/%{name}_monocle_*.qm
%{_datadir}/%{name}/settings/monoclesettings.xml

%files monocle-fxb
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_fxb.so
%{_datadir}/applications/%{name}-monocle-fxb.desktop

%ifarch i586 i686
%files monocle-mu
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_mu.so
%endif

%files monocle-pdf
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_monocle_pdf.so
%{_datadir}/applications/%{name}-monocle-pdf.desktop

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

%files nacheku
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_nacheku.so
%{_datadir}/%{name}/settings/nachekusettings.xml

%files netstoremanager
%defattr(-,root,root)
%{plugin_dir}/*%{name}_netstoremanager.so
%{_datadir}/%{name}/settings/netstoremanagersettings.xml
%{_datadir}/%{name}/translations/%{name}_netstoremanager_??.qm
%{_datadir}/%{name}/translations/%{name}_netstoremanager_??_??.qm

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

%files otlozhu
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_otlozhu.so
%{_datadir}/%{name}/translations/%{name}_otlozhu_*.qm

%files pintab
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_pintab.so
%{_datadir}/%{name}/translations/%{name}_pintab_*.qm

%files pogooglue
%defattr(-,root,root)
%{plugin_dir}/*%{name}_pogooglue*
%{translations_dir}/leechcraft_pogooglue*

%files poleemery
%defattr(-,root,root)
%{_datadir}/%{name}/settings/poleemerysettings.xml
%{_datadir}/%{name}/translations/%{name}_poleemery_*.qm
%{_libdir}/%{name}/plugins/*%{name}_poleemery*

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

%files poshuku-cleanweb
%defattr(-,root,root)
%{settings_dir}/poshukucleanwebsettings.xml
%{translations_dir}/%{name}_poshuku_cleanweb*.qm
%{plugin_dir}/*%{name}_poshuku_cleanweb.so

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

%files sb2
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_sb2.so
%{_datadir}/%{name}/qml/sb2/

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

%files shaitan
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_shaitan.so

%files shellopen
%defattr(-,root,root)
%{translations_dir}/%{name}_shellopen*.qm
%{plugin_dir}/*%{name}_shellopen.so

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

%files tabsessionmanager
%defattr(-,root,root)
%{plugin_dir}/*%{name}_tabsessmanager.so
%{_datadir}/%{name}/translations/%{name}_tabsessmanager_*.qm

%files tabslist
%defattr(-,root,root)
%{plugin_dir}/*%{name}_tabslist.so
%{translations_dir}/leechcraft_tabslist*

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

%files vrooby
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_vrooby.so
%{_datadir}/%{name}/translations/%{name}_vrooby_*.qm

%files xproxy
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_xproxy.so
%{_datadir}/%{name}/settings/xproxysettings.xml
%{_datadir}/%{name}/translations/%{name}_xproxy_*.qm

%files xtazy
%defattr(-,root,root)
%{_datadir}/%{name}/settings/xtazysettings.xml
%{_libdir}/%{name}/plugins/*%{name}_xtazy.so
%{_datadir}/%{name}/translations/%{name}_xtazy*

%changelog