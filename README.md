# SmartH2O Telegram Bot

Este proyecto es una integración de notificaciones por Telegram para el proyecto académico **SmartH2O**. Permite enviar alertas de forma automatizada y segura.

## 📋 ¿Qué hace este proyecto?
Contiene los scripts para conectarse a la API de Telegram y enviar notificaciones. Incluye buenas prácticas de seguridad (variables de entorno), protección contra inyección de HTML y una clase `TelegramBot` escalable.

## 🚀 Instalación y Preparación

1. Asegúrate de tener Python instalado.
2. Instala las dependencias necesarias:

**Windows PowerShell / Linux / Mac:**
```bash
pip install -r requirements.txt
```

## 🔐 Configuración (Archivo `.env`)

> ⚠️ **ADVERTENCIA IMPORTANTE:** El token funciona como la contraseña de tu bot. **NUNCA** debes subir tu archivo `.env` a GitHub ni compartirlo en lugares públicos. 

Para configurar tu proyecto localmente:

1. Duplica el archivo `.env.example` y nómbralo `.env`:
   - **En Windows PowerShell:** `Copy-Item .env.example .env`
   - **En Linux / Git Bash:** `cp .env.example .env`

2. Abre el archivo `.env` y rellena las dos variables:
   - `TELEGRAM_BOT_TOKEN`: La credencial que autoriza a tu código a usar el bot.
   - `TELEGRAM_CHAT_ID`: El identificador de la conversación donde llegarán los mensajes.

### 🤖 ¿Cómo obtener el TELEGRAM_BOT_TOKEN?
1. Abre Telegram y busca a **@BotFather**.
2. Escríbele `/newbot` y sigue las instrucciones para darle un nombre.
3. Al finalizar, BotFather te dará un Token (se ve parecido a esto: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`).
4. Cópialo y pégalo en tu archivo `.env`.

### 🔍 ¿Cómo obtener el TELEGRAM_CHAT_ID?
El Chat ID le dice al bot a quién enviarle el mensaje (puede ser a ti directamente o a un grupo).

1. Abre Telegram y búscate a ti mismo o crea un grupo y añade a tu bot.
2. **Escríbele un mensaje al bot** (ej. "hola"). Esto es obligatorio para que Telegram registre el chat.
3. En tu terminal, ejecuta este comando:

**Windows PowerShell / Linux / Git Bash:**
```bash
python src/get_chat_id.py
```
> **Nota para grupos:** Si agregaste el bot a un grupo, el `chat_id` normalmente empezará con un signo negativo (ej: `-100123456789`). Es completamente normal. Cópialo completo con el guion.

## 🧪 Probar el funcionamiento

Una vez que tengas tu `.env` con el TOKEN y el CHAT_ID, puedes ejecutar la prueba:

**Windows PowerShell / Linux / Git Bash:**
```bash
python src/test_bot.py
```

Si todo está bien, verás un mensaje de éxito en la consola y recibirás la notificación en Telegram.

## 🛠️ Errores comunes y soluciones

- **`TELEGRAM_BOT_TOKEN no está configurado`**: Significa que no creaste el archivo `.env` o el nombre de la variable no coincide.
- **`Error devuelto por Telegram: Bad Request: chat not found`**: El bot no encuentra el CHAT_ID. Asegúrate de haberle mandado un mensaje primero.
- **`Error devuelto por Telegram: Unauthorized`**: Tu Token es incorrecto o está incompleto en el `.env`.
