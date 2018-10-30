%bcond_with debug

Name:		rpm-helper
Version:	0.24.17
Release:	9
Summary:	Helper scripts for rpm scriptlets
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		https://github.com/OpenMandrivaSoftware/rpm-helper
Source0:	%{name}-%{version}.tar.xz
%if %{with debug}
Patch0:		rpm-helper-debug-useradd.patch
Patch1:		try-to-print-cmdline.patch
Requires:	strace
%endif
Requires(pre):	grep
Requires(pre):	util-linux >= 2.27.1
Requires(pre):	shadow >= 2:4.5
Requires(pre):	chkconfig >= 1.7
Requires(pre):	coreutils >= 8.24
# for addgroup which uses xargs
Requires(pre):	findutils
# for /etc/passwd and /etc/group
Requires(pre):	setup >= 2.8.9
# for /bin/systemctl
Requires(pre):	systemd >= 228
Requires(pre):	/bin/sh
#Conflicts:  chkconfig < 1.3.50-1
BuildArch:	noarch

%description
Helper scripts for rpm installation.

%prep
%autosetup

%install
%makeinstall_std

# Make sure these are always executable
chmod 0755 %{buildroot}%{_datadir}/%{name}/*

#%check
# only test in place is for add-syslog, which is dependent on it's former perl
# implementation
#make test

%pre
printf '%s\n' "Installing prerequired packages"

%files
%doc README NEWS AUTHORS
%{_datadir}/%{name}
%{_sys_macros_dir}/%{name}.macros
%{_localstatedir}/lib/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/ssl
