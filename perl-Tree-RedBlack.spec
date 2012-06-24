%include	/usr/lib/rpm/macros.perl
Summary:	Tree-RedBlack perl module
Summary(pl):	Modu� perla Tree-RedBlack
Name:		perl-Tree-RedBlack
Version:	0.2
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tree/Tree-RedBlack-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Tree-RedBlack perl module. 

%description -l pl
Modu� perla Tree-RedBlack.

%prep
%setup -q -n Tree-RedBlack-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tree/RedBlack
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Tree/RedBlack.pm
%{perl_sitelib}/Tree/RedBlack
%{perl_sitearch}/auto/Tree/RedBlack

%{_mandir}/man3/*
