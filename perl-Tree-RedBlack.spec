%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	RedBlack
Summary:	Tree::RedBlack - Perl implementation of Red/Black tree, a type of balanced tree.
Name:		perl-Tree-RedBlack
Version:	0.3
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a perl implementation of the Red/Black tree algorithm found in
the book "Algorithms", by Cormen, Leiserson & Rivest (more commonly known
as "CLR" or "The White Book").  A Red/Black tree is a binary tree which
remains "balanced"- that is, the longest length from root to a node is
at most one more than the shortest such length.  It is fairly efficient;
no operation takes more than O(lg(n)) time.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tree/RedBlack.pm
%{perl_sitelib}/Tree/RedBlack
%{_mandir}/man3/*
