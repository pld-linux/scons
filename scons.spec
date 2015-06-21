Summary:	An Open Source software construction tool
Summary(pl.UTF-8):	OpenSourcowe narzędzie do tworzenia oprogramowania
Name:		scons
Version:	2.3.5
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/scons/%{name}-%{version}.tar.gz
# Source0-md5:	a8988c7ef11133bb3b6ccf0af67ce010
URL:		http://www.scons.org/
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
Requires:	python >= 1:2.4
Requires:	python-devel-tools >= 1:2.4
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
%setup -q

%{__sed} -i -e "s,'lib','share',g" script/{scons,sconsign}
%{__sed} -i -e '1s,#!.*python,#!%{__python},' script/scons*

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

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec %{__rm} {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# LICENSE.txt must be packaged (see LICENSE.txt file)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt
%attr(755,root,root) %{_bindir}/scons*
%{py_sitescriptdir}/SCons
%{_mandir}/man1/scons*.1*
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/scons-%{version}-py*.egg-info
%endif
%changelog
* Sun Jun 21 2015 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/scons.git;a=log;h=master

* Sun Aug 25 2013 Jakub Bogusz <qboosh@pld-linux.org> ca30b95
- updated to 2.3.0

* Thu Sep 15 2011 lisu <lisu@pld-linux.org> 10b8b09
- updated to 2.1.0
- merged with DEVEL

* Fri Aug 20 2010 lisu <lisu@pld-linux.org> 7774fb1
- updated to 2.0.1
- merge with DEVEL

* Wed Aug 04 2010 lisu <lisu@pld-linux.org> 955dbd2
- 1.3.1

* Thu Jul 08 2010 Jacek Konieczny <jajcus@pld-linux.org> 606c88a
- %files fixed for Python 2.7

* Thu Jul 08 2010 Arkadiusz Miśkiewicz <arekm@maven.pl> 4a306e4
- release 2

* Thu Mar 25 2010 lisu <lisu@pld-linux.org> 08848df
- up to 1.3.0
- more verbose files
- adapter

* Thu Dec 10 2009 Elan Ruusamäe <glen@pld-linux.org> 1fefc13
- kill env shebang; rel 2

* Sat Jan 17 2009 lisu <lisu@pld-linux.org> 454da74
- remove DEVEL stuff

* Mon Dec 22 2008 lisu <lisu@pld-linux.org> e9f606d
- do not give dir name in %%setup

* Mon Dec 22 2008 lisu <lisu@pld-linux.org> 5c64cb9
- up to 1.2.0

* Mon Nov 24 2008 lisu <lisu@pld-linux.org> 3bfdf32
- 1.1.0

* Fri Oct 03 2008 Arkadiusz Miśkiewicz <arekm@maven.pl> 76be354
- release 2

* Mon Sep 22 2008 Paweł Sikora <pluto@pld-linux.org> 57d8979
- updated to 1.0.1.

* Thu Jun 19 2008 lisu <lisu@pld-linux.org> f4508c6
- 0.98.5
- STBR

* Tue May 06 2008 lisu <lisu@pld-linux.org> aa2e8bb
- 0.98.3

* Mon Apr 28 2008 lisu <lisu@pld-linux.org> 832d62b
- 0.98.2

* Fri Apr 04 2008 lisu <lisu@pld-linux.org> 01fd4e5
- up to final 0.98.0
- use python macro

* Sat May 26 2007 Jakub Bogusz <qboosh@pld-linux.org> 91b0d20
- updated to 0.9 7

* Sun Apr 29 2007 Jakub Bogusz <qboosh@pld-linux.org> 80b6cdc
- R: python-devel-tools (for pdb)

