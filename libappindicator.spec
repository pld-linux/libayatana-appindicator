#
# Conditional build:
%bcond_without	gtk2		# GTK+ 2.x version
%bcond_without	gtk3		# GTK+ 3.x version
%bcond_without	static_libs	# static libraries
%bcond_without	dotnet		# Mono bindings
%bcond_without	vala		# Vala APIs

%ifnarch %{ix86} %{x8664} arm aarch64 ia64 mips ppc ppc64 s390x sparc sparcv9 sparc64
%undefine	with_dotnet
%endif
%ifarch i386
%undefine	with_dotnet
%endif
Summary:	Application indicators library
Summary(pl.UTF-8):	Biblioteka wskaźników aplikacji
Name:		libappindicator
Version:	12.10.0
Release:	6
License:	LGPL v2.1 or LGPL v3
Group:		Libraries
#Source0Download: https://launchpad.net/libappindicator/+download
Source0:	http://launchpad.net/libappindicator/12.10/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	41910f2005edee9240da1e53fffcdc12
Patch0:		%{name}-python.patch
Patch1:		%{name}-mono.patch
Patch2:		mono4.patch
URL:		https://launchpad.net/libappindicator
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-glib-devel >= 0.82
%{?with_dotnet:BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.1}
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gobject-introspection-devel >= 0.10
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.18}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	gtk-doc >= 1.9
%{?with_gtk2:BuildRequires:	libdbusmenu-gtk2-devel >= 0.5.90}
%{?with_gtk3:BuildRequires:	libdbusmenu-gtk3-devel >= 0.5.90}
%{?with_gtk2:BuildRequires:	libindicator-devel >= 0.4.93}
%{?with_gtk3:BuildRequires:	libindicator-gtk3-devel >= 0.4.93}
BuildRequires:	libtool >= 2:2.2
%{?with_dotnet:BuildRequires:	mono-csharp >= 1.0}
# for mono-nunit >= 2.4.7
%{?with_dotnet:BuildRequires:	mono-devel >= 2.4.7}
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.3.5
BuildRequires:	python-pygobject-devel >= 0.22
BuildRequires:	python-pygtk-devel >= 2:2.14.0
BuildRequires:	sed >= 4.0
%{?with_vala:BuildRequires:	vala >= 2:0.14.0}
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to allow applications to export a menu into the Unity Menu
bar. Based on KSNI it also works in KDE and will fallback to generic
Systray support if none of those are available.

%description -l pl.UTF-8
Biblioteka pozwalająca aplikacjom eksportować menu do paska menu
Unity. Jest oparta na KSNI, działa także w KDE, a w przypadku braku
obu - potrafi korzystać ze zwykłej szufladki systemowej.

%package gtk2
Summary:	Application indicators library (GTK+ 2.x version)
Summary(pl.UTF-8):	Biblioteka wskaźników aplikacji (wersja dla GTK+ 2.x)
Group:		Libraries
Requires:	glib2 >= 1:2.26
Requires:	gtk+2 >= 2:2.18
Requires:	libdbusmenu-gtk2 >= 0.5.90
Requires:	libindicator >= 0.4.93

%description gtk2
A library to allow applications to export a menu into the Unity Menu
bar. Based on KSNI it also works in KDE and will fallback to generic
Systray support if none of those are available.

This package contains GTK+ 2.x based version of libappindicator.

%description gtk2 -l pl.UTF-8
Biblioteka pozwalająca aplikacjom eksportować menu do paska menu
Unity. Jest oparta na KSNI, działa także w KDE, a w przypadku braku
obu - potrafi korzystać ze zwykłej szufladki systemowej.

Ten pakiet zawiera bibliotekę libappindicator opartą na GTK+ 2.x.

%package gtk2-devel
Summary:	Development files for libappindicator (GTK+ 2.x version)
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libappindicator (wersja dla GTK+ 2.x)
Group:		Development/Libraries
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26
Requires:	gtk+2-devel >= 2:2.18
Requires:	libdbusmenu-devel >= 0.5.90

%description gtk2-devel
This package contains the header files for developing applications
that use libappindicator (GTK+ 2.x version).

%description gtk2-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libappindicator (w wersji dla GTK+ 2.x).

%package gtk2-static
Summary:	Static libappindicator library (GTK+ 2.x version)
Summary(pl.UTF-8):	Statyczna biblioteka libappindicator (wersja dla GTK+ 2.x)
Group:		Development/Libraries
Requires:	%{name}-gtk2-devel = %{version}-%{release}

%description gtk2-static
Static libappindicator library (GTK+ 2.x version).

%description gtk2-static -l pl.UTF-8
Statyczna biblioteka libappindicator (wersja dla GTK+ 2.x).

