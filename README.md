# Sistema de monitorización IoT y control de aforo

Este repositorio consolida la información técnica de dos componentes relacionados:

- `edge-cameras/`: adquisición en campo mediante cámaras Bosch, Raspberry Pi y transmisores LoRaWAN Dragino o Milesight.
- `monitoring-platform/`: recepción, decodificación, persistencia MySQL y visualización mediante Grafana.

## Flujo previsto

```text
Cámara o sensor
  -> Raspberry / transmisor LoRaWAN
  -> gateway LoRaWAN
  -> decodificador Java
  -> MySQL
  -> Grafana
```

Los dos proyectos originales describían extremos distintos de este flujo. No existe todavía evidencia suficiente para afirmar que el formato emitido por todos los scripts de cámaras sea compatible directamente con los decodificadores Java. Esa integración debe validarse con payloads de prueba no sensibles.

## Configuración privada

Los valores reales no forman parte del repositorio. El código utiliza variables de entorno y la documentación emplea marcadores explícitos:

- `<CAMERA_PASSWORD>`: contraseña de administración de una cámara.
- `<CAMERA_HOST_OR_IP>`: dirección privada o nombre DNS de una cámara.
- `<GATEWAY_USERNAME>` y `<GATEWAY_PASSWORD>`: credenciales del gateway.
- `<DATABASE_JDBC_URL>`, `<DATABASE_USERNAME>` y `<DATABASE_PASSWORD>`: conexión MySQL.
- `<DEVICE_DEV_EUI>`: identificador de un dispositivo desplegado.
- `<LORAWAN_APP_KEY>`: clave de activación LoRaWAN.
- `<GRAFANA_DATASOURCE_UID>`: identificador de la fuente de datos local.

Consulta `.env.example` para conocer todos los parámetros requeridos. Un archivo `.env` real está excluido mediante `.gitignore`.

## Documentación de consolidación

- [Discrepancias entre las fuentes](docs/DISCREPANCIAS.md)
- [Política de publicación segura](docs/SEGURIDAD.md)

## Estado

Esta carpeta es una base documental y técnica consolidada. Los repositorios originales no se han modificado. Antes de desplegar el sistema deben corregirse los problemas de compilación heredados, validar el esquema SQL frente a los decodificadores y probar el contrato de payload extremo a extremo.

