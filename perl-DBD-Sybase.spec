%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Sybase
Summary:	DBD::Sybase perl module
Summary(pl):	Modu� perla DBD::Sybase
Name:		perl-DBD-Sybase
Version:	0.94
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	freetds-devel
BuildRequires:	perl-DBI >= 1.00
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Sybase - a Sybase and MS SQL DBI driver.

%description -l pl
DBD::Sybase - sterownik DBI do Sybase i MS SQL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
SYBASE=/usr ; export SYBASE
perl Makefile.PL </dev/null

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf BUGS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/DBD/Sybase.pm
%dir %{perl_sitearch}/auto/DBD/Sybase
%{perl_sitearch}/auto/DBD/Sybase/Sybase.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/Sybase/Sybase.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
