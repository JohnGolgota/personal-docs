$basePath = Join-Path $env:HOME "Docs" "containers" "minecraft"
$dataPath = Join-Path $basePath "data"
$backupPath = Join-Path $basePath "data_backups"

$timeStamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupFolder = Join-Path $backupPath (get-date -Format "yyyy-MM-dd") $timeStamp
$backupFile = Join-Path $backupFolder "backup_$timeStamp.zip"

$logFile = Join-Path $backupFolder "initBk.log"

try
{
	New-Item -Path $backupFolder -ItemType Directory -Force

	Start-Transcript -Path $logFile -Append

	Write-Host "Init Backup: $(Get-Date)"
	Write-Host "Origin: $dataPath"
	Write-Host "Destination: $backupFile"

	if (-not (Test-Path $dataPath))
	{
		throw "Data path not found: $dataPath"
	}

	Write-Host "Compressing data..."
	Compress-Archive -Path $dataPath -DestinationPath $backupFile -CompressionLevel Optimal

	$backupSize = (Get-Item $backupFile).Length
	$backupSizeMB = [math]::Round($backupSize / 1MB, 2)

	Write-Host "Backup complete: $backupFile ($backupSizeMB MB)"

} catch
{
	Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
	exit 1
} finally
{
	Stop-Transcript
}

