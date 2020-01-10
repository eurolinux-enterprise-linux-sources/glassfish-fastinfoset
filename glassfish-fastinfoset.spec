Name: glassfish-fastinfoset
Version: 1.2.12
Release: 8%{?dist}
Summary: Fast Infoset
Group: Development/Libraries
License: ASL 2.0
URL: https://fi.dev.java.net

# svn export https://svn.java.net/svn/fi~svn/tags/1_2_12/ glassfish-fastinfoset-1.2.12
# find glassfish-fastinfoset-1.2.12/ -name '*.class' -delete
# find glassfish-fastinfoset-1.2.12/ -name '*.jar' -delete
# rm -rf glassfish-fastinfoset-1.2.12/roundtrip-tests
# tar czf glassfish-fastinfoset-1.2.12-src-svn.tar.gz glassfish-fastinfoset-1.2.12
Source0: %{name}-%{version}-src-svn.tar.gz

# Replace javax.xml.bind jsr173_api with stax (bea-)stax-api:
Patch0: %{name}-%{version}-pom.patch

BuildRequires: maven-local

Requires: bea-stax-api
Requires: jpackage-utils
Requires: xsom

BuildArch: noarch


%package javadoc
Group: Development/Libraries
Summary: Javadoc for %{name}
Requires: jpackage-utils


%description
Fast Infoset specifies a standardized binary encoding for the XML Information
Set. An XML infoset (such as a DOM tree, StAX events or SAX events in
programmatic representations) may be serialized to an XML 1.x document or, as
specified by the Fast Infoset standard, may be serialized to a fast infoset
document.  Fast infoset documents are generally smaller in size and faster to
parse and serialize than equivalent XML documents.


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0 -p1


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Oct 24 2013 Ade Lee <alee@redhat.com> 1.2.12-8
- Resolves: rhbz#1017803 -  glassfish-fastinfoset: mock build failed on RHEL 7

* Fri Feb 22 2013 Juan Hernandez <juan.hernandez@redhat.com> - 1.2.12-7
- Remove the wagon-webdav build extension (rhbz 914033)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.12-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 7 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.2.12-3
- Changed name from glassfish-fi to glassfish-fastinfoset

* Tue Feb 14 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.2.12-2
- Cleanup of the spec file

* Sat Jan 21 2012 Marek Goldmann <mgoldman@redhat.com> 1.2.12-1
- Initial packaging
