#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Python 2 and 3 ast modules with type comment support
Summary(pl.UTF-8):	Moduły ast z Pythona 2 i 3 z obsługą komentarzy o typach
Name:		python3-typed_ast
Version:	1.5.4
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/typed-ast/
Source0:	https://files.pythonhosted.org/packages/source/t/typed-ast/typed_ast-%{version}.tar.gz
# Source0-md5:	1b0183d362a886a447d8314a97bc37b3
URL:		https://pypi.org/project/typed-ast/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
typed_ast is a Python 3 package that provides a Python 2.7 and Python 3
parser similar to the standard ast library. Unlike ast, the parsers in
typed_ast include PEP 484 type comments and are independent of the
version of Python under which they are run. The typed_ast parsers
produce the standard Python AST (plus type comments), and are both
fast and correct, as they are based on the CPython 2.7 and 3.7
parsers. typed_ast runs on CPython 3.6-3.10 on Linux, OS X and
Windows.

%description -l pl.UTF-8
typed_ast to pakiet Pythona 3 udostępniający parser dla Pythona 2.7
oraz Pythona 3, podobny do biblioteki standardowej ast. W
przeciwieństwie do ast, parsery w module typed_ast zawierają
komentarze o typach zgodne z PEP 484 i są niezależne od wersji
Pythona, przez którą są uruchamiane. Parsery typed_ast tworzą
standardowe pythonowe drzewo składniowe (AST), wzbogacone o komentarze
o typach; są szybkie i poprawne, jako że są oparte na kodzie CPythona
2.7 oraz 3.7. typed_ast działa na CPythonie 3.6-3.10 pod Linuksem, OS
X oraz Windows.

%prep
%setup -q -n typed_ast-%{version}

%build
%py3_build

%if %{with tests}
export PYTHONPATH=$(echo $(pwd)/build-3/lib.*)
# run from subdir, so python won't catch PWD as PYTHONPATH
cd ast3
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/typed_ast/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{py3_sitedir}/typed_ast
%attr(755,root,root) %{py3_sitedir}/typed_ast/_ast*.cpython-*.so
%{py3_sitedir}/typed_ast/*.py
%{py3_sitedir}/typed_ast/__pycache__
%{py3_sitedir}/typed_ast-%{version}-py*.egg-info
