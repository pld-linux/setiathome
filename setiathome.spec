Summary:	SETI@home client
Summary(pl):	Klient SETI@home
Name:		setiathome
Version:	3.03
Release:	2
Group:		Applications/Console
License:	Freeware
%define	i386_suffix	i386-pc-linux-gnu-gnulibc2.1
%define	i686_suffix	i686-pc-linux-gnu-gnulibc2.1
%define	alpha_suffix	alpha-unknown-linux-gnu
%define	sparc_suffix	sparc-unknown-linux-gnu
%define	ppc_suffix	powerpc-unknown-linux-gnu
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
%define _suffix %{alpha-unknown-linux-gnu}
%define	_srcnum	2
%endif
%ifarch sparc
%define _suffix %{sparc_suffix}
%define	_srcnum	3
%endif
%ifarch ppc
%define _suffix %{powerpc-unknown-linux-gnu}
%define	_srcnum	4
%endif
Source0:	ftp://ftp.cdrom.com/pub/setiathome/%{name}-%{version}.%{i686_suffix}.tar
Source1:	ftp://ftp.cdrom.com/pub/setiathome/%{name}-%{version}.%{i386_suffix}.tar
Source2:	ftp://ftp.cdrom.com/pub/setiathome/%{name}-%{version}.%{alpha_suffix}.tar
Source3:	ftp://ftp.cdrom.com/pub/setiathome/%{name}-%{version}.%{sparc_suffix}.tar
Source4:	ftp://ftp.cdrom.com/pub/setiathome/%{name}-%{version}.%{ppc_suffix}.tar
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
