Summary:	An Open Source software construction tool
Summary(pl.UTF-8):	OpenSourcowe narzędzie do tworzenia oprogramowania
Name:		scons
Version:	4.4.0
Release:	2
License:	MIT
Group:		Development/Tools
Source0:	https://downloads.sourceforge.net/scons/SCons-%{version}.tar.gz
# Source0-md5:	056b141b420583e8faef8b1c64bc43cf
URL:		https://www.scons.org/
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3 >= 1:3.6
Requires:	python3-modules >= 1:3.6
Requires:	python3-devel-tools >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCons is an Open Source software construction tool - that is, a build
tool; an improved substitute for the classic Make utility; a better
way to build software. SCons is based on the design which won the
Software Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of all
dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines.
SCons uses MD5 signatures to rebuild only when the contents of a file
have really changed, not just when the timestamp has been touched.
SCons supports side-by-side variant builds, and is easily extended
with user-defined Builder and/or Scanner objects.

%description -l pl.UTF-8
SCons to wypuszczone z ogólnodostępnymi źródłami narzędzie do
budowania oprogramowania; jest to ulepszony zamiennik klasycznego
narzędzia Make. SCons jest oparte na opracowaniu, które wygrało
konkurs Software Carpentry owania w sierpniu 2000.

"Pliki konfiguracyjne" SCons to skrypty Pythona, co eliminuje potrzebę
uczenia się składni nowego narzędzia. SCons zachowuje globalny widok
wszystkich zależności w drzewie i może przeszukiwać pliki źródeł (lub
inne) w poszukiwaniu niejawnych zależności, takich jak pliki podane w
liniach #include. SCons używa sygnatur MD5, aby przebudowywać tylko
wtedy, kiedy naprawdę się zmieniła zawartość pliku, a nie przy samej
zmianie czasu modyfikacji. SCons obsługuje budowanie wariantowe i jest
łatwo rozszerzalny przez zdefiniowane przez użytkownika obiekty
Builder i/lub Scanner.

%prep
%setup -q -n SCons-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install \
	--install-data %{_mandir}/man1

# program not installed
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/scons-time.1*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/scons
%attr(755,root,root) %{_bindir}/scons-configure-cache
%attr(755,root,root) %{_bindir}/sconsign
%{py3_sitescriptdir}/SCons
%{py3_sitescriptdir}/SCons-%{version}-py*.egg-info
%{_mandir}/man1/scons.1*
%{_mandir}/man1/sconsign.1*
