Summary:	An Open Source software construction tool
Summary(pl):	OpenSourcowe narz�dzie do tworzenia oprogramowania
Name:		scons
Version:	0.95
Release:	1
License:	MIT, freely distributable
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/scons/%{name}-%{version}.tar.gz
# Source0-md5:	2d08d41b9de7553729eab45adbd943c0
URL:		http://www.scons.org/
Requires:	python >= 1.5
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

%description -l pl
SCons to wypuszczone z og�lnodost�pnymi �r�d�ami narz�dzie do
budowania oprogramowania; jest to ulepszony zamiennik klasycznego
narz�dzia Make. SCons jest oparte na opracowaniu, kt�re wygra�o
konkurs Software Carpentry owania w sierpniu 2000.

"Pliki konfiguracyjne" SCons to skrypty Pythona, co eliminuje potrzeb�
uczenia si� sk�adni nowego narz�dzia. SCons zachowuje globalny widok
wszystkich zale�no�ci w drzewie i mo�e przeszukiwa� pliki �r�de� (lub
inne) w poszukiwaniu niejawnych zale�no�ci, takich jak pliki podane w
liniach #include. SCons u�ywa sygnatur MD5, aby przebudowywa� tylko
wtedy, kiedy naprawd� si� zmieni�a zawarto�� pliku, a nie przy samej
zmianie czasu modyfikacji. SCons obs�uguje budowanie wariantowe i jest
�atwo rozszerzalny przez zdefiniowane przez u�ytkownika obiekty
Builder i/lub Scanner.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--record=INSTALLED_FILES \
	--install-lib=%{_libdir}/%{name} \
	--install-scripts=%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install scons*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man?/*
