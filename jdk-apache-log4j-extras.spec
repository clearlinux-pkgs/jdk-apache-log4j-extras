Name     : jdk-apache-log4j-extras
Version  : 1.2.17
Release  : 4
URL      : https://repo1.maven.org/maven2/log4j/apache-log4j-extras/1.2.17/apache-log4j-extras-1.2.17.jar
Source0  : https://repo1.maven.org/maven2/log4j/apache-log4j-extras/1.2.17/apache-log4j-extras-1.2.17.jar
Source1  : https://repo1.maven.org/maven2/log4j/apache-log4j-extras/1.2.17/apache-log4j-extras-1.2.17.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-apache-log4j-extras-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-apache-log4j-extras package.
Group: Data

%description data
data components for the jdk-apache-log4j-extras package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/apache-log4j-extras.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/apache-log4j-extras.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/apache-log4j-extras.xml \
%{buildroot}/usr/share/maven-poms/apache-log4j-extras.pom \
%{buildroot}/usr/share/java/apache-log4j-extras.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/apache-log4j-extras.jar
/usr/share/maven-metadata/apache-log4j-extras.xml
/usr/share/maven-poms/apache-log4j-extras.pom
