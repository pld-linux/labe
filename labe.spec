%define		_subver	2
Summary:	LABE stands for Ldap Address Book Editor
Summary(pl):	LABE jest edytorem ksi±¿ki adresowej LDAP
Name:		labe
Version:	3.3
Release:	0.%{_subver}.2
License:	GPL
Group:		Applications/Databases
Source0:	http://www.savoirfairelinux.com/%{name}/%{name}-%{version}-%{_subver}.tgz
# Source0-md5:	f7b1adfe0c0194403279d16b96f51d31
Source1:	%{name}-httpd.conf
Source2:	%{name}-pl.inc
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-pl.patch
Patch2:		%{name}-path.patch
URL:		http://www.savoirfairelinux.com/labe/
BuildArch:	noarch
Requires:	openldap
Requires:	php-ldap
Requires:	php-pcre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LABE is a web application created to administrate a centralised LDAP
directory, compatible with Mozilla, Evolution and Outlook.

%description -l pl
LABE jest aplikacj± WWW stworzon± do scentralizowanego administrowania
katalogiem LDAP, kompatybilnego z Mozill±, Evolution i Outlookiem.

%prep
%setup -q -n %{name}-%{version}-%{_subver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} create_dir \
	DESTDIR=$RPM_BUILD_ROOT \
	ROOT=%{_datadir}

%{__make} copy \
	DESTDIR=$RPM_BUILD_ROOT \
	ROOT=%{_datadir}

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/httpd/httpd.conf,%{_datadir}/openldap/schema}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/httpd.conf/99_%{name}.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/lang/pl.inc
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/uninstall.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/restore_old_configs.sh
mv $RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/extension.schema $RPM_BUILD_ROOT%{_datadir}/openldap/schema/extension.schema

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/CHANGELOG doc/README doc/TODO
%{_sysconfdir}/%{name}
%{_datadir}/openldap/schema/extension.schema
%{_sysconfdir}/httpd/httpd.conf/99_%{name}.conf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/class
%{_datadir}/%{name}/inc
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/templates
%dir %attr(755,http,root) %{_datadir}/%{name}/templates_c
%{_datadir}/%{name}/index.php
%attr(755,root,root) %{_datadir}/%{name}/setup.sh
%attr(755,root,root) %{_datadir}/%{name}/restore_old_configs.sh
