%define galagover 0.5.2

%define pkgconfigdir %{_datadir}/pkgconfig
%define monodir %{_prefix}/lib/mono

Summary:	Galago Mono bindings
Name:		galago-sharp
Version:	0.5.0
Release:	17
License:	LGPL
Group:		Development/Other
Url:		http://www.galago-project.org/
Source0:	http://galago-project.org/files/releases/source/galago-sharp/%{name}-%{version}.tar.bz2
Source1:	galago-sharp-0.5.0-dll.config
Source2:	libgalago-%{galagover}.tar.bz2
Patch0:		galago-sharp-0.5.0-nunit.patch
Patch1:		galago-sharp-0.5.0-disable-tests.patch
Patch2:		galago-sharp-0.5.0-automake-1.13.patch
BuildRequires:	libgalago-devel >= 0.5.0
BuildRequires:	mono-devel
#gw only needed for the tests
#BuildRequires: dbus-sharp
BuildRequires:	gtk-sharp2-devel
BuildRequires:	glib-sharp2
BuildRequires:	libxslt-proc
BuildRequires:	automake1.8
BuildRequires:	perl-XML-LibXML
BuildArch:	noarch
Requires:	galago3 >= %{galagover}

%description
This are the Mono/.NET bindings for the Galago desktop presence framework.

%prep
%setup -q -a 2
cp %{SOURCE1}  galago-sharp.dll.config
%apply_patches
aclocal
autoconf
autoheader
automake
mv libgalago-%{galagover} sources/libgalago

%build
%configure --libdir=%_prefix/lib
%make

%check
%make check

%install
%makeinstall_std pcdatadir=%{pkgconfigdir}
cp galago-sharp.dll.config %{buildroot}%{monodir}/gac/%{name}/*/

%files
%doc README ChangeLog AUTHORS NEWS
%{monodir}/%{name}
%{monodir}/gac/%{name}
%{pkgconfigdir}/%{name}.pc
%{_datadir}/gapi-2.0/galago-api.xml


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-13mdv2011.0
+ Revision: 664807
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-12mdv2011.0
+ Revision: 522707
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.0-11mdv2010.0
+ Revision: 424549
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.0-10mdv2010.0
+ Revision: 424512
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.5.0-9mdv2009.1
+ Revision: 351187
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-8mdv2009.0
+ Revision: 221024
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-7mdv2008.1
+ Revision: 178949
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Götz Waschk <waschk@mandriva.org>
    - filter out new automatic mono deps

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 0.5.0-5mdv2008.0
+ Revision: 62986
- fix buildrequires
- disable tests to get rid of dbus-sharp dep


* Fri Mar 30 2007 Götz Waschk <waschk@mandriva.org> 0.5.0-5mdv2007.1
+ Revision: 149805
- fix dll map for loading libgalago

* Fri Jan 05 2007 Götz Waschk <waschk@mandriva.org> 0.5.0-4mdv2007.1
+ Revision: 104444
- fix build on x86_64
- Import galago-sharp

* Fri Jan 05 2007 Götz Waschk <waschk@mandriva.org> 0.5.0-4mdv2007.1
- new libgalago

* Tue Jul 18 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-3mdv2007.0
- fix deps

* Tue Apr 25 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-2mdk
- fix typo in dep

* Sat Apr 22 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdk
- update file list
- fix build
- update source 1
- bump deps
- fix URLs
- new version

* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 0.3.2-4mdk
- fix buildrequires

* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 0.3.2-3mdk
- add dllmap
- fix buildrequires

* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 0.3.2-2mdk
- fix buildrequires

* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdk
- initial package

