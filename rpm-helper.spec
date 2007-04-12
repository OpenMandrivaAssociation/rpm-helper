Name:       rpm-helper
Version:    0.18.4
Release:    %mkrel 2
Summary:    Helper scripts for rpm scriptlets
Source0:    %{name}-%{version}.tar.bz2
License:    GPL
Group:      System/Configuration/Packaging
URL:        http://www.mandrivalinux.com/
Requires:   grep
Requires:   shadow-utils
Requires:   chkconfig
Requires:   coreutils
# for addgroup which uses xargs
Requires:   findutils
Conflicts:  chkconfig < 1.3.4-10mdk
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Helper scripts for rpm scriptlets to help create/remove :
- groups
- services
- shells
- users

%prep
%setup -q

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_datadir}/%{name}
%{_sys_macros_dir}/%{name}.macros


