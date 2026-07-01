# Launcher for Windows: creates .venv if needed, then runs pyPracLab.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$Venv = ".venv"
$Py = Join-Path $Venv "Scripts\python.exe"

if (-not (Test-Path $Py)) {
    Write-Host "Creating virtualenv..."
    python -m venv $Venv
    & (Join-Path $Venv "Scripts\pip.exe") install --upgrade pip
    & (Join-Path $Venv "Scripts\pip.exe") install -r requirements.txt
    # stdlib curses does not exist on Windows; the TUI needs this shim.
    & (Join-Path $Venv "Scripts\pip.exe") install windows-curses
}

& $Py -m pypractlab @args
