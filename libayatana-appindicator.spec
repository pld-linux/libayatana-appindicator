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
Name:		libayatana-appindicator
Version:	0.5.5
Release:	1
License:	LGPL v2.1 or LGPL v3
Group:		Libraries
#Source0Download: https://github.com/AyatanaIndicators/libayatana-appindicator/releases
Source0:	https://github.com/AyatanaIndicators/libayatana-appindicator/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fd6705ad2793dced95056036ecd73b7f
Patch0:		libappindicator-mono.patch
Patch1:		mono4.patch
URL:		https://github.com/AyatanaIndicators/libayatana-appindicator
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-glib-devel >= 0.82
%{?with_dotnet:BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.1}
BuildRequires:	glib2-devel >= 1:2.35.4
BuildRequires:	gobject-introspection-devel >= 0.10
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.18}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	gtk-doc >= 1.14
%{?with_gtk2:BuildRequires:	libayatana-indicator-devel >= 0.6.0}
%{?with_gtk3:BuildRequires:	libayatana-indicator-gtk3-devel >= 0.6.0}
%{?with_gtk2:BuildRequires:	libdbusmenu-gtk2-devel >= 0.5.90}
%{?with_gtk3:BuildRequires:	libdbusmenu-gtk3-devel >= 0.5.90}
BuildRequires:	libtool >= 2:2.2
%{?with_dotnet:BuildRequires:	mono-csharp >= 1.0}
# for mono-nunit >= 2.4.7
%{?with_dotnet:BuildRequires:	mono-devel >= 2.4.7}
BuildRequires:	pkgconfig
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
Requires:	glib2 >= 1:2.35.4
Requires:	gtk+2 >= 2:2.18
Requires:	libayatana-indicator >= 0.6.0
Requires:	libdbusmenu-gtk2 >= 0.5.90

%description gtk2
A library to allow applications to export a menu into the Unity Menu
bar. Based on KSNI it also works in KDE and will fallback to generic
Systray support if none of those are available.

This package contains GTK+ 2.x based version of
libayatana-appindicator.

%description gtk2 -l pl.UTF-8
Biblioteka pozwalająca aplikacjom eksportować menu do paska menu
Unity. Jest oparta na KSNI, działa także w KDE, a w przypadku braku
obu - potrafi korzystać ze zwykłej szufladki systemowej.

Ten pakiet zawiera bibliotekę libayatana-appindicator opartą na GTK+
2.x.

%package gtk2-devel
Summary:	Development files for libayatana-appindicator (GTK+ 2.x version)
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libayatana-appindicator (wersja dla GTK+ 2.x)
Group:		Development/Libraries
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.35.4
Requires:	gtk+2-devel >= 2:2.18
Requires:	libdbusmenu-devel >= 0.5.90

%description gtk2-devel
This package contains the header files for developing applications
that use libayatana-appindicator (GTK+ 2.x version).

%description gtk2-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libayatana-appindicator (w wersji dla GTK+
2.x).

%package gtk2-static
Summary:	Static libayatana-appindicator library (GTK+ 2.x version)
Summary(pl.UTF-8):	Statyczna biblioteka libayatana-appindicator (wersja dla GTK+ 2.x)
Group:		Development/Libraries
Requires:	%{name}-gtk2-devel = %{version}-%{release}

%description gtk2-static
Static libayatana-appindicator library (GTK+ 2.x version).

%description gtk2-static -l pl.UTF-8
Statyczna biblioteka libayatana-appindicator (wersja dla GTK+ 2.x).

%package -n dotnet-appindicator-sharp-gtk2
Summary:	Application indicators library for .NET (GTK+ 2.x version)
Summary(pl.UTF-8):	Biblioteka wskaźników aplikacji dla .NET (wersja GTK+ 2.x)
Group:		Libraries
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	dotnet-gtk-sharp2 >= 2.12.1

%description -n dotnet-appindicator-sharp-gtk2
Mono/.NET binding for libayatana-appindicator library (GTK+ 2.x
version).

%description -n dotnet-appindicator-sharp-gtk2 -l pl.UTF-8
Wiązania Mono/.NET do biblioteki libayatana-appindicator (wersja GTK+
2.x).

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

%package -n vala-libayatana-appindicator-gtk2
Summary:	Vala API for libayatana-appindicator library (GTK+ 2.x version)
Summary(pl.UTF-8):	API języka Vala do biblioteki libayatana-appindicator (wersja GTK+ 2.x)
Group:		Development/Libraries
Requires:	%{name}-gtk2-devel = %{version}-%{release}
Requires:	vala >= 2:0.14.0
BuildArch:	noarch

%description -n vala-libayatana-appindicator-gtk2
Vala API for libayatana-appindicator library (GTK+ 2.x version).

%description -n vala-libayatana-appindicator-gtk2 -l pl.UTF-8
API języka Vala do biblioteki libayatana-appindicator (wersja GTK+
2.x).

%package gtk3
Summary:	Application indicators library (GTK+ 3.x version)
Summary(pl.UTF-8):	Biblioteka wskaźników aplikacji (wersja dla GTK+ 3.x)
Group:		Libraries
Requires:	glib2 >= 1:2.35.4
Requires:	gtk+3 >= 3.0
Requires:	libayatana-indicator-gtk3 >= 0.6.0
Requires:	libdbusmenu-gtk3 >= 0.5.90

