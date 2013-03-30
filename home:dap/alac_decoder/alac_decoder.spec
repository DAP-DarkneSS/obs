#
# spec file for package alac_decoder
#
# Copyright (c) 2004 David Hammerton (source)
# (c) 2013 Perlow Dmitriy A. (spec file)
#
# Please submit bugfixes or comments via https://bugs.links2linux.org
#

Name:           alac_decoder
Version:        0.2.0
Release:        0
License:        MIT
Summary:        A basic decoder for Apple Lossless Audio Codec files
Url:            http://craz.net/programs/itunes/alac.html
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Source:         http://craz.net/programs/itunes/files/alac_decoder-%{version}.tgz
Source1:        LICENSE

BuildRequires:  glibc-devel
BuildRequires:  make

BuildRoot:      %{_tmppath}/build-%{name}-%{version}

%description
Located here is a basic decoder for Apple Lossless Audio Codec files (ALAC).
ALAC is a proprietary lossless audio compression scheme. Apple never released
any documents on the format.
What I provide here is a C implementation of a decoder, written from reverse
engineering the file format. It turns out that most of the algorithms in the
codec are fairly well known. ALAC uses an adaptive FIR prediction algorithm
and stores the error values using a modified rice or golumb algorithm.
Further details are in alac.c. 

Although an encoder is not provided, by using the decoder as a sort of
specification it should be fairly trivial to write an encoder. By exploiting
other lossless audio encoders, such as FLAC, the task will be much easier.
Although one wouldn't be able to copy the compression algorithms verbatim, as
adaptive compression is used in ALAC and not in FLAC. There are, however, a
bunch of academic papers on the issue. 

The program located here will not be able to handle all ALAC files, it can
only handle mono or stereo files. ALAC allows up to 8 channels. It should be
trivial to finish the implementation once I find files that I can test it
with. The ALAC decoder supports both 16 and 24 bit sample sizes. 

The decoder is fairly self explanatory, it can read an ALAC stream from either
a file or from stdin, and write it as raw PCM data or as a WAV file to either
stdout or a file. In theory one should be able to stream data to the decoder.

%prep
%setup -q -n %{name}
cp %{SOURCE1} .

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} alac %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/alac

%changelog
