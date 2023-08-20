import random
import telebot
import configparser
import constants as consts

config = configparser.ConfigParser()
config.read('settings.ini')
TOKEN = config['bot']['TOKEN']
REPO_LINK = config['bot']['REPO_LINK']

bot = telebot.TeleBot(TOKEN)


def show_main_commands(chat_id, first_time=False):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True)
    for command in consts.MAIN_COMMANDS_LIST:
        markup.add(command)
    bot.send_message(chat_id,
                     text=consts.WHAT_TO_DO_FIRST if first_time else random.choice(consts.WHAT_TO_DO_LIST),
                     reply_markup=markup)


@bot.message_handler(commands=['start', 'reset'])
def handle_start_reset(message):
    bot.send_message(message.chat.id,
                     text=consts.START_GREETING)
    bot.send_sticker(message.chat.id,
                     sticker=consts.HELLO_STICKER_ID)
    show_main_commands(message.chat.id,
                       first_time=True)


@bot.message_handler(func=lambda msg: msg.text == consts.ASK_FOR_FINISH)
def handle_finish(message):
    bot.send_message(message.chat.id,
                     text=consts.FINAL_GREETING,
                     reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(func=lambda msg: msg.text == consts.ASK_FOR_REPO_LINK)
def handle_repo_link(message):
    bot.send_message(message.chat.id,
                     text=REPO_LINK)
    show_main_commands(message.chat.id)


@bot.message_handler(func=lambda msg: msg.text == consts.ASK_TO_SHOW_PICS)
def handle_show_photo(message):
    bot.send_message(message.chat.id,
                     text=consts.ASK_WHICH_PIC,
                     reply_markup=telebot.util.quick_markup(
                         {'1': {'callback_data': '1st_pic'},
                          '2': {'callback_data': '2nd_pic'}}
                     ))


@bot.callback_query_handler(func=lambda callback: callback.message.text == consts.ASK_WHICH_PIC)
def handle_pics_query(callback):
    bot.send_photo(callback.message.chat.id,
                   photo=consts.SELFIE_PHOTO if callback.data == '1st_pic' else consts.CHILD_PHOTO,
                   protect_content=True)
    show_main_commands(callback.message.chat.id)


@bot.message_handler(func=lambda msg: msg.text == consts.ASK_TO_TELL_SMT)
def handle_tell_smt(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True)
    for line in consts.STORY_LIST:
        markup.row(line)
    for line in consts.TELL_ME_DESC_LIST:
        bot.send_message(message.chat.id,
                         text=line,
                         reply_markup=markup)
    bot.register_next_step_handler(message, handle_story_options)


def handle_story_options(message):
    if message.text == consts.ASK_FOR_LOVE_STORY:
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, consts.LOVE_STORY)
    elif message.text == consts.ABOUT_GPT:
        bot.send_chat_action(message.chat.id, 'record_voice')
        bot.send_voice(message.chat.id, consts.GPT_VOICE)
    elif message.text == consts.ABOUT_SQL_NOSQL:
        bot.send_chat_action(message.chat.id, 'record_voice')
        bot.send_voice(message.chat.id, consts.SQL_NOSQL_VOICE)
    elif message.text == consts.ABOUT_HOBBY:
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, consts.HOBBY_POST)
    elif message.text == '/reset':
        handle_start_reset(message)
        return
    else:
        handle_unknown_command(message)
        bot.register_next_step_handler(message, handle_story_options)
        return
    show_main_commands(message.chat.id)


@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, consts.WRONG_COMMAND)


if __name__ == '__main__':
    bot.infinity_polling()
