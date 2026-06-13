import os
import html
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class TelegramBot:
    """
    Clase para manejar la conexión y envíos de mensajes a Telegram de forma segura.
    Reutilizable para futuros módulos (ej: rules, detector, notifier).
    """
    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.base_url = "https://api.telegram.org/bot{}/sendMessage"
    
    def validate_config(self):
        """Valida que las credenciales existan en el entorno."""
        if not self.token:
            print("❌ Error: TELEGRAM_BOT_TOKEN no está configurado en el archivo .env.")
            return False
        if not self.chat_id:
            print("❌ Error: TELEGRAM_CHAT_ID no está configurado en el archivo .env.")
            return False
        return True

    def send_message(self, title, description, severity="MEDIA"):
        """Envía el mensaje formateado en HTML escapando caracteres peligrosos."""
        if not self.validate_config():
            return False
            
        if not title or not description:
            print("❌ Error: El título y la descripción del mensaje no pueden estar vacíos.")
            return False

        # Escapar contenido dinámico para evitar inyección o ruptura de etiquetas HTML
        safe_title = html.escape(title)
        safe_description = html.escape(description)
        safe_severity = html.escape(severity)

        # Formatear el mensaje usando HTML para mayor robustez
        mensaje = (
            "🚨 <b>Alerta SmartH2O</b>\n\n"
            f"<b>Severidad:</b> {safe_severity}\n"
            f"<b>Título:</b> {safe_title}\n"
            f"<b>Descripción:</b> {safe_description}"
        )

        url = self.base_url.format(self.token)
        payload = {
            "chat_id": self.chat_id,
            "text": mensaje,
            "parse_mode": "HTML"
        }

        try:
            # Se utiliza timeout de 10 segundos según buenas prácticas
            response = requests.post(url, json=payload, timeout=10)
            
            # Validar si la respuesta HTTP es exitosa
            response.raise_for_status()
            
            # Validar si Telegram procesó correctamente la solicitud
            data = response.json()
            if data.get("ok"):
                return True
            else:
                # Extraer error sin exponer el token
                error_desc = data.get('description', 'Desconocido')
                print(f"❌ Error devuelto por Telegram: {error_desc}")
                return False

        except requests.exceptions.Timeout:
            print("❌ Error: Tiempo de espera agotado al conectar con Telegram.")
        except requests.exceptions.ConnectionError:
            print("❌ Error: Fallo de conexión al intentar comunicarse con Telegram.")
        except requests.exceptions.HTTPError as err:
            # Ocultar token en caso de venir en la URL de error
            safe_error = str(err).replace(self.token, "***TOKEN_OCULTO***")
            print(f"❌ Error HTTP al enviar el mensaje: {safe_error}")
        except Exception as e:
            # Ocultar token en excepciones genéricas
            safe_error = str(e).replace(self.token, "***TOKEN_OCULTO***")
            print(f"❌ Error inesperado: {safe_error}")
        
        return False

def send_telegram_alert(title, description, severity="MEDIA"):
    """
    Envía una alerta de SmartH2O a través del bot de Telegram.
    (Mantiene compatibilidad con la versión anterior para no romper el código actual).

    Args:
        title (str): El título de la alerta.
        description (str): La descripción detallada de la alerta.
        severity (str, opcional): La severidad de la alerta (por defecto "MEDIA").
    
    Returns:
        bool: True si el mensaje se envió con éxito, False en caso contrario.
    """
    bot = TelegramBot()
    return bot.send_message(title, description, severity)
