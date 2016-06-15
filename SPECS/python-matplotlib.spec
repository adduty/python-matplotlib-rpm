Name: python-matplotlib
Version: 1.5.1
Release:	1%{?dist}
Summary: Python 2D plotting library

Group: Development/Libraries
License: Python
URL: http://matplotlib.org
Source0: matplotlib-%{version}.tar.gz

BuildRequires: agg-devel
BuildRequires: cycler >= 0.9
BuildRequires: freetype-devel >= 2.3
BuildRequires: gcc-c++
BuildRequires: gtk2-devel
BuildRequires: libpng-devel
BuildRequires: numpy >= 1.6
BuildRequires: pycairo-devel
BuildRequires: python-dateutil
BuildRequires: pygtk2-devel >= 2.4
BuildRequires: pyparsing
BuildRequires: python >= 2.7
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: pytz
BuildRequires: wxPython >= 2.8
BuildRequires: zlib-devel
Requires: dejavu-sans-fonts
Requires: dvipng
Requires: numpy >= 1.6
Requires: pycairo
Requires: pygtk2
Requires: pyparsing
Requires: python >= 2.7
Requires: python-dateutil >= 1.1
Requires: pytz
%if 0%{?fedora} >= 18
Requires: stix-math-fonts
%else
Requires: stix-math-fonts
%endif
Requires: wxPython

%description
Matplotlib is a python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. matplotlib can be used in python
scripts, the python and ipython shell, web application servers, and 
six graphical user interface toolkits.

Matplotlib tries to make easy things easy and hard things possible.
You can generate plots, histograms, power spectra, bar charts,
errorcharts, scatterplots, etc, with just a few lines of code.

%prep
%setup -q -n matplotlib-%{version}.tar.gz


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

