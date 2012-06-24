%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	RedBlack
Summary:	Tree::RedBlack - Perl implementation of Red/Black tree, a type of balanced tree
Summary(pl):	Tree::RedBlack - implementacja perlowa drzew czerwono-czarnych
Name:		perl-Tree-RedBlack
Version:	0.3
Release:	9
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	96d0822d005045fd90251a0cd9ccacea
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

%description -l pl
To jest perlowa implementacja algorytmu drzew czerwono-czarnych, kt�r�
mo�na znale�� w ksi��ce "Algorithms" autorstwa Cormena, Leisersona i
Rivesta (cz�ciej znanej jako "CLR" lub "Bia�a ksi�ga"). Drzewo
czerwono-czarne to binarne drzewo, kt�re pozostaje wywa�one - czyli
najd�u�sza droga od korzenia do li�cia jest najwy�ej o jeden d�u�sza
od najkr�tszej. Jest do�� wydajne; �adna operacja nie trwa d�u�ej ni�
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
