Summary:	SETI@home client
Summary(pl):	Klient SETI@home
Name:		setiathome
Version:	3.08
Release:	0.2
Group:		Applications
License:	Freeware
%define	i386_suffix	i386-pc-linux-gnu-gnulibc2.1
%define	i686_suffix	i686-pc-linux-gnu
%define	alpha_suffix	alpha-unknown-linux-gnu
%define	sparc_suffix	sparc-unknown-linux-gnu
%define	ppc_suffix	powerpc-unknown-linux-gnu
%define	i386_version	3.03
%define	alpha_version	3.03
%define	sparc_version	3.03
%define	ppc_version	3.03
%ifarch %{ix86}
%ifarch i686 athlon
%define _suffix %{i686_suffix}
%define	_srcnum	0
%else
%define _suffix %{i386_suffix}
%define	_srcnum	1
%endif
%endif
%ifarch alpha
%define _suffix %{alpha_suffix}
%define	_srcnum	2
%endif
%ifarch sparc
%define _suffix %{sparc_suffix}
%define	_srcnum	3
%endif
%ifarch ppc
%define _suffix %{ppc_suffix}
%define	_srcnum	4
%endif
Source0:	ftp://alien.ssl.berkeley.edu/pub/%{name}-%{version}.%{i686_suffix}.tar
# Source0-md5:	01d05178bd22c36b2e411dd12f23661a
Source1:	ftp://alien.ssl.berkeley.edu/pub/%{name}-%{i386_version}.%{i386_suffix}.tar
Source2:	ftp://alien.ssl.berkeley.edu/pub/%{name}-%{alpha_version}.%{alpha_suffix}.tar
# Source2-md5:	ddc9d38ffb5bc7c1189857fc054b7252
Source3:	ftp://alien.ssl.berkeley.edu/pub/%{name}-%{sparc_version}.%{sparc_suffix}.tar
# Source3-md5:	1091488f55cbbfa4451c3f03cc9f8177
Source4:	ftp://alien.ssl.berkeley.edu/pub/%{name}-%{ppc_version}.%{ppc_suffix}.tar
# Source4-md5:	cb47ccfd01e6f9764edb74ce37aa216b
URL:		http://www.setiathome.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seti@home is a program to waste Your cpu time :)

%description -l pl
Seti@home jest pakietem do marnowania czasu Twojego procesora :)

%prep
%setup -q -T -b%{_srcnum} -n %{name}-%{version}.%{_suffix}

%install
rm -rf $RPM_BUILD_ROOT
install -D setiathome $RPM_BUILD_ROOT%{_bindir}/setiathome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/setiathome
