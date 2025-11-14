# Marketing Analytics Setup Script for Windows PowerShell

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Marketing Analytics Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check Python version
Write-Host "Checking Python version..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
Write-Host "Found: $pythonVersion" -ForegroundColor Green
Write-Host ""

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Set your OpenAI API key:" -ForegroundColor White
Write-Host "   `$env:OPENAI_API_KEY='your-api-key-here'" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Run the analytics:" -ForegroundColor White
Write-Host "   python analyze.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "Reports will be saved to: .\reports\" -ForegroundColor White
Write-Host ""
