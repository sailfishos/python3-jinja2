# Adapted from Fedora's packaging (2014-02-17)
# http://pkgs.fedoraproject.org/cgit/python-jinja2.git/tree/python-jinja2.spec

%global upstream_name Jinja2

Name:           python-jinja2
Version:        2.7.2
Release:        1
Summary:        General purpose template engine
Group:          Development/Languages
License:        BSD
URL:            http://jinja.pocoo.org/
# Source   http://pypi.python.org/packages/source/J/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-markupsafe
Requires:       python-markupsafe

%description
Jinja2 is a template engine written in pure Python.  It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.

%prep
%setup -q -n %{name}-%{version}/%{name}

# cleanup
find . -name '*.pyo' -o -name '*.pyc' -delete

# fix EOL
sed -i 's|\r$||g' LICENSE

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build \
            --root %{buildroot}

%files
%{python_sitelib}/*
