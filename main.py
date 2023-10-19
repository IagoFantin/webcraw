import telebot

CHAVE_API = "6655322495:AAEsAsewvO3aQRmHLqv54X8rP65fc3IfCMk"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return mensagem.text == "/opção1"

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = '''
    Olá, eu sou o Bot Promo SNKRS! Escolha uma opção para continuar (Clique no item):
    /opção1 Promoções
    Responda qualquer outra coisa, e não vai funcionar, clique na opção 1
    '''
    bot.reply_to(mensagem, texto)

bot.polling()