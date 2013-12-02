Name:           genivi-shell
Version:        0.0.1
Release:        0
Summary:        GENIVI Shell Plugin-in
License:        Apache-2.0
Group:          Graphics & UI Framework/Wayland Window System
Url:            http://git.projects.genivi.org/wayland-ivi-extension.git
Source0:         %name-%version.tar.gz
BuildRequires:  autoconf >= 2.64, automake >= 1.11
BuildRequires:  cmake
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(weston)
BuildRequires:  pkgconfig(xkbcommon)

%description
This package provides a weston plugin implementing the GENIVI layer
manager client interface.

%package devel
Summary: Development files for package %{name}
Group:   Graphics & UI Framework/Development
%description devel
This package provides header files and other developer files needed for
creating GENIIVI layer manager clients.

%package libs
Summary: Client libraries for package %{name}
Group:   Graphics & UI Framework/Libraries
%description libs
This package provides the client libraries needed for
running GENIIVI layer manager clients.


%prep
%setup -q

%cmake .

%build

make %{?_smp_mflags};

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/weston/ivi-shell.so

%files devel
%defattr(-,root,root)
%{_bindir}/EGLWLMockNavigation
%{_includedir}/ilm/ilm_client.h
%{_includedir}/ilm/ilm_common.h
%{_includedir}/ilm/ilm_configuration.h
%{_includedir}/ilm/ilm_control.h
%{_includedir}/ilm/ilm_platform.h
%{_includedir}/ilm/ilm_tools.h
%{_includedir}/ilm/ilm_types.h
%{_includedir}/layermanager/Bitmap.h
%{_includedir}/layermanager/IlmMatrix.h
%{_includedir}/layermanager/IpcModuleLoader.h
%{_includedir}/layermanager/Log.h
%{_includedir}/layermanager/LogMessageBuffer.h

%files libs
%defattr(-,root,root)
%{_libdir}/libilmClient.so
%{_libdir}/libilmCommon.so
%{_libdir}/libilmControl.so
