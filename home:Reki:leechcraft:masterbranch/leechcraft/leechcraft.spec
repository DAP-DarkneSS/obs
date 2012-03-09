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

%define plugin_dir %{_libdir}/%{name}/plugins
%define translations_dir %{_datadir}/%{name}/translations
%define settings_dir %{_datadir}/%{name}/settings
%define azoth_dir %{_datadir}/%{name}/azoth
Name:           leechcraft
Version:        git
%define LEECHCRAFT_VERSION 0.4.95-1139-g431f415
Release:        1
License:        GPL-2.0+
Summary:        Modular Internet Client
Url:            http://leechcraft.org
Group:          Productivity/Networking/Other
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
#another AdiumStyle for Azoth, modified for compatiblity with AzothAdium
#http://www.adiumxtras.com/index.php?a=xtras&xtra_id=2160
Source2:        renkoo_adiumstyle.tar.xz
# Fixing a bug with finding dynamic libqxmpp1 libs
Patch1:         find_qxmpp.patch
# Fixing path to php-cli
Patch2:         eiskaltdcpp-fix-php5-issue.patch
# Set AppQStyle to default from plastique
Patch3:         defaultstyle.patch

BuildRequires:  xz
BuildRequires:  aspell-devel aspell
BuildRequires:  boost-devel
BuildRequires:  cmake > 2.8
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcurl-devel
BuildRequires:  libqt4-devel >= 4.6
BuildRequires:  phonon-devel
BuildRequires:  libqxmpp-devel >= 0.3.45.1
BuildRequires:  speex-devel
BuildRequires:  fdupes
BuildRequires:  libGeoIP-devel
BuildRequires:  libtorrent-rasterbar-devel >= 0.15.6
BuildRequires:  libqjson-devel
BuildRequires:  libqt4-sql
BuildRequires:  libqscintilla-devel
BuildRequires:  libqca2-devel
BuildRequires:  update-desktop-files
BuildRequires:  kdebase4-workspace-devel
BuildRequires:  libbz2-devel
BuildRequires:  libQtWebKit-devel
BuildRequires:  libmsn-devel
BuildRequires:  telepathy-qt4-devel
BuildRequires:  qwt-devel >= 6
BuildRequires:  file-devel

Requires:       oxygen-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Core executable of Leechcraft.
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
Files required for development for LeechCraft.

This package contains header files required to develop new modules for
LeechCraft.

%package aggregator
Summary:        LeechCraft RSS/Atom Aggregator Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}

%description aggregator
RSS/Atom feed reader for LeechCraft.

This package contains Aggregator, the RSS/Atom feed reader. It features:
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
Aggregator BodyFetch plugin for automatic fetching of full news bodies
instead of short teasers. Segfaults sometimes, but is already usable.

%package auscrie
Summary:        LeechCraft Screenshoter Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description auscrie
Screenshooter for LeechCraft.

This package contains Auscrie, an auto screenshoter for LeechCraft.
It can make screenshots of LeechCraft and then either save them locally
or upload them to an imagebin.


%package popishu
Summary:        LeechCraft Text editor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description popishu
Popishu is a text editor for Leechcraft.

%package cstp
Summary:        LeechCraft HTTP Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-http

%description cstp
HTTP client for LeechCraft.

This package contains clean and simple HTTP implementation.

%package dbusmanager
Summary:        LeechCraft D-Bus Module
Group:          Productivity/Networking/Other
Provides:       %{name}-visualnotifications
Requires:       %{name} = %{version}

%description dbusmanager
D-Bus side of LeechCraft.

This package provides some DBus-related features, like integration with
desktop notifications (KDE ≥ 4.4 and others supporting libnotify
interfaces).

%package deadlyrics
Summary:        LeechCraft Lyrics finder Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

%description deadlyrics
Song lyrics finder for LeechCraft.

This package contains a simple client for finding song lyrics on various
sites.

%package historyholder
Summary:        LeechCraft History Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description historyholder
History keeper for LeechCraft.

This package contains a history keeper that stores information about
finished downloads and similar events.

%package kinotify
Summary:        LeechCraft Kinetic notifications Module
Group:          Productivity/Networking/Other
Provides:       %{name}-visualnotifications
Requires:       %{name} = %{version}

%description kinotify
Fancy notifications for LeechCraft.

This package contains Kinotify which provides fancy notifications for
LeechCraft instead of old-style tray-based ones.

