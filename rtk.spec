Name:           rtk
Version:        0.42.3
Release:        %autorelease
Summary:        CLI proxy that reduces LLM token consumption by 60-90% on common dev commands

License:        Apache-2.0
URL:            https://github.com/rtk-ai/rtk
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo >= 1.91
BuildRequires:  rust >= 1.91
BuildRequires:  gcc
ExclusiveArch:  %{rust_arches}

%description
RTK (Rust Token Killer) is a high-performance CLI proxy that filters and
compresses command outputs before they reach LLM context windows, saving
60-90%% of tokens on common development operations such as builds, tests,
git, and infrastructure commands.

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