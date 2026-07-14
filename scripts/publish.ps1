param(
    [string]$RepoName = "claude-certified-associate-foundations"
)

$ErrorActionPreference = "Stop"
$Description = "Independent study guide for the Claude Certified Associate - Foundations certification"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI is required. Install it from https://cli.github.com/"
}

gh auth status | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Authenticate first with: gh auth login"
}

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $RepoRoot

git rev-parse --is-inside-work-tree 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    git init -b main
}

git add -A
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Build Claude Foundations study repository"
}

$Owner = gh api user --jq .login
$FullName = "$Owner/$RepoName"

gh repo view $FullName 2>$null | Out-Null
if ($LASTEXITCODE -eq 0) {
    git remote get-url origin 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        git remote add origin "https://github.com/$FullName.git"
    }
    $Branch = git branch --show-current
    git push -u origin $Branch
}
else {
    gh repo create $FullName `
        --public `
        --description $Description `
        --source . `
        --remote origin `
        --push
}

Write-Host "Published: https://github.com/$FullName"
Write-Host "After the first documentation workflow succeeds, enable GitHub Pages with Source: GitHub Actions if needed."
