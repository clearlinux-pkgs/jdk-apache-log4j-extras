PKG_NAME := jdk-apache-log4j-extras
URL := https://repo1.maven.org/maven2/log4j/apache-log4j-extras/1.2.17/apache-log4j-extras-1.2.17.jar
ARCHIVES := https://repo1.maven.org/maven2/log4j/apache-log4j-extras/1.2.17/apache-log4j-extras-1.2.17.pom %{buildroot}

include ../common/Makefile.common