%package -n dotnet-appindicator-sharp-gtk2
Summary:	Application indicators library for .NET (GTK+ 2.x version)
Summary(pl.UTF-8):	Biblioteka wskaźników aplikacji dla .NET (wersja GTK+ 2.x)
Group:		Libraries
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	dotnet-gtk-sharp2 >= 2.12.1

%description -n dotnet-appindicator-sharp-gtk2
Mono/.NET binding for libappindicator library (GTK+ 2.x version).

%description -n dotnet-appindicator-sharp-gtk2 -l pl.UTF-8
Wiązania Mono/.NET do biblioteki libappindicator (wersja GTK+ 2.x).

%package -n dotnet-appindicator-sharp-gtk2-devel
Summary:	Development files for appindicator .NET binding (GTK+ 2.x version)
Summary(pl.UTF-8):	Pliki programistyczne wiązania .NET do biblioteki appindicator (wersja GTK+ 2.x)
Group:		Development/Libraries
Requires:	dotnet-appindicator-sharp-gtk2 = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.12.1

%description -n dotnet-appindicator-sharp-gtk2-devel
Development files for appindicator .NET binding (GTK+ 2.x version).

%description -n dotnet-appindicator-sharp-gtk2-devel -l pl.UTF-8
Pliki programistyczne wiązania .NET do biblioteki appindicator (wersja
GTK+ 2.x).

%package -n python-appindicator-gtk2
Summary:	Python binding for appindicator library (GTK+ 2.x version)
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki appindicator (wersja GTK+ 2.x)
Group:		Libraries/Python
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	python-pygobject >= 0.22

%description -n python-appindicator-gtk2
Python binding for appindicator library (GTK+ 2.x version).

%description -n python-appindicator-gtk2 -l pl.UTF-8
Wiązanie Pythona do biblioteki appindicator (wersja GTK+ 2.x).

%package -n python-appindicator-gtk2-devel
Summary:	Development files for Python appindicator binding (GTK+ 2.x version)
Summary(pl.UTF-8):	Pliki programistyczne wiązania Pythona do biblioteki appindicator (wersja GTK+ 2.x)
Group:		Development/Libraries
Requires:	python-appindicator-gtk2 = %{version}-%{release}
Requires:	python-pygobject-devel >= 0.22

%description -n python-appindicator-gtk2-devel
Development files for Python appindicator binding (GTK+ 2.x version).

%description -n python-appindicator-gtk2-devel -l pl.UTF-8
Pliki programistyczne wiązania Pythona do biblioteki appindicator
(wersja GTK+ 2.x).

%package -n vala-libappindicator-gtk2
Summary:	Vala API for libappindicator library (GTK+ 2.x version)
Summary(pl.UTF-8):	API języka Vala do biblioteki libappindicator (wersja GTK+ 2.x)
Group:		Development/Libraries
Requires:	%{name}-gtk2-devel = %{version}-%{release}
Requires:	vala >= 2:0.14.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-libappindicator-gtk2
Vala API for libappindicator library (GTK+ 2.x version).

%description -n vala-libappindicator-gtk2 -l pl.UTF-8
API języka Vala do biblioteki libappindicator (wersja GTK+ 2.x).

%package gtk3
Summary:	Application indicators library (GTK+ 3.x version)
Summary(pl.UTF-8):	Biblioteka wskaźników aplikacji (wersja dla GTK+ 3.x)
Group:		Libraries
Requires:	glib2 >= 1:2.26
Requires:	gtk+3 >= 3.0
Requires:	libdbusmenu-gtk3 >= 0.5.90
Requires:	libindicator-gtk3 >= 0.4.93

%description gtk3
A library to allow applications to export a menu into the Unity Menu
bar. Based on KSNI it also works in KDE and will fallback to generic
Systray support if none of those are available.

This package contains GTK+ 3.x based version of libappindicator.

%description gtk3 -l pl.UTF-8
Biblioteka pozwalająca aplikacjom eksportować menu do paska menu
Unity. Jest oparta na KSNI, działa także w KDE, a w przypadku braku
obu - potrafi korzystać ze zwykłej szufladki systemowej.

Ten pakiet zawiera bibliotekę libappindicator opartą na GTK+ 3.x.

%package gtk3-devel
Summary:	Development files for libappindicator (GTK+ 3.x version)
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libappindicator (wersja dla GTK+ 3.x)
Group:		Development/Libraries
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26
Requires:	gtk+3-devel >= 3.0
Requires:	libdbusmenu-devel >= 0.5.90

%description gtk3-devel
This package contains the header files for developing applications
that use libappindicator (GTK+ 3.x version).

%description gtk3-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libappindicator (w wersji dla GTK+ 3.x).

%package gtk3-static
Summary:	Static libappindicator library (GTK+ 3.x version)
Summary(pl.UTF-8):	Statyczna biblioteka libappindicator (wersja dla GTK+ 3.x)
Group:		Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}

