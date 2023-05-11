#!/usr/bin/env powershell

Set-ExecutionPolicy Unrestricted

if (Test-Path ./output-files) {
    Write-Host Initializing
}
else {
    Write-Host Initializing first time setup ...
    Write-Host creating Output Directory ...
    mkdir output-files
}

pip install requests
