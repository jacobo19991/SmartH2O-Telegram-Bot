# Análisis de Integración IoT

## 1. Puntos de monitoreo e integración

| Zona | Sensor sugerido | Dato enviado | Sistema que recibe el dato | Observación de integración |
| :--- | :--- | :--- | :--- | :--- |
| Zona Norte | Sensor de Temperatura DHT22 | `temperature`, `humidity` | InfluxDB | Frecuencia de envío sugerida: 5 minutos. |
| Zona Sur | Sensor de Movimiento PIR | `motion_status` | InfluxDB | Envío por eventos (solo cuando detecta movimiento). |
| Planta Baja | Sensor de Calidad de Aire (MQ-135) | `co2_level`, `air_quality` | InfluxDB | Calibración inicial requerida. |
| Cuarto de Servidores | Sensor de Humedad y Temperatura | `temp_server`, `hum_server` | InfluxDB | Monitoreo crítico, frecuencia de 1 minuto. |
| Almacén | Sensor de Apertura de Puertas magnético | `door_status` | InfluxDB | Monitoreo de seguridad y control de acceso. |

## 2. Variables a monitorear

| Nombre visible | Nombre técnico sugerido | Unidad | Tipo de dato | Uso dentro del sistema |
| :--- | :--- | :--- | :--- | :--- |
| Temperatura | `temperature` | °C | Float | Evaluar condiciones ambientales y disparar alertas de calor. |
| Humedad Relativa | `humidity` | % | Float | Prevenir condensación o sequedad extrema. |
| Nivel de CO2 | `co2_level` | ppm | Integer | Asegurar calidad del aire y ventilación. |
| Estado de Movimiento | `motion_status` | N/A | Boolean | Detectar presencia fuera de horario. |
| Estado de Puerta | `door_status` | N/A | Boolean | Auditar accesos a zonas restringidas. |

## 3. Flujo de integración de datos

1. **Sensor IoT:** El dispositivo físico captura la medición del entorno (ej. temperatura o movimiento).
2. **Envío de medición:** El dispositivo envía el dato al servidor central a través de un protocolo de mensajería (ej. MQTT o HTTP REST).
3. **Almacenamiento en InfluxDB:** El backend procesa el mensaje y guarda la serie temporal en la base de datos InfluxDB.
4. **Consulta por el detector:** El motor de reglas (ej. Telegraf, Kapacitor o un script en Python) consulta periódicamente los últimos valores de InfluxDB.
5. **Comparación contra umbrales:** El detector evalúa si los datos obtenidos superan o incumplen los valores límite predefinidos (normal, advertencia, crítico).
6. **Generación de alerta:** Si se rompe una regla, el sistema dispara una alerta que es notificada al equipo o registrada en un dashboard.

## 4. Umbrales relacionados con reglas

| Variable | Rango normal | Advertencia | Crítico | Regla asociada |
| :--- | :--- | :--- | :--- | :--- |
| `temperature` | 18°C - 25°C | 25°C - 28°C | > 28°C o < 15°C | Alerta de sobrecalentamiento / congelación. |
| `humidity` | 40% - 60% | 60% - 70% | > 70% o < 30% | Alerta de condensación / ambiente seco. |
| `co2_level` | < 800 ppm | 800 - 1200 ppm | > 1200 ppm | Alerta de mala calidad del aire. |
| `motion_status` | `false` (inactivo)| N/A | `true` (en horario no hábil) | Alerta de intrusión. |
| `door_status` | `closed` | Abierta > 5 min | Abierta > 15 min | Alerta de puerta abierta prolongada. |

## 5. Decisión técnica D01

**Decisión:** Uso de InfluxDB para métricas de sensores.

**Justificación:** Los datos provenientes de los sensores IoT consisten principalmente en mediciones estructuradas como series de tiempo (timestamp + valor). InfluxDB está optimizada para la escritura rápida, compresión y consulta eficiente de este tipo de datos, superando el rendimiento de bases de datos relacionales tradicionales en estos escenarios.

**Impacto en la integración:** 
- Obliga a formatear los mensajes provenientes de los sensores (o a través de un broker MQTT) al formato Line Protocol o utilizar la API HTTP de InfluxDB.
- Facilita la integración futura con herramientas de visualización como Grafana.

**Estado de la decisión:** Aprobada.

---
**Pendientes de validación con el equipo:**
- *¿Se utilizará MQTT como broker intermedio antes de InfluxDB?*
- *¿Los umbrales definidos para el cuarto de servidores serán los mismos que para las áreas generales o tendrán reglas más estrictas?*
