import telebot
import constants as const
import functions as func


bot = telebot.TeleBot(const.botToken)
me = bot.get_me()
func.log("Бот", func.str_or_empty_if_None(me.first_name), func.str_or_empty_if_None(me.last_name), "запущен.--------------------------------")
mode = dict()
ban_limit = dict()
ban_limit_number = 4
get_to_banlist = True


@bot.message_handler(commands=['start'])
def command_start(message):
    if message.text == "/start" or message.text == "/start@" + me.username:
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            users = func.get_user_info(message)
            bot.send_message(message.chat.id, "Приветствую. Я {} 😊\n"
                                              "Вы мой {}-й новый пользователь из {}.\n\n"
                                              "Вот мой маленький список команд:\n"
                                              "".format(me.first_name, str(users[0]), str(users[1])) +
                             const.help_command + "\n" + const.commands + "\n\nПриятного пользования.")
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(commands=['help'])
def command_help(message):
    if message.text == "/help" or message.text == "/help@" + me.username:
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)
            bot.send_message(message.chat.id, "Вот мой маленький список команд:\n"
                                              "" + const.commands)
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(commands=['getstickers'])
def command_getstickers(message):
    if message.text == "/getstickers" or message.text == "/getstickers@" + me.username:
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)
            bot.send_message(message.chat.id,
                             "Пожалуйста, вот наш фирменный набор стикеров: t.me/addstickers/podsl315.")
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(commands=['bugreport'])
def command_bugreport(message):
    if message.text == "/bugreport" or message.text == "/bugreport@" + me.username:
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)
            additional_message = ''
            if message.text == "/bugreport@" + me.username:
                additional_message = "Пишите мне лично (@" + me.username + "), так как у меня нет доступа к сообщениям в этой группе.\n"
            bot.send_message(message.chat.id, "Что вы хотите сообщить?\n" + additional_message +
                                              "Команда «/cancel» для отмены.")
            if message.text == "/bugreport@" + me.username:
                try:
                    bot.send_message(message.from_user.id, "Что вы хотите сообщить?\n"
                                                           "Команда «/cancel» для отмены.")
                except:
                    pass
            mode[message.from_user.id] = 11
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(commands=['feedback'])
def command_feedback(message):
    if message.text == "/feedback" or message.text == "/feedback@" + me.username:
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)
            bot.send_message(message.chat.id, "Оставить свой отзыв Вы всегда можете по ссылке telegram.me/storebot?start="
                                              "" + me.username + ".\n"
                                              "Просто нажмите «Начать» и следуйте подсказкам бота.\n"
                                              "__________\n"
                                              "*отправив ещё один отзыв, Вы замените тот, что отправили ранее")
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(commands=['cancel'])
def command_cancel(message):
    if message.text == "/cancel" or message.text == "/cancel@" + me.username:
        global mode, ban_limit
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None or mode[message.from_user.id] == 21:
            if mode[message.from_user.id] == 21:
                func.log(func.user_from_message(message), "(в бане) :", message.text)
            else:
                func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)
            if message.from_user.id not in mode:
                mode[message.from_user.id] = 0
            if mode[message.from_user.id] == 0:
                bot.send_message(message.chat.id, "Отменять-то нечего...")
            else:
                mode[message.from_user.id] = 0
                bot.send_message(message.chat.id, "Действие отменено.\n"
                                                  "Команда «/help» для помощи.")
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(commands=['timestats'])
def command_timestats(message):
    if message.text == "/timestats" or message.text == "/timestats@" + me.username:
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)
            bot.send_message(message.chat.id, func.get_bot_statistics())
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(commands=['banappeal'])
def command_banappeal(message):
    if message.text == "/banappeal" or message.text == "/banappeal@" + me.username:
        banreason = func.is_banned(message.from_user.id)
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)
            bot.send_message(message.chat.id, "Подавать апелляцию не на что. Функционал бота для Вас открыт.")
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            if func.ban_appeal_sended(message.from_user.id):
                bot.send_message(message.chat.id, "Вы уже подали на апелляцию ранее.")
            else:
                mode[message.from_user.id] = 21
                bot.send_message(message.chat.id, "Ваш комментарий... Пару слов, если желаете.\n"
                                                  "«/skip» для пропуска\n"
                                                  "«/cancel» для отмены")
    else:
        content_type_text(message)


