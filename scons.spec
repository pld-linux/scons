Summary:	An Open Source software construction tool
Summary(pl):	OpenSourcowe narzêdzie do tworzenia oprogramowania
Name:		scons
Version:	0.96.92
Release:	1
License:	MIT, freely distributable
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/scons/%{name}-%{version}.tar.gz
# Source0-md5:	0b6b388cdd640b7f297f37a678c65d5c
URL:		http://www.scons.org/
BuildRequires:	python-devel >= 1.6
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
Requires:	python
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
SCons to wypuszczone z ogólnodostêpnymi ¼ród³ami narzêdzie do
budowania oprogramowania; jest to ulepszony zamiennik klasycznego
narzêdzia Make. SCons jest oparte na opracowaniu, które wygra³o
konkurs Software Carpentry owania w sierpniu 2000.

"Pliki konfiguracyjne" SCons to skrypty Pythona, co eliminuje potrzebê
uczenia siê sk³adni nowego narzêdzia. SCons zachowuje globalny widok
wszystkich zale¿no¶ci w drzewie i mo¿e przeszukiwaæ pliki ¼róde³ (lub
inne) w poszukiwaniu niejawnych zale¿no¶ci, takich jak pliki podane w
liniach #include. SCons u¿ywa sygnatur MD5, aby przebudowywaæ tylko
wtedy, kiedy naprawdê siê zmieni³a zawarto¶æ pliku, a nie przy samej
zmianie czasu modyfikacji. SCons obs³uguje budowanie wariantowe i jest
³atwo rozszerzalny przez zdefiniowane przez u¿ytkownika obiekty
Builder i/lub Scanner.

%prep
%setup -q
%{__sed} -i "s,'lib','share',g" script/{scons,sconsign}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
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
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
%{_mandir}/man1/*
