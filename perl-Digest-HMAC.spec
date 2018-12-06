#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-HMAC
Version  : 1.03
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Digest-HMAC-1.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Digest-HMAC-1.03.tar.gz
Summary  : Keyed-Hashing for Message Authentication
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1.  The HMAC mechanism is described in
RFC 2104.

%package dev
Summary: dev components for the perl-Digest-HMAC package.
Group: Development
Provides: perl-Digest-HMAC-devel = %{version}-%{release}

%description dev
dev components for the perl-Digest-HMAC package.


%prep
%setup -q -n Digest-HMAC-1.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Digest/HMAC.pm
/usr/lib/perl5/vendor_perl/5.28.1/Digest/HMAC_MD5.pm
/usr/lib/perl5/vendor_perl/5.28.1/Digest/HMAC_SHA1.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Digest::HMAC.3
/usr/share/man/man3/Digest::HMAC_MD5.3
/usr/share/man/man3/Digest::HMAC_SHA1.3
