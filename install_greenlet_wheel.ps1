# PowerShell script to install pre-built greenlet wheel to avoid build errors on Windows

# Check if greenlet is already installed
$greenletInstalled = pip show greenlet -q
if (-not $greenletInstalled) {
    Write-Host "Greenlet not found, attempting to install pre-built wheel..."

    # Define URL for pre-built greenlet wheel for Python 3.12 on Windows 64-bit
    $wheelUrl = "https://github.com/greenlet/greenlet/releases/download/3.1.1/greenlet-3.1.1-cp312-cp312-win_amd64.whl"

    # Download the wheel
    $wheelFile = "greenlet-3.1.1-cp312-cp312-win_amd64.whl"
    Invoke-WebRequest -Uri $wheelUrl -OutFile $wheelFile

    # Install the wheel
    pip install $wheelFile

    # Remove the wheel file
    Remove-Item $wheelFile

    Write-Host "Greenlet installed successfully from pre-built wheel."
} else {
    Write-Host "Greenlet is already installed."
}
