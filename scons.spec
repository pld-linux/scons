Summary:	an Open Source software construction tool
Summary(pl):	OpenSourcowe narzêdzie do tworzenia oprogramowania
Name:		scons
Version:	0.92
Release:	1
Source0:	http://dl.sourceforge.net/sourceforge/scons/%{name}-%{version}.tar.gz
# Source0-md5:	8e3b76343e6772d56ce7894e67ef1ebf
License:	MIT, freely distributable
Group:		Development/Tools
BuildArch:	noarch
Requires:	python >= 1.5
Url:		http://www.scons.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCons is an Open Source software construction tool--that is, a build
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
with user- defined Builder and/or Scanner objects.

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
install scons*.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}/
%{_mandir}/man?/*
