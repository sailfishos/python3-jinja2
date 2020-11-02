Name:           python3-jinja2
Version:        2.7.2
Release:        1
Summary:        General purpose template engine
License:        BSD
URL:            http://jinja.pocoo.org/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-markupsafe
Requires:       python3-markupsafe

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
%autosetup -n %{name}-%{version}/python-jinja2

# cleanup
find . -name '*.pyo' -o -name '*.pyc' -delete

# fix EOL
sed -i 's|\r$||g' LICENSE

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{python3_sitelib}/*
