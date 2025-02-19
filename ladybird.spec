%define devname %mklibname Ladybird -d

Name:		ladybird
Version:	0.0
Release:	0.20250219.1
Source0:	https://github.com/LadybirdBrowser/ladybird/archive/refs/heads/master.tar.gz
# Usually downloaded at build time
Source10:	https://curl.se/ca/cacert-2023-12-12.pem
Source11:	https://raw.githubusercontent.com/publicsuffix/list/master/public_suffix_list.dat
Summary:	Truly independent web browser
URL:		https://ladybird.org/
License:	BSD-2-Clause
Group:		Applications/Internet
BuildRequires:	cmake
BuildSystem:	cmake
BuildOption:	-DENABLE_NETWORK_DOWNLOADS:BOOL=OFF
BuildOption:	-DENABLE_CACERT_DOWNLOAD:BOOL=OFF
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(harfbuzz)
BuildRequires:	cmake(CURL)
BuildRequires:	cmake(simdutf)
BuildRequires:	pkgconfig(libavif)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libwoff2dec)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libjxl)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(skia)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbcomp)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xkbregistry)

%patchlist
ladybird-compile.patch

%description
An independent web browser, not using the Chromium or Firefox rendering
engines or forks thereof.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Development files for %{name}

%prep -a
mkdir -p _OMV_rpm_build/caches/CACERT _OMV_rpm_build/caches/PublicSuffix _OMV_rpm_build/Lagom
cp %{S:10} _OMV_rpm_build/caches/CACERT/
cp %{S:10} _OMV_rpm_build/Lagom/cacert.pem
cp %{S:11} _OMV_rpm_build/caches/PublicSuffix/public_suffix_list.dat

%build -p
export LD_LIBRARY_PATH=$(pwd)/_OMV_rpm_build/%{_lib}

%files
%{_bindir}/Ladybird
%{_bindir}/js
%{_libdir}/*.so.*
%{_libexecdir}/*
%{_datadir}/Ladybird
%{_datadir}/Lagom

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
