# Start-Process

## Description

The `Start-Process` cmdlet starts one or more processes on the local computer.

```powershell
$options = @{
    FilePath = "node.exe" # path to the executable
    ArgumentList = "--version" # arguments to pass to the executable
    WorkingDirectory = "C:\Windows\System32" # working directory
    Wait = $false # wait for the process to exit
    WindowStyle = "Hidden" # hidden window
    UseNewEnvironment = $false # inherit the parent environment
}
Start-Process @options
```

Para verificar que el proceso se ha iniciado correctamente, puedes usar el comando `Get-Process` para ver los procesos en ejecución.

```powershell
Get-Process
```
