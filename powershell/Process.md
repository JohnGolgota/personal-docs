# Process

## Start-Process

### Example

nohup equivalent... i think

```pwsh
Start-Process pwsh
-ArgumentList "-File /example.ps1"
-NoNewWindow
-RedirectStandardOutput '/temp/output.txt'
-RedirectStandardError '/temp/errors.txt'
```