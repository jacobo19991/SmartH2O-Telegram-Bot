import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener variables de entorno
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(title, description, severity="MEDIA"):
    """
    Envía una alerta de SmartH2O a través del bot de Telegram.

    Args:
        title (str): El título de la alerta.
        description (str): La descripción detallada de la alerta.
        severity (str, opcional): La severidad de la alerta (por defecto "MEDIA").
    
    Returns:
        bool: True si el mensaje se envió con éxito, False en caso contrario.
    """
    # Validar configuración
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN no está configurado en el archivo .env.")
        return False
    
    if not TELEGRAM_CHAT_ID:
        print("Error: TELEGRAM_CHAT_ID no está configurado en el archivo .env.")
        return False

    # Validar contenido
    if not title or not description:
        print("Error: El título y la descripción del mensaje no pueden estar vacíos.")
        return False

    # Formatear el mensaje
    mensaje = f"🚨 *Alerta SmartH2O*\n\n"
    mensaje += f"*Severidad:* {severity}\n"
    mensaje += f"*Título:* {title}\n"
    mensaje += f"*Descripción:* {description}"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        
        # Validar si la respuesta HTTP es exitosa
        response.raise_for_status()
        
        # Validar si Telegram procesó correctamente la solicitud
        data = response.json()
        if data.get("ok"):
            print("Mensaje enviado exitosamente a Telegram.")
            return True
        else:
            print(f"Error devuelto por Telegram: {data.get('description')}")
            return False

    except requests.exceptions.Timeout:
        print("Error: Tiempo de espera agotado al conectar con Telegram.")
    except requests.exceptions.ConnectionError:
        print("Error: Fallo de conexión al intentar comunicarse con Telegram.")
    except requests.exceptions.HTTPError as err:
        print(f"Error HTTP al enviar el mensaje: {err}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return False