@bot.message_handler(commands=['getlocationaccess'])
def command_getlocationaccess(message):
    if message.text == "/getlocationaccess" or message.text == "/getlocationaccess@" + me.username:
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)

            if func.is_allowed_to_location(message.from_user.id):
                bot.send_message(message.chat.id, "У Вас и так уже есть доступ к команде /location.")
            else:
                if func.asked_location_access_before(message.from_user.id):
                    bot.send_message(message.chat.id, "Вы уже запросили разрешение ранее.")
                else:
                    mode[message.from_user.id] = 31
                    bot.send_message(message.chat.id, "Ваш комментарий... Пару слов, если желаете.\n"
                                                      "«/skip» для пропуска\n"
                                                      "«/cancel» для отмены")
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(commands=['location'])
def command_location(message):
    if message.text == "/location" or message.text == "/location@" + me.username:
        global mode, ban_limit
        mode[message.from_user.id] = 0
        ban_limit[message.from_user.id] = 0
        banreason = func.is_banned(message.from_user.id)
        if banreason is None:
            func.log(func.user_from_message(message), ":", message.text)
            func.check_user_id(message)
            if func.is_allowed_to_location(message.from_user.id):
                location = func.get_location()
                bot.send_message(message.chat.id, "Вот расположение разработчика.")
                bot.send_location(message.chat.id, location[0], location[1])
            else:
                bot.send_message(message.chat.id, "Доступ запрещён.\n"
                                                  "/getlocationaccess - запросить разрешение на доступ.")
        else:
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            bot.send_message(message.chat.id, func.banmessage(banreason, message))
    else:
        content_type_text(message)


@bot.message_handler(content_types=['location'])
def content_type_location(message):
    global mode, ban_limit
    mode[message.from_user.id] = 0
    ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None:
        func.log(func.user_from_message(message), ": Геолокация.")
        func.check_user_id(message)
        if message.from_user.id == const.ids['Я']:
            func.write_my_location(message.location.latitude, message.location.longitude)
            bot.send_message(message.chat.id, "Данные записаны.")
        else:
            bot.send_message(message.chat.id, "Получил геолокацию, но что делать с ней дальше я не знаю...")
    else:
        func.log(func.user_from_message(message), "(в бане) : Геолокация.")
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


@bot.message_handler(content_types=['audio'])
def content_type_audio(message):
    global mode, ban_limit
    mode[message.from_user.id] = 0
    ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None:
        func.log(func.user_from_message(message), ": Музыка " + str(message.audio.performer) + " - " +
                 str(message.audio.title))
        func.check_user_id(message)
        bot.send_message(message.chat.id, "Хорошая песенка.")
    else:
        func.log(func.user_from_message(message), "(в бане) : Музыка " + str(message.audio.performer) + " - " +
                 str(message.audio.title))
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


@bot.message_handler(content_types=['sticker'])
def content_type_sticker(message):
    global mode, ban_limit
    mode[message.from_user.id] = 0
    ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None:
        func.log(func.user_from_message(message), ": Стикер.")
        func.check_user_id(message)
        bot.send_message(message.chat.id, "Я вижу тут стикер.")
    else:
        func.log(func.user_from_message(message), "(в бане) : Стикер.")
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


