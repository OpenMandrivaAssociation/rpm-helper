Name:		rpm-helper
Version:	0.24.12
Release:	1
Summary:	Helper scripts for rpm scriptlets
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		https://abf.rosalinux.ru/proyvind/rpm-helper
Source0:	%{name}-%{version}.tar.xz
Requires:	grep
Requires:	shadow-utils
Requires:	chkconfig
Requires(pre):	coreutils
# for addgroup which uses xargs
Requires:	findutils
# for /etc/passwd and /etc/group
Requires:	setup
# for /bin/systemctl
Requires:	systemd-units
#Conflicts:  chkconfig < 1.3.50-1
BuildArch:	noarch

%description
Helper scripts for rpm installation.

%prep
%setup -q

%install
%makeinstall_std

# Make sure these are always executable
chmod 0755 %{buildroot}%{_datadir}/%{name}/*

%check
make test

%files
%doc README NEWS AUTHORS
%{_datadir}/%{name}
%{_sys_macros_dir}/%{name}.macros
%{_localstatedir}/lib/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/ssl
