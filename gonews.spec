Name:           gonews
Version:        0.0.1
Release:        1%{?dist}
Summary:        gonews Daily News Retrieval Platform

Group:          Development/Tools
License:        MIT
URL:            https://github.com/DongJeremy/%{name}
Source0:        https://github.com/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  golang, upx
Requires:       redis, git

%description
Gonews for Daily News Retrieval Platform

%prep
%setup -q


%build
go build -ldflags "-s -w" -o gonews main.go
upx --brute gonews


%install
install -d -p %{buildroot}/usr/local/%{name}/
install -p -m 0755 gonews %{buildroot}/usr/local/%{name}/%{name}
install -p -m 0644 config.ini %{buildroot}/usr/local/%{name}/
cp -a dist/ %{buildroot}/usr/local/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 %{name}.service $RPM_BUILD_ROOT%{_unitdir}


%files
%defattr(-,root,root)
/usr/local/%{name}
%{_unitdir}/%{name}.service


%changelog