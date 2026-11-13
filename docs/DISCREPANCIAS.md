# Discrepancias entre `REMOTE_CAM` y `Sistema_monitoreo`

## Alcance distinto

`REMOTE_CAM` describe un sistema de control de aforo en playas y aparcamientos mediante cámaras Bosch. `Sistema_monitoreo` describe monitorización ambiental y de seguridad de centros mediante sensores comerciales. No son dos versiones equivalentes: representan casos de uso y capas diferentes.

## Dispositivos

- Cámaras: Bosch 7000i/8000i, Raspberry Pi, Dragino, Milesight y sensores IR.
- Plataforma: SenseCAP S2101, Milesight EM320/WS202/AM107/EM500, Dragino CPL01 y Adeunis Motion V2.
- Sólo coinciden parcialmente los fabricantes Dragino y Milesight; no coinciden necesariamente los modelos ni sus payloads.

## Datos y payloads

- La capa de cámaras produce contadores de paso y admite downlinks para fecha, hora y reinicio.
- La plataforma central procesa temperatura, humedad, presencia, puertas, CO2, presión, batería y métricas LoRaWAN.
- No se documenta un contrato común que relacione los contadores Bosch con una tabla y un decodificador concretos.
- Los scripts de cámaras usan formatos de payload diferentes según Dragino y Milesight; esto debe normalizarse y probarse.

## Persistencia

- `REMOTE_CAM` guarda temporalmente contadores en archivos de texto.
- `Sistema_monitoreo` usa MySQL y tablas separadas por familia de dispositivo.
- La documentación llama a la base de datos `iotib`, mientras varias clases Java usaban `iotib2`.
- El README indica siete tablas, pero el código y el SQL deben verificarse conjuntamente antes de considerarlo un esquema definitivo.

## Código y estructura Java

- El README de scripts menciona rutas `Scripts_Java/src/main/java/Iotib`, pero el repositorio usa `Scripts/src`.
- `pom.xml` declara una clase principal `com.mycompany.decoder.Decoder`, mientras `Decoder.java` declara `Iotib.decoder`.
- El módulo de paquetes perdidos usa el paquete `com.mycompany.paquetesperdidos`, distinto del módulo de decodificación.
- Hay nombres inconsistentes: `Database`/`database`, `DRAGINO_Payload`/`DRAGINOPayload` y `SenseCap_Payload`/`SenseCapPayload`.
- Estas diferencias pueden impedir una compilación Maven limpia.

## Configuración y seguridad

- `REMOTE_CAM` contenía una contraseña real de cámara y una IP privada en el código actual.
- El historial remoto de `REMOTE_CAM` contiene claves LoRaWAN, DevEUI, contraseñas, IP y coordenadas que no se han copiado a esta consolidación.
- `Sistema_monitoreo` afirmaba no incluir credenciales, pero contenía credenciales por defecto de gateway y MySQL, una IP local y UID de Grafana.
- Algunos clientes desactivan la verificación TLS. Esto es aceptable sólo como limitación documentada de laboratorio, no como configuración de producción.

## Frecuencia y parámetros LoRaWAN

- Ambos usan EU868 y OTAA en parte de la solución.
- El README de la plataforma describía incorrectamente la AppKey como una clave de 32 bits; una AppKey LoRaWAN es de 128 bits y suele representarse mediante 32 caracteres hexadecimales.
- La plataforma generaliza SF12 y clase A; la documentación de cámaras incluye también un dispositivo clase C.
- No debe aplicarse una única clase, intervalo o spreading factor a todos los dispositivos sin validar cada modelo.

## Ubicaciones

- `REMOTE_CAM` describe ubicaciones reales y el historial contenía coordenadas exactas.
- `Sistema_monitoreo` indica expresamente que las ubicaciones de sus dashboards son simuladas.
- Esta consolidación no incorpora coordenadas reales ni metadatos GPS de las fotografías.

## Conclusión

La interpretación más coherente es tratar `edge-cameras` como un subsistema de adquisición adicional conectado conceptualmente a `monitoring-platform`. La unión funcional aún requiere definir un esquema de payload, una tabla para aforo, un decodificador y pruebas de integración.

