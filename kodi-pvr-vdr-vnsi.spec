%global kodi_addon pvr.vdr.vnsi
%global kodi_version 18.0
%global kodi_codename Leia

%undefine __cmake_in_source_build

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        3.6.3
Release:        3%{?dist}
Summary:        VDR PVR for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
%ifarch %{arm}
BuildRequires:  mesa-libGLES-devel
%else
BuildRequires:  mesa-libGL-devel
%endif
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename}


%build
%cmake3
%cmake3_build


%install
%cmake3_install


%files
%doc README.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.6.3-1
- Update to 3.6.3

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.6.0-2
- Enable arm build

* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.6.0-1
- Update to 3.6.0
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.2-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:2.6.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.6.25-1
- Update to 2.6.25

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:2.6.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 06 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.6.21-1
- Update to 2.6.21

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
