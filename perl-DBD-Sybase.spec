%define		pdir	DBD
%define		pnam	Sybase
Summary:	DBD::Sybase - Sybase database driver for the DBI module
Summary(pl.UTF-8):	DBD::Sybase - sterownik DBI do bazy danych Sybase
Name:		perl-DBD-Sybase
Version:	1.16
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5fea4769991b900d448025a32f42c4fe
Patch0:		x32.patch
URL:		http://search.cpan.org/dist/DBD-Sybase/
BuildRequires:	freetds-devel
BuildRequires:	perl-DBI >= 1.00
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Sybase is a Perl module which works with the DBI module to
provide access to Sybase databases. With FreeTDS DBD::Sybase can be
also used to query a MS-SQL 7 or 2000 database server from a
UNIX/Linux host.

%description -l pl.UTF-8
DBD::Sybase jest modułem Perla współpracującym z modułem DBI i
umożliwiającym dostęp do baz danych Sybase. Przy wykorzystaniu
FreeTDS, DBD::Sybase można również wykorzystać do dostępu z poziomu
Uniksa/Linuksa do serwerów bazodanowych MS-SQL 7 lub 2000.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
SYBASE=/usr ; export SYBASE
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as man
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/DBD/dbd-sybase.pod

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%{perl_vendorarch}/DBD/Sybase.pm
%dir %{perl_vendorarch}/auto/DBD/Sybase
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/Sybase/Sybase.so
%{_mandir}/man3/DBD::Sybase.3*
%{_examplesdir}/%{name}-%{version}
