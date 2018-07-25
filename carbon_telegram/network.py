from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot

# # Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

# logger = logging.getLogger(__name__)

class Receiver(object):
	def __init__(self, token):
		self.updater = Updater(token)
		self.dispatcher = self.updater.dispatcher
		self.dispatcher.add_handler(MessageHandler(Filters.text, self.receive))

		self.updater.start_polling()

		print "Listening for messages..."
		self.updater.idle()
		print "Shutting down listener."

	def receive(self, bot, update):
		print "Chat: %s, '%s'" % (update.message.chat.id, update.message.text)


class Sender(object):
	def __init__(self, token, chat_id):
		self.bot = Bot(token)
		self.chat_id = chat_id

	def send(self, message):
		self.bot.send_message(self.chat_id, message)
