#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Samba filesharing dialog for KDE6
Name:		kdenetwork-filesharing
Version:	25.12.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/kdenetwork-filesharing/-/archive/%{gitbranch}/kdenetwork-filesharing-%{gitbranchd}.tar.bz2#/kdenetwork-filesharing-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdenetwork-filesharing-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6QuickWidgets)
BuildRequires:	cmake(QCoro6)
BuildRequires:	cmake(packagekitqt6)
BuildRequires:	samba-client
Requires:	samba-client

%rename plasma6-kdenetwork-filesharing

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DSAMBA_INSTALL=ON
BuildOption:	-DSAMBA_PACKAGE_NAME=\"samba-client,samba-server\"

%description
Samba filesharing dialog for KDE6.

%files -f %{name}.lang
%{_libdir}/qt6/plugins/kf6/propertiesdialog/sambausershareplugin.so
%{_libdir}/qt6/plugins/kf6/propertiesdialog/SambaAcl.so
%{_datadir}/metainfo/org.kde.kdenetwork-filesharing.metainfo.xml
%{_libdir}/libexec/kf6/kauth/authhelper
%{_datadir}/dbus-1/system-services/org.kde.filesharing.samba.service
%{_datadir}/dbus-1/system.d/org.kde.filesharing.samba.conf
%{_datadir}/polkit-1/actions/org.kde.filesharing.samba.policy
