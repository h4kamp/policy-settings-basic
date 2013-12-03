# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       policy-settings-basic-n900

# >> macros
# << macros

Summary:    Precompiled basic MeeGo policy settings for the N900
Version:    0.1.2
Release:    1
Group:      System/Resource Policy
License:    GPLv2
BuildArch:  noarch
URL:        https://github.com/nemomobile/policy-settings-basic/
Source0:    %{name}-%{version}.tar.gz
Source100:  policy-settings-basic-n900.yaml
Requires:   ohm >= 1.1.16
Requires:   ohm-plugins-misc
Requires:   ohm-plugin-resolver
Requires:   ohm-plugin-ruleengine
Requires:   ohm-plugin-videoep
Requires:   ohm-plugin-fmradio
Requires:   ohm-plugin-dspep
Requires:   ohm-plugins-dbus
Requires:   ohm-plugin-telephony
Requires:   ohm-plugin-media
Requires:   ohm-plugin-accessories
Requires:   pulseaudio-policy-enforcement
BuildRequires:  libdres-utils
BuildRequires:  swi-prolog
BuildRequires:  swi-prolog-library
BuildRequires:  libprolog
BuildRequires:  prolog-resourcepolicy-extensions
Provides:   policy-settings

%description
Precompiled basic MeeGo policy settings for the N900.

%package text
Summary:    Basic MeeGo policy settings sources for the N900
Group:      System/Resource Policy
Requires:   swi-prolog-library
Requires:   ohm >= 1.1.16
Requires:   ohm-plugins-misc
Requires:   ohm-plugin-resolver
Requires:   ohm-plugin-ruleengine
Requires:   pulseaudio-policy-enforcement
Provides:   policy-settings

%description text
Basic MeeGo policy settings sources for the N900.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%autogen --disable-static
%configure --disable-static

# >> build post
make %{?jobs:-j%jobs}
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
make DESTDIR=%{buildroot} INSTALL_SYMLINKS=1 install
install -d %{buildroot}/%{_sysconfdir}/dbus-1/system.d
install -m 644 basic/etc/dbus-1/system.d/ohm-policy.conf %{buildroot}/%{_sysconfdir}/dbus-1/system.d
# << install post

%files
%defattr(-,root,root,-)
# >> files
%{_datadir}/policy/etc/current
%{_datadir}/policy/rules/current
%config %{_sysconfdir}/ohm/*.ini
%config %{_sysconfdir}/ohm/plugins.d/*.ini
%config %{_sysconfdir}/pulse/xpolicy.conf
%config %{_sysconfdir}/dbus-1/system.d/ohm-policy.conf
%{_datadir}/policy/rules/basic/*.plc
%{_datadir}/policy/rules/basic/*.dresc
%{_datadir}/policy/etc/basic/*.conf
%{_datadir}/policy/etc/basic/ohm
%{_datadir}/policy/etc/basic/pulse
# << files

%files text
%defattr(-,root,root,-)
# >> files text
%{_datadir}/policy/etc/current
%{_datadir}/policy/rules/current
%config %{_sysconfdir}/ohm/*.ini
%config %{_sysconfdir}/ohm/plugins.d/*.ini
%config %{_sysconfdir}/pulse/xpolicy.conf
%{_datadir}/policy/rules/basic/*.pl
%{_datadir}/policy/rules/basic/*.dres
%{_datadir}/policy/etc/basic/*.conf
%{_datadir}/policy/etc/basic/ohm
%{_datadir}/policy/etc/basic/pulse
# << files text