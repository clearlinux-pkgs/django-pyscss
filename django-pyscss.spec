#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-pyscss
Version  : 2.0.2
Release  : 27
URL      : http://pypi.debian.net/django-pyscss/django-pyscss-2.0.2.tar.gz
Source0  : http://pypi.debian.net/django-pyscss/django-pyscss-2.0.2.tar.gz
Summary  : Makes it easier to use PySCSS in Django.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: django-pyscss-python3
Requires: django-pyscss-license
Requires: django-pyscss-python
Requires: Django
Requires: pyScss
BuildRequires : Django
BuildRequires : Django-python
BuildRequires : Pillow-python
BuildRequires : buildreq-distutils3
BuildRequires : django-appconf-python
BuildRequires : django-discover-runner-python
BuildRequires : django_compressor-python
BuildRequires : enum34-python
BuildRequires : funcsigs-python
BuildRequires : pathlib-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyScss
BuildRequires : pyScss-python
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : setuptools
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
Requires: django-pyscss-python3

%description python
python components for the django-pyscss package.


%package python3
Summary: python3 components for the django-pyscss package.
Group: Default
Requires: python3-core

%description python3
python3 components for the django-pyscss package.


%prep
%setup -q -n django-pyscss-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532217617
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || : ; py.test-3.4 --verbose || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/django-pyscss
cp LICENSE %{buildroot}/usr/share/doc/django-pyscss/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/django-pyscss/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
