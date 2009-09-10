%define name	skyutils
%define version	2.8
%define release	%mkrel 6

%define major	2.8
%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d

Summary: 	Library package needed by smssend
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://zekiller.skytech.org/fichiers/%{name}-%{version}.tar.bz2
URL: 		http://zekiller.skytech.org/coders_en.html
License: 	GPL
Group: 		Development/C
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	sed, /sbin/ldconfig

%description
Author Christophe CALMEJANE says:
This package contains utils functions that I use in many
of my projects. From chained list to HTTP protocol, you
may find many useful functions.

This package is needed if you want to install smssend.

%package -n %libname
Group:		System/Libraries
Summary:	Library package needed by smssend

%description -n %libname
Author Christophe CALMEJANE says:
This package contains utils functions that I use in many
of my projects. From chained list to HTTP protocol, you
may find many useful functions.

This package is needed if you want to install smssend.

%package -n %libname-devel
Summary:	Development parts of %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel %{name}-devel

%description -n %libname-devel
Static library of %{name}


%prep
%setup -q

%build

#enable ansi soooo beutiful...

%configure --enable-ansi

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/skyutils-config

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc README
%_libdir/libskyutils-*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%_bindir/*
%_libdir/libskyutils.so
%_libdir/libskyutils.*a
%_includedir/*.h

