%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	RedBlack
Summary:	Tree::RedBlack - Perl implementation of Red/Black tree, a type of balanced tree
Summary(pl):	Tree::RedBlack - implementacja drzew czerwono-czarnych
Name:		perl-Tree-RedBlack
Version:	0.3
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
To jest perlowa implementacja algorytmu drzew czerwono-czarnych, któr±
mo¿na znale¼æ w ksi±¿ce "Algorithms" autorstwa Cormena, Leisersona i
Rivesta (czê¶ciej znanej jako "CLR" lub "Bia³a ksiêga"). Drzewo
czerwono-czarne to binarne drzewo, które pozostaje wywa¿one - czyli
najd³u¿sza droga od korzenia do li¶cia jest najwy¿ej o jeden d³u¿sza
od najkrótszej. Jest do¶æ wydajne; ¿adna operacja nie trwa d³u¿ej ni¿
O(log(n)).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Tree/RedBlack.pm
%{perl_sitelib}/Tree/RedBlack
%{_mandir}/man3/*
