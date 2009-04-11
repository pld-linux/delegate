# TODO:
# - path, files, configs, fixes etc (see http://cvs.openpkg.org/fileview?f=openpkg-src/delegate/delegate.spec&v=1.141)
Summary:	A multi-purpose application level gateway, or a proxy server
Name:		delegate
Version:	9.9.2
Release:	0.1
License:	Freely distributable via publicly accessible on-line media
Group:		Networking/Daemons
Source0:	ftp://ftp.delegate.org/pub/DeleGate/%{name}%{version}.tar.gz
# Source0-md5:	903d76beaaa1125d828829b52339086a
URL:		http://www.delegate.org/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DeleGate is a multi-purpose application level gateway, or a proxy
server which runs on multiple platforms (Unix, Windows, MacOS X and
OS/2). DeleGate mediates communication of various protocols (HTTP,
FTP, NNTP, SMTP, POP, IMAP, LDAP, Telnet, SOCKS, DNS, etc.), applying
cache and conversion for mediated data, controlling access from
clients and routing toward servers. It translates protocols between
clients and servers, applying SSL(TLS) to arbitrary protocols,
converting between IPv4 and IPv6, merging several servers into a
single server view with aliasing and filtering. Born as a tiny proxy
for Gopher in March 1994, it has steadily grown into a general purpose
proxy server. Besides being a proxy, DeleGate can be used as a simple
origin server for some protocols (HTTP, FTP and NNTP).

%prep
%setup -q -n %{name}%{version}

cat << 'EOF' > src/DELEGATE_CONF
ADMIN = root@localhost
CC = %{__cc}
CXX = %{__cxx}
CFLAGS = %{rpmcflags} %{rpmcppflags}
EOF

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}

install src/delegated $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT *.html *.txt doc/*.*