@bot.message_handler(content_types=['text'])
def content_type_text(message):
    global mode, ban_limit
    if message.from_user.id not in mode:
        mode[message.from_user.id] = 0
    if message.from_user.id not in ban_limit:
        ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None or mode[message.from_user.id] == 21:
        func.check_user_id(message)
        if mode[message.from_user.id] == 0:
            func.log(func.user_from_message(message), ": Неопознанный набор символов: " + message.text)
            bot.send_message(message.chat.id, "Простите, но я не понимаю Вас...")
            if get_to_banlist:
                ban_limit[message.from_user.id] += 1
            if ban_limit[message.from_user.id] == ban_limit_number:
                func.add_to_anlist(message.from_user.id, "Флуд.")
                bot.send_message(message.chat.id, func.banmessage("Флуд."))
                ban_limit[message.from_user.id] = 0
            elif ban_limit[message.from_user.id] > 1:
                bot.send_message(message.chat.id, "Внимание! Вы подозреваетесь во флуде.\n"
                                                  "Осталось сообщений: " +
                                 str(ban_limit_number-ban_limit[message.from_user.id]) + ".")
        # /bugreport
        elif mode[message.from_user.id] == 11:
            mode[message.from_user.id] = 0
            ban_limit[message.from_user.id] = 0
            func.log(func.user_from_message(message), ":", message.text)
            bot.send_message(const.ids['Я'], func.get_time(True, message) + " - " + func.user_from_message(message) +
                             " : Отзыв.\n" + message.text)
            bot.send_message(message.chat.id, "Отзыв успешно отправлен. От разработчика: «"
                                              "Спасибо за проявленный интерес к моему боту. Я Вам отвечу в ближайшее "
                                              "время, если это нужно.»")
        # /banappeal
        elif mode[message.from_user.id] == 21:
            mode[message.from_user.id] = 0
            ban_limit[message.from_user.id] = 0
            func.log(func.user_from_message(message), "(в бане) :", message.text)
            func.send_ban_appeal(message.from_user.id)
            msg = "Запрос на бан-апелляцию от пользователя\n" \
                  "" + func.user_from_message(message) + "."
            if not (message.text == "/skip" or message.text == "/skip@" + me.username):
                msg += "\nКомментарий: " + message.text + "."
            bot.send_message(const.ids['Я'], msg)
            bot.send_message(message.chat.id, "Запрос на апелляцию будет рассмотрен.")
        # /getlocationaccess
        elif mode[message.from_user.id] == 31:
            mode[message.from_user.id] = 0
            ban_limit[message.from_user.id] = 0
            func.log(func.user_from_message(message), ":", message.text)
            func.ask_location_access(message.from_user.id)
            msg = "Запрос на доступ к локации от пользователя\n" \
                  "" + func.user_from_message(message) + "."
            if not (message.text == "/skip" or message.text == "/skip@" + me.username):
                msg += "\nКомментарий: " + message.text + "."
            bot.send_message(const.ids['Я'], msg)
            bot.send_message(message.chat.id, "Запрос будет рассмотрен разработчиком в ближайшем времени.")

    else:
        func.log(func.user_from_message(message), "(в бане) :", message.text)
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


@bot.message_handler(content_types=['photo'])
def content_type_photo(message):
    global mode, ban_limit
    mode[message.from_user.id] = 0
    ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None:
        func.log(func.user_from_message(message), ": Картинка.")
        func.check_user_id(message)
        bot.send_message(message.chat.id, "Хм... Это картинка!")
    else:
        func.log(func.user_from_message(message), "(в бане) : Картинка.")
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


@bot.message_handler(content_types=['document'])
def content_type_document(message):
    global mode, ban_limit
    mode[message.from_user.id] = 0
    ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None:
        func.log(func.user_from_message(message), ": Документ.")
        func.check_user_id(message)
        bot.send_message(message.chat.id, "Ух, это документ!")
    else:
        func.log(func.user_from_message(message), "(в бане) : Документ.")
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


@bot.message_handler(content_types=['video'])
def content_type_video(message):
    global mode, ban_limit
    mode[message.from_user.id] = 0
    ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None:
        func.log(func.user_from_message(message), ": Видео.")
        func.check_user_id(message)
        bot.send_message(message.chat.id, "Оп, видосик.")
    else:
        func.log(func.user_from_message(message), "(в бане) : Видео.")
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


@bot.message_handler(content_types=['voice'])
def content_type_voice(message):
    global mode, ban_limit
    mode[message.from_user.id] = 0
    ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None:
        func.log(func.user_from_message(message), ": Голос.")
        func.check_user_id(message)
        bot.send_message(message.chat.id, "Это голос. Определённо он.")
    else:
        func.log(func.user_from_message(message), "(в бане) : Голос.")
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


@bot.message_handler(content_types=['contact'])
def content_type_contact(message):
    global mode, ban_limit
    mode[message.from_user.id] = 0
    ban_limit[message.from_user.id] = 0
    banreason = func.is_banned(message.from_user.id)
    if banreason is None:
        func.log(func.user_from_message(message), ": Контакт.")
        func.check_user_id(message)
        bot.send_message(message.chat.id, "Контакт? Я позвоню позже.")

    else:
        func.log(func.user_from_message(message), "(в бане) : Контакт.")
        bot.send_message(message.chat.id, func.banmessage(banreason, message))


bot.polling(none_stop=True)

"""
mode:
0 - обычный режим
11 - /bugreport
21 - /banappeal
31 - /getlocationaccess
"""