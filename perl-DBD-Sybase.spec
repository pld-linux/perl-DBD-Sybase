%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Sybase
Summary:	DBD::Sybase - Sybase database driver for the DBI module
Summary(pl):	DBD::Sybase - sterownik DBI do bazy danych Sybase
Name:		perl-DBD-Sybase
Version:	1.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	325f97ccd5255aa05f5605241da5e1e8
BuildRequires:	freetds-devel
BuildRequires:	perl-DBI >= 1.00
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Sybase is a Perl module which works with the DBI module to
provide access to Sybase databases. With FreeTDS DBD::Sybase can be
also used to query a MS-SQL 7 or 2000 database server from a
UNIX/Linux host.

%description -l pl
DBD::Sybase jest modu³em Perla wspó³pracuj±cym z modu³em DBI i
umo¿liwiaj±cym dostêp do baz danych Sybase. Przy wykorzystaniu
FreeTDS, DBD::Sybase mo¿na równie¿ wykorzystaæ do dostêpu z poziomu
UNIX-a/Linuksa do serwerów bazodanowych MS-SQL 7 lub 2000.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__perl} -pi -e 's@/lib([ "])@/%{_lib}$1@g' Makefile.PL

%build
SYBASE=/usr ; export SYBASE
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%{perl_vendorarch}/DBD/Sybase.pm
%dir %{perl_vendorarch}/auto/DBD/Sybase
%{perl_vendorarch}/auto/DBD/Sybase/Sybase.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/Sybase/Sybase.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
