# SmartH2O Telegram Bot

Este proyecto es una integración de notificaciones por Telegram para el proyecto **SmartH2O**. Permite enviar alertas y notificaciones fácilmente a un chat o grupo de Telegram de forma segura.

## 📋 ¿Qué hace este proyecto?
Contiene los scripts base para conectarse a la API de Telegram y enviar mensajes automáticos sobre el estado, alertas o severidades del sistema SmartH2O.

## 🚀 Cómo instalar las dependencias

Es necesario instalar las bibliotecas de Python requeridas (`requests` y `python-dotenv`) para que el bot funcione.

**Para Windows PowerShell / Linux / Mac:**
```bash
pip install -r requirements.txt
```

## 🔐 Configuración (Crear tu archivo `.env`)

Por seguridad, nunca debes colocar tu token ni chat ID directamente en el código.

1. Haz una copia del archivo `.env.example` y nómbrala `.env`
   - **En Windows PowerShell:**
     ```powershell
     Copy-Item .env.example .env
     ```
   - **En Linux / Git Bash:**
     ```bash
     cp .env.example .env
     ```
2. Abre el archivo `.env` recién creado con un editor de texto.
3. Reemplaza `your_telegram_bot_token_here` por el Token de tu bot.
4. Reemplaza `your_telegram_chat_id_here` por el ID de tu chat.

> ⚠️ **ADVERTENCIA IMPORTANTE:** El archivo `.env` contiene credenciales secretas. **NUNCA** debes subirlo a GitHub ni compartirlo. Por eso ya se encuentra dentro del `.gitignore`.

## 🔍 Cómo obtener el Chat ID

Si no conoces el `TELEGRAM_CHAT_ID` donde el bot debe enviar los mensajes:

1. Agrega tu bot a un grupo de Telegram o inicia un chat privado con él.
2. Escríbele cualquier mensaje (por ejemplo: "hola").
3. Ejecuta el siguiente comando para averiguar el ID:

**Windows PowerShell / Linux / Git Bash:**
```bash
python src/get_chat_id.py
```
Anota el número que aparezca en consola y ponlo en tu archivo `.env`.

## 🧪 Cómo probar el bot

Una vez que tengas tu archivo `.env` configurado correctamente con ambos valores, puedes probar que el bot funciona enviando un mensaje de prueba:

**Windows PowerShell / Linux / Git Bash:**
```bash
python src/test_bot.py
```
Deberías recibir un mensaje de alerta en tu aplicación de Telegram.
