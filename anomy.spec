Summary:	Anomy Sanitizer
Name:		anomy-sanitizer
Version:	1.76
Release:	5
License:	GPL
Group:		Networking/Mail
URL:		https://mailtools.anomy.net/
Source:		http://mailtools.anomy.net/dist/%{name}-%{version}.tar.bz2
Source1:	%{name}.conf.bz2
Requires:	perl
BuildArch:	noarch

%description
The Anomy sanitizer is what most people would call "an email virus scanner".
That description is not totally accurate, but it does cover one of the more
important jobs that the sanitizer can do for you - it can scan email
attachments for viruses. Other things it can do:

* Disable potentially dangerous HTML code, such as javascript, within incoming
  email.
* Protect you from email-based break-in attempts which exploit bugs in common
  email programs (Outlook, Eudora, Pine, ...).
* Block or "mangle" attachments based on their file names. This way if you
  don't need to receive e.g. visual basic scripts, then you don't have to worry
  about the security risk they imply (the ILOVEYOU virus was a visual basic
  program). This lets you protect yourself and your users from whole classes
  of attacks, without relying on complex, resource intensive and outdated
  virus scanning solutions.

%prep
%setup -q -n anomy

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/var/spool/anomy

cp -R bin/Anomy %{buildroot}%{perl_vendorlib}/Anomy
cp -r bin/*.pl %{buildroot}%{_bindir}
bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf

%files
%defattr(-, root, root, 0755)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{perl_vendorlib}/Anomy/*
%{_bindir}/*
%dir /var/spool/anomy
