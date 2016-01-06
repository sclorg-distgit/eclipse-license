%{?scl:%scl_package eclipse-license}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global license_ver 1.0.1
%global qualifier v20140414-1359
%global gittag org.eclipse.license-license-%{license_ver}.%{qualifier}

Name:      %{?scl_prefix}eclipse-license
Version:   %{license_ver}
Release:   7.1.bs2%{?dist}
Summary:   Shared license feature for Eclipse

License:   EPL
URL:       http://wiki.eclipse.org/CBI
Source0:   http://git.eclipse.org/c/cbi/org.eclipse.license.git/snapshot/%{gittag}.tar.bz2

BuildArch: noarch

BuildRequires: %{?scl_prefix}tycho
BuildRequires: %{?scl_prefix}tycho-extras
BuildRequires: %{?scl_prefix}eclipse-filesystem

Requires: %{?scl_prefix}eclipse-filesystem

%description
Shared license feature for Eclipse. Other features may consume this
feature to avoid unnecessary duplication of license boiler plate.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n %{gittag}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build -j
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc org.eclipse.license/epl-v10.html

%changelog
* Tue Jun 30 2015 Mat Booth <mat.booth@redhat.com> - 1.0.1-7.1
- Import latest from Fedora

* Tue Jun 30 2015 Mat Booth <mat.booth@redhat.com> - 1.0.1-7
- BR on eclipse-filesystem

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 26 2014 Mat Booth <mat.booth@redhat.com> - 1.0.1-5
- Build/install with xmvn
- Require eclipse-filesystem

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Mat Booth <mat.booth@redhat.com> - 1.0.1-3
- Update to latest upstream.

* Thu Mar 13 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-2
- Use Xmvn.

* Thu Mar 13 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-1
- Initial version of license shared feature.