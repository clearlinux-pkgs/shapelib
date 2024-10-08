#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v18
# autospec commit: f35655a
#
Name     : shapelib
Version  : 1.6.1
Release  : 26
URL      : https://github.com/OSGeo/shapelib/archive/v1.6.1/shapelib-1.6.1.tar.gz
Source0  : https://github.com/OSGeo/shapelib/archive/v1.6.1/shapelib-1.6.1.tar.gz
Summary  : C API for processing ESRI Shapefiles
Group    : Development/Tools
License  : GPL-2.0+ LGPL-2.0 MIT
Requires: shapelib-bin = %{version}-%{release}
Requires: shapelib-lib = %{version}-%{release}
Requires: shapelib-license = %{version}-%{release}
BuildRequires : file
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Building on Unix
----------------
1) run ./configure to generate build scripts
Note: type ./configure --help for a list of fine-tuning options

%package bin
Summary: bin components for the shapelib package.
Group: Binaries
Requires: shapelib-license = %{version}-%{release}

%description bin
bin components for the shapelib package.


%package dev
Summary: dev components for the shapelib package.
Group: Development
Requires: shapelib-lib = %{version}-%{release}
Requires: shapelib-bin = %{version}-%{release}
Provides: shapelib-devel = %{version}-%{release}
Requires: shapelib = %{version}-%{release}

%description dev
dev components for the shapelib package.


%package lib
Summary: lib components for the shapelib package.
Group: Libraries
Requires: shapelib-license = %{version}-%{release}

%description lib
lib components for the shapelib package.


%package license
Summary: license components for the shapelib package.
Group: Default

%description license
license components for the shapelib package.


%prep
%setup -q -n shapelib-1.6.1
cd %{_builddir}/shapelib-1.6.1
pushd ..
cp -a shapelib-1.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724169326
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%autogen --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724169326
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/shapelib
cp %{_builddir}/shapelib-%{version}/LICENSE-LGPL %{buildroot}/usr/share/package-licenses/shapelib/3cc956929ff9e4c1c89a2c826cdc7fec5e0b21ab || :
cp %{_builddir}/shapelib-%{version}/LICENSE-MIT %{buildroot}/usr/share/package-licenses/shapelib/c507647040d9200a3dae49cafa3675a7598ac8f8 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/Shape_PointInPoly
/V3/usr/bin/csv2shp
/V3/usr/bin/dbfadd
/V3/usr/bin/dbfcat
/V3/usr/bin/dbfcreate
/V3/usr/bin/dbfdump
/V3/usr/bin/dbfinfo
/V3/usr/bin/shpadd
/V3/usr/bin/shpcat
/V3/usr/bin/shpcentrd
/V3/usr/bin/shpcreate
/V3/usr/bin/shpdata
/V3/usr/bin/shpdump
/V3/usr/bin/shpdxf
/V3/usr/bin/shpfix
/V3/usr/bin/shpinfo
/V3/usr/bin/shprewind
/V3/usr/bin/shpsort
/V3/usr/bin/shptreedump
/V3/usr/bin/shputils
/V3/usr/bin/shpwkb
/usr/bin/Shape_PointInPoly
/usr/bin/csv2shp
/usr/bin/dbfadd
/usr/bin/dbfcat
/usr/bin/dbfcreate
/usr/bin/dbfdump
/usr/bin/dbfinfo
/usr/bin/shpadd
/usr/bin/shpcat
/usr/bin/shpcentrd
/usr/bin/shpcreate
/usr/bin/shpdata
/usr/bin/shpdump
/usr/bin/shpdxf
/usr/bin/shpfix
/usr/bin/shpinfo
/usr/bin/shprewind
/usr/bin/shpsort
/usr/bin/shptreedump
/usr/bin/shputils
/usr/bin/shpwkb

%files dev
%defattr(-,root,root,-)
/usr/include/shapefil.h
/usr/lib64/libshp.so
/usr/lib64/pkgconfig/shapelib.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libshp.so.4.1.0
/usr/lib64/libshp.so.4
/usr/lib64/libshp.so.4.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/shapelib/3cc956929ff9e4c1c89a2c826cdc7fec5e0b21ab
/usr/share/package-licenses/shapelib/c507647040d9200a3dae49cafa3675a7598ac8f8
