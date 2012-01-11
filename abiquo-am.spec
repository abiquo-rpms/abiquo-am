%define abiquo_basedir /opt/abiquo

Name:     abiquo-am
Version:  2.0
Release:  1%{?dist}%{?buildstamp}
Summary:  Abiquo Appliance Manager
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  %{?abiquo_binaries_url}am.war
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core
BuildArch: noarch
BuildRequires: unzip

%description
Next Generation Cloud Management Solution

This package contains the enterprise am component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/am
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/am/ %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc %{_docdir}/%{name}/README
%{abiquo_basedir}/tomcat/webapps/am
#%config(noreplace) %{abiquo_basedir}/config/*



%changelog
* Mon Dec 19 2011 Sergio Rubio <srubio@abiquo.com> - 2.0-1
- bumped version to 2.0

* Fri Sep 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-1
- bumped version to 1.8.5

* Mon May 23 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- updated to 1.8

* Thu Apr 14 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7.6-1
- bumped version

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump

* Mon Feb 14 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6
- fixed release string

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5.GA
- GA build

* Thu Dec 30 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- use the AM WAR as the source

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
