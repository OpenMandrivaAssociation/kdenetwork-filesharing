%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Samba filesharing dialog for KDE5
Name:		kdenetwork-filesharing
Version:	23.08.5
Release:	3
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	cmake(QCoro5)
BuildRequires:	cmake(packagekitqt5)
BuildRequires:	samba-client
Requires:	samba-client

%description
Samba filesharing dialog for KDE5.

%files -f kfileshare.lang
%{_libdir}/qt5/plugins/kf5/propertiesdialog/sambausershareplugin.so
%{_libdir}/qt5/plugins/kf5/propertiesdialog/SambaAcl.so
%{_datadir}/metainfo/org.kde.kdenetwork-filesharing.metainfo.xml
%{_libdir}/libexec/kauth/authhelper
%{_datadir}/dbus-1/system-services/org.kde.filesharing.samba.service
%{_datadir}/dbus-1/system.d/org.kde.filesharing.samba.conf
%{_datadir}/polkit-1/actions/org.kde.filesharing.samba.policy

#-------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 \
	-DSAMBA_INSTALL=ON \
	-DSAMBA_PACKAGE_NAME=\"samba-client,samba-server\"

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kfileshare --with-html