%package lmp
Summary:        LeechCraft Media player Module
Group:          Productivity/Networking/Other
Provides:       %{name}-audioplayer
Requires:       %{name} = %{version}

%description lmp
Media previewer for LeechCraft.

This package contains the LMP, LeechCraft Media Previewer, small and
dirty media player designed to preview already downloaded files or to
stream media content live.

%package networkmonitor
Summary:        LeechCraft Network Monitor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description networkmonitor
Network monitor for LeechCraft.

This package contains a monitor that watches for HTTP requests
and responses around.

%package newlife
Summary:        LeechCraft Importer Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description newlife
Settings importer for LeechCraft.

This package contains importer of settings, preferences etc. from
various applications into LeechCraft. Currently it supports importing
RSS feeds and settings from Akregator and Liferea.

%package poshuku
Summary:        LeechCraft Web Browser Module
Group:          Productivity/Networking/Other
Provides:       %{name}-webbrowser
Requires:       %{name} = %{version}

%description poshuku
Web browser for LeechCraft.

This package contains a full-featured web browser for LeechCraft based
on WebKit. Poshuku is fully extensible with plugins. Currently it
features:
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
Greasemonkey scripts for leechcraft-poshuku.

%package poshuku-cleanweb
Summary:        LeechCraft Poshuku - Ad Filter Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku

%description poshuku-cleanweb
Ad filter for Web browser for LeechCraft.

This package contains a plugin for the Poshuku web browser that
filters out ads according to predefined rules. It is compatible with
Firefox's AdBlock rules list files. It also supports disabling Flash
and allowing it to load only after you click on the corresponding
button.

%package poshuku-filescheme
Summary:        LeechCraft Poshuku - Schemes Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-filescheme
file://-schemes support for a Web browser for LeechCraft.

This package contains a plugin for the Poshuku web browser that allows
it to handle file:// schemes.

%package poshuku-fua
Summary:        LeechCraft Poshuku - Change user agent Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-fua
Fake user agent plugin for Web browser for LeechCraft.

This package contains a plugin for the Poshuku web browser that allows
it to set fake user agents for different domains or even URLs based on
regexps.

%package poshuku-wyfv
Summary:        LeechCraft Poshuku - Flash Video Replacer Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-wyfv
Flash video replacer for Web browser for LeechCraft.

This package contains a plugin for the Poshuku web browser that
replaces default flash-based video players on some sites with any
suitable LeechCraft's media player thus avoiding the need for Flash.

%package poshuku-pintab
Summary:        LeechCraft Poshuku - Pin tabs Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-pintab
Poshuku PinTab allows to pin selected Poshuku tabs so that they cannot be
closed until unpinned.

%package poshuku-pogooglue
Summary:        LeechCraft Poshuku - quick google search Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-pogooglue
Poshuku Pogooglue allows to search instantly selected text in Google.

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
Online bookmarks plugin for LeechCraft.

This package contains a plugin for the Poshuku web browser that allows
to synchronize bookmarks with services like Read It Later.

%package poshuku-delicious
Summary:        LeechCraft Poshuku - Onlinebookmarks Delicious Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}

%description poshuku-delicious
Poshuku OB Del.icio.us provides support for the Del.icio.us service.

%package poshuku-readitlater
Summary:        LeechCraft Poshuku - Onlinebookmarks ReadItLater Module
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}

%description poshuku-readitlater
Poshuku OB Read it Later provides support for the Read it Later service.

%package seekthru
Summary:        LeechCraft OpenSearch Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

%description seekthru
OpenSearch-support plugin for LeechCraft.

This package contains a search client for OpenSearch-aware web sites.

%package summary
Summary:        LeechCraft Summary info Module
Group:          Productivity/Networking/Other
Provides:       %{name}-summaryrepresentation
Requires:       %{name} = %{version}

%description summary
Quick summary of what's going on in LeechCraft.

This package contains Summary which shows currently running download
tasks like BitTorrent files as well as news, events and statuses, like
unread items in RSS feed reader. It also allows to perform search
queries with instaled search plugins.

#%%package tabpp
#Summary:        LeechCraft Tab++ Module
#Group:          Productivity/Networking/Other
#Requires:       %%{name} = %%{version}

#%%description tabpp
#Tabbing experience enhancer for LeechCraft.
#
#This package contains Tab++ which shows the tree of tabs in groups. For
#example, tabs with pages in a browser that belong to the same subdomain
#will be grouped, and subdomains of the same parent domain will become
#its children as well.

%package vgrabber
Summary:        LeechCraft Vkontakte grabber Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

