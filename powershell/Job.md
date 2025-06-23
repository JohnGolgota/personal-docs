# Job

background jobs

## Start-Job

### Example

```pwsh
$job = Start-Job -ScriptBlock {
    Write-Host "Hello World"
}
```

```pwsh
Start-Job -Name nginxProxy -FilePath "example.ps1"
```