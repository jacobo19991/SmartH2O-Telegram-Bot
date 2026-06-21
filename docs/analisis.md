# Análisis del Escenario Hídrico - SmartH2O

## 1. Objetivo del análisis

Este documento define los puntos de monitoreo, variables principales y umbrales iniciales del sistema SmartH2O. Su propósito es dejar clara la base técnica para detectar comportamientos anómalos en el consumo de agua y facilitar la integración con InfluxDB, el detector de reglas y el bot de alertas.

## 2. Puntos de monitoreo

| ID del sensor | Zona | Punto de medición | Patrón de uso esperado | Observación de integración |
|---|---|---|---|---|
| SH2O-ZA-001 | Zona A | Sanitarios piso 1 | Alto consumo durante horario laboral | Se espera mayor caudal en horas de mayor tráfico. |
| SH2O-ZB-001 | Zona B | Cocina / comedor institucional | Consumo alto en horarios de comida | Es normal que existan picos durante desayuno, almuerzo o limpieza. |
| SH2O-ZC-001 | Zona C | Áreas verdes / riego exterior | Consumo programado en horarios específicos | Se debe detectar consumo fuera del horario de riego. |
| SH2O-ZD-001 | Zona D | Cuarto de mantenimiento / cisterna | Flujo controlado según demanda | Punto crítico para detectar fugas o flujo continuo. |
| SH2O-ZE-001 | Zona E | Sanitarios piso 2 | Bajo consumo, especialmente en horario nocturno | Puede servir como referencia para detectar consumo fuera de horario. |

## 3. Variables a monitorear

| Nombre visible | Nombre técnico | Unidad | Tipo de dato | Uso dentro del sistema |
|---|---|---|---|---|
| Identificador del sensor | sensor_id | N/A | String | Identifica el punto de medición que envía la lectura. |
| Fecha y hora | timestamp | ISO 8601 | DateTime/String | Registra cuándo ocurrió la medición. |
| Caudal instantáneo | flow_rate | L/min | Float | Permite detectar consumo alto o posible fuga. |
| Volumen acumulado | cumulative_volume | L | Float | Permite conocer el consumo total diario por zona. |
| Estado del sensor | status | normal/warning/critical/offline | Enum/String | Indica la condición general del sensor o lectura. |
| Bandera de anomalía | anomaly_flag | true/false | Boolean | Marca si la lectura presenta comportamiento anómalo. |
| Ubicación | location | building/floor/zone | Object | Relaciona la lectura con edificio, piso y zona. |

## 4. Umbrales de comportamiento normal y anómalo

| Zona | Comportamiento normal | Advertencia | Crítico / Anomalía | Posible causa |
|---|---|---|---|---|
| Sanitarios piso 1 | 0–15 L/min en horario laboral | Más de 15 L/min por más de 5 minutos | Más de 20 L/min por más de 10 minutos | Posible fuga o uso excesivo. |
| Cocina / comedor | 0–18 L/min en horarios de comida | Más de 18 L/min por más de 5 minutos | Más de 25 L/min por más de 10 minutos | Consumo anormal o llave abierta. |
| Riego exterior | Consumo solo en horario programado | Consumo fuera del horario esperado | Caudal nocturno mayor a 5 L/min | Riego activo fuera de horario o fuga. |
| Cisterna / mantenimiento | Flujo variable según demanda | Flujo continuo por más de 10 minutos | Flujo alto sostenido por más de 15 minutos | Posible fuga, rebalse o falla. |
| Sanitarios piso 2 | 0–10 L/min en horario laboral | Más de 10 L/min por más de 5 minutos | Caudal nocturno mayor a 5 L/min | Consumo fuera de patrón o fuga. |

## 5. Reglas iniciales de anomalía

| Regla | Condición | Severidad | Canal | Descripción |
|---|---|---|---|---|
| R01 | flow_rate > 20 L/min durante más de 10 minutos | critical | Telegram | Posible fuga o consumo excesivo sostenido. |
| R02 | flow_rate > 5 L/min en horario nocturno | warning | Telegram | Consumo fuera del horario esperado. |
| R03 | Sensor sin datos por más de 10 minutos | warning | Telegram/email | Posible desconexión o falla del sensor. |
| R04 | cumulative_volume supera el consumo esperado diario | critical | Telegram/email | Consumo acumulado anormal para la zona. |

## 6. Pendientes de validación

- Confirmar si el envío de datos será mediante MQTT o REST.
- Confirmar si InfluxDB será la base de datos definitiva.
- Validar los umbrales con el equipo.
- Confirmar los horarios laborales, nocturnos y de riego.
- Definir si las alertas se enviarán por Telegram, email o ambos canales.
