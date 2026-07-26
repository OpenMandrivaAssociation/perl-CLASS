%define upstream_name    CLASS
Name:		perl-%{upstream_name}
Version:	1.00
Release:	6

Summary:	Alias for __PACKAGE__
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
CLASS and $CLASS are both synonyms for __PACKAGE__. Easier to type.

$CLASS has the additional benefit of working in strings.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 653552
- rebuild for updated spec-helper

* Wed Aug 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 573087
- import perl-CLASS