%description gtk3
A library to allow applications to export a menu into the Unity Menu
bar. Based on KSNI it also works in KDE and will fallback to generic
Systray support if none of those are available.

This package contains GTK+ 3.x based version of
libayatana-appindicator.

%description gtk3 -l pl.UTF-8
Biblioteka pozwalająca aplikacjom eksportować menu do paska menu
Unity. Jest oparta na KSNI, działa także w KDE, a w przypadku braku
obu - potrafi korzystać ze zwykłej szufladki systemowej.

Ten pakiet zawiera bibliotekę libayatana-appindicator opartą na GTK+
3.x.

%package gtk3-devel
Summary:	Development files for libayatana-appindicator (GTK+ 3.x version)
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libayatana-appindicator (wersja dla GTK+ 3.x)
Group:		Development/Libraries
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.35.4
Requires:	gtk+3-devel >= 3.0
Requires:	libdbusmenu-devel >= 0.5.90

%description gtk3-devel
This package contains the header files for developing applications
that use libayatana-appindicator (GTK+ 3.x version).

%description gtk3-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libayatana-appindicator (w wersji dla GTK+
3.x).

%package gtk3-static
Summary:	Static libayatana-appindicator library (GTK+ 3.x version)
Summary(pl.UTF-8):	Statyczna biblioteka libayatana-appindicator (wersja dla GTK+ 3.x)
Group:		Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}

%description gtk3-static
Static libayatana-appindicator library (GTK+ 3.x version).

%description gtk3-static -l pl.UTF-8
Statyczna biblioteka libayatana-appindicator (wersja dla GTK+ 3.x).

%package -n vala-libayatana-appindicator-gtk3
Summary:	Vala API for libayatana-appindicator library (GTK+ 3.x version)
Summary(pl.UTF-8):	API języka Vala do biblioteki libayatana-appindicator (wersja GTK+ 3.x)
Group:		Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}
Requires:	vala >= 2:0.14.0

%description -n vala-libayatana-appindicator-gtk3
Vala API for libayatana-appindicator library (GTK+ 3.x version).

%description -n vala-libayatana-appindicator-gtk3 -l pl.UTF-8
API języka Vala do biblioteki libayatana-appindicator (wersja GTK+
3.x).

%package apidocs
Summary:	API documentation for libayatana-appindicator library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libayatana-appindicator
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libayatana-appindicator library (both GTK+ 2.x
and 3.x based).

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libayatana-appindicator (zarówno w wersji
GTK+ 2.x, jak i 3.x).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
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
%{__make} %{?with_dotnet:-j1}
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
%attr(755,root,root) %{_libdir}/libayatana-appindicator.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libayatana-appindicator.so.1
%{_libdir}/girepository-1.0/AyatanaAppIndicator-0.1.typelib

%files gtk2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libayatana-appindicator.so
%{_includedir}/libayatana-appindicator-0.1
%{_datadir}/gir-1.0/AyatanaAppIndicator-0.1.gir
%{_pkgconfigdir}/ayatana-appindicator-0.1.pc

%if %{with static_libs}
%files gtk2-static
%defattr(644,root,root,755)
%{_libdir}/libayatana-appindicator.a
%endif

%if %{with dotnet}
%files -n dotnet-appindicator-sharp-gtk2
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/ayatana-appindicator-sharp
%{_prefix}/lib/mono/gac/policy.0.0.ayatana-appindicator-sharp
# another location - for non-mono implementations?
# we don't use it, so it's disabled by -mono patch
#%dir %{_libdir}/cli/appindicator-sharp-0.1
#%{_libdir}/cli/appindicator-sharp-0.1/appindicator-sharp.dll
#%{_libdir}/cli/appindicator-sharp-0.1/appindicator-sharp.dll.config
#%{_libdir}/cli/appindicator-sharp-0.1/policy.*.appindicator-sharp.*

%files -n dotnet-appindicator-sharp-gtk2-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/ayatana-appindicator-sharp
%{_pkgconfigdir}/ayatana-appindicator-sharp-0.1.pc
%endif

%if %{with vala}
%files -n vala-libayatana-appindicator-gtk2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/ayatana-appindicator-0.1.deps
%{_datadir}/vala/vapi/ayatana-appindicator-0.1.vapi
%endif
%endif

%if %{with gtk3}
%files gtk3
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libayatana-appindicator3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libayatana-appindicator3.so.1
%{_libdir}/girepository-1.0/AyatanaAppIndicator3-0.1.typelib

%files gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libayatana-appindicator3.so
%{_includedir}/libayatana-appindicator3-0.1
%{_datadir}/gir-1.0/AyatanaAppIndicator3-0.1.gir
%{_pkgconfigdir}/ayatana-appindicator3-0.1.pc

%if %{with static_libs}
%files gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libayatana-appindicator3.a
%endif

%if %{with vala}
%files -n vala-libayatana-appindicator-gtk3
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/ayatana-appindicator3-0.1.deps
%{_datadir}/vala/vapi/ayatana-appindicator3-0.1.vapi
%endif
%endif

