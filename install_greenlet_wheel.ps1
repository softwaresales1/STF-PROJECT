# PowerShell script to download and install pre-built greenlet wheel for Windows

$pythonVersion = "cp311"  # Python 3.11
$arch = "win_amd64"       # 64-bit Windows
$greenletVersion = "1.1.3"

# Construct wheel filename
$wheelFile = "greenlet-$greenletVersion-$pythonVersion-$pythonVersion-$arch.whl"

# URL to download wheel from Gohlke's unofficial binaries
$url = "https://download.lfd.uci.edu/pythonlibs/w4tscw6k/$wheelFile"

# Download wheel
Write-Host "Downloading $wheelFile from $url ..."
try {
    Invoke-WebRequest -Uri $url -OutFile $wheelFile -ErrorAction Stop
} catch {
    Write-Host "Failed to download $wheelFile from $url"
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
& .\venv_py311\Scripts\Activate.ps1

# Install wheel
Write-Host "Installing greenlet wheel..."
pip install .\$wheelFile

# Cleanup
Write-Host "Cleaning up..."
Remove-Item $wheelFile

Write-Host "Greenlet installation completed."
