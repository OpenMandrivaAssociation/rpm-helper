%bcond_with debug

Name:		rpm-helper
Version:	0.24.20
Release:	2
Summary:	Helper scripts for rpm scriptlets
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		https://github.com/OpenMandrivaSoftware/rpm-helper
Source0:	https://github.com/OpenMandrivaSoftware/rpm-helper/archive/refs/tags/%{version}.tar.gz
%if %{with debug}
Patch0:		rpm-helper-debug-useradd.patch
Patch1:		try-to-print-cmdline.patch
Requires:	strace
%endif
Requires:	grep
Requires(pre):	shadow
Requires:	shadow >= 2:4.5
Requires:	chkconfig >= 1.7
Requires:	coreutils >= 8.24
# for addgroup which uses xargs
Requires:	findutils
# for /etc/passwd and /etc/group
Requires:	setup >= 2.8.9
# for /bin/systemctl
Requires:	systemd >= 228
Requires:	/bin/sh
#Conflicts:  chkconfig < 1.3.50-1
BuildArch:	noarch

%description
Helper scripts for rpm installation.

%prep
%autosetup

%install
%make_install

# Make sure these are always executable
chmod 0755 %{buildroot}%{_datadir}/%{name}/*

#%check
# only test in place is for add-syslog, which is dependent on it's former perl
# implementation
#make test

%pre
printf '%s\n' "Installing prerequired packages."

%files
%doc README NEWS AUTHORS
%{_datadir}/%{name}
%{_usrlibrpm}/macros.d/macros.%{name}
%{_localstatedir}/lib/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/ssl
