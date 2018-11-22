%define	modname	SUPER
%define	modver	1.20141117

Summary:	Perl module for controlling superclass method dispatch
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://metacpan.org/pod/SUPER
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/SUPER-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Perl module for controlling superclass method dispatch

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/SUPER.pm
%{_mandir}/man3*/*
