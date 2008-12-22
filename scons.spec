%define	_snap	d20081207
Summary:	An Open Source software construction tool
Summary(pl.UTF-8):	OpenSourcowe narzędzie do tworzenia oprogramowania
Name:		scons
Version:	1.2.0
Release:	1
License:	MIT, freely distributable
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/scons/%{name}-%{version}.tar.gz
# Source0-md5:	53b6aa7281811717a57598e319441cf7
URL:		http://www.scons.org/
BuildRequires:	python-devel >= 1.6
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
Requires:	python
Requires:	python-devel-tools
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
%setup -q -n %{name}-%{version}
%{__sed} -i -e "s,'lib','share',g" script/{scons,sconsign}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--no-version-script \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \
	--install-data=%{_datadir} \
	--install-lib=%{py_sitescriptdir} \
	--install-scripts=%{_bindir}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#LICENSE.txt must be added (read LICENSE.txt file)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
%{_mandir}/man1/*
