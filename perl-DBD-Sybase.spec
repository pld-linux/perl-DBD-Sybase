%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Sybase
Summary:	DBD::Sybase perl module
Summary(pl):	Modu³ perla DBD::Sybase
Name:		perl-DBD-Sybase
Version:	0.95
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3e905acf6fe894b59112d94a00e4c1f
BuildRequires:	freetds-devel
BuildRequires:	perl-DBI >= 1.00
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Sybase - a Sybase and MS SQL DBI driver.

%description -l pl
DBD::Sybase - sterownik DBI do Sybase i MS SQL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
SYBASE=/usr ; export SYBASE
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor 

%{__make} OPTIMIZE="%{rpmcflags}"

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
