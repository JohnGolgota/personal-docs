# Minecraft

## main server

usa rcon-cli para cambiar la dificultad del mundo y agregar/quitar jugadores de la white list
[Minecraft Server on Docker (Java Edition)](https://docker-minecraft-server.readthedocs.io/en/latest/)

## cronjob

### cron 2:30 am every day backup

```bash
30 2 * * * /usr/bin/pwsh -f /home/serv/personal-docs/containers/minecraft/initBk.ps1
```
