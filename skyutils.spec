%define name	skyutils
%define version	2.8
%define release	11

%define major	2.8
%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d

Summary: 	Library package needed by smssend
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://zekiller.skytech.org/fichiers/%{name}-%{version}.tar.bz2
Patch0:		skyutils-2.8-fix-link.patch
Patch1:		skyutils-2.8-fix-str-fmt.patch
URL: 		https://zekiller.skytech.org/coders_en.html
License: 	GPL
Group: 		Development/C
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	sed
BuildRequires:	openssl-devel

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
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %libname-devel
Static library of %{name}


%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi
%configure2_5x --enable-ansi
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

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



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8-10mdv2011.0
+ Revision: 614897
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 2.8-9mdv2010.1
+ Revision: 536662
- rebuild

* Tue Feb 23 2010 Funda Wang <fwang@mandriva.org> 2.8-8mdv2010.1
+ Revision: 509860
- BR openssl

* Mon Feb 22 2010 Funda Wang <fwang@mandriva.org> 2.8-7mdv2010.1
+ Revision: 509753
- fix requires and provides
- fix linkage
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild
    - fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.8-2mdv2008.1
+ Revision: 127328
- kill re-definition of %%buildroot on Pixel's request
- import skyutils


* Thu Oct 27 2005 Lenny Cartier <lenny@mandriva.com> 2.8-2mdk
- rebuild

* Fri Jul 29 2005 Lenny Cartier <lenny@mandriva.com> 2.8-1mdk
- 2.8

* Wed Feb 02 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.7-1mdk
- 2.7

* Thu Jan 13 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.6-2mdk
- rebuild

* Fri Dec 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.6-1mdk
- 2.6
- fix provides
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- spec cosmetics

* Thu Feb 13 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.4-1mdk
- 2.4
- use mklibname

* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.1-2mdk
- rebuild

* Tue Apr 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.1-1mdk
- 2.1

* Wed Apr 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.0-1mdk
- 2.0

* Wed Oct 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.14-1mdk
- 1.14

* Wed Aug 29 2001  Lenny Cartier <lenny@mandrakesoft.com> 1.13-1mdk
- updated by Christian Zoffoli <czoffoli@linux-mandrake.com> :
	- updated to 1.13
	- fixed typo in description
	- fixed some links

* Mon Jan 29 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.10-1mdk
- updated to 1.10

* Tue Dec 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.07-1mdk 
- updated to 1.07

* Wed Oct 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.05-1mdk
- used srpm from Alexander Skwar :
	Tue Oct  3 2000 Alexander Skwar <ASkwar@linux-mandrake.com> 
	- First Mandrake version



