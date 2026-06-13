import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener solo el token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def get_chat_id():
    """
    Obtiene los últimos mensajes enviados al bot para extraer el chat_id.
    
    IMPORTANTE:
    Antes de ejecutar este script:
    1. Agrega el bot a tu grupo de Telegram (o inicia un chat directo con él).
    2. Envía un mensaje cualquiera al grupo (por ejemplo: "Hola bot").
    3. Ejecuta este script.
    """
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN no está configurado en el archivo .env.")
        print("Asegúrate de haber creado tu archivo .env y colocado tu token allí.")
        return

    print("Obteniendo actualizaciones de Telegram...\n")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if not data.get("ok"):
            print(f"Error de Telegram: {data.get('description')}")
            return
            
        resultados = data.get("result", [])
        
        if not resultados:
            print("No se encontraron mensajes recientes.")
            print("Por favor, envía un mensaje al bot en Telegram y vuelve a intentarlo.")
            return
            
        print("--- RESULTADOS ENCONTRADOS ---")
        for actualizacion in resultados:
            if "message" in actualizacion:
                chat = actualizacion["message"]["chat"]
                remitente = actualizacion["message"].get("from", {}).get("first_name", "Desconocido")
                texto = actualizacion["message"].get("text", "[Sin texto]")
                
                print(f"Mensaje de: {remitente}")
                print(f"Texto: {texto}")
                print(f"-> TU CHAT_ID ES: {chat['id']}")
                print("-" * 30)
                
        print("\nCopia el número de CHAT_ID y pégalo en tu archivo .env como TELEGRAM_CHAT_ID")
        
    except Exception as e:
        print(f"Error al conectar con Telegram: {e}")

if __name__ == "__main__":
    get_chat_id()
