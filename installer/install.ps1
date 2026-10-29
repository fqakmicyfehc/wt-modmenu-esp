# wt-modmenu-esp installer for Windows 10/11
param(
    [string]$InstallDir = "$env:LOCALAPPDATA\wt-modmenu-esp",
    [switch]$SkipPythonCheck
)

Write-Host "[*] Installing wt-modmenu-esp to $InstallDir"

if (-not $SkipPythonCheck) {
    $py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $py) { Write-Error "Python 3.11+ required"; exit 1 }
    python -c "import sys; assert sys.version_info >= (3,11)" | Out-Null
}

if (-not (Test-Path $InstallDir)) { New-Item -ItemType Directory -Path $InstallDir | Out-Null }

$repoRoot = Split-Path $PSScriptRoot -Parent
Copy-Item -Recurse -Force "$repoRoot\src" "$InstallDir\src"
Copy-Item -Recurse -Force "$repoRoot\offsets" "$InstallDir\offsets"
Copy-Item -Force "$repoRoot\requirements.txt" $InstallDir

Push-Location $InstallDir
python -m pip install --upgrade -r requirements.txt
Pop-Location

Write-Host "[+] Done. Launch with: python -m src.host.bootstrap"
Write-Host "[!] Educational use only. Running against live servers = ban."