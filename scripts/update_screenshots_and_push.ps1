param(
    [string]$ConfigImagePath,
    [string]$LossImagePath,
    [string]$RepoRoot = (Get-Location).Path
)

if (-not (Test-Path $RepoRoot)) {
    Write-Error "Repo root path '$RepoRoot' does not exist."
    exit 1
}

$screenshotsDir = Join-Path $RepoRoot 'screenshots'
if (-not (Test-Path $screenshotsDir)) {
    New-Item -ItemType Directory -Path $screenshotsDir | Out-Null
}

function Copy-IfExists([string]$src, [string]$dst) {
    if ([string]::IsNullOrWhiteSpace($src)) { return $false }
    if (-not (Test-Path $src)) { Write-Host "Source not found: $src"; return $false }
    Copy-Item -Path $src -Destination $dst -Force
    Write-Host "Copied: $src -> $dst"
    return $true
}

$madeChange = $false
if (Copy-IfExists -src $ConfigImagePath -dst (Join-Path $screenshotsDir 'training_config.png')) { $madeChange = $true }
if (Copy-IfExists -src $LossImagePath -dst (Join-Path $screenshotsDir 'loss_curve.png')) { $madeChange = $true }

if (-not $madeChange) {
    Write-Host "No screenshots were copied. Provide at least one valid image path for -ConfigImagePath or -LossImagePath.";
    exit 0
}

Push-Location $RepoRoot
try {
    git add screenshots/training_config.png screenshots/loss_curve.png 2>$null
    $now = Get-Date -Format 'yyyy-MM-dd HH:mm'
    git commit -m "Add/update LlamaFactory screenshots: $now" 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Committed screenshots. Pushing to origin/main..."
        git push origin main
        if ($LASTEXITCODE -eq 0) { Write-Host "Push completed." } else { Write-Host "Push failed. Check remote/authentication." }
    } else {
        Write-Host "No changes to commit (files unchanged)."
    }
} finally {
    Pop-Location
}
