#
# spec file for packages with different qmmp skins.
#
# spec-file: Copyright (c) 2011 2012 Perlow Dmitriy A.
#

Name:           qmmp-skins
Version:        1
Release:        1
Summary:        Different qmmp skins
URL:            http://is.gd/da_obs

Source0:        KDE_v_Gronpipmaster_copy_2.wsz
Source1:        Alucard.wsz
Source2:        http://www.deviantart.com/download/262664530/oxygen_skin_for_qmmp_by_al_dy-d4cdt8y.zip
Source3:        http://qmmp.googlecode.com/files/qmmp_black.tar.bz2

License:        Unknown
Group:          System/GUI/Other
BuildArch:      noarch
BuildRequires:  unzip

%description
There are different qmmp skins.

%package -n qmmp-skin-KDE
Summary:        Qmmp skin in the KDE style
URL:            http://kubuntu.ru/node/3439
Version:        2
Requires:       qmmp
BuildArch:      noarch

%description -n qmmp-skin-KDE
Here it is a nice qmmp style in the KDE style.

%package -n qmmp-skin-Alucard
Summary:        Qmmp skin in the Hellsing style
Requires:       qmmp
BuildArch:      noarch

%description -n qmmp-skin-Alucard
Here it is a nice green qmmp style with Alucard
the main character of Hellsing anime.

%package -n qmmp-skin-black
Summary:        Black qmmp skin
URL:            http://code.google.com/p/qmmp/downloads/list
Requires:       qmmp
BuildArch:      noarch

%description -n qmmp-skin-black
Here it is a nice black qmmp style.

%package -n qmmp-skin-Air
Summary:        Qmmp skin in the Air style
URL:            http://al-dy.deviantart.com/art/Oxygen-skin-for-QMMP-262664530
Version:        0.1
Requires:       qmmp
BuildArch:      noarch

%description -n qmmp-skin-Air
Here it is a nice qmmp style in the KDE default style Air.

%prep
# unzip %%{SOURCE0} -d %%{_builddir}
# unzip %%{SOURCE1} -d %%{_builddir}
unzip %{SOURCE2} -d %{_builddir}
tar -xf %{SOURCE3} -C %{_builddir}

%build

%install
mkdir -p %{buildroot}%{_datadir}/qmmp/skins/

%{__install} %{SOURCE0} %{buildroot}%{_datadir}/qmmp/skins/
%{__install} %{SOURCE1} %{buildroot}%{_datadir}/qmmp/skins/
# cp -R "%%{_builddir}/kde v.Gronpipmaster" %%{buildroot}%%{_datadir}/qmmp/skins/
# cp -R %%{_builddir}/Alucard %%{buildroot}%%{_datadir}/qmmp/skins/
cp -R %{_builddir}/qmmp_black %{buildroot}%{_datadir}/qmmp/skins/
cp -R %{_builddir}/oxygen %{buildroot}%{_datadir}/qmmp/skins/

# chmod -x "%%{buildroot}%%{_datadir}/qmmp/skins/kde v.Gronpipmaster/pledit.txt"

%clean
rm -rf %{buildroot}

%files -n qmmp-skin-KDE
%defattr(-,root,root)
%dir %{_datadir}/qmmp/
%dir %{_datadir}/qmmp/skins/
%{_datadir}/qmmp/skins/KDE_v_Gronpipmaster_copy_2.wsz

%files -n qmmp-skin-Alucard
%defattr(-,root,root)
%dir %{_datadir}/qmmp/
%dir %{_datadir}/qmmp/skins/
%{_datadir}/qmmp/skins/Alucard.wsz

%files -n qmmp-skin-Air
%defattr(-,root,root)
%dir %{_datadir}/qmmp/
%dir %{_datadir}/qmmp/skins/
%{_datadir}/qmmp/skins/oxygen

%files -n qmmp-skin-black
%defattr(-,root,root)
%dir %{_datadir}/qmmp/
%dir %{_datadir}/qmmp/skins/
%{_datadir}/qmmp/skins/qmmp_black

%changelog
