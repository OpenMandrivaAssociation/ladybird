%define devname %mklibname Ladybird -d
# sourcedate is taken from package-source.sh archive name
# which is the same date the archive is created on. in format: YYYYMMDD
%define sourcedate 20260125

Name:		ladybird
Version:	0.0
Release:	2
# Using date-stamped source tarball created by package-source.sh script
Source0:	ladybird-%{sourcedate}.tar.zst
#Source0:	https://github.com/LadybirdBrowser/ladybird/archive/refs/heads/master.tar.gz
# Usually downloaded at build time
Source10:	https://curl.se/ca/cacert-2025-12-02.pem
Source11:	https://raw.githubusercontent.com/publicsuffix/list/master/public_suffix_list.dat
Summary:	Early preview of a truly independent web browser
URL:		https://ladybird.org/
License:	BSD-2-Clause
Group:		Applications/Internet
BuildRequires:	cmake
BuildSystem:	cmake
BuildOption:	-DENABLE_NETWORK_DOWNLOADS:BOOL=OFF
BuildOption:	-DENABLE_CACERT_DOWNLOAD:BOOL=OFF
BuildOption:	-DENABLE_QT=ON
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(CURL)
BuildRequires:	cmake(simdutf)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(libtommath)
BuildRequires:	pkgconfig(libavif)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libwoff2dec)
BuildRequires:	pkgconfig(libwoff2enc)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libjxl)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(skia)
BuildRequires:	pkgconfig(angle)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(simdjson)
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
# above patch fixes build by modifying internal subpackage LibGfx
# CMakeLists harfbuzz detection to use pkgconfig method and also fixes
# fontconfig detection in a similar way but wraps it in the HAS_FONTCONFIG flag
# in line with the other CMakeLists fontconfig entries.
ladybird-skia-skcms-linkage.patch

%description
An independent web browser, not using the Chromium or Firefox rendering
engines or forks thereof.

THIS IS AN EARLY PREVIEW VERSION. A first usable alpha version is planned
for Summer 2026. These early previews are not fully working yet, but can
help curious people see the progress and catch bugs.

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
%{_bindir}/wasm
%{_libdir}/*.so.*
%{_libexecdir}/*
%{_datadir}/Ladybird
%{_datadir}/Lagom
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/org.ladybird.Ladybird.desktop
%{_datadir}/dbus-1/services/org.ladybird.Ladybird.service
%{_datadir}/metainfo/org.ladybird.Ladybird.metainfo.xml

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
