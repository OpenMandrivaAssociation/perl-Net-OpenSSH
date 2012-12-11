%define upstream_name    Net-OpenSSH
%define upstream_version 0.52

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl SSH client package implemented on top of OpenSSH
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	openssh-clients
Requires:	openssh-clients
BuildArch:	noarch

%description
Net::OpenSSH is a secure shell client package implemented on top of OpenSSH
binary client ('ssh').

This package is implemented around the multiplexing feature found in
later versions of OpenSSH. That feature allows reuse of a previous SSH
connection for running new commands (I believe that OpenSSH 4.1 is the
first one to provide all the required functionality).

When a new Net::OpenSSH object is created, the OpenSSH 'ssh' client is
run in master mode, establishing a permanent (actually, for the
lifetime of the object) connection to the server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.520.0-1mdv2011.0
+ Revision: 673817
- update to new version 0.52

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.500.0-3
+ Revision: 657804
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.500.0-2mdv2011.0
+ Revision: 624998
- Changed the summary and revamped the description
- import perl-Net-OpenSSH

