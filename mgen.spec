Name:           mgen
Version:        5.1.2
Release:        1%{?dist}
Summary:        MGEN traffic generator

License:        FIXME
URL:            https://github.com/nv6/mgen
%undefine       _disable_source_fetch
Source0:        https://github.com/nv6/mgen/releases/download/%{version}/mgen-protolib-src.tar.gz
%define         SHA256SUM0 2b48034664ddd352227756af26f5f0218a1e699b90cba7a726a90dfedf5a6c32
Requires:       libpcap
BuildRequires:  gcc make libpcap-devel

%description
Multi-Generator (MGEN) traffic generation tool from US NRL

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%setup -q

%build
make -C ./makefiles -f Makefile.linux

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 ./makefiles/%{name} %{buildroot}/%{_bindir}

%clean
rm -rf %{_buildrootdir}
rm -rf %{_builddir}
rm -rf %{_sourcedir}

%files
%license LICENSE
%{_bindir}/%{name}