%description vgrabber
Vkontakte.ru plugin for LeechCraft.

This package contains a music search/grabber for the vkontakte.ru social
network.

%package shellopen
Summary:        LeechCraft Shellopen Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description shellopen
Support for opening files with external apps in LeechCraft.

This package contains module that adds an option to open files and
handle entities with external applications. For example, you may choose
to open a video file with your favorite media player instead of LC's
one.

%package secman
Summary:        LeechCraft Security manager Module
Group:          Productivity/Networking/Other
Provides:       %{name}-securestorage
Requires:       %{name} = %{version}
Requires:       %{name}-secman-simplestorage = %{version}

%description secman
Security manager for LeechCraft.

This package contains the base plugin for secure storage and such
stuff for LeechCraft. Particular storage backends are implemented
by plugins for this plugin.

%package secman-simplestorage
Summary:        LeechCraft Simple storage Module
Group:          Productivity/Networking/Other
Requires:       %{name}-secman = %{version}

%description secman-simplestorage
Simple storage backend for SecMan.

This package contains a simple, unencrypted storage backend for
SecMan, LeechCraft's security manager plugin.

%package azoth
Summary:        LeechCraft Instant messenger Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-azoth-chatstyler = %{version}
Requires:       %{name}-securestorage = %{version}

%description azoth
IM client for LeechCraft.

This package contains a simple IM client for LeechCraft.

%package azoth-acetamide
Summary:        LeechCraft Azoth - IRC Module
Group:          Productivity/Networking/Other
Provides:       %{name}-acetamine = %{version}
Obsoletes:      %{name}-acetamine < %{version}
Requires:       %{name}-azoth = %{version}

%description azoth-acetamide
This package contains a IRC support for LeechCraft Azoth Module.

%package azoth-chathistory
Summary:        LeechCraft Azoth - Chat history Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-chathistory
This package contains a chat history module for LeechCraft Azoth
Module.

%package azoth-autopaste
Summary:        LeechCraft Azoth - Autopaste Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-autopaste
This package contains an autopaste for automatic pasting of long
messages to pastebins

%package azoth-embedmedia
Summary:        LeechCraft Azoth - Media Objects Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-embedmedia
This package enables embedding different media objects in chat
tab for LeechCraft Azoth Module.

%package azoth-hili
Summary:        LeechCraft Azoth - Conference highlights Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-hili
This package contains a plugin for customizing conference highlights
for LeechCraft Azoth Module.

%package azoth-juick
Summary:        LeechCraft Azoth - Juick.com service Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-juick
This package contains a plugin for the juick.com microblogging service
for LeechCraft Azoth Module.

%package azoth-nativeemoticons
Summary:        LeechCraft Azoth - Emoticons packs
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-nativeemoticons
This package contains a plugin for supporting emoticons packs in LeechCraft
Azoth Module.

%package azoth-p100q
Summary:        LeechCraft Azoth - Psto.net service Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-p100q
This package contains a plugin for the psto.net microblogging service
for LeechCraft Azoth Module.

%package azoth-standardstyles
Summary:        LeechCraft Azoth - Standard chat styles Module
Group:          Productivity/Networking/Other
Provides:       %{name}-azoth-chatstyler
Requires:       %{name}-azoth = %{version}

%description azoth-standardstyles
This package provides standard styles for LeechCraft Azoth Module.

%package azoth-xoox
Summary:        LeechCraft Azoth - XMPP Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-xoox
This package contains a XMPP support for LeechCraft Azoth Module.

%package azoth-xtazy
Summary:        LeechCraft Azoth - Publishing current user tune Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-xtazy
This package contains a plugin for publishing current user tune for
LeechCraft Azoth Module.

%package azoth-depester
Summary:        LeechCraft Azoth - Ignore Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-depester
This package contains LeechCraft Azoth Module for ignoring unwanted participants.

%package azoth-herbicide
Summary:        LeechCraft Azoth - Antispam Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-herbicide
This package contains a basic antispam plugin for LeechCraft Azoth Module.

%package azoth-keeso
Summary:        LeechCraft Azoth - Text transform Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-keeso
This package contains text transform plugin for LeechCraft Azoth Module.


%package azoth-rosenthal
Summary:        LeechCraft Azoth - Spell Checker Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-rosenthal
This package contains  a spell checker plugin for LeechCraft Azoth Module

%package azoth-lastseen
Summary:        LeechCraft Azoth - Contact last seen time Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-lastseen
Azoth LastSeen for client-side recording of contacts' last online and
availability time. It doesn't depend on the concrete protocol implementation.

