import os
import telebot
from telegram import (ReplyKeyBoardMarkup, ReplyKeyBoardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)
import logging

token = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(token)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = loggin.getLogger(__name__)

GENDER, PHOTO, LOCATION = range(3)


def start(bot, update):
    reply_keyboard = [['Boy', 'Girl', 'Non-binary']]

    update.message.reply_text(
        'Oi! Vamos conversar'
        'Digita /cancel pra parar'
        'Are you a boy or a girl?'
        reply_markup=ReplyKeyBoardMarkup(reply_keyboard, onte_time_keyboard=True)
        'What is the name of your rival?'
    )

    return GENDER

def gender(bot, update):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Ah, fodac, ninguem liga pra ele msm'
                              'Manda a fota sua, ou /skip se não quiser.',
                              reply_markup=ReplyKeyboardRemove())

    return PHOTO

def photo(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('user_photo,jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo,jpg')
    update.message.reply_text('Show. Manda sua localização agr')

    return LOCATION

def skip_photo(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text('Tá então, manda a localização.') 

    return LOCATION

def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)  
    update.message.reply_text('Massa')

    return ConversationHandler.END

def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Tá, tchau',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [RegexHandler('^(Boy|Girl|Other)$', gender)],

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('skip', skip_location)],

            BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()