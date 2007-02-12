Summary:	tcpdump trace file analyzer
Summary(pl.UTF-8):	Analizator pliku śledzenia tcpdump
Name:		tcpdstat-uw
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://staff.washington.edu/dittrich/talks/core02/tools/%{name}.tar
# Source0-md5:	64b246fb0a4ee47ae37e83d721b205df
URL:		http://www.csl.sony.co.jp/person/kjc/papers/freenix2000/node14.html
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpdstat a program to extract statistical information from tcpdump
trace files. Tcpdstat reads a tcpdump file using the pcap library and
prints the statistics of a trace. The output includes the number of
packets, the average rate and its standard deviation, the number of
unique source and destination address pairs, and the breakdown of
protocols. Tcpdstat is intended to provide a rough idea of the trace
content. The output can be easily converted to a HTTP format. It also
provides helpful information to find anomaly in a trace.

%description -l pl.UTF-8
Tcpdstat jest programem wyłuskującym statystyki z plików śledzenia
tcpdumpa. Tcpdstat czyta taki plik używając biblioteki pcap i
wyświetla statystyki śledzenia. Wyjście zawiera liczbę pakietów,
średnią przepływność i jej odchylenie standardowe, liczbę unikalnych
par adresów źródeł i celów oraz rozkład protokołów. Tcpdstat ma
zapewniać ogólny ogląd prześledzonych połączeń. Wyjście może być łatwo
przekonwertowane na format HTTP. Podaje również informacje przydatne w
odnajdywaniu anomalii.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	INCLUDES="-I."

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install tcpdstat $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.uw
%attr(755,root,root) %{_bindir}/*
