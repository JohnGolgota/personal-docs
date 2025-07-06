# ⚙️ CONFIGURACIÓN BÁSICA
$serviceName = "ngrok-tunnel" # Nombre del servicio
# $programPath = "C:\Users\DESARROLLO\AppData\Local\fnm_multishells\16352_1751662991399\node.exe"
$programPath = "C:\Users\DESARROLLO\scoop\shims\ngrok.exe"
# $scriptPath = "C:\ruta\a\main.js"
$scriptPath = ""
$workingDirectory = "C:\custom_path"
$logDirectory = join-path $workingDirectory "logs" $serviceName

# 🧱 Asegúrate de que los directorios existen
New-Item -ItemType Directory -Force -Path $logDirectory | Out-Null

# 🪵 Archivos de logonline-agents
$stdoutLog = Join-Path $logDirectory "ngrok.log"
$stderrLog = Join-Path $logDirectory "ngrok.err"

# 🛠 Ruta al ejecutable de NSSM (ajusta si lo tienes en otro lugar)
$nssm = "C:\Program Files\nssm\win64\nssm.exe"

# 📌 Instalar el servicio
& $nssm install $serviceName $programPath $scriptPath

# 🔧 Configurar detalles
& $nssm set $serviceName AppDirectory $workingDirectory
& $nssm set $serviceName AppStdout $stdoutLog
& $nssm set $serviceName AppStderr $stderrLog
& $nssm set $serviceName AppRotateFiles 1
& $nssm set $serviceName AppNoConsole 1
& $nssm set $serviceName Start SERVICE_AUTO_START

# ▶️ Iniciar el servicio
& $nssm start $serviceName

# update
# Cambiar los argumentos del servicio
& $nssm set $serviceName AppParameters "http --domain=violently-master-wahoo.ngrok-free.app 80"
