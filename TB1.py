import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level = logging.INFO,
					filename='TB1.log'
					)

def start_bot(update: Updater, context:CallbackContext):
	print(update)
	mytext = '''Hello {}
	
	I have only /start command! =)'''.format(update.message.chat.first_name)
	logging.info('User {} press /start'.format(update.message.chat.username))
	update.message.reply_text(mytext)

def chat(update: Updater, context:CallbackContext):
	text = update.message.text
	logging.info(text)

	update.message.reply_text(text)

def main():
	upd = Updater(settings.TOKEN_TELEGRAM_TB1)

	upd.dispatcher.add_handler(CommandHandler("start", start_bot))
	upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	upd.start_polling()
	upd.idle()

if __name__ == "__main__":
	logging.info('Bot started!')
	main()
