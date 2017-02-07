def str_or_empty_if_None(s):
    return '' if s is None else str(s)


def log(*log_text):
    time = get_time(True)
    message = time + " - "
    for i in range(len(log_text)):
        if log_text[i] is not '':
            if log_text[i] is not '':
                message += log_text[i]
            if i < len(log_text)-1:
                message += ' '
    try:
        print(message)
    except:
        print(str(message.encode('windows-1251')))

    f = open('files/log.txt', 'a')
    try:
        f.write(message + "\n")
    except:
        f.write(str(message.encode()) + "\n")
    f.close()


def get_time(with_date=False, message=None):
    from datetime import datetime
    if message is None:
        date = datetime.now()
    else:
        date = datetime.fromtimestamp(message.date)
    if with_date:
        return_string = str(date)[:19]
    else:
        return_string = str(date)[11:19]
    return return_string


def user_from_message(message, full=True):
    if full:
        to_return = str(message.from_user.first_name) + " " + str(message.from_user.last_name) + " (" + \
                    str(message.from_user.username) + " - " + str(message.from_user.id) + ")"
    else:
        to_return = str(message.from_user.username) + " ( " + str(message.from_user.id) + " )"
    return to_return


def get_user_info(message=None):
    kol = num = 0
    f = open('files/unique users.txt')
    if message is not None:
        for line in f:
            kol += 1
            if str(message.from_user.id) == line[:-1]:
                num = kol-1
    else:
        for line in f:
            kol += 1
    kol -= 1
    f.close()

    if message is not None and num == 0:
        f = open('files/unique users.txt', 'a')
        f.write(str(message.from_user.id) + "\n")
        f.close()
        kol += 1
        num = kol
    return [num, kol]


def check_user_id(message):
    exist = False
    f = open('files/unique users.txt')
    for line in f:
        if str(message.from_user.id) == line[:-1]:
            exist = True
            break
    f.close()

    if not exist:
        f = open('files/unique users.txt', 'a')
        f.write(str(message.from_user.id) + "\n")
        f.close()


def is_allowed_to_location(id):
    allowed = False
    f = open('files/location/location ids.txt')
    for line in f:
        if str(id) == line[:-1]:
            allowed = True
    f.close()
    return allowed


def write_my_location(latitude, longitude):
    f = open('files/location/location.txt', 'w')
    f.write(str(latitude) + " " + str(longitude))
    f.close()


def get_location():
    f = open('files/location/location.txt')
    s = f.read()
    f.close()
    return [float(s[:s.find(' ')]), float(s[s.find(' ')+1:])]


def is_banned(id):
    banned = False
    reason = ""
    f = open('files/ban/banlist.txt')
    for line in f:
        if str(id) == line[:line.find(' ')]:
            banned = True
            reason = line[line.find(' ')+1:-1]
            break
    f.close()
    if banned:
        return reason
    else:
        return None


def add_to_anlist(id, reason):
    f = open("files/ban/banlist.txt", 'a')
    f.write(str(id) + " " + reason + "\n")
    f.close()


def send_ban_appeal(id):
    f = open("files/ban/ban appeal ids.txt", 'a')
    f.write(str(id) + "\n")
    f.close()


def ban_appeal_sended(id):
    to_return = False
    f = open("files/ban/ban appeal ids.txt")
    for line in f:
        if str(id) == line[:-1]:
            to_return = True
            break
    f.close()
    return to_return


def banmessage(banreason, message=None):
    if message is None:
        to_return = "Вы добавлены в чёрный список!\n" \
                    "Причина: «" + banreason + "»"
    else:
        to_return = "Вы были добавлены в чёрный список.\n" \
                    "Причина: «" + banreason + "»"
        if not ban_appeal_sended(message.from_user.id):
            to_return += "\nВы можете подать на апелляцию с помощью команды «/banappeal»."
    return to_return


def get_bot_statistics():
    from datetime import datetime
    # Бот создан 24.01.2017 в 13:59:00
    create_date = datetime(2017, 1, 24, 14, 0, 0)

    d = str(create_date)[:-3]
    year = d[:d.find('-')]
    d = d.replace(year+'-', '')
    month = d[:d.find('-')]
    d = d.replace(month+'-', '')
    d = d[:d.find(' ')] + '.' + month + '.' + year + " в" + d[d.find(' '):]
    msg = "Бот создан " + d + "."

    d = datetime.now() - create_date
    d = str(d)
    d = d[:d.find('.')-3]
    days = int(d[:d.find(' ')])
    if 11 <= divmod(days, 100)[1] <= 14:
        ins = "дней"
    elif divmod(days, 10)[1] == 1:
        ins = "день"
    elif divmod(days, 10)[1] >= 5 or divmod(days, 10)[1] == 0:
        ins = "дней"
    else:
        ins = "дня"
    d = d[:d.find(' ')+1] + ins + d[d.find(','):]
    msg += "\nC момента создания: " + d + "."

    users = get_user_info()
    msg += "\nУникальных пользователей: " + str(users[1]) + "."

    return msg


def asked_location_access_before(id):
    to_return = False
    f = open("files/location/request location access ids.txt")
    for line in f:
        if str(id) == line[:-1]:
            to_return = True
            break
    f.close()
    return to_return


def ask_location_access(id):
    f = open("files/location/request location access ids.txt", 'a')
    f.write(str(id) + "\n")
    f.close()

