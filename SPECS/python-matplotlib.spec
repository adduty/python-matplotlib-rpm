%global __provides_exclude_from .*/site-packages/.*\\.so$
%global with_html               1

Name: python-matplotlib
Version: 1.5.1
Release: 1%{?dist}
Summary: Python 2D plotting library

Group: Development/Libraries
License: Python
URL: http://matplotlib.org
Source0: matplotlib-%{version}.tar.gz

Patch0: %{name}-tk.patch

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
BuildRequires: python < 3
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
Requires: python < 3
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

%package        qt4
Summary:        Qt4 backend for python-matplotlib
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  PyQt4-devel
Requires:       PyQt4

%description    qt4
%{summary}

%package        tk
Summary:        Tk backend for python-matplotlib
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  tcl-devel
BuildRequires:  tkinter
BuildRequires:  tk-devel
Requires:       tkinter

%description    tk
%{summary}

%package        wx
Summary:        wxPython backend for python-matplotlib
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  wxPython-devel
Requires:       wxPython

%description    wx
%{summary}

%package        doc
Summary:        Documentation files for python-matplotlib
Group:          Documentation
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with_html}                                                                                                                                                                                                                             
BuildRequires:  python-ipython-sphinx
BuildRequires:  python-numpydoc
BuildRequires:  python-sphinx
BuildRequires:  tex(latex)
BuildRequires:  texlive
BuildRequires:  dvipng
%endif

%description    doc
%{summary}

%prep
%setup -q -n matplotlib-%{version}

# Correct tcl/tk detection
%patch0 -p1 -b .tk
sed -i -e 's|@@libdir@@|%{_libdir}|' setupext.py

chmod -x lib/matplotlib/mpl-data/images/*.svg

%build
python2.7 setup.py build
%if %{with_html}                                                                                                                                                                                                                             
# Need to make built matplotlib libs available for the sphinx extensions:
pushd doc
    export PYTHONPATH=`realpath ../build/lib.linux*`
    %{__python2} make.py html
popd
%endif

# Ensure all example files are non-executable so that the -doc
# package doesn't drag in dependencies
find examples -name '*.py' -exec chmod a-x '{}' \;

%install
python2.7 setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{python_sitearch}/matplotlib/dates.py
rm -rf $RPM_BUILD_ROOT%{python_sitearch}/matplotlib/mpl-data/fonts


%files
%doc README.txt
%doc lib/dateutil_py2/LICENSE
%doc lib/matplotlib/mpl-data/fonts/ttf/LICENSE_STIX
%doc lib/pytz/LICENSE.txt
%doc CHANGELOG
%doc CXX
%doc INSTALL
%doc PKG-INFO
%doc TODO
%{python_sitearch}/*egg-info
%{python_sitearch}/matplotlib/
%{python_sitearch}/mpl_toolkits/
%{python_sitearch}/pylab.py*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt4.*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt4agg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_tkagg.*
%exclude %{python_sitearch}/matplotlib/backends/tkagg.*
%exclude %{python_sitearch}/matplotlib/backends/_tkagg.so
%exclude %{python_sitearch}/matplotlib/backends/backend_wx.*
%exclude %{python_sitearch}/matplotlib/backends/backend_wxagg.*

%files qt4
%{python_sitearch}/matplotlib/backends/backend_qt4.*
%{python_sitearch}/matplotlib/backends/backend_qt4agg.*

%files tk
%{python_sitearch}/matplotlib/backends/backend_tkagg.py*
%{python_sitearch}/matplotlib/backends/tkagg.py*
%{python_sitearch}/matplotlib/backends/_tkagg.so

%files wx
%{python_sitearch}/matplotlib/backends/backend_wx.*
%{python_sitearch}/matplotlib/backends/backend_wxagg.*

%files doc
%doc examples
%if %{with_html}                                                                                                                                                                                                                             
%doc doc/build/html/*
%endif

%changelog
* Thu Jun 16 2016 Andrew Duty <tisbeok@gmail.com> 1.5.1-1
- Initial package for MESAplot 0.3.4.
