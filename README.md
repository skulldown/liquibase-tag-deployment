





# Get the release info from GitHub
$release = gh release view --json tagName,body | ConvertFrom-Json
$tag = $release.tagName
$description = $release.body

# Normalize line endings and split into lines
$lines = $description -replace "`r`n", "`n" -replace "`r", "`n" -split "`n"

# Step 1: Find the CR List line
$crLine = $lines | Where-Object { $_ -match '^CR List:' }

# Step 2: Extract CR values into a list
$crValues = @()
if ($crLine -match '^CR List:\s*(.+)$') {
    $rawList = $matches[1]
    $crValues = $rawList -split '\s*,\s*'  # Split on commas
}

# Build JSON output
$releaseDetails = [PSCustomObject]@{
    tag         = $tag
    <!-- description = $description -->
    cr_numbers  = $crValues
}

# Convert to JSON and print
$jsonOutput = $releaseDetails | ConvertTo-Json -Depth 3
Write-Host "`n===== RELEASE DETAILS JSON ====="
Write-Host $jsonOutput
