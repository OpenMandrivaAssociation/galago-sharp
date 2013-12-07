%define galagover 0.5.2

%define pkgconfigdir %{_datadir}/pkgconfig
%define monodir %{_prefix}/lib/mono

Summary:	Galago Mono bindings
Name:		galago-sharp
Version:	0.5.0
Release:	21
License:	LGPLv2
Group:		Development/Other
Url:		http://www.galago-project.org/
Source0:	http://galago-project.org/files/releases/source/galago-sharp/%{name}-%{version}.tar.bz2
Source1:	galago-sharp-0.5.0-dll.config
Source2:	http://galago-project.org/files/releases/source/libgalago/libgalago-%{galagover}.tar.bz2
Patch0:		galago-sharp-0.5.0-nunit.patch
Patch1:		galago-sharp-0.5.0-disable-tests.patch
Patch2:		galago-sharp-0.5.0-automake-1.13.patch
BuildArch:	noarch

BuildRequires:	perl-XML-LibXML
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gapi-2.0)
BuildRequires:	pkgconfig(glib-sharp-2.0)
BuildRequires:	pkgconfig(libgalago)
BuildRequires:	pkgconfig(mono)
#gw only needed for the tests
#BuildRequires:	dbus-sharp
Requires:	galago3 >= 0.5.2

%description
This are the Mono/.NET bindings for the Galago desktop presence framework.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
The pkgconfig for %{name}.

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
%configure --libdir=%{_prefix}/lib
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
%{_datadir}/gapi-2.0/galago-api.xml

%files devel
%{pkgconfigdir}/%{name}.pc