%package azoth-adiumstyles
Summary:        LeechCraft Azoth - Adium Styles Module
Group:          Productivity/Networking/Other
Provides:       %{name}-azoth-chatstyler
Requires:       %{name}-azoth = %{version}

%description azoth-adiumstyles
Azoth AdiumStyles for, well, support for Adium styles. It is still
experimental and quite basic, but, nevertheless, already usable.

%package azoth-autoidler
Summary:        LeechCraft Azoth - Automatic Change of Status Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-autoidler
Azoth Autoidler for automatic change of status due to inactivity period.

%package azoth-metacontacts
Summary:        LeechCraft Azoth - Metacontacts Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-metacontacts
Metacontacts module provides metacontacts for LeechCraft Internet Client.

%package azoth-isterique
Summary:        LeechCraft Azoth - Isterique Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-isterique
Azoth Isterique removes excessive CAPS usage from incoming messages.

%package azoth-modnok
Summary:        LeechCraft Azoth - LaTeX support Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-modnok
Azoth Modnok for inline in-chat LaTeX rendering and display. It doesn't
depend on the underlying protocol, and if the protocol supports rich text
formatting in outgoing messages, it is able to replace the formulas with
corresponding images in outgoing messages as well, so your buddies would
see nice rendered formulas instead of raw LaTeX code, even if their client
doesn't have a LaTeX formatter.

%package azoth-astrality
Summary:        LeechCraft Azoth - Telepathy Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       telepathy-mission-control
Requires:       telepathy-haze

%description azoth-astrality
Support protocols provided by Telepathy.

%package azoth-zheet
Summary:        LeechCraft Azoth - MSN Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-zheet
Azoth Zheet provide msn messenger support for Azoth

%package azoth-vader
Summary:        LeechCraft Azoth - MrIM Module
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-vader
Azoth Vader provide mrim messenger support for Azoth

%package bittorrent
Summary:        LeechCraft BitTorrent client Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

%description bittorrent
This package contains Bittorrent client for Leechcraft

%package netstoremanager
Summary:        LeechCraft Network file storages Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description netstoremanager
This package contains network storage plugin for Leechcraft


#%%package eiskaltdcpp
#Summary:        LeechCraft DC++ Module
#Group:          Productivity/Networking/Other
#Requires:       %%{name} = %%{version}

#%%description eiskaltdcpp
#DC++ client for LeechCraft.
#
#This package contains EiskaltDC++ DirectConnect client ported to
#LeechCraft.

%package advancednotifications
Summary:        LeechCraft Notifications framework Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-visualnotifications = %{version}

%description advancednotifications
Advanced Notifications module for more customizable notifications
for Leechcraft.

%package glance
Summary:        LeechCraft Opened tabs overview Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description glance
Glance feature moved from the Core to a separate plugin.

%package tabslist
Summary:        LeechCraft TabsList Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description tabslist
TabsList for showing the list of currently opened tabs and quickly selecting one of them.

#%%package blackdash
#Summary:        LeechCraft Dashboard Module
#Group:          Productivity/Networking/Other
#Requires:       %%{name} = %%{version}

#%%description blackdash
#Dashboard

%package gmailnotifier
Summary:        LeechCraft GMail notifier Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}

%description gmailnotifier
Provides notifications about new mail in your GMail inbox.


%package lackman
Summary:        LeechCraft Package manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       xz
Recommends:     %{name}-poshuku = %{version}

%description lackman
LeechCraft package manager for installing script plugins, iconsets, additional data and other similar packages.

#%%package lcftp
#Summary:        LeechCraft FTP Client Module
#Group:          Productivity/Networking/Other
#Requires:       %%{name} = %%{version}

#%%description lcftp
#FTP client with recursive downloads, uploads and two-panel interface.

%package syncer
Summary:        LeechCraft Sync setting Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description syncer
Allows to synchronize data and settings between LeechCraft instances running on different machines.

%package lhtr
Summary:        LeechCraft HTML WYSIWYG editor Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description lhtr
HTML WYSIWYG editor module, usable with mail and blog modules

%package knowhow
Summary:        LeechCraft Tips of the day Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description knowhow
Display tips of the day window after launch LeechCraft

%package choroid
Summary:        LeechCraft Image viewer Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description choroid
Image viewer module for  LeechCraft


%package anhero
Summary:        LeechCraft Crash handler Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description anhero
Crash handler which uses KDE utils to handle crashes, show backtraces and aid in sending bug reports.

