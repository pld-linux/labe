# TODO
# - webapps
%define		_subver	2
Summary:	LABE stands for Ldap Address Book Editor
Summary(pl.UTF-8):	LABE jest edytorem książki adresowej LDAP
Name:		labe
Version:	3.3
Release:	0.%{_subver}.3
License:	GPL
Group:		Applications/Databases
Source0:	http://www.savoirfairelinux.com/labe/%{name}-%{version}-%{_subver}.tgz
# Source0-md5:	f7b1adfe0c0194403279d16b96f51d31
Source1:	%{name}-httpd.conf
Source2:	%{name}-pl.inc
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-pl.patch
Patch2:		%{name}-path.patch
Patch3:		%{name}-usability.patch
URL:		http://www.savoirfairelinux.com/labe/
Requires:	php(iconv)
Requires:	php(ldap)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LABE is a web application created to administrate a centralised LDAP
directory, compatible with Mozilla, Evolution and Outlook.

%description -l pl.UTF-8
LABE jest aplikacją WWW stworzoną do scentralizowanego administrowania
katalogiem LDAP, kompatybilnego z Mozillą, Evolution i Outlookiem.

%prep
%setup -q -n %{name}-%{version}-%{_subver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/httpd,%{_datadir}/openldap/schema}

%{__make} create_dir \
	DESTDIR=$RPM_BUILD_ROOT \
	ROOT=%{_datadir}

%{__make} copy \
	DESTDIR=$RPM_BUILD_ROOT \
	ROOT=%{_datadir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/%{name}.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/lang/pl.inc
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/uninstall.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/restore_old_configs.sh
mv $RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/extension.schema $RPM_BUILD_ROOT%{_datadir}/openldap/schema/extension.schema

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
elif [ -d /etc/httpd/httpd.conf ]; then
	ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 027
	if [ -d /etc/httpd/httpd.conf ]; then
		rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	else
		grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
			/etc/httpd/httpd.conf.tmp
		mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc doc/CHANGELOG doc/README doc/TODO
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/connect.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd/%{name}.conf
%{_datadir}/openldap/schema/extension.schema
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/class
%{_datadir}/%{name}/inc
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/templates
%dir %attr(755,http,root) %{_datadir}/%{name}/templates_c
%{_datadir}/%{name}/index.php
%attr(755,root,root) %{_datadir}/%{name}/setup.sh
%attr(755,root,root) %{_datadir}/%{name}/restore_old_configs.sh
