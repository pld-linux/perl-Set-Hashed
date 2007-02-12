#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Hashed
Summary:	Set::Hashed Perl module - yet another extension for set operations
Summary(pl.UTF-8):   Moduł Perla Set::Hashed - jeszcze jedno rozszerzenie do operacji na zbiorach
Name:		perl-Set-Hashed
Version:	0.07
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.ling.uni-potsdam.de/~moocow/projects/diplom/modules/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f8558db56028508d34e7b6fd72cd6536
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Hashed provides set operations for scalars (including references)
based on an internal representation as a hash. It provides a subset
(sic) of the functionality provided by the Set::Scalar module, and
seems to be slightly faster where the functionality overlaps.

%description -l pl.UTF-8
Moduł Set::Hashed udostępnia operacje na zbiorach dla skalarów (wraz z
referencjami) bazujące na wewnętrznej reprezentacji jako hasza. Moduł
ten daje podzbiór funkcjonalności modułu Set::Scalar, ale wydaje się
być trochę szybszy tam, gdzie funkcjonalność się pokrywa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
