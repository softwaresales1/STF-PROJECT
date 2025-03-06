# Ensure the script runs with elevated privileges
if (-Not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Please run this script as an administrator." -ForegroundColor Red
    exit 1
}

# Step 1: Set PowerShell Execution Policy
Write-Host "Setting PowerShell execution policy to RemoteSigned..." -ForegroundColor Yellow
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Step 2: Grant Execute Permissions to Activate.ps1
$activateScript = "C:\Users\user\Desktop\forge\env\Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    Write-Host "Granting execute permissions to Activate.ps1..." -ForegroundColor Yellow
    icacls $activateScript /grant Everyone:F > $null
} else {
    Write-Host "Activate.ps1 not found at $activateScript. Skipping permission grant." -ForegroundColor Red
}

# Step 3: Install pytest in the virtual environment
Write-Host "Activating virtual environment and installing pytest..." -ForegroundColor Yellow
& "C:\Users\user\Desktop\forge\env\Scripts\Activate.ps1" | Out-Null
pip install pytest

# Step 4: Configure VS Code Settings
Write-Host "Updating VS Code settings for Python testing and terminal..." -ForegroundColor Yellow
$vscodeSettingsPath = "$env:APPDATA\Code\User\settings.json"
$settings = @{
    "python.testing.pytestEnabled" = $true
    "python.testing.unittestEnabled" = $false
    "python.testing.autoTestDiscoverOnSaveEnabled" = $true
    "terminal.integrated.defaultProfile.windows" = "Command Prompt"
}

# Convert settings to JSON and update the file
if (Test-Path $vscodeSettingsPath) {
    $currentSettings = Get-Content $vscodeSettingsPath -Raw | ConvertFrom-Json
    foreach ($key in $settings.Keys) {
        $currentSettings | Add-Member -Name $key -Value $settings[$key] -Force
    }
    $currentSettings | ConvertTo-Json | Set-Content $vscodeSettingsPath
} else {
    $settings | ConvertTo-Json | Set-Content $vscodeSettingsPath
}

# Step 5: Verify Python Interpreter
Write-Host "Verifying Python interpreter in the virtual environment..." -ForegroundColor Yellow
$pythonPath = "C:\Users\user\Desktop\forge\env\Scripts\python.exe"
if (Test-Path $pythonPath) {
    & $pythonPath --version
} else {
    Write-Host "Python interpreter not found at $pythonPath." -ForegroundColor Red
}

# Step 6: Restart VS Code
Write-Host "All configurations completed. Please restart VS Code to apply changes." -ForegroundColor Green