%package tabsessionmanager
Summary:        LeechCraft Tab Session Manager Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description tabsessionmanager
This package contains Tab Session Manager for Leechcraft.

%package sidebar
Summary:        LeechCraft Sidebar Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description sidebar
A nice side bar with quick launch, tabs and tray areas

#%%package snails
#Summary:        LeechCraft Email client module
#Group:          Productivity/Networking/Other
#Requires:       %%{name} = %%{version}

#%%description snails
#Email (IMAP) client module for LeechCraft


%package liznoo
Summary:        LeechCraft Power managment module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description liznoo
Power managment module for LeechCraft

%package pintab
Summary:        LeechCraft Pinning tabs Module
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description pintab
Pintab module allows to pin important tabs in LeechCraft

%prep
%setup -q -a 2 -n %{name}-%{version}

%patch1
%if 0%{suse_version} > 1140
%patch2
%endif
%patch3

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
        -DENABLE_AZOTH_ASTRALITY=True \
        -DENABLE_LIZNOO=True \
        -DENABLE_NETSTOREMANAGER=True \
        -DENABLE_PINTAB=True \
        -DLEECHCRAFT_VERSION=%{LEECHCRAFT_VERSION}

%build
cd build
make %{?_smp_mflags}

%install
cd build
%makeinstall
cd ../renkoo_adiumstyle
cp -r ./*.AdiumMessageStyle/ %{buildroot}/%{azoth_dir}/styles/adium/

%suse_update_desktop_file -i %{name}
#%%fdupes -s %%{buildroot}%%{_datadir}/%%{name}/eiskaltdcpp
%fdupes -s %{buildroot}%{_datadir}/%{name}/translations
%fdupes -s %{buildroot}%{_datadir}/%{name}/azoth
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

#%%files  eiskaltdcpp
#%%defattr(-,root,root)
#%%{_datadir}/%%{name}/eiskaltdcpp
#%%dir %%{translations_dir}/??
#%%dir %%{translations_dir}/??/LC_MESSAGES
#%%lang(be) %%{translations_dir}/be/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(bg) %%{translations_dir}/bg/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(cs) %%{translations_dir}/cs/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(en) %%{translations_dir}/en/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(es) %%{translations_dir}/es/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(fr) %%{translations_dir}/fr/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(hu) %%{translations_dir}/hu/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(pl) %%{translations_dir}/pl/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(ru) %%{translations_dir}/ru/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(sk) %%{translations_dir}/sk/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(sr) %%{translations_dir}/sr/LC_MESSAGES/libeiskaltdcpp.mo
#%%lang(uk) %%{translations_dir}/uk/LC_MESSAGES/libeiskaltdcpp.mo
#%%{plugin_dir}/*%%{name}_eiskaltdcpp.so
#%%doc %%{_mandir}/man1/eiskaltdcpp-qt.1.gz

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

%files poshuku-pintab
%defattr(-,root,root,-)
%{plugin_dir}/*_poshuku_pintab.so

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

%files poshuku-wyfv
%defattr(-,root,root)
%{settings_dir}/poshukuwyfvsettings.xml
%{translations_dir}/%{name}_poshuku_wyfv*.qm
%{plugin_dir}/*%{name}_poshuku_wyfv.so

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

#%%files blackdash
#%%defattr(-,root,root)
#%%{plugin_dir}/*%%{name}_blackdash.so

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

#%%files lcftp
#%%defattr(-,root,root)
#%%{plugin_dir}/*%%{name}_lcftp.so
#%%{settings_dir}/lcftpsettings.xml
#%%{translations_dir}/leechcraft_lcftp*

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
%{_datadir}/%{name}/translations/%{name}_lhtr_en.qm
%{_datadir}/%{name}/translations/%{name}_lhtr_ru_RU.qm

%files azoth-astrality
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_azoth_astrality.so
%{_datadir}/%{name}/translations/%{name}_azoth_astrality_en.qm
%{_datadir}/%{name}/translations/%{name}_azoth_astrality_ru_RU.qm

#%%files snails
#%%defattr(-,root,root)
#%%{_libdir}/%%{name}/plugins/lib%%{name}_snails.so

%files liznoo
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/lib%{name}_liznoo.so
%{_datadir}/%{name}/settings/liznoosettings.xml
%{_datadir}/%{name}/translations/%{name}_liznoo_en.qm
%{_datadir}/%{name}/translations/%{name}_liznoo_ru_RU.qm

%files pintab
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_pintab.so

%changelog
