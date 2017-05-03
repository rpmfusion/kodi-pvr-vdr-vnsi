%global commit 7a17f8956734b38bffbb1c5d41e515a00144ca52
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170324

%global kodi_addon pvr.vdr.vnsi
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        2.6.20
Release:        1%{?dist}
Summary:        Kodi PVR addon VNSI

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
BuildRequires:  mesa-libGL-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
PVR client to connect VDR to Kodi over the VNSI interface VDR. Supports
streaming of live TV & recordings, EPG, timers over the VNSI plugin.

Note: this package requires the VNSI plugin (package vdr-vnsiserver on Fedora)
to be installed on the VDR backend.


%prep
%autosetup -n %{kodi_addon}-%{commit}

cp -p %{SOURCE1} .


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%license gpl-2.0.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Wed Apr 26 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:2.6.20-1
- Update to latest stable release for Kodi 17

* Sat Jul 23 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.11.19-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.10-2
- Update for Kodi 15.1
- Fix description
- Add license file

* Mon Aug 17 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.10-1
- Initial RPM release