%description gtk3-static
Static libappindicator library (GTK+ 3.x version).

%description gtk3-static -l pl.UTF-8
Statyczna biblioteka libappindicator (wersja dla GTK+ 3.x).

%package -n vala-libappindicator-gtk3
Summary:	Vala API for libappindicator library (GTK+ 3.x version)
Summary(pl.UTF-8):	API języka Vala do biblioteki libappindicator (wersja GTK+ 3.x)
Group:		Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}
Requires:	vala >= 2:0.14.0

%description -n vala-libappindicator-gtk3
Vala API for libappindicator library (GTK+ 3.x version).

%description -n vala-libappindicator-gtk3 -l pl.UTF-8
API języka Vala do biblioteki libappindicator (wersja GTK+ 3.x).

%package apidocs
Summary:	API documentation for libappindicator library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libappindicator
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libappindicator library (both GTK+ 2.x and 3.x
based).

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libappindicator (zarówno w wersji GTK+
2.x, jak i 3.x).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# to allow deprecation warnings
%{__sed} -i -e 's/-Werror //' src/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

for gtkver in %{?with_gtk2:2} %{?with_gtk3:3}; do
install -d build-gtk$gtkver
cd build-gtk$gtkver
../%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--with-gtk=$gtkver \
	--with-html-dir=%{_gtkdocdir}
# -j1 because of racy mono build
%{__make} -j1
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT

for gtkver in %{?with_gtk2:2} %{?with_gtk3:3}; do
%{__make} -C build-gtk$gtkver install -j1 \
	DESTDIR=$RPM_BUILD_ROOT
done

%if %{with gtk2} || %{with gtk3}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%if %{with gtk2}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/appindicator/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/appindicator/*.a
%endif
%py_postclean
%else
# although mono bindings are built also --with-gtk=3, they are always GTK 2.x based
[ ! -d $RPM_BUILD_ROOT%{_prefix}/lib/mono ] || %{__rm} -r $RPM_BUILD_ROOT%{_prefix}/lib/mono
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	gtk2 -p /sbin/ldconfig
%postun	gtk2 -p /sbin/ldconfig

%post	gtk3 -p /sbin/ldconfig
%postun	gtk3 -p /sbin/ldconfig

%if %{with gtk2}
%files gtk2
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libappindicator.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappindicator.so.1
%{_libdir}/girepository-1.0/AppIndicator-0.1.typelib

%files gtk2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappindicator.so
%{_includedir}/libappindicator-0.1
%{_datadir}/gir-1.0/AppIndicator-0.1.gir
%{_pkgconfigdir}/appindicator-0.1.pc

%if %{with static_libs}
%files gtk2-static
%defattr(644,root,root,755)
%{_libdir}/libappindicator.a
%endif

%if %{with dotnet}
%files -n dotnet-appindicator-sharp-gtk2
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/appindicator-sharp
%{_prefix}/lib/mono/gac/policy.0.0.appindicator-sharp
# another location - for non-mono implementations?
# we don't use it, so it's disabled by -mono patch
#%dir %{_libdir}/cli/appindicator-sharp-0.1
#%{_libdir}/cli/appindicator-sharp-0.1/appindicator-sharp.dll
#%{_libdir}/cli/appindicator-sharp-0.1/appindicator-sharp.dll.config
#%{_libdir}/cli/appindicator-sharp-0.1/policy.*.appindicator-sharp.*

%files -n dotnet-appindicator-sharp-gtk2-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/appindicator-sharp
%{_pkgconfigdir}/appindicator-sharp-0.1.pc
%endif

%files -n python-appindicator-gtk2
%defattr(644,root,root,755)
%dir %{py_sitedir}/appindicator
%attr(755,root,root) %{py_sitedir}/appindicator/_appindicator.so
%{py_sitedir}/appindicator/__init__.py[co]

%files -n python-appindicator-gtk2-devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/appindicator.defs

%if %{with vala}
%files -n vala-libappindicator-gtk2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/appindicator-0.1.deps
%{_datadir}/vala/vapi/appindicator-0.1.vapi
%endif
%endif

%if %{with gtk3}
%files gtk3
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libappindicator3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappindicator3.so.1
%{_libdir}/girepository-1.0/AppIndicator3-0.1.typelib

%files gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappindicator3.so
%{_includedir}/libappindicator3-0.1
%{_datadir}/gir-1.0/AppIndicator3-0.1.gir
%{_pkgconfigdir}/appindicator3-0.1.pc

%if %{with static_libs}
%files gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libappindicator3.a
%endif

%if %{with vala}
%files -n vala-libappindicator-gtk3
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/appindicator3-0.1.deps
%{_datadir}/vala/vapi/appindicator3-0.1.vapi
%endif
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libappindicator
