Name:           genivi-shell
Version:        0.1.3
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
BuildRequires:  weston-ivi-shell
BuildRequires:  weston-ivi-shell-devel

%description
This package provides a weston plugin implementing the GENIVI layer
manager client interface.

%package devel
Summary: Development files for package %{name}
Group:   Graphics & UI Framework/Development
%description devel
This package provides header files and other developer files needed for
creating GENIVI layer manager clients.

%prep
%setup -q

%cmake .

%build

make %{?_smp_mflags}

%install
%make_install

# install client header of ivi-application/controller
install -m 755 protocol/ivi-controller-client-protocol.h %{buildroot}%{_includedir}/ilm
install -m 755 protocol/ivi-application-client-protocol.h %{buildroot}%{_includedir}/ilm

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/IVISurfaceCreator
%{_bindir}/LayerManagerControl
%{_bindir}/EGLWLMockNavigation
%{_libdir}/libilmClient.so.*
%{_libdir}/libilmCommon.so.*
%{_libdir}/libilmControl.so.*
%{_libdir}/weston/ivi-controller.so

%files devel
%defattr(-,root,root)
%{_includedir}/ilm/ilm_client.h
%{_includedir}/ilm/ilm_common.h
%{_includedir}/ilm/ilm_configuration.h
%{_includedir}/ilm/ilm_control.h
%{_includedir}/ilm/ilm_platform.h
%{_includedir}/ilm/ilm_tools.h
%{_includedir}/ilm/ilm_types.h
%{_includedir}/ilm/ivi-controller-client-protocol.h
%{_includedir}/ilm/ivi-application-client-protocol.h
%{_libdir}/libilmClient.so
%{_libdir}/libilmCommon.so
%{_libdir}/libilmControl.so
