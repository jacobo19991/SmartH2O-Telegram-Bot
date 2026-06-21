# Análisis del Escenario Hídrico - SmartH2O

## 1. Objetivo del análisis

Este documento define los puntos de monitoreo, las variables principales y los umbrales iniciales del sistema SmartH2O.
El propósito es dejar clara la base técnica para detectar comportamientos anómalos en el consumo de agua y facilitar la integración con InfluxDB, el detector de reglas y el bot de alertas.
SmartH2O se enfoca en el monitoreo inteligente del consumo hídrico, por lo tanto este análisis se centra en caudal, volumen acumulado, estado del sensor, ubicación y posibles fugas.

## 2. Puntos de monitoreo

| Zona | Punto de medición |
| --- | --- |
| Zona A | Sanitarios piso 1 |
| Zona B | Cocina / comedor institucional |
| Zona C | Áreas verdes / riego exterior |
| Zona D | Cuarto de mantenimiento / cisterna |
| Zona E | Sanitarios piso 2 |

## 3. Variables correctas

- `sensor_id`
- `timestamp`
- `flow_rate`
- `cumulative_volume`
- `status`
- `anomaly_flag`
- `location`

## 4. Flujo de integración

Sensor / Simulador IoT → MQTT/REST → Servicio de Ingestión → InfluxDB → Detector de reglas → Bot de Telegram / Email

## 5. Tabla de umbrales normales y anómalos relacionados con consumo de agua

| Zona | Comportamiento normal | Advertencia | Crítico / Anomalía | Posible causa |
| --- | --- | --- | --- | --- |
| Sanitarios piso 1 | 0–15 L/min en horario laboral | Más de 15 L/min por más de 5 minutos | Más de 20 L/min por más de 10 minutos | Posible fuga o uso excesivo. |
| Cocina / comedor | 0–18 L/min en horarios de comida | Más de 18 L/min por más de 5 minutos | Más de 25 L/min por más de 10 minutos | Consumo anormal o llave abierta. |
| Riego exterior | Consumo solo en horario programado | Consumo fuera del horario esperado | Caudal nocturno mayor a 5 L/min | Riego activo fuera de horario o fuga. |
| Cisterna / mantenimiento | Flujo variable según demanda | Flujo continuo por más de 10 minutos | Flujo alto sostenido por más de 15 minutos | Posible fuga, rebalse o falla. |
| Sanitarios piso 2 | 0–10 L/min en horario laboral | Más de 10 L/min por más de 5 minutos | Caudal nocturno mayor a 5 L/min | Consumo fuera de patrón o fuga. |

## 6. Reglas iniciales

- R01: `flow_rate` > 20 L/min durante más de 10 minutos → critical → Telegram → posible fuga.
- R02: `flow_rate` > 5 L/min en horario nocturno → warning → Telegram → consumo fuera de horario.
- R03: sensor sin datos por más de 10 minutos → warning → Telegram/email → posible desconexión.
- R04: `cumulative_volume` supera el consumo esperado diario → critical → Telegram/email → consumo acumulado anormal.

## 7. Decisión técnica D01

**Decisión:** Uso de InfluxDB para almacenar métricas de consumo de agua.
**Justificación:** Las lecturas de SmartH2O son datos asociados al tiempo (series temporales). InfluxDB es adecuada para almacenar, consultar y facilitar la detección de anomalías hídricas.

## 8. Pendientes de validación con el equipo

- Confirmar si el envío de datos será mediante MQTT o REST.
- Confirmar si InfluxDB será la base de datos definitiva.
- Validar los umbrales con el equipo.
- Confirmar los horarios laborales, nocturnos y de riego.
- Definir canales definitivos.
