%define		subver	db0abbb
%define		rel		0.1
Summary:	Network Time Protocol client
Name:		ntimed
Version:	0
Release:	0.%{subver}.%{rel}
License:	BSD-2-Clause
Group:		Networking/Daemons
Source0:	https://github.com/bsdphk/Ntimed/archive/master/%{name}-g%{subver}.tar.gz
# Source0-md5:	e963b1b1c6ef2fce65335709aa2e9479
URL:		http://phk.freebsd.dk/time/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ntimed is a new NTP client package sponsored by the Linux Foundation
as part of its Core Infrastructure Initiative, which is a
post-Heartbleed effort to secure the software that runs the internet.

%prep
%setup -qc
mv Ntimed-*/* .

head -n 26 configure > LICENSE

%build
sh configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIE -pie"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p ntimed-client $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%attr(755,root,root) %{_sbindir}/ntimed-client
