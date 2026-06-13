from telegram_bot import send_telegram_alert

def main():
    print("Iniciando prueba del bot de Telegram de SmartH2O...\n")
    
    # Enviar mensaje de prueba
    exito = send_telegram_alert(
        title="Prueba de integración del bot",
        description="El bot de SmartH2O está funcionando correctamente.",
        severity="BAJA"
    )
    
    if exito:
        print("\n✅ Prueba finalizada con éxito.")
    else:
        print("\n❌ La prueba falló. Revisa los errores en la consola.")

if __name__ == "__main__":
    main()
