#
# Conditional build:
%bcond_with	tests		# perform "make test" (require Internet connection)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Google-Images
Summary:	WWW::Google::Images - Google Images Agent
Summary(pl):	WWW::Google::Images - agent Google Images
Name:		perl-WWW-Google-Images
Version:	0.5.1
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	09cdaa726f31fca0d7d9894d8f52d260
URL:		http://search.cpan.org/dist/WWW-Google-Images/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-URI
BuildRequires:	perl-WWW-Mechanize >= 0.5
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module may be used search images on Google. Its interface is
heavily inspired from WWW::Google::Groups.

%description -l pl
Ten modu³ mo¿e byæ u¿ywany do wyszukiwania obrazków w Google. Jego
interfejs jest w znacznym stopniu zainspirowany WWW::Google::Groups.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/WWW/Google/*.pm
%{perl_vendorlib}/WWW/Google/Images
%{_mandir}/man?/*
