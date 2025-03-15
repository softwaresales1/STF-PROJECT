# PowerShell script for setting up a Django project

# Enhanced error handling
$ErrorActionPreference = "Stop"

# Logging function
function Log {
    param (
        [string]$message
    )
    Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $message"
}

# Help message
function Show-Help {
    Write-Host "Usage: .\build.ps1 [options]"
    Write-Host "Options:"
    Write-Host "  -h, --help        Show this help message"
    Write-Host "  -c, --clean       Remove virtual environment before setup"
    Write-Host "  -t, --test        Run tests after setup"
    Write-Host "  -p, --python      Specify Python version (default: python3)"
    exit
}

# Parse arguments
$PythonCmd = "python3"
$RunTests = $false
$Clean = $false

param (
    [switch]$clean,
    [switch]$test,
    [string]$python = "python3"
)

if ($clean) {
    $Clean = $true
}

if ($test) {
    $RunTests = $true
}

# Clean virtual environment if requested
if ($Clean -and (Test-Path "venv")) {
    Log "Removing existing virtual environment..."
    Remove-Item -Recurse -Force "venv"
}

# Create and activate virtual environment
if (-not (Test-Path "venv")) {
    Log "Creating virtual environment..."
    & $PythonCmd -m venv venv
}

Log "Activating virtual environment..."
& .\venv\Scripts\Activate.ps1

# Install dependencies
Log "Upgrading pip..."
pip install --upgrade pip

Log "Installing requirements..."
pip install -r requirements.txt

# Django commands
Log "Running Django migrations..."
python manage.py migrate --no-input

Log "Collecting static files..."
python manage.py collectstatic --no-input

# Optional: Run tests
if ($RunTests) {
    Log "Running tests..."
    python manage.py test
}

Log "Build completed successfully!"
