%define snapshot	20120110
%define major		0
%define libname		%mklibname qdjango %major

Name:		qdjango
Summary:	Object Relation Mapper library built on top of Qt
Version:	0.1
Release:	0.%{snapshot}.1
Source0:	%{name}-git%{snapshot}.tar.xz
Patch0:		qdjango-git20120110-mdv-build-shared.patch
Patch1:		qdjango-git20120110-mdv-library_path.patch
Group:		System/Libraries
License:	LGPLv3+
BuildRequires:	cmake
BuildRequires:	qt4-devel

%description
QDjango is a simple yet powerful Object Relation Mapper (ORM) written in C++
and built on top of the Qt library. Where possible it tries to follow
django's ORM API, hence its name. It is released under the terms of the GNU
Lesser General Public License version 3.

QDjango builds upon Qt's Meta-Object System, so if you are familiar with Qt,
you should feel right at home using QDjango. QDjango's features include:

  * support for a wide range of database backends thanks to QtSql
  * database fields are declared using Qt's  Q_PROPERTY macro
  * QDjango can create and drop database tables and indices for registered
    models
  * thread-aware access to the database
  * support for accessing your models from QtScript

#------------------------------------------------------------------------------

%package -n %{libname}
Summary:        Object Relation Mapper library built on top of Qt

%description -n %{libname}
QDjango is a simple yet powerful Object Relation Mapper (ORM) written in C++
and built on top of the Qt library. Where possible it tries to follow
django's ORM API, hence its name. It is released under the terms of the GNU
Lesser General Public License version 3.

QDjango builds upon Qt's Meta-Object System, so if you are familiar with Qt,
you should feel right at home using QDjango. QDjango's features include:

  * support for a wide range of database backends thanks to QtSql
  * database fields are declared using Qt's  Q_PROPERTY macro
  * QDjango can create and drop database tables and indices for registered
    models
  * thread-aware access to the database
  * support for accessing your models from QtScript

%files -n %{libname}
%{_libdir}/libqdjango-*.so.%{major}*

#------------------------------------------------------------------------------

%package devel
Summary:        Development files for QDjango library
Requires:	qt4-devel
Requires:	%{libname} = %{version}

%description devel
QDjango is a simple yet powerful Object Relation Mapper (ORM) written in C++
and built on top of the Qt library. Where possible it tries to follow
django's ORM API, hence its name. It is released under the terms of the GNU
Lesser General Public License version 3.

This package contains files required for development purposes only.

%files devel
%{_includedir}/qdjango
%{_libdir}/libqdjango-*.so

#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}-git%{snapshot}
%patch0 -p1
%patch1 -p1

%build
%cmake
%make

%install
pushd build
%makeinstall_std
popd


%changelog
* Mon Jan 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.1-0.20120110.1
+ Revision: 766978
- fix libraries installation path
- imported package qdjango

