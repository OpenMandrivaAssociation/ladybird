%define devname %mklibname Ladybird -d
# sourcedate is taken from package-source.sh archive name
# which is the same date the archive is created on. in format: YYYYMMDD
%define sourcedate 20250607

Name:		ladybird
Version:	0.0
Release:	
# Using date-stamped source tarball created by package-source.sh script
Source0:	ladybird-%{sourcedate}.tar.zst
#Source0:	https://github.com/LadybirdBrowser/ladybird/archive/refs/heads/master.tar.gz
# Usually downloaded at build time
Source10:	https://curl.se/ca/cacert-2023-12-12.pem
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
ladybird-libgfx-harfbuzz-fontconfig-fix.patch
# above patch fixes build by modifying internal subpackage LibGfx
# CMakeLists harfbuzz detection to use pkgconfig method and also fixes
# fontconfig detection in a similar way but wraps it in the HAS_FONTCONFIG flag
# in line with the other CMakeLists fontconfig entries.

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

%install -p
mkdir -p %{buildroot}%{_datadir}/applications

# Translations in the desktop file shamelessly stolen from Falkon
cat >%{buildroot}%{_datadir}/applications/%{name}.desktop <<'EOF'
[Desktop Entry]
Name=Ladybird Web Browser
Name[ar]=فالكون متصفّح وبّo
Name[az]=Ladybird Veb Bələdçi
Name[bg]=Ladybird Уеб браузър
Name[ca]=Navegador web Ladybird
Name[ca@valencia]=Navegador web Ladybird
Name[cs]=Ladybird Webový prohlížeč
Name[da]=Ladybird Webbrowser
Name[de]=Ladybird Web-Browser
Name[el]=Ladybird Περιηγητής ιστού
Name[en_GB]=Ladybird Web Browser
Name[eo]=Ladybird Retumilo
Name[es]=Navegador web Ladybird
Name[et]=Veebilehitseja Ladybird
Name[eu]=Ladybird Web arakatzailea
Name[fi]=Verkkoselain Ladybird
Name[fr]=Navigateur Web Ladybird
Name[gl]=Navegador web Ladybird
Name[ia]=Ladybird: Navigator Web
Name[id]=Ladybird Penelusur Web
Name[is]=Ladybird Vafri
Name[it]=Ladybird Web browser
Name[ka]=Ladybird ვებ-ბრაუზერი
Name[ko]=Ladybird 웹 브라우저
Name[lt]=Ladybird Saityno naršyklė
Name[nl]=Ladybird Webbrowser
Name[nn]=Ladybird Nettlesar
Name[pa]=ਫਾਲਕਨ ਵੈੱਬ ਬਰਾਊਜ਼ਰ
Name[pl]=Przeglądarka internetowa Ladybird
Name[pt]=Navegador Web Ladybird
Name[pt_BR]=Navegador Web Ladybird
Name[ru]=Ladybird интернет-браузер
Name[sk]=Webový prehliadač Ladybird
Name[sl]=Ladybird Spletni brskalnik
Name[sv]=Ladybird Webbläsare
Name[tr]=Ladybird Web Tarayıcı
Name[uk]=Ladybird Переглядач інтернету
Name[x-test]=xxLadybird Web Browserxx
Name[zh_CN]=Ladybird 网页浏览器
Name[zh_TW]=Ladybird 網路瀏覽器
Type=Application
Icon=ladybird
Categories=KDE;Qt;X-MandrivaLinux-CrossDesktop;Network;WebBrowser;
Comment=A fast and secure web browser
Comment[ar]=متصفّح وبّ سريع وآمن
Comment[az]=Sürətli və təhlükəsiz veb bələdçi
Comment[bg]=Бърз и сигурен уеб браузър
Comment[ca]=Un navegador web ràpid i segur
Comment[ca@valencia]=Un navegador web ràpid i segur
Comment[cs]=Rychlý a bezpečný webový prohlížeč
Comment[da]=En hurtig og sikker webbrowser
Comment[de]=Ein schneller und sicherer Webbrowser
Comment[el]=Ένας γρήγορος και ασφαλής περιηγητής ιστού
Comment[en_GB]=A fast and secure web browser
Comment[eo]=Rapida kaj sekura TTT-legilo
Comment[es]=Un navegador web rápido y seguro
Comment[et]=Kiire ja turvaline veebilehitseja
Comment[eu]=Web arakatzaile azkar eta seguru bat
Comment[fi]=Nopea ja turvallinen verkkoselain
Comment[fr]=Un navigateur Web rapide et sécurisé
Comment[gl]=Un navegador rápido e seguro.
Comment[he]=דפדפן אינטרנט מהיר ומאובטח
Comment[hu]=Gyors és biztonságos webböngésző
Comment[ia]=Un rapide e secure navigator web
Comment[id]=Sebuah penelusur web yang cepat dan aman
Comment[is]=Hraðvirkur og öruggur vafri
Comment[it]=Un browser web veloce e sicuro
Comment[ka]=სწრაფი და დაცული ბრაუზერი
Comment[ko]=빠르고 안전한 웹 브라우저
Comment[lt]=Greita ir saugi saityno naršyklė
Comment[lv]=Ātra un droša tīmekļa pārlūkprogramma
Comment[nl]=Een snelle en veilige webbrowser
Comment[nn]=Ein kjapp og sikker nettlesar
Comment[pa]=ਤੇਜ਼ ਅਤੇ ਸੁਰੱਕਿਅਤ ਵੈੱਬ ਬਰਾਊਜ਼ਰ
Comment[pl]=Szybka i bezpieczna przeglądarka internetowa
Comment[pt]=Um navegador Web rápido e seguro
Comment[pt_BR]=Um navegar Web rápido e seguro
Comment[ru]=Быстрый и безопасный веб-браузер
Comment[sk]=Rýchly a bezpečný prehliadač internetu
Comment[sl]=Hiter in varen spletni brskalnik
Comment[sv]=En snabb och säker webbläsare
Comment[tr]=Hızlı ve güvenli bir web tarayıcısı
Comment[uk]=Проста і безпечна програма для перегляду інтернету
Comment[x-test]=xxA fast and secure web browserxx
Comment[zh_CN]=一款安全快速的网页浏览器
Comment[zh_TW]=快速且安全的網路瀏覽器
GenericName=Web Browser
GenericName[ar]=متصفّح وبّ
GenericName[az]=Veb Bələdçi
GenericName[bg]=Уеб браузър
GenericName[ca]=Navegador web
GenericName[ca@valencia]=Navegador web
GenericName[cs]=Webový prohlížeč
GenericName[da]=Webbrowser
GenericName[de]=Webbrowser
GenericName[el]=Περιηγητής ιστού
GenericName[en_GB]=Web Browser
GenericName[eo]=Retumilo
GenericName[es]=Navegador web
GenericName[et]=Veebilehitseja
GenericName[eu]=Web arakatzailea
GenericName[fi]=Verkkoselain
GenericName[fr]=Navigateur Web
GenericName[gl]=Navegador web
GenericName[he]=דפדפן
GenericName[hu]=Webböngésző
GenericName[ia]=Navigator Web
GenericName[id]=Penelusur Web
GenericName[is]=Vafri
GenericName[it]=Browser web
GenericName[ka]=ვებ-ბრაუზერი
GenericName[ko]=웹 브라우저
GenericName[lt]=Saityno naršyklė
GenericName[lv]=Tīmekļa pārlūks
GenericName[nl]=Webbrowser
GenericName[nn]=Nettlesar
GenericName[pa]=ਵੈੱਬ ਬਰਾਊਜ਼ਰ
GenericName[pl]=Przeglądarka sieciowa
GenericName[pt]=Navegador Web
GenericName[pt_BR]=Navegador Web
GenericName[ru]=Веб-браузер
GenericName[sk]=Webový prehliadač
GenericName[sl]=Spletni brskalnik
GenericName[sv]=Webbläsare
GenericName[tr]=Web Tarayıcısı
GenericName[uk]=Переглядач інтернету
GenericName[x-test]=xxWeb Browserxx
GenericName[zh_CN]=网页浏览器
GenericName[zh_TW]=網路瀏覽器
Exec=Ladybird %u
MimeType=text/html;application/xhtml+xml;x-scheme-handler/http;x-scheme-handler/https;application/x-mimearchive;
Terminal=false
EOF

# install available .desktop file Icon sizes
for i in 48 128
do
	install -Dpm 0644 Base/res/icons/${i}x${i}/app-browser.png \
	%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/ladybird.png
done

%files
%{_bindir}/Ladybird
%{_bindir}/js
%{_libdir}/*.so.*
%{_libexecdir}/*
%{_datadir}/Ladybird
%{_datadir}/Lagom
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/ladybird.png

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
