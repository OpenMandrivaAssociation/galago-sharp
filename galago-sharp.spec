%define name galago-sharp
%define version 0.5.0
%define galagover 0.5.2

%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif
%define monodir %_prefix/lib/mono
Summary: Galago Mono bindings
Name: %{name}
Version: %{version}
Release: %mkrel 14
Source0: http://galago-project.org/files/releases/source/galago-sharp/%{name}-%{version}.tar.bz2
Source1: galago-sharp-0.5.0-dll.config
Source2: libgalago-%galagover.tar.bz2
Patch: galago-sharp-0.5.0-nunit.patch
Patch1: galago-sharp-0.5.0-disable-tests.patch
License: LGPL
Group: Development/Other
Url: http://www.galago-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgalago-devel >= 0.5.0
BuildRequires: mono-devel
#gw only needed for the tests
#BuildRequires: dbus-sharp
BuildRequires: gtk-sharp2-devel glib-sharp2
BuildRequires: libxslt-proc
BuildRequires: automake1.8
BuildArch: noarch
Requires: galago3 >= %galagover
%define _requires_exceptions lib.*galago

%description
This are the Mono/.NET bindings for the Galago desktop presence framework.

%prep
%setup -q -a 2
cp %SOURCE1  galago-sharp.dll.config
%patch -p1
%patch1 -p1
aclocal-1.8
autoconf
autoheader
automake-1.8
mv libgalago-%galagover sources/libgalago

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std pcdatadir=%pkgconfigdir
cp galago-sharp.dll.config %buildroot%monodir/gac/%name/*/
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog AUTHORS NEWS
%monodir/%name
%monodir/gac/%name
%pkgconfigdir/%name.pc
%_datadir/gapi-2.0/galago-api.xml
