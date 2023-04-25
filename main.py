import telebot
from telebot import types
from requests import get
TOKEN = "5609278859:AAFLmhUHt-ePtaJQ0-TKu_vp7KlOrGT3Ua4"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def start(message):
    marup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Тепловые явления")
    item2 = types.KeyboardButton("Электр явления")
    item3 = types.KeyboardButton("Световые явления")
    item4 = types.KeyboardButton("Весь список")

    marup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Привет! Выбери какие формулы тебе нужны", reply_markup=marup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Электр явления":
            bot.send_message(message.chat.id, '''введите номер id нужной формулы
id-12 Закон Кулона
id-13 Сила тока
id-14 Напряжение
id-15 Сопротивление проводника
id-16 Закон Ома
id-17 Сила тока при последовательном соединение проводников
id-18 Общее сопротивление при последовательном соемтнение проводников
id-19 Общее напряжение при последовательном соединение проводников
id-20 Сила тока при параллельном соединение проводников
id-21 Общее сопротивление при параллельном соединение проводников(первый варинат)
id-22 Общее сопротивление при параллельном соединение проводников(второй варинат)
id-23 Общее напряжение при параллельном соединение проводников
id-24 Работа тока
id-25 Мощность тока
id-26 Закон Джоуля-Ленца''')
        if message.text == "Тепловые явления":
            bot.send_message(message.chat.id, '''введите номер id нужной формулы
id-1 Закон сохранения механической энергии
id-2 Объемное расширение твердых тел
id-3 Линейное расширение твердых тел 
id-4 Удельная теплоемкость вещества
id-5 Теплоемкость тела
id-6 Количество теплоты при теплопередаче
id-7 Количество теплоты при сгорание топлива 
id-8 Количество теплоты при плавлении (кристализации) твердых тел
id-9 Количество теплоты при испарении(конденсации) жидких тел
id-10 Относительная влажность воздуха
id-11 КПД тепловой машины''')
        if message.text == "Световые явления":
            bot.send_message(message.chat.id, '''введите номер id нужной формулы
id-27 Закон отражения света
id-28 Закон преломления света
id-29 Оптическая сила линзы
id-30 Формула линзы
''')
        if message.text == "Весь список":
            bot.send_message(message.chat.id, '''введите номер id нужной формулы
id-1 Закон сохранения механической энергии
id-2 Объемноое расширение твердых тел
id-3 Линейное расширение твердых тел 
id-4 Удельная теплоемкость вещества
id-5 Теплоемкость тела
id-6 Количество теплоты при теплопередаче
id-7 Количество теплоты при сгорание топлива 
id-8 Количество теплоты при плавлении (кристализации) твердых тел
id-9 Количество теплоты при испарении(конденсации) жидких тел
id-10 Относительная влажность воздуха
id-11 КПД тепловой машины
id-12 Закон Кулона
id-13 Сила тока
id-14 Напряжение
id-15 Сопротивление проводника
id-16 Закон Ома
id-17 Сила тока при последовательном соединение проводников
id-18 Общее сопротивление при последовательном соединение проводников
id-19 Общее напряжение при последовательном соединение проводников
id-20 Сила тока при параллельном соединение проводников
id-21 Общее сопротивление при параллельном соединение проводников(первый варинат)
id-22 Общее сопротивление при параллельном соединение проводников(второй варинат)
id-23 Общее напряжение при параллельном соединение проводников
id-24 Работа тока
id-25 Мощность тока
id-26 Закон Джоуля-Ленца
id-27 Закон отражения света
id-28 Закон преломления света
id-29 Оптическая сила линзы
id-30 Формула линзы''')


        if message.text == "1": 
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/QAhUDPgHdI.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "2":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/JmI5sNLgnQ.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "3":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/TbBSGO9Lnr.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "4":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/WGWZ6CALve.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "5":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/IUUHqq32sb.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "6":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/DALgvCU9DK.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "7":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/DALgvCU9DK.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "8":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/Td669W1MCH.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "9":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/Enodrk75Rh.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "10":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/u5AevPjwml.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "11":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/Wm6Jpea1Ls.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "12":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/DT0fwlpsix.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "13":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/TkLmOI7UbX.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "14":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/jaRolRx7qd.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "15":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/JFoJrwqOzZ.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "16":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/1Xzu5x6oet.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "17":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/XqAPHoD4sY.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "18":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/Jd3Wze14EJ.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "19":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/YkJ2JWhc6A.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "20":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/DHDpSy444k.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "21":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/tNY9wvcLuo.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "22":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/8vld0SloIN.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "23":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/jg6uHULS0y.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "24":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/BRLDEFPtaM.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "25":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/UnRSIzONTw.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "26":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/JSsRZH97Ps.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "27":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/C7TwdjCygx.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "28":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/HxM2TKjKKY.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "29":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/cn04TeBJeY.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')
        if message.text == "30":
            bot.send_photo(message.chat.id, get("https://imgbox.io/ib/tRwMLzIwYS.jpeg").content)
            bot.send_message(message.chat.id, 'введите номер id нужной формулы')    
bot.polling(none_stop=True, timeout=300)