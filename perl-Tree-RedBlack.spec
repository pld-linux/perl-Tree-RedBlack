%define		pdir	Tree
%define		pnam	RedBlack
%include	/usr/lib/rpm/macros.perl
Summary:	Tree::RedBlack - Perl implementation of Red/Black tree, a type of balanced tree
Summary(pl.UTF-8):	Tree::RedBlack - implementacja perlowa drzew czerwono-czarnych
Name:		perl-Tree-RedBlack
Version:	0.5
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46a749fa2aa047d5a044ecf0a0fbc925
URL:		http://search.cpan.org/dist/Tree-RedBlack/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl implementation of the Red/Black tree algorithm found in
the book "Algorithms", by Cormen, Leiserson & Rivest (more commonly
known as "CLR" or "The White Book"). A Red/Black tree is a binary tree
which remains "balanced" - that is, the longest length from root to a
node is at most one more than the shortest such length. It is fairly
efficient; no operation takes more than O(lg(n)) time.

%description -l pl.UTF-8
To jest perlowa implementacja algorytmu drzew czerwono-czarnych, którą
można znaleźć w książce "Algorithms" autorstwa Cormena, Leisersona i
Rivesta (częściej znanej jako "CLR" lub "Biała księga"). Drzewo
czerwono-czarne to binarne drzewo, które pozostaje wyważone - czyli
najdłuższa droga od korzenia do liścia jest najwyżej o jeden dłuższa
od najkrótszej. Jest dość wydajne; żadna operacja nie trwa dłużej niż
O(log(n)).

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
%{perl_vendorlib}/Tree/RedBlack.pm
%{perl_vendorlib}/Tree/RedBlack
%{_mandir}/man3/*
