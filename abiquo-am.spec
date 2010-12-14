%define abiquo_basedir /opt/abiquo

Name:     abiquo-am
Version: 1.7
Release: 3%{?dist}%{?buildstamp}
Summary:  Abiquo Appliance Manager
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the enterprise am component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.


%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
chmod +rw WEB-INF -R
chmod +rw META-INF -R
cp -r . $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/am/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
#%doc %{_docdir}/%{name}/README
%{abiquo_basedir}/tomcat/webapps/am
#%config(noreplace) %{abiquo_basedir}/config/*



%changelog
* Tue Dec 14 2010 Sergio Rubio <rubiojr@frameos.org> - 1.7-3
- remove libs from WAR

* Tue Dec 14 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- updated to use the new WAR packaging system

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- Added buildstamp to the package

* Mon Jul 05 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Updated to upstream 1.6

* Wed May 26 2010 Sergio Rubio srubio@abiquo.com 1.5.1
- Initial Release
