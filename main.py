import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def reply_whatsapp():
    # Recibimos el mensaje del usuario
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    # Lógica de respuesta de Élite
    if 'hola' in incoming_msg:
        msg.body("🔱 Bienvenido a la Élite de Éxito Soñado. \n\nEscribe 'LIBRO' para conocer 'Sin Máscara' o 'AYUDA' para soporte.")
    elif 'libro' in incoming_msg:
        msg.body("📖 'Sin Máscara' no es solo un libro, es tu nueva mentalidad. \n\nConsíguelo aquí: [Tu Enlace de Amazon/Venta]")
    else:
        msg.body("Para avanzar hacia el éxito, por favor elige una opción válida o espera a que un operador te atienda.")

    return str(response)

if __name__ == "__main__":
    # Render usa el puerto que le asigne el sistema
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
