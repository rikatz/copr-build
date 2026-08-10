Name:           herdr
Version:        0.8.0
Release:        %autorelease
Summary:        the runtime your coding agents live on

License:        Apache-2.0
URL:            https://github.com/herdrdev/herdr
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo >= 1.91
BuildRequires:  rust >= 1.91
BuildRequires:  zig = 0.15.2
BuildRequires:  gcc
BuildRequires:  cmake
ExclusiveArch:  %{rust_arches}

%description
Herdr is the runtime your coding agents live on - 
laptop, desktop, or a box you rent. It holds real terminals open so the work 
survives the lid closing, and gets you back in from anything with a keyboard.

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked
cargo tree --workspace --edges no-build,no-dev,no-proc-macro --no-dedupe \
    --prefix none --format '{l}' | sort -u > LICENSE.summary
cargo tree --workspace --edges no-build,no-dev,no-proc-macro --no-dedupe \
    --prefix none --format '{l}: {p}' | sort -u > LICENSE.dependencies

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE LICENSE.summary LICENSE.dependencies
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
%autochangelog
