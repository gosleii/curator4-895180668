import telebot

bot = telebot.TeleBot('7042867386:AAH-IZ3oJt337uuYf8lmZaAJq4Y7kaVHNas')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     '*Привет! Здесь собраны полезные материалы для студентов-медиков. Выбирай нужный предмет и прокачивай знания*',
                     parse_mode='Markdown')


@bot.message_handler(commands=['anatomy'])
def anatomy(message):
    bot.send_message(message.chat.id,
                     'Мастхев по анатомии - [канал Эдгара Кафарова](https://youtube.com/@kafarovanatom?si=im26L4ISdDw22r36)\n'
                     'Здесь найдешь объяснения на препаратах - [Андрей Стрелков](https://youtube.com/@user-rq4rn6gg5o?si=K7HiwhGWqxKNls8x)\n'
                     'Короткие видео для повторения материала - [Easy Anatomy](https: // youtube.com / @ easyanatomyapplication?si = zsgtOnSdC59BKTPZ)', parse_mode="Markdown")


@bot.message_handler(commands=['chemistry'])
def chemistry(message):
    bot.send_message(message.chat.id,
                     '[Лекции, после который влюбишься в биохимию](https://youtube.com/@user-th9uf8ui9s?si=j4lzlfrwvgyK9tgV)\n'
                     '[Биохимия врисункахисхемах](https: // youtube.com / @ risuem_biohimiyu?si=H1u7nEhUtw__Xyqa)', parse_mode="Markdown")

@bot.message_handler(commands=['pharma'])
def pharma(message):
    bot.send_message(message.chat.id,
                     'Разобраться в механизмах действия препаратов поможет [SciDrugs](https://youtube.com/@scidrugs?si=UqLB4sSaitSVyMt1)\n'
                     '[Лучшие лекции по фармакологии](https: // youtube.com / @ scidrugs?si=UqLB4sSaitSVyMt1)', parse_mode="Markdown")

@bot.message_handler(commands=['neurology'])
def neurology(message):
    bot.send_message(message.chat.id,
                     'Поможет разложить общую неврологию по полочкам - [EasyNeurology](https://youtube.com/@easyneurology1984?si=wB4vetvMZczbkL8V)', parse_mode="Markdown")


bot.infinity_polling()