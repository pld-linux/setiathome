Summary:	SETI@home client
Summary(pl):	Klient SETI@home
Name:		setiathome
Version:	3.03
Release:	1
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
License:	Freeware
%ifarch %{ix86}
%ifarch i686 athlon
%define _suffix i686-pc-linux-gnu-gnulibc2.1
%else
%define _suffix i386-pc-linux-gnu-gnulibc2.1
%endif
%endif
%ifarch sparc
%define _suffix sparc-unknown-linux-gnu
%endif
%ifarch alpha
%define _suffix alpha-unknown-linux-gnu
%endif
Source0:	ftp://ftp.cdrom.com/pub/setiathome/%{name}-%{version}.%{_suffix}.tar
URL:		http://www.setiathome.com/
ExclusiveArch:	%{ix86} sparc alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seti@home is a program to waste Your cpu time :)

%description -l pl
Seti@home jest pakietem do marnowania czasu Twojego procesora :)

%prep
%setup -q -n %{name}-%{version}.%{_suffix}

%install
rm -rf $RPM_BUILD_ROOT
install -D setiathome $RPM_BUILD_ROOT%{_bindir}/setiathome

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/setiathome
