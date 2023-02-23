Vendor:         Microsoft Corporation
Distribution:   Mariner
%global		priority	69
%global		fontname	ipa-gothic
%global		fontconf	%{priority}-%{fontname}.conf
%global		archiveversion	00303
%global		archivename	ipag%{archiveversion}

Name:		%{fontname}-fonts
Version:	003.03
Release:	22%{?dist}
Summary:	Japanese Gothic-typeface OpenType font by IPA

License:	IPA
URL:		http://ossipedia.ipa.go.jp/ipafont/
Source0:	http://info.openlab.ipa.go.jp/ipafont/fontdata/%{archivename}.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel libappstream-glib
Requires:	fontpackages-filesystem

%description
IPA Font is a Japanese OpenType fonts that is JIS X 0213:2004
compliant, provided by Information-technology Promotion Agency, Japan.

This package contains Gothic (sans-serif) style font.

%prep
%setup -q -n %{archivename}


%build

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p	%{SOURCE1}	\
			$RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

install -m 0755 -d $RPM_BUILD_ROOT%{_metainfodir}
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_metainfodir}

ln -s	%{_fontconfig_templatedir}/%{fontconf}	\
	$RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf

%doc Readme_%{archivename}.txt
%license IPA_Font_License_Agreement_v1.0.txt
%{_metainfodir}/%{fontname}.metainfo.xml


%changelog
* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 003.03-16
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 003.03-12
- Update the priority to change the default font to Noto.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 003.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Akira TAGOH <tagoh@redhat.com> - 003.03-7
- Add metainfo file.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Akira TAGOH <tagoh@redhat.com>
- the spec file cleanup.

* Fri Aug 17 2012 Akira TAGOH <tagoh@redhat.com> - 003.03-3
- Enable hinting explicitly since autohinting seems broken for this font.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Akira TAGOH <tagoh@redhat.com> - 003.03-1
- New upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 25 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-5
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-4
- Get rid of compare="contains".

* Fri Apr 16 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-3
- Get rid of binding="same" from the fontconfig config file. (#578020)

* Tue Feb 16 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-1
- New upstream release.
- add a fallback rule for sans-serif.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-3
- Disable hinting.

* Wed Apr 22 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-2
- Correct the source URL.

* Tue Apr 21 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-1
- Initial package.

