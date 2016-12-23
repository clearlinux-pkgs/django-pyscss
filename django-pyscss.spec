#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-pyscss
Version  : 2.0.2
Release  : 21
URL      : https://pypi.python.org/packages/source/d/django-pyscss/django-pyscss-2.0.2.tar.gz
Source0  : https://pypi.python.org/packages/source/d/django-pyscss/django-pyscss-2.0.2.tar.gz
Summary  : Makes it easier to use PySCSS in Django.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: django-pyscss-python
BuildRequires : Django-python
BuildRequires : Pillow-python
BuildRequires : django-appconf-python
BuildRequires : django-discover-runner-python
BuildRequires : django_compressor-python
BuildRequires : enum34-python
BuildRequires : funcsigs-python
BuildRequires : pathlib-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyScss-python
BuildRequires : python-dev
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python

%description
django-pyscss
-------------
A collection of tools for making it easier to use pyScss within Django.

%package python
Summary: python components for the django-pyscss package.
Group: Default

%description python
python components for the django-pyscss package.


%prep
%setup -q -n django-pyscss-2.0.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || : ; py.test-3.4 --verbose || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
