# Monitoreo Remoto de Centros con Tecnología IoT y LoRaWAN

> ⚠️ Proyecto desarrollado durante mi etapa como técnico IoT en colaboración con FUEIB. Esta versión es una **recreación técnica** con fines demostrativos. No incluye datos sensibles ni contraseñas.

Este proyecto implementa una solución de **monitoreo remoto** para centros de telecomunicaciones mediante sensores IoT conectados vía **LoRaWAN** (larga distancia y bajo consumo).  
Permite recopilar en tiempo real variables como temperatura, humedad, presencia de personas y estado de puertas, facilitando una supervisión eficiente y sostenible.

---

## 🧩 Componentes del Sistema

- **Sensores IoT**: Captan datos ambientales clave.
- **Gateway LoRaWAN**: Puente entre sensores y servidor.
- **Base de datos MySQL**: Almacenamiento persistente y estructurado.
- **Scripts Java**: Procesan y decodifican los paquetes LoRa.
- **Grafana Dashboards**: Visualización interactiva de los datos.

---

## ⚙️ Objetivos del Proyecto

- Supervisión remota de entornos sin intervención constante.
- Centralización de datos de múltiples sensores en una plataforma visual.
- Detección automática de incidencias (puertas abiertas, temperaturas anómalas, etc.).

> 📁 Este repositorio incluye scripts, modelo de base de datos, dashboards y documentación técnica.

---

## 📡 LoRaWAN y Seguridad

Los sensores transmiten datos al **gateway** mediante tecnología LoRa.  
Para establecer conexión segura, se utilizan tres claves:

- **DevEUI**: Identificador único del dispositivo.
- **AppEUI**: (opcional) Identificador de la aplicación.
- **AppKey**: Clave secreta LoRaWAN de 128 bits (32 caracteres hexadecimales), generada de forma segura o proporcionada por el fabricante.

---

## 🔌 Dispositivos IoT Utilizados

| Sensor              | Fabricante | Variables Monitorizadas                        |
|---------------------|------------|------------------------------------------------|
| SenseCap S2101      | Seeed      | Temperatura exterior                           |
| Milesight EM320     | Milesight  | Temperatura y humedad interior                 |
| Milesight WS202     | Milesight  | Presencia de personas                          |
| Dragino CPL01       | Dragino    | Estado de puertas (abierta/cerrada)            |
| Milesight AM107     | Milesight  | Temperatura, CO₂, presión y humedad            |
| Adeunis Motion V2   | Adeunis    | Movimiento y luminosidad                       |
| Milesight EM500     | Milesight  | Temperatura, CO₂, humedad y presión exteriores |

📁 `Dispositivos/` → Incluye manuales y guías técnicas para decodificación.

---

## ⚙️ Configuración de Sensores

| Sensor     | App de Configuración        |
|------------|-----------------------------|
| Milesight  | Milesight Toolbox           |
| SenseCap   | SenseCAP Mate               |
| Adeunis    | IOTConfigurator             |

**Parámetros comunes:**

- Frecuencia: `868 MHz (EU868)`
- Modo: `OTAA`
- Clase: `A`
- SF: `12` (mayor alcance)

---

## 🗃️ Base de Datos (MySQL)

La base de datos almacena los datos recibidos desde los sensores a través de los scripts Java, distribuyéndolos en distintas tablas según el tipo de dispositivo.

📁 `DB/` → Estructura vacía de la base de datos en formato SQL.

---

## 💻 Scripts Java

Dos programas desarrollados en Java:

### `Decoder.java`
- Obtiene paquetes desde el gateway.
- Decodifica según el tipo de sensor.
- Almacena los datos en la base de datos.

### `PaquetesPerdidos.java`
- Calcula los paquetes perdidos por cada dispositivo (devEUI) mensualmente.
- Almacena el resultado en una tabla específica.

📁 `Scripts/` → Contiene todas las clases, documentación y lógica de decodificación.

---

## 📊 Visualización con Grafana

Obtiene los datos de la DB para poder mostrarlos en forma de gráficas y parametros interactivos en tiempo real para poder llevar un control de dichos datos con dashboards personalizados para centros geolocalizados.

-  Mapa de dispositivos distribuidos en Mallorca
- ⚠️ La ubicación recreada de los centros es falsa

📁 `Grafana/` → Exportación de dashboards en formato `.json`.

---

## Tecnologías Utilizadas

- **LoRaWAN** (SF12, OTAA, 868 MHz)
- **Java** para la lógica de backend y decodificación
- **MySQL** como sistema de almacenamiento de datos
- **Grafana** para visualización en tiempo real
- Apps: **Milesight Toolbox**, **SenseCAP Mate**, **IOTConfigurator**

---

## ✅ Resultado Final

- Sistema funcional y desplegado en entorno real.
- Visualización clara y trazabilidad histórica de los datos.
- Escalable a nuevos entornos (granjas, edificios, etc.).
- Arquitectura segura, robusta y de bajo consumo energético.
