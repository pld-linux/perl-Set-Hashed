%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Hashed
Summary:	Set::Hashed Perl module - yet another extension for set operations
Summary(pl):	Modu³ Perla Set::Hashed - jeszcze jedno rozszerzenie do operacji na zbiorach
Name:		perl-Set-Hashed
Version:	0.07
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.ling.uni-potsdam.de/~moocow/projects/diplom/modules/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Hashed provides set operations for scalars (including references)
based on an internal representation as a hash. It provides a subset
(sic) of the functionality provided by the Set::Scalar module, and
seems to be slightly faster where the functionality overlaps.
		
%description -l pl
Modu³ Set::Hashed udostêpnia operacje na zbiorach dla skalarów (wraz z
referencjami) bazuj±ce na wewnêtrznej reprezentacji jako hasza. Modu³
ten daje podzbiór funkcjonalno¶ci modu³u Set::Scalar, ale wydaje siê
byæ trochê szybszy tam, gdzie funkcjonalno¶æ siê pokrywa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Set/Hashed.pm
%{_mandir}/man3/*
