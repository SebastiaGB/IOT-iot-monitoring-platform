# Política de publicación segura

## Nunca publicar valores reales

- Contraseñas de cámaras, gateway, base de datos o Grafana.
- AppKey, NwkSKey, AppSKey, tokens o claves privadas.
- DevEUI de dispositivos desplegados cuando permita identificar la instalación.
- IP públicas, topología interna, SSID o coordenadas operativas.
- Archivos `.env`, certificados, copias de seguridad con datos o volcados de producción.

## Marcadores permitidos

Usa marcadores descriptivos, por ejemplo:

```text
<CAMERA_PASSWORD>
<CAMERA_HOST_OR_IP>
<DEVICE_DEV_EUI>
<LORAWAN_APP_KEY>
<DATABASE_PASSWORD>
```

## Reglas operativas

1. Los secretos se inyectan mediante variables de entorno o un gestor de secretos.
2. `.env.example` contiene sólo nombres y marcadores.
3. Las imágenes se publican sin EXIF ni coordenadas GPS.
4. Los ejemplos SQL no contienen filas reales.
5. Antes de cada publicación se ejecuta un escáner de secretos sobre archivos e historial.
6. Si una clave llegó a Git, se rota; borrarla del último commit no basta.

