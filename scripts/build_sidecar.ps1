# Builds the Rust ESP sidecar (fast world projection) into bin/
cargo build --release --manifest-path src/sidecars/espcore/Cargo.toml
New-Item -ItemType Directory -Force -Path bin | Out-Null
Copy-Item src/sidecars/espcore/target/release/espcore.exe bin/espcore.exe -Force
Write-Host "[+] sidecar built -> bin/espcore.exe"