#
# spec file for package perl-XML-Twig
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-XML-Twig
Version:        3.39
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Summary:        Tree interface to XML documents
Url:            http://search.cpan.org/dist/XML::Twig
Group:          Development/Libraries/Perl
# http://search.cpan.org/CPAN/authors/id/M/MI/MIROD/XML-Twig-%{version}.tar.gz
Source:         XML-Twig-%{version}.tar.gz
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-macros
Requires:       perl-XML-Parser
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
XML::Twig is (yet another!) XML transformation module.

Its strong points: can be used to process huge documents while still
being in tree mode; not bound by DOM or SAX, so it is very perlish and
offers a very comprehensive set of methods; simple to use; DWIMs as
much as possible

What it doesn't offer: full SAX support (it can export SAX, but only
reads XML), full XPath support (unless you use XML::Twig::XPath), nor
DOM support.

Other drawbacks: it is a big module, and with over 500 methods
available it can be a bit overwhelming. A good starting point is the
tutorial at http://xmltwig.com/xmltwig/tutorial/index.html. In fact the
whole XML::Twig page at http://xmltwig.com/xmltwig/ has plenty of
information to get you started with XML::Twig

%prep
%setup -q -n XML-Twig-%{version}

%build
perl Makefile.PL
make

%check
make test

%install
%perl_make_install
%perl_process_packlist

%clean
%{?buildroot:rm -rf %{buildroot}}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/XML
%{perl_vendorlib}/XML/Twig.pm
%{perl_vendorlib}/XML/Twig
%{_bindir}/xml_grep
%{_bindir}/xml_merge
%{_bindir}/xml_pp
%{_bindir}/xml_spellcheck
%{_bindir}/xml_split
%doc %{_mandir}/man1/xml_*.1%{ext_man}
%doc %{_mandir}/man3/XML::Twig.%{perl_man3ext}%{ext_man}

%changelog
