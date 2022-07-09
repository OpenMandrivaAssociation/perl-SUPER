%define	modname	SUPER
%define	modver	1.20190531

Summary:	Perl module for controlling superclass method dispatch
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://metacpan.org/pod/SUPER
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/SUPER-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
Perl module for controlling superclass method dispatch

%prep
%autosetup -p1 -n %{modname}-%{modver}

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
