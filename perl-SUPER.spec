%define	modname	SUPER

Summary:	Perl module for controlling superclass method dispatch
Name:		perl-%{modname}
Version:	1.20190531
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		https://metacpan.org/pod/SUPER
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/SUPER-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Sub::Identify)

%description
Perl module for controlling superclass method dispatch

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/SUPER.pm
%doc %{_mandir}/man3*/*
