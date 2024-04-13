#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.02.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kalgebra
Summary:	Kalgebra
Name:		ka6-%{kaname}
Version:	24.02.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	38179b327a754467a23a4bc5679f6c68
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6WebEngine-devel >= 5.15.5
BuildRequires:	Qt6Widgets-devel >= 5.11.1
BuildRequires:	Qt6Xml-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-analitza-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAlgebra is a fully featured calculator that lets you plot different
types of 2D and 3D functions and to calculate easy (and not so easy)
calculations, such as addition, trigonometric functions or
derivatives.

The application has been thought to be progressively understood for
students, so that starting to use it doesn't get in the way. The
language is deeply integrated with the UI, providing a dictionary with
representations for all the available operations, code highlighting
and code completion.

%description -l pl.UTF-8
KAlgebra jest wszechstronnym kalkulatorem, pozwalającym rysować różne
typy funkcji dwu- i trójwymiarowych i przeliczać łatwe (i nie tylko)
operacje matematycze, jak dodawanie, funkcje trygonometryczne i
pochodne.

Aplikacja została pomyślana tak, aby była stopniowo rozumiana przez
studentów. Język jest głęboko zintegrowany z interfejsem użykownika,
dostarczając słownik z reprezentacją wszystkich dostępnych operacji, a
także podświetlanie kodu i podpowiadanie dopełnień.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calgebra
%attr(755,root,root) %{_bindir}/kalgebra
%attr(755,root,root) %{_bindir}/kalgebramobile
%{_iconsdir}/hicolor/64x64/apps/kalgebra.png
%{_iconsdir}/hicolor/scalable/apps/kalgebra.svgz
%{_datadir}/katepart5/syntax/kalgebra.xml
%{_datadir}/metainfo/org.kde.graphsplasmoid.appdata.xml
%{_datadir}/metainfo/org.kde.kalgebra.appdata.xml
%{_datadir}/metainfo/org.kde.kalgebramobile.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/contents/ui/config.ui
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/metadata.json
%{_desktopdir}/org.kde.kalgebra.desktop
%{_desktopdir}/org.kde.kalgebramobile.desktop
