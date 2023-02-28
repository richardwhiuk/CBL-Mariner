Summary:        Google's data interchange format
Name:           protobuf
Version:        3.17.3
Release:        2%{?dist}
License:        BSD
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Libraries
URL:            https://developers.google.com/protocol-buffers/
Source0:        https://github.com/protocolbuffers/protobuf/releases/download/v%{version}/%{name}-all-%{version}.tar.gz
# Below is a manually created tarball, no download link.
# We're using pre-populated maven modules and plugins from this tarball, since network is disabled during build time.
# Use generate_source_tarbbal.sh to get this generated from a source code file.
# Unfortunately it is not possible to just run mvn dependency:go-offline as it does not download things reqires for specific targets.
# So you would need to run all targets used in this spec file such as: "mvn package", "mvn install", "maven test" to download all dependecies.
# How to re-build this file:
#   1. wget https://github.com/protocolbuffers/protobuf/releases/download/v%%{version}/%%{name}-all-%%{version}.tar.gz
#   2. tar -xf %%{name}-%%{version}.tar.gz
#   3. cd %%{name}-%%{version}
#   4. mvm verify --fail-never
#   5. cd /home/{user}/.m2
#   5. tar  --sort=name \
#           --mtime="2021-04-26 00:00Z" \
#           --owner=0 --group=0 --numeric-owner \
#           --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
#           -cf %%{name}-%%{version}-m2.tar.gz repository/
#
Source1:        %{name}-%{version}-m2.tar.gz
BuildRequires:  curl
BuildRequires:  libstdc++
BuildRequires:  make
BuildRequires:  unzip
Provides:       %{name}-compiler = %{version}-%{release}
Provides:       %{name}-lite = %{version}-%{release}

%description
Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data. You can find protobuf's documentation on the Google Developers site.

%package        devel
Summary:        Development files for protobuf
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-lite-devel = %{version}-%{release}

%description    devel
The protobuf-devel package contains libraries and header files for
developing applications that use protobuf.

%package        static
Summary:        protobuf static lib
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-lite-static = %{version}-%{release}

%description    static
The protobuf-static package contains static protobuf libraries.

%package -n     python3-%{name}
Summary:        protobuf python3 lib
Group:          Development/Libraries
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       %{name} = %{version}-%{release}
Requires:       python3
Requires:       python3-libs
Provides:       %{name}-python3 = %{version}-%{release}

%description -n python3-%{name}
This contains protobuf python3 libraries.

%package        java
Summary:        protobuf java lib
Group:          Development/Libraries
BuildRequires:  chkconfig
BuildRequires:  maven
BuildRequires:  msopenjdk-11
Requires:       %{name} = %{version}-%{release}
Requires:       msopenjdk-11
Provides:       %{name}-java = %{version}-%{release}

%description    java
This contains protobuf java libraries.

%prep
%autosetup
# populate m2 cache
mkdir /root/.m2
pushd /root/.m2
tar -xf %{SOURCE1} --no-same-owner
popd

%build
%configure --disable-silent-rules
export JAVA_HOME=$(find %{_lib}/jvm -name "openjdk*")
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(find $JAVA_HOME/lib -name "jli")
%make_build

# build python subpackage
pushd python
%py3_build
popd

# build java subpackage
pushd java
mvn -o package -DskipTests
popd

%install
%make_install

# install python subpackage
pushd python
%py3_install
popd

# install java subpackage
pushd java
mvn -o install -DskipTests
install -vdm755 %{buildroot}%{_libdir}/java/protobuf
install -vm644 core/target/protobuf-java-%{version}.jar %{buildroot}%{_libdir}/java/protobuf
install -vm644 util/target/protobuf-java-util-%{version}.jar %{buildroot}%{_libdir}/java/protobuf
popd

%ldconfig_scriptlets

%check
# run C++ unit tests
%make_build check

# run java subpackage tests
cd java
mvn -o test

%files
%defattr(-,root,root)
%license LICENSE
%{_bindir}/protoc
%{_libdir}/libprotobuf-lite.so.28*
%{_libdir}/libprotobuf.so.28*
%{_libdir}/libprotoc.so.28*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libprotobuf-lite.la
%{_libdir}/libprotobuf-lite.so
%{_libdir}/libprotobuf.la
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.la
%{_libdir}/libprotoc.so

%files static
%defattr(-,root,root)
%{_libdir}/libprotobuf-lite.a
%{_libdir}/libprotobuf.a
%{_libdir}/libprotoc.a

%files -n python3-%{name}
%{python3_sitelib}/*

%files java
%{_libdir}/java/protobuf/*.jar

%changelog
* Fri Feb 24 2023 Mykhailo Bykhovtsev <mbykhovtsev@microsoft.com> - 3.17.3-2
- Re-added back java subpackage
- Added check section for running tests

* Fri Jul 23 2021 Thomas Crain <thcrain@microsoft.com> - 3.17.3-1
- Upgrade to latest upstream version, using upstream release tarball
- Add soname version to %%file packaging
- Remove protobuf-m2-%{version}.tar.gz source tarball (no longer needed with java removal)
- Change python3 subpackage name to python3-protobuf, to match Mariner naming conventions
- Remove python 2 subpackage
- Lint spec

* Mon Dec 07 2020 Joe Schmitt <joschmit@microsoft.com> - 3.6.1-9
- Remove java subpackage.

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 3.6.1-8
- Added %%license line automatically

*   Thu Apr 30 2020 Emre Girgin <mrgirgin@microsoft.com> 3.6.1-7
-   Renaming apache-maven to maven

*   Wed Apr 29 2020 Nicolas Guibourge <nicolasg@microsoft.com> 3.6.1-6
-   Add add JAVA_HOME and path to libjli.so in LD_LIBRARY_PATH

*   Mon Apr 13 2020 Jon Slobodzian <joslobo@microsoft.com> 3.6.1-5
-   Verified license. Removed sha1. Fixed Source0 URL. Updated URL.

*   Thu Apr 09 2020 Andrew Phelps <anphel@microsoft.com> 3.6.1-4
-   Support building offline.

*   Thu Feb 27 2020 Andrew Phelps <anphel@microsoft.com> 3.6.1-3
-   Removed "--build=unknown-unknown-linux" configure flag

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 3.6.1-2
-   Initial CBL-Mariner import from Photon (license: Apache2).

*   Tue Sep 18 2018 Tapas Kundu <tkundu@vmware.com> 3.6.1-1
-   Update to version 3.6.1

*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 3.2.0-6
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.

*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.2.0-5
-   Use python2 explicitly while building

*   Thu May 18 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.2.0-4
-   Renamed openjdk to openjdk8

*   Fri Apr 28 2017 Siju Maliakkal <smaliakkal@vmware.com> 3.2.0-3
-   Update python3 version

*   Thu Apr 13 2017 Vinay Kulkarni <kulkarniv@vmware.com> 3.2.0-2
-   Build protobuf-java.

*   Fri Mar 31 2017 Rongrong Qiu <rqiu@vmware.com> 3.2.0-1
-   Upgrade to 3.2.0

*   Tue Mar 28 2017 Vinay Kulkarni <kulkarniv@vmware.com> 2.6.1-3
-   Build protobuf-python.

*   Mon Mar 20 2017 Vinay Kulkarni <kulkarniv@vmware.com> 2.6.1-2
-   Build static lib.

*   Fri Mar 03 2017 Xiaolin Li <xiaolinl@vmware.com> 2.6.1-1
-   Initial packaging for Photon
