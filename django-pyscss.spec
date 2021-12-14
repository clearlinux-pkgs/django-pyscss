#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-pyscss
Version  : 2.0.2
Release  : 53
URL      : https://files.pythonhosted.org/packages/4b/7f/d771802305184aac6010826f60a0b2ecaa3f57d19ab0e405f0c8db07e809/django-pyscss-2.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4b/7f/d771802305184aac6010826f60a0b2ecaa3f57d19ab0e405f0c8db07e809/django-pyscss-2.0.2.tar.gz
Summary  : Makes it easier to use PySCSS in Django.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: django-pyscss-license = %{version}-%{release}
Requires: django-pyscss-python = %{version}-%{release}
Requires: django-pyscss-python3 = %{version}-%{release}
Requires: Django
Requires: pyScss
BuildRequires : Django
BuildRequires : Django-python
BuildRequires : Pillow-python
BuildRequires : buildreq-distutils3
BuildRequires : django-appconf-python
BuildRequires : django-discover-runner-python
BuildRequires : django_compressor-python
BuildRequires : funcsigs-python
BuildRequires : pathlib-python
BuildRequires : pyScss
BuildRequires : pyScss-python
BuildRequires : pytest
BuildRequires : python-mock-python
BuildRequires : six
BuildRequires : six-python

%description
-------------
        
        A collection of tools for making it easier to use pyScss within Django.

%package license
Summary: license components for the django-pyscss package.
Group: Default

%description license
license components for the django-pyscss package.


%package python
Summary: python components for the django-pyscss package.
Group: Default
Requires: django-pyscss-python3 = %{version}-%{release}

%description python
python components for the django-pyscss package.


%package python3
Summary: python3 components for the django-pyscss package.
Group: Default
Requires: python3-core
Provides: pypi(django_pyscss)
Requires: pypi(django)
Requires: pypi(pyscss)

%description python3
python3 components for the django-pyscss package.


%prep
%setup -q -n django-pyscss-2.0.2
cd %{_builddir}/django-pyscss-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635724299
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest --verbose || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django-pyscss
cp %{_builddir}/django-pyscss-2.0.2/LICENSE %{buildroot}/usr/share/package-licenses/django-pyscss/09032647465ef808c0e5503092f5fa338baa62ad
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django-pyscss/09032647465ef808c0e5503092f5fa338baa62ad

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
