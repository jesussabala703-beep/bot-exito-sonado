import os
import telebot
from telebot import types
from flask import Flask, request

TOKEN = "8678891271:AAFmqAcuScUWNQslGSYdTMu5twlumr3QJeQ"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# URL de tu WhatsApp con mensaje preparado
WA_LINK = "https://wa.me/16813392738?text="

@bot.message_handler(commands=['start', 'libro'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Botones de Pago / Categorías
    btn_zinli = types.InlineKeyboardButton("💳 Pagar vía Zinli", url=f"{WA_LINK}Hola%20Éxito%20Soñado,%20quiero%20pagar%20mi%20libro%20por%20Zinli")
    btn_kontigo = types.InlineKeyboardButton("📱 Pagar vía Kontigo", url=f"{WA_LINK}Hola%20Éxito%20Soñado,%20quiero%20pagar%20mi%20libro%20por%20Kontigo")
    btn_bcv = types.InlineKeyboardButton("🏦 Pago Móvil / BCV", url=f"{WA_LINK}Hola%20Éxito%20Soñado,%20quiero%20pagar%20mi%20libro%20en%20Bolívares%20(BCV)")
    
    markup.add(btn_zinli, btn_kontigo, btn_bcv)
    
    texto = (
        "🔱 **Éxito Soñado: Sistema de Élite**\n\n"
        "Has seleccionado el manual 'Sin Máscara'. El conocimiento está a un paso.\n\n"
        "**Selecciona tu método de pago preferido:**"
    )
    bot.send_message(message.chat.id, texto, reply_markup=markup, parse_mode='Markdown')

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    return "Servidor de Éxito Soñado Activo", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
