from telegram_bot import send_telegram_alert

def main():
    print("Iniciando prueba del bot de Telegram de SmartH2O...\n")
    print("Enviando mensaje...")
    
    # Enviar mensaje de prueba (incluye caracteres < > para verificar escape HTML)
    exito = send_telegram_alert(
        title="Prueba de integración del bot <OK>",
        description="El bot de SmartH2O está funcionando correctamente y las etiquetas HTML están seguras.",
        severity="BAJA"
    )
    
    if exito:
        print("\n✅ Prueba finalizada con éxito. ¡Revisa tu aplicación de Telegram!")
    else:
        print("\n❌ La prueba falló. Revisa los errores en la consola.")
        print("💡 Sugerencia: Revisa que tu archivo .env esté bien configurado.")

if __name__ == "__main__":
    main()
