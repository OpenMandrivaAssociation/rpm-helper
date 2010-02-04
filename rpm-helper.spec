Name:       rpm-helper
Version:    0.23.0
Release:    %mkrel 1
Summary:    Helper scripts for rpm scriptlets
License:    GPL
Group:      System/Configuration/Packaging
URL:        http://www.mandrivalinux.com/
Source0:    %{name}-%{version}.tar.bz2
Requires:   grep
Requires:   shadow-utils
Requires:   chkconfig
Requires:   coreutils
# for addgroup which uses xargs
Requires:   findutils
# for /etc/passwd and /etc/group
Requires:   setup
Conflicts:  chkconfig < 1.3.4-10mdk
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Helper scripts for rpm installation.

%prep
%setup -q

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_datadir}/%{name}
%{_sys_macros_dir}/%{name}.macros
%config(noreplace) %{_sysconfdir}/sysconfig/ssl
