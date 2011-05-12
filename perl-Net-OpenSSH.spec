%define upstream_name    Net-OpenSSH
%define upstream_version 0.52

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl SSH client package implemented on top of OpenSSH
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: openssh-clients
Requires: openssh-clients
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


