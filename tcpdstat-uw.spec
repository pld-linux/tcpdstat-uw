Summary:	tcpdump trace file analyzer
Summary(pl):	Analizator pliku ¶ledzenia tcpdump
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

%description -l pl
Tcpdstat jest programem wy³uskuj±cym statystyki z plików ¶ledzenia
tcpdumpa. Tcpdstat czyta taki plik u¿ywaj±c biblioteki pcap i
wy¶wietla statystyki ¶ledzenia. Wyj¶cie zawiera liczbê pakietów,
¶redni± przep³ywno¶æ i jej odchylenie standardowe, liczbê unikalnych
par adresów ¼róde³ i celów oraz rozk³ad protoko³ów. Tcpdstat ma
zapewniaæ ogólny ogl±d prze¶ledzonych po³±czeñ. Wyj¶cie mo¿e byæ ³atwo
przekonwertowane na format HTTP. Podaje równie¿ informacje przydatne w
odnajdywaniu anomalii.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man3}

install tcpdstat $RPM_BUILD_ROOT%{_bindir}
install queue.man $RPM_BUILD_ROOT%{_mandir}/man3/queue.3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.uw
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man3/
