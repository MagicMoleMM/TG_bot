# -*- coding: utf-8 -*-
import config
import telebot
import pandas as pd
import datetime
import logging

token = config.token
bot = telebot.TeleBot(token)

logging.basicConfig(filename='bot_log.log', encoding='utf-8',format='%(asctime)s %(message)s', level=logging.INFO)
logging.info('EXIT')

nakshatra = pd.read_csv('res/Nakshatra.csv', delimiter=';')
nakshatra_key = pd.read_csv('res/Nakshatra_key.csv', delimiter=';')
var_key = pd.read_csv('res/var_key.csv', delimiter=';')
tithi = pd.read_csv('res/tithi.csv', delimiter=';')
tithi_key = pd.read_csv('res/moon_key.csv', delimiter=';')
yoga = pd.read_csv('res/yoga.csv', delimiter=';')
yoga_key = pd.read_csv('res/yoga_key.csv', delimiter=';')
carana = pd.read_csv('res/carana.csv', delimiter=';')
carana_key = pd.read_csv('res/carana_key.csv', delimiter=';')
sign = pd.read_csv('res/sign.csv', delimiter=';')
sign_key = pd.read_csv('res/sign_key.csv', delimiter=';')
sun_sign = pd.read_csv('res/sun_sign.csv', delimiter=';')
yoga_comb = pd.read_csv('res/yoga_all.csv', delimiter=';')
yoga_comb_key = pd.read_csv('res/yoga_all_key.csv', delimiter=';')


def today():
    r = datetime.datetime.today().strftime('%d.%m.%Y')
    return r


now = today()
yesterday = (datetime.datetime.now() -
             datetime.timedelta(days=1)).strftime('%d.%m.%Y')
tomorrow = (datetime.datetime.now() +
            datetime.timedelta(days=1)).strftime('%d.%m.%Y')
now_weekday = datetime.datetime.now().weekday()
tomorrow_weekday = (datetime.datetime.now() +
                    datetime.timedelta(days=1)).weekday()

nakshatra_text_today1 = list(
    nakshatra[nakshatra.Nakshatra_date == now].Nakshatra_text)
nakshatra_time_today1 = list(
    nakshatra[nakshatra.Nakshatra_date == now].Nakshatra_time)
nakshatra_text_today = list(
    nakshatra[nakshatra.Nakshatra_date == now].Nakshatra_text)[-1]
nakshatra_time_today = list(
    nakshatra[nakshatra.Nakshatra_date == now].Nakshatra_time)[0]
nakshatra_small_today = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_today].naksh_small)[0]
nakshatra_rus_today = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_today].naksh_rus)[0]
nakshatra_shakti_today = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_today].naksh_shakti)[0]
nakshatra_shakti_text_today = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_today].naksh_shakti_text)[0]

var_today = list(var_key[var_key.var_day_number == now_weekday].var_day)[0]
var_today_planet = list(
    var_key[var_key.var_day_number == now_weekday].var_planet)[0]
var_today_text = list(
    var_key[var_key.var_day_number == now_weekday].var_text)[0]

tithi_today1 = list(tithi[tithi.tithi_date == now].tithi_day)
tithi_time_today1 = list(tithi[tithi.tithi_date == now].tithi_time)
tithi_today = list(tithi[tithi.tithi_date == now].tithi_day)[-1]
tithi_time_today = list(tithi[tithi.tithi_date == now].tithi_time)[0]
tithi_today_name = list(
    tithi_key[tithi_today == tithi_key.moon_day].moon_day_name)[0]
tithi_today_small = list(
    tithi_key[tithi_today == tithi_key.moon_day].moon_text_small)[0]
tithi_today_text = list(
    tithi_key[tithi_today == tithi_key.moon_day].moon_text)[0]

yoga_today_en1 = list(yoga[yoga.yoga_date == now].yoga_name)
yoga_time_today1 = list(yoga[yoga.yoga_date == now].yoga_time)
yoga_today_en = list(yoga[yoga.yoga_date == now].yoga_name)[-1]
yoga_time_today = list(yoga[yoga.yoga_date == now].yoga_time)[0]
yoga_today_rus = list(yoga_key[yoga_today_en == yoga_key.yoga_en].yoga_rus)[0]
yoga_today_index = list(
    yoga_key[yoga_today_en == yoga_key.yoga_en].yoga_index)[0]

carana_today_en1 = list(carana[carana.carana_date == now].carana_name)
carana_time_today1 = list(carana[carana.carana_date == now].carana_time)

nakshatra_text_tomorrow1 = list(
    nakshatra[nakshatra.Nakshatra_date == tomorrow].Nakshatra_text)
nakshatra_time_tomorrow1 = list(
    nakshatra[nakshatra.Nakshatra_date == tomorrow].Nakshatra_time)
nakshatra_text_tomorrow = list(
    nakshatra[nakshatra.Nakshatra_date == tomorrow].Nakshatra_text)[-1]
nakshatra_time_tomorrow = list(
    nakshatra[nakshatra.Nakshatra_date == tomorrow].Nakshatra_time)[0]
nakshatra_small_tomorrow = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_tomorrow].naksh_small)[0]
nakshatra_rus_tomorrow = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_tomorrow].naksh_rus)[0]
nakshatra_shakti_tomorrow = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_tomorrow].naksh_shakti)[0]
nakshatra_shakti_text_tomorrow = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_tomorrow].naksh_shakti_text)[0]

var_tomorrow = list(
    var_key[var_key.var_day_number == tomorrow_weekday].var_day)[0]
var_tomorrow_planet = list(
    var_key[var_key.var_day_number == tomorrow_weekday].var_planet)[0]
var_tomorrow_text = list(
    var_key[var_key.var_day_number == tomorrow_weekday].var_text)[0]

tithi_tomorrow1 = list(tithi[tithi.tithi_date == tomorrow].tithi_day)
tithi_time_tomorrow1 = list(tithi[tithi.tithi_date == tomorrow].tithi_time)
tithi_tomorrow = list(tithi[tithi.tithi_date == tomorrow].tithi_day)[-1]
tithi_time_tomorrow = list(tithi[tithi.tithi_date == tomorrow].tithi_time)[0]
tithi_tomorrow_name = list(
    tithi_key[tithi_tomorrow == tithi_key.moon_day].moon_day_name)[0]
tithi_tomorrow_small = list(
    tithi_key[tithi_tomorrow == tithi_key.moon_day].moon_text_small)[0]
tithi_tomorrow_text = list(
    tithi_key[tithi_tomorrow == tithi_key.moon_day].moon_text)[0]

yoga_tomorrow_en1 = list(yoga[yoga.yoga_date == tomorrow].yoga_name)
yoga_time_tomorrow1 = list(yoga[yoga.yoga_date == tomorrow].yoga_time)
yoga_tomorrow_en = list(yoga[yoga.yoga_date == tomorrow].yoga_name)[-1]
yoga_time_tomorrow = list(yoga[yoga.yoga_date == tomorrow].yoga_time)[0]
yoga_tomorrow_rus = list(
    yoga_key[yoga_tomorrow_en == yoga_key.yoga_en].yoga_rus)[0]
yoga_tomorrow_index = list(
    yoga_key[yoga_tomorrow_en == yoga_key.yoga_en].yoga_index)[0]

carana_tomorrow_en1 = list(
    carana[carana.carana_date == tomorrow].carana_name)
carana_time_tomorrow1 = list(
    carana[carana.carana_date == tomorrow].carana_time)

nakshatra_text_yesterday = list(
    nakshatra[nakshatra.Nakshatra_date == yesterday].Nakshatra_text)[-1]
nakshatra_time_yesterday = list(
    nakshatra[nakshatra.Nakshatra_date == yesterday].Nakshatra_time)[0]
nakshatra_small_yesterday = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_yesterday].naksh_small)[0]
nakshatra_rus_yesterday = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_yesterday].naksh_rus)[0]
nakshatra_shakti_yesterday = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_yesterday].naksh_shakti)[0]
nakshatra_shakti_text_yesterday = list(
    nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_yesterday].naksh_shakti_text)[0]

tithi_yesterday = list(tithi[tithi.tithi_date == yesterday].tithi_day)[-1]
tithi_time_yesterday = list(tithi[tithi.tithi_date == yesterday].tithi_time)[0]
tithi_yesterday_name = list(
    tithi_key[tithi_yesterday == tithi_key.moon_day].moon_day_name)[0]
tithi_yesterday_small = list(
    tithi_key[tithi_yesterday == tithi_key.moon_day].moon_text_small)[0]
tithi_yesterday_text = list(
    tithi_key[tithi_yesterday == tithi_key.moon_day].moon_text)[0]

yoga_yesterday_en = list(yoga[yoga.yoga_date == yesterday].yoga_name)[-1]
yoga_time_yesterday = list(yoga[yoga.yoga_date == yesterday].yoga_time)[0]
yoga_yesterday_rus = list(
    yoga_key[yoga_yesterday_en == yoga_key.yoga_en].yoga_rus)[0]
yoga_yesterday_index = list(
    yoga_key[yoga_yesterday_en == yoga_key.yoga_en].yoga_index)[0]

nakshatra_names_tomorrow = []
for i in range(len(nakshatra_text_tomorrow1)):
    nakshatra_names_tomorrow = nakshatra_names_tomorrow + \
        [list(nakshatra_key[nakshatra_key.naksh_en ==
              nakshatra_text_tomorrow1[i]].naksh_rus)[0]]
if (nakshatra_time_tomorrow != '[весь день]'):
    nakshatra_names_2 = [nakshatra_rus_today] + nakshatra_names_tomorrow
else:
    nakshatra_names_2 = nakshatra_names_tomorrow

nakshatra_names_today = []
for i in range(len(nakshatra_text_today1)):
    nakshatra_names_today = nakshatra_names_today + \
        [list(nakshatra_key[nakshatra_key.naksh_en ==
              nakshatra_text_today1[i]].naksh_rus)[0]]
if (nakshatra_time_today != '[весь день]'):
    nakshatra_names_1 = [nakshatra_rus_yesterday] + nakshatra_names_today
else:
    nakshatra_names_1 = nakshatra_names_today


users = []

HELP = '''
*МУХУРТА*

*Жизнь в ритме Вселенной*

Ведический календарь связывает нас с определенными принципами или законами Мироздания, источником которого является Господь. В определенные дни те или иные Законы проявляются  в  материальном мире более ярко, ощутимо и доступны для планирования ежедневных действий. Знание свойств времени позволяет нам жить в гармонии со звездами, очищать свое сознание и идти к Богу.

*Выбор благоприятного времени:*

    ✔️ Растущая Луна (Шукла-пакша) благоприятна для начала новых дел, убывающая Луна (Кришна-пакша) - для выполнения текущей работы и завершения дел. 
    ✔️ Лунные дни, благоприятные для начинаний: 5-й, 10-й, 15-й, 20-й, 25-й (пурна титхи), а также 3-й 8-й, 13-й, 18-й, 23-й и 28-й (джая титхи).
    ✔️ Неблагоприятные дни для начинаний: 4-й, 9-й, 14-й и 19-й, 24-й, 29-й (рикта). 
    ✔️ 15-й лунный день (полнолуние) считается благоприятным для любой благочестивой деятельности. Заключение брака в этот день не рекомендуется.
    ✔️ 30-й лунный день (новолуние), считается неблагоприятным для материальных дел, его хорошо посвятить духовной практике и поминанию предков.
    ✔️ Четверг и пятница - благоприятны для начала всех дел. 
    ✔️ Вторник, субботу  - дни Марса и Сатурна желательно исключить для всех благоприятных действий. 
    ✔️ Накшатра Пушья приносит успех во всех начинаниях, кроме брака. 
    ✔️ Накшатра Шравана - благоприятна для любых благочестивых действий.
    ✔️ Накшатры Бхарани и Криттика, а также последние четверти Ашлеши, Джйештхи и Ревати лучше избегать для начинаний.

*Благоприятная Амрита Сидха йога (вар+накшатра):*

    ✔️ Хаста + Воскресенье, кроме 5 титхи.
    ✔️ Мригашира + Понедельник, кроме 6 титхи.
    ✔️ Ашвини + Вторник, кроме въезда в новый дом, кроме 7 титхи.
    ✔️ Анурадха + Среда, кроме 8 титхи. 
    ✔️ Пушья+четверг, кроме брака и 9 титхи (4-8 дней в году).
    ✔️ Ревати + Пятница, кроме 10 титхи.
    ✔️ Рохини + Суббота, исключая 11 титхи и путешествия.

Следует не начинать важные дела в «Сурья-санкранти» - это период 6 часов 24 минуты до и после перехода Солнца из одного знака в другой.

Смена накшатры, караны, титхи, йоги во время любого события всегда проблематична. Результат — неопределенность (двойственность) в этих событиях.

🚩 ВНИМАНИЕ: В календаре указано московское время (UTC/GMT +3 часа)

'''

HELP1 = '''
*Классификация накшатр*

*🏡 Дхрува (неподвижные): Рохини, Уттарапхалгуни, Уттарашадха, Уттарабхадрапада*

Рекомендуется совершать деятельность, рассчитанную на долговременный результат: заключать брак, начинать новый бизнес, сажать семена, переезжать в новый дом, давать клятвы, принимать обеты, закладывать фундамент дома, начинать строительство и т.д.

*🍀 Мриду (мягкие): Читра, Мригашира, Анурадха, Ревати*

Заключение брака, знакомство, зачатие детей, на­чало новых проектов, покупки, путешествия, а также выполнение торжественных ритуалов: открытие чего-либо, чествование и т.д.

*🏁 Кшипра (быстрые): Ашвини, Пушья, Хаста*

Торговля, покупки, короткие поездки, занятие спор­том, изготовление и одевание украшений, начало биз­неса, образование и обучение, прием лекарств.

*🚀 Чара, (подвижные): Шравана, Дхаништха, Свати, Шатабхиша, Пурнавасу*

Путешествия, приобретение транспортных средств, начало лечения, начало ремонта, обучение, садоводство.

*💢 Тикшна, (резкие): Мула, Джйештха, Ардра, Ашлеша*

Активные действия, наступление, встреча с противником. Возможны обвинения и ссоры. В это время благоприятно заниматься духовной практикой. Рекомендуется не начинать поездку, не совершать покупки.

*⚡ Урга (ужасные): Пурвапхалгуни, Пурвашадха, Бхарани, Пурвабхадрапада, Магха.*

Следует соблюдать осторожность: появляется опас­ность отравлений, разрушений, несчастных случаев, обманов. Рекомендуется не совершать поездок, не брать деньги под залог или в долг. В эти дни успешны: работа с огнем или оружием, ядами и химическими веществами, подрезание деревьев, соревнования, рискованные действия.

*🔀 Мриду-тикшна (смешанные): Криттика, Вишакха*

Заниматься рутинной деятельностью, повседневными обязанностями, не следует начинать новые важные дела.
'''


@bot.message_handler(commands=['help_1'])
def help(message):
    bot.send_message(message.chat.id, HELP, parse_mode='Markdown')


@bot.message_handler(commands=['help_2'])
def help(message):
    bot.send_message(message.chat.id, HELP1, parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def start_message(message):
    if (bot.get_chat_member('@astro_analysis', message.from_user.id).status) != "left":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(telebot.types.KeyboardButton(text='🙏 Прогноз на сегодня'),
                   telebot.types.KeyboardButton(text='☀️ Прогноз на завтра'))
        markup.row(telebot.types.KeyboardButton(text='🌼 Другая дата'),
                   telebot.types.KeyboardButton(text='🔭 О ведической астрологии'))
        text=f"Привет {message.from_user.first_name}! Я *АстроБот* 😇, расскажу какой сегодня день! Выбери в меню, что тебе интересно узнать прямо сейчас!\nЕсли кнопки меню скрыты, используй значок 🎛 рядом с клавиатурой, чтобы их открыть."
        with open('res/photo_2022-08-25_15-12-28.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text, reply_markup=markup, parse_mode='Markdown')

    else:
        bot.send_message(
            message.chat.id, f'Привет, {message.from_user.first_name}!')
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(
            '🫶 Astro-analysis (ссылка на канал)', url='https://t.me/astro_analysis')
        button2 = telebot.types.InlineKeyboardButton(
            'Я подписан(а)', callback_data="user")
        markup.add(button1, button2)
        bot.send_message(
            message.chat.id, '☘️ Для продолжения работы подпишитесь на канал по ведической астрологии Astro-analysis', reply_markup=markup)
    logging.info(f'User {message.from_user.first_name} {message.from_user.last_name}, id - {message.from_user.id}  start.')

@bot.message_handler(content_types='text')
def message_reply(message):

    if (message.text == "🙏 Прогноз на сегодня") and (bot.get_chat_member('@astro_analysis', message.from_user.id).status) != "left":
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
            text=f'💫 Накшатра {", ".join(nakshatra_names_1)} подробно', callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(
            text=' 🌙 Карана / ✨ Йога подробно', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(
            text='🎁 Комбинационные йоги', callback_data=8))

        answer0 = f'Cегодня - *{now}*\n\n'

        answer1 = f'{var_today}, *{var_today_planet}*.\n{var_today_text}\n\n'

        if (nakshatra_time_today != '[весь день]'):
            answer2 = f'Луна в накшатре *{nakshatra_rus_yesterday}* до *{nakshatra_time_today}.\n{nakshatra_small_yesterday}*\n{nakshatra_shakti_text_yesterday}\n\n'
        else:
            answer2 = ''

        answer3 = ""
        for i in range(len(nakshatra_text_today1)):
            answer3 = answer3 + \
                f'Луна входит в накшатру *{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_today1[i]].naksh_rus)[0]}* в *{nakshatra_time_today1[i]}.\n{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_today1[i]].naksh_small)[0]}*\n{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_today1[i]].naksh_shakti_text)[0]}\n\n'

        if (tithi_time_today != '[весь день]'):
            answer4 = f'*{tithi_yesterday}-й* лунный день *({tithi_yesterday_name})* длится до *{tithi_time_today}.\n{tithi_yesterday_small}.*\n{tithi_yesterday_text}\n\n'
        else:
            answer4 = ''

        answer5 = ""
        for i in range(len(tithi_today1)):
            answer5 = answer5 + \
                f'*{tithi_today1[i]}-й* лунный день *({list(tithi_key[tithi_today1[i] == tithi_key.moon_day].moon_day_name)[0]})* начинается в *{tithi_time_today1[i]}.\n{list(tithi_key[tithi_today1[i] == tithi_key.moon_day].moon_text_small)[0]}.*\n{list(tithi_key[tithi_today1[i] == tithi_key.moon_day].moon_text)[0]}\n\n'

        answer6 = ""
        for i in range(len(carana_today_en1)):
            answer6 = answer6 + \
                f'*{list(carana_key[carana_today_en1[i] == carana_key.carana_rus].carana_index)[0]}* карана *{carana_today_en1[i]}* c *{carana_time_today1[i]}.*\n'

        if (yoga_time_today != '[весь день]'):
            answer7 = f'*{yoga_yesterday_index}* йога *{yoga_yesterday_rus}* до *{yoga_time_today}.*\n'
        else:
            answer7 = ''

        answer8 = ""
        for i in range(len(yoga_today_en1)):
            answer8 = answer8 + \
                f'*{list(yoga_key[yoga_today_en1[i] == yoga_key.yoga_en].yoga_index)[0]}* йога *{list(yoga_key[yoga_today_en1[i] == yoga_key.yoga_en].yoga_rus)[0]}* c *{yoga_time_today1[i]}.*\n'

        answer9 = ''
        if now in list(sign.sign_date):
            sign_name = list(sign[sign.sign_date == now].sign_rus)[0]
            answer9 = f'Луна в знаке *{sign_name}* с *{list(sign[sign.sign_date == now].sign_time)[0]}*\n{list(sign_key[sign_key.sign_rus == sign_name].sign_text)[0]}\n\n'
        else:
            answer9 = ""

        answer10 = "\n"

        answer11 = ''
        if now in list(sun_sign.sun_date):
            sign_name = list(sun_sign[sun_sign.sun_date == now].sun_text_rus)[0]
            answer11 = f'\n☀️ _Солнце в знаке {sign_name} с {list(sun_sign[sun_sign.sun_date == now].sun_time)[0]}_\n\n'
        else:
            answer11 = ""

        answer12 = ''
        if now in list(sun_sign.eclipse_date):
            eclipse_name = list(sun_sign[sun_sign.eclipse_date == now].eclipse_text)[0]
            answer12 = f'*{eclipse_name} в {list(sun_sign[sun_sign.eclipse_date == now].eclipse_time)[0]}*\n\n'
        else:
            answer12 = ""

        answer = answer0 + answer12 + answer4 + answer5 + answer1 + answer9 + \
            answer2 + answer3 + answer7 + answer8 + answer10 + answer6 +answer11

        bot.send_message(message.chat.id, text=answer,
                         reply_markup=markup, parse_mode='Markdown')

    elif (message.text == '☀️ Прогноз на завтра') and (bot.get_chat_member('@astro_analysis', message.from_user.id).status) != "left":
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
            text=f'💫 Накшатра {", ".join(nakshatra_names_2)} подробно', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(
            text=' 🌙 Карана / ✨ Йога подробно', callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(
            text='🎁 Комбинационные йоги', callback_data=9))

        answer0 = f'Завтра - *{tomorrow}*\n\n'

        answer1 = f'{var_tomorrow}, *{var_tomorrow_planet}*.\n{var_tomorrow_text}\n\n'

        if (nakshatra_time_tomorrow != '[весь день]'):
            answer2 = f'Луна в накшатре *{nakshatra_rus_today}* до *{nakshatra_time_tomorrow}.\n{nakshatra_small_today}*\n{nakshatra_shakti_text_today}\n\n'
        else:
            answer2 = ''

        answer3 = ""
        for i in range(len(nakshatra_text_tomorrow1)):
            answer3 = answer3 + \
                f'Луна входит в накшатру *{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_tomorrow1[i]].naksh_rus)[0]}* в *{nakshatra_time_tomorrow1[i]}.\n{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_tomorrow1[i]].naksh_small)[0]}*\n{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_tomorrow1[i]].naksh_shakti_text)[0]}\n\n'

        if (tithi_time_tomorrow != '[весь день]'):
            answer4 = f'*{tithi_today}-й* лунный день *({tithi_today_name})* длится до *{tithi_time_tomorrow}.\n{tithi_today_small}.*\n{tithi_today_text}\n\n'
        else:
            answer4 = ''

        answer5 = ""
        for i in range(len(tithi_tomorrow1)):
            answer5 = answer5 + \
                f'*{tithi_tomorrow1[i]}-й* лунный день *({list(tithi_key[tithi_tomorrow1[i] == tithi_key.moon_day].moon_day_name)[0]})* начинается в *{tithi_time_tomorrow1[i]}.\n{list(tithi_key[tithi_tomorrow1[i] == tithi_key.moon_day].moon_text_small)[0]}.*\n{list(tithi_key[tithi_tomorrow1[i] == tithi_key.moon_day].moon_text)[0]}\n\n'

        answer6 = ""
        for i in range(len(carana_tomorrow_en1)):
            answer6 = answer6 + \
                f'*{list(carana_key[carana_tomorrow_en1[i] == carana_key.carana_rus].carana_index)[0]}* карана *{carana_tomorrow_en1[i]}* c *{carana_time_tomorrow1[i]}.*\n'

        if (yoga_time_tomorrow != '[весь день]'):
            answer7 = f'*{yoga_today_index}* йога *{yoga_today_rus}* до *{yoga_time_tomorrow}.*\n'
        else:
            answer7 = ''

        answer8 = ""
        for i in range(len(yoga_tomorrow_en1)):
            answer8 = answer8 + \
                f'*{list(yoga_key[yoga_tomorrow_en1[i] == yoga_key.yoga_en].yoga_index)[0]}* йога *{list(yoga_key[yoga_tomorrow_en1[i] == yoga_key.yoga_en].yoga_rus)[0]}* c *{yoga_time_tomorrow1[i]}.*\n'

        answer9 = ''
        if tomorrow in list(sign.sign_date):
            sign_name = list(sign[sign.sign_date == tomorrow].sign_rus)[0]
            answer9 = f'Луна в знаке *{sign_name}* с *{list(sign[sign.sign_date == tomorrow].sign_time)[0]}*\n{list(sign_key[sign_key.sign_rus == sign_name].sign_text)[0]}\n\n'
        else:
            answer9 = ""

        answer10 = "\n"

        answer11 = ''
        if tomorrow in list(sun_sign.sun_date):
            sign_name = list(sun_sign[sun_sign.sun_date == tomorrow].sun_text_rus)[0]
            answer11 = f'\n☀️ _Солнце в знаке {sign_name} с {list(sun_sign[sun_sign.sun_date == tomorrow].sun_time)[0]}_\n\n'
        else:
            answer11 = ""

        answer12 = ''
        if tomorrow in list(sun_sign.eclipse_date):
            eclipse_name = list(sun_sign[sun_sign.eclipse_date == tomorrow].eclipse_text)[0]
            answer12 = f'*{eclipse_name} в {list(sun_sign[sun_sign.eclipse_date == tomorrow].eclipse_time)[0]}*\n\n'
        else:
            answer12 = ""

        answer = answer0 + answer12 + answer4 + answer5 + answer1 + answer9 + \
            answer2 + answer3 + answer7 + answer8 + answer10 + answer6 + answer11

        bot.send_message(message.chat.id, text=answer,
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == "🔭 О ведической астрологии":
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🕉️ Джйотиш (ссылка на сайт)', url='https://www.astro-analysis.net'))
        markup.row(telebot.types.InlineKeyboardButton(
            text='⭐ Astro-analysis (ссылка на сайт - визитку)', url='https://astro-analysis.tb.ru'))
        markup.row(telebot.types.InlineKeyboardButton(
            text='🙏 Поддержи бота AstroGoodDay!', url='https://pay.cloudtips.ru/p/520a11b1'))
        text='🔭 Узнай больше о ведической астрологии, Мухурте (выборе благоприятного времени) и персональном календаре по ссылке:'
        with open('res/photo_2022-08-25_17-30-00.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text, reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🌼 Другая дата':
        bot.send_message(
            message.chat.id, text=f'🗓️ Введите дату в формате *ДД.ММ.ГГГГ* (например 07.09.2022) в диапазоне с {now} по {list(yoga.yoga_date)[-1]}', parse_mode='Markdown')

    elif (message.text in list(tithi.tithi_date)) and (bot.get_chat_member('@astro_analysis', message.from_user.id).status) != "left":
        global date
        date = message.text
        date_weekday = datetime.datetime.strptime(date, '%d.%m.%Y').weekday()
        date1 = (datetime.datetime.strptime(date, '%d.%m.%Y') -
                 datetime.timedelta(days=1)).strftime('%d.%m.%Y')

        global nakshatra_text_date_1
        nakshatra_text_date_1 = list(
            nakshatra[nakshatra.Nakshatra_date == date].Nakshatra_text)
        nakshatra_time_date_1 = list(
            nakshatra[nakshatra.Nakshatra_date == date].Nakshatra_time)
        nakshatra_time_date = list(
            nakshatra[nakshatra.Nakshatra_date == date].Nakshatra_time)[-0]

        var_date = list(
            var_key[var_key.var_day_number == date_weekday].var_day)[0]
        var_date_planet = list(
            var_key[var_key.var_day_number == date_weekday].var_planet)[0]
        var_date_text = list(
            var_key[var_key.var_day_number == date_weekday].var_text)[0]

        tithi_date_1 = list(tithi[tithi.tithi_date == date].tithi_day)
        tithi_time_date_1 = list(tithi[tithi.tithi_date == date].tithi_time)
        tithi_time_date = list(tithi[tithi.tithi_date == date].tithi_time)[0]

        global yoga_date_en_1
        yoga_date_en_1 = list(yoga[yoga.yoga_date == date].yoga_name)
        yoga_time_date_1 = list(yoga[yoga.yoga_date == date].yoga_time)
        yoga_time_date = list(yoga[yoga.yoga_date == date].yoga_time)[0]

        global carana_date_en_1
        carana_date_en_1 = list(carana[carana.carana_date == date].carana_name)
        carana_time_date_1 = list(
            carana[carana.carana_date == date].carana_time)

        global nakshatra_text_date1
        nakshatra_text_date1 = list(
            nakshatra[nakshatra.Nakshatra_date == date1].Nakshatra_text)[-1]
        nakshatra_small_date1 = list(
            nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_date1].naksh_small)[0]
        nakshatra_rus_date1 = list(
            nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_date1].naksh_rus)[0]
        nakshatra_shakti_text_date1 = list(
            nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_date1].naksh_shakti_text)[0]

        tithi_date1 = list(tithi[tithi.tithi_date == date1].tithi_day)[-1]
        tithi_date1_name = list(
            tithi_key[tithi_date1 == tithi_key.moon_day].moon_day_name)[0]
        tithi_date1_small = list(
            tithi_key[tithi_date1 == tithi_key.moon_day].moon_text_small)[0]
        tithi_date1_text = list(
            tithi_key[tithi_date1 == tithi_key.moon_day].moon_text)[0]

        global yoga_date_en1
        yoga_date_en1 = list(yoga[yoga.yoga_date == date1].yoga_name)[-1]
        yoga_date1_rus = list(
            yoga_key[yoga_date_en1 == yoga_key.yoga_en].yoga_rus)[0]
        yoga_date1_index = list(
            yoga_key[yoga_date_en1 == yoga_key.yoga_en].yoga_index)[0]

        nakshatra_names_date = []
        for i in range(len(nakshatra_text_date_1)):
            nakshatra_names_date = nakshatra_names_date + \
                [list(nakshatra_key[nakshatra_key.naksh_en ==
                                    nakshatra_text_date_1[i]].naksh_rus)[0]]
        if (nakshatra_time_today != '[весь день]'):
            nakshatra_names_3 = [nakshatra_rus_date1] + nakshatra_names_date
        else:
            nakshatra_names_3 = nakshatra_names_date

        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
            text=f'💫 Накшатра {", ".join(nakshatra_names_3)} подробно', callback_data=5))
        markup.add(telebot.types.InlineKeyboardButton(
            text=' 🌙 Карана / ✨ Йога подробно', callback_data=6))
        markup.add(telebot.types.InlineKeyboardButton(
            text='🎁 Комбинационные йоги', callback_data=10))

        answer0 = f'Прогноз на *{date}*\n\n'

        answer1 = f'{var_date}, *{var_date_planet}*.\n{var_date_text}\n\n'

        if (nakshatra_time_date != '[весь день]'):
            answer2 = f'Луна в накшатре *{nakshatra_rus_date1}* до *{nakshatra_time_date}.\n{nakshatra_small_date1}*\n{nakshatra_shakti_text_date1}\n\n'
        else:
            answer2 = ''

        answer3 = ""
        for i in range(len(nakshatra_text_date_1)):
            answer3 = answer3 + \
                f'Луна входит в накшатру *{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_date_1[i]].naksh_rus)[0]}* в *{nakshatra_time_date_1[i]}.\n{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_date_1[i]].naksh_small)[0]}*\n{list(nakshatra_key[nakshatra_key.naksh_en == nakshatra_text_date_1[i]].naksh_shakti_text)[0]}\n\n'

        if (tithi_time_date != '[весь день]'):
            answer4 = f'*{tithi_date1}-й* лунный день *({tithi_date1_name})* длится до *{tithi_time_date}.\n{tithi_date1_small}.*\n{tithi_date1_text}\n\n'
        else:
            answer4 = ''

        answer5 = ""
        for i in range(len(tithi_date_1)):
            answer5 = answer5 + \
                f'*{tithi_date_1[i]}-й* лунный день *({list(tithi_key[tithi_date_1[i] == tithi_key.moon_day].moon_day_name)[0]})* начинается в *{tithi_time_date_1[i]}.\n{list(tithi_key[tithi_date_1[i] == tithi_key.moon_day].moon_text_small)[0]}.*\n{list(tithi_key[tithi_date_1[i] == tithi_key.moon_day].moon_text)[0]}\n\n'

        answer6 = ""
        for i in range(len(carana_date_en_1)):
            answer6 = answer6 + \
                f'*{list(carana_key[carana_date_en_1[i] == carana_key.carana_rus].carana_index)[0]}* карана *{carana_date_en_1[i]}* c *{carana_time_date_1[i]}.*\n'

        if (yoga_time_date != '[весь день]'):
            answer7 = f'*{yoga_date1_index}* йога *{yoga_date1_rus}* до *{yoga_time_date}.*\n'
        else:
            answer7 = ''

        answer8 = ""
        for i in range(len(yoga_date_en_1)):
            answer8 = answer8 + \
                f'*{list(yoga_key[yoga_date_en_1[i] == yoga_key.yoga_en].yoga_index)[0]}* йога *{list(yoga_key[yoga_date_en_1[i] == yoga_key.yoga_en].yoga_rus)[0]}* c *{yoga_time_date_1[i]}.*\n'

        answer9 = ''
        if date in list(sign.sign_date):
            sign_name = list(sign[sign.sign_date == date].sign_rus)[0]
            answer9 = f'Луна в знаке *{sign_name}* с *{list(sign[sign.sign_date == date].sign_time)[0]}*\n{list(sign_key[sign_key.sign_rus == sign_name].sign_text)[0]}\n\n'
        else:
            answer9 = ""

        answer10 = "\n"

        answer11 = ''
        if date in list(sun_sign.sun_date):
            sign_name = list(sun_sign[sun_sign.sun_date == date].sun_text_rus)[0]
            answer11 = f'\n☀️ _Солнце в знаке {sign_name} с {list(sun_sign[sun_sign.sun_date == date].sun_time)[0]}_\n\n'
        else:
            answer11 = ""

        answer12 = ''
        if date in list(sun_sign.eclipse_date):
            eclipse_name = list(sun_sign[sun_sign.eclipse_date == date].eclipse_text)[0]
            answer12 = f'*{eclipse_name} в {list(sun_sign[sun_sign.eclipse_date == date].eclipse_time)[0]}*\n\n'
        else:
            answer12 = ""

        answer = answer0 + answer12 + answer4 + answer5 + answer1 + answer9 + \
            answer2 + answer3 + answer7 + answer8 + answer10 + answer6 + answer11

        bot.send_message(message.chat.id, text=answer,
                         reply_markup=markup, parse_mode='Markdown')

    elif (message.text not in list(tithi.tithi_date)) or (bot.get_chat_member('@astro_analysis', message.from_user.id).status) == "left":
        date = message.text
        bot.send_message(
            message.chat.id, text=f'Даты {date} нет в списке, 🗓️ введите дату в формате *ДД.ММ.ГГГГ* (например 07.09.2022) в диапазоне с {now} по {list(yoga.yoga_date)[-1]}\nИли Вы не подписаны на канал Astro-analysis', parse_mode='Markdown')

    # global users
    # users = users + [message.from_user.id,
    #                  message.from_user.first_name, message.from_user.last_name]
    # print(users)
    logging.info(f'User {message.from_user.first_name} {message.from_user.last_name}, id - {message.from_user.id} enter in bot.')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Отличный выбор')

    answer = ''

    if call.data == "user":

        try:
            bot.get_chat_member('@astro_analysis', call.from_user.id).status
        except:
            bot.send_message(
                call.message.chat.id, f"{call.from_user.first_name}, что-то пошло не так, попробуй еще раз.")
        else:
            if (bot.get_chat_member('@astro_analysis', call.from_user.id).status) != "left":
                markup = telebot.types.ReplyKeyboardMarkup(
                    resize_keyboard=True)
                markup.row(telebot.types.KeyboardButton(text='🙏 Прогноз на сегодня'),
                           telebot.types.KeyboardButton(text='☀️ Прогноз на завтра'))
                markup.row(telebot.types.KeyboardButton(text='🌼 Другая дата'),
                           telebot.types.KeyboardButton(text='🔭 О ведической астрологии'))
                text=f"Привет {call.from_user.first_name}! Я *АстроБот* 😇, расскажу какой сегодня день! Выбери, что тебе интересно узнать прямо сейчас!"
                with open('res/photo_2022-08-25_15-12-28.jpg', 'rb') as photo:
                    bot.send_photo(call.message.chat.id, photo, caption=text, reply_markup=markup, parse_mode='Markdown')
            else:
                markup = telebot.types.InlineKeyboardMarkup()
                button1 = telebot.types.InlineKeyboardButton(
                    '🫶 Astro-analysis (ссылка на канал)', url='https://t.me/astro_analysis')
                markup.add(button1)
                bot.send_message(
                    call.message.chat.id, f'Увы, {call.from_user.first_name}, Вы не подписаны на канал 😿.\nДля продолжения работы подпишитесь на канал по ведической астрологии Astro-analysis', reply_markup=markup)

    elif call.data == '1':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        if (nakshatra_time_today != '[весь день]'):
            names = [nakshatra_text_yesterday] + nakshatra_text_today1
        else:
            names = nakshatra_text_today1

        for name in names:
            answer = answer + f"💫 *Описание накшатры {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_rus)[0]}:*\n\n*Управитель: *{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_ruler)[0]}*\nБожество:* {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_got)[0]}*\nСимвол:* {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_simbol)[0]}\n\n*Благоприятная деятельность:* \n{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_action_good)[0]}\n\n*Неблагоприятная деятельность:* \n{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_action_bad)[0]}\n\n"
        bot.send_message(call.message.chat.id, text=answer,
                         parse_mode='Markdown', reply_markup=markup)

    elif call.data == '2':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        answer1 = ""
        answer2 = ""

        if (yoga_time_today != '[весь день]'):
            names = [yoga_yesterday_en] + yoga_today_en1
        else:
            names = yoga_today_en1

        for carana in carana_today_en1:
            answer1 = answer1 + \
                f"🌙 *Карана - {carana}*\n\nБожество - *{list(carana_key[carana == carana_key.carana_rus].carana_got)[0]}*\nОписание: {list(carana_key[carana == carana_key.carana_rus].carana_text)[0]}\n\n"
        for name in names:
            answer2 = answer2 + \
                f"✨ *Йога - {list(yoga_key[name == yoga_key.yoga_en].yoga_rus)[0]}*\n\nБожество - *{list(yoga_key[name == yoga_key.yoga_en].yoga_got)[0]}*, Планета  - *{list(yoga_key[name == yoga_key.yoga_en].yoga_planet)[0]}*\nОписание: {list(yoga_key[name == yoga_key.yoga_en].yoga_text)[0]}\n\n"
        answer = answer2 + answer1
        bot.send_message(call.message.chat.id, text=answer,
                         parse_mode='Markdown', reply_markup=markup)

    elif call.data == '3':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        if (nakshatra_time_tomorrow != '[весь день]'):
            names = [nakshatra_text_today] + nakshatra_text_tomorrow1
        else:
            names = nakshatra_text_tomorrow1

        for name in names:
            answer = answer + f"💫 *Описание накшатры {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_rus)[0]}:*\n\n*Управитель: *{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_ruler)[0]}*\nБожество:* {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_got)[0]}*\nСимвол:* {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_simbol)[0]}\n\n*Благоприятная деятельность:* \n{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_action_good)[0]}\n\n*Неблагоприятная деятельность:* \n{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_action_bad)[0]}\n\n"
        bot.send_message(call.message.chat.id, text=answer,
                         parse_mode='Markdown', reply_markup=markup)

    elif call.data == '4':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        answer1 = ""
        answer2 = ""

        if (yoga_time_tomorrow != '[весь день]'):
            names = [yoga_today_en] + yoga_tomorrow_en1
        else:
            names = yoga_tomorrow_en1

        for carana in carana_tomorrow_en1:
            answer1 = answer1 + \
                f"🌙 *Карана - {carana}*\n\nБожество - *{list(carana_key[carana == carana_key.carana_rus].carana_got)[0]}*\nОписание: {list(carana_key[carana == carana_key.carana_rus].carana_text)[0]}\n\n"
        for name in names:
            answer2 = answer2 + \
                f"✨ *Йога - {list(yoga_key[name == yoga_key.yoga_en].yoga_rus)[0]}*\n\nБожество - *{list(yoga_key[name == yoga_key.yoga_en].yoga_got)[0]}*, Планета  - *{list(yoga_key[name == yoga_key.yoga_en].yoga_planet)[0]}*\nОписание: {list(yoga_key[name == yoga_key.yoga_en].yoga_text)[0]}\n\n"
        answer = answer2 + answer1
        bot.send_message(call.message.chat.id, text=answer,
                         parse_mode='Markdown', reply_markup=markup)

    elif call.data == '5':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        if (nakshatra_time_tomorrow != '[весь день]'):
            names = [nakshatra_text_date1] + nakshatra_text_date_1
        else:
            names = nakshatra_text_date_1

        for name in names:
            answer = answer + f"💫 *Описание накшатры {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_rus)[0]}:*\n\n*Управитель: *{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_ruler)[0]}*\nБожество:* {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_got)[0]}*\nСимвол:* {list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_simbol)[0]}\n\n*Благоприятная деятельность:* \n{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_action_good)[0]}\n\n*Неблагоприятная деятельность:* \n{list(nakshatra_key[nakshatra_key.naksh_en == name].naksh_action_bad)[0]}\n\n"
        bot.send_message(call.message.chat.id, text=answer,
                         parse_mode='Markdown', reply_markup=markup)

    elif call.data == '6':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        answer1 = ""
        answer2 = ""

        if (yoga_time_tomorrow != '[весь день]'):
            names = [yoga_date_en1] + yoga_date_en_1
        else:
            names = yoga_date_en_1

        for carana in carana_date_en_1:
            answer1 = answer1 + \
                f"🌙 *Карана - {carana}*\n\nБожество - *{list(carana_key[carana == carana_key.carana_rus].carana_got)[0]}*\nОписание: {list(carana_key[carana == carana_key.carana_rus].carana_text)[0]}\n\n"
        for name in names:
            answer2 = answer2 + \
                f"✨ *Йога - {list(yoga_key[name == yoga_key.yoga_en].yoga_rus)[0]}*\n\nБожество - *{list(yoga_key[name == yoga_key.yoga_en].yoga_got)[0]}*, Планета  - *{list(yoga_key[name == yoga_key.yoga_en].yoga_planet)[0]}*\nОписание: {list(yoga_key[name == yoga_key.yoga_en].yoga_text)[0]}\n\n"
        answer = answer2 + answer1
        bot.send_message(call.message.chat.id, text=answer,
                         parse_mode='Markdown', reply_markup=markup)

    elif call.data == '7':
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '8':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        yoga_comb_today1 = list(yoga_comb[yoga_comb.yoga_date == now].yoga_name)
        yoga_comb_time_today_on1 = list(yoga_comb[yoga_comb.yoga_date == now].yoga_time_on)
        yoga_comb_time_today_off1 = list(yoga_comb[yoga_comb.yoga_date == now].yoga_time_off)
        
        answer = ""
        if len(yoga_comb_today1)>0:
            for i in range(len(yoga_comb_today1)):
                answer = answer + \
                    f"{list(yoga_comb_key[yoga_comb_key.yoga_name == yoga_comb_today1[i]].yoga_text_small)[0]} *{yoga_comb_today1[i]}* ({list(yoga_comb[yoga_comb.yoga_date == now].yoga_text)[i]}) начинается *{yoga_comb_time_today_on1[i]}* и длится до *{yoga_comb_time_today_off1[i]}*.\nПродолжительность - *{list(yoga_comb[yoga_comb.yoga_date == now].yoga_len)[i]}* час.\n\n{list(yoga_comb_key[yoga_comb_key.yoga_name == yoga_comb_today1[i]].yoga_text)[0]}\n\n"

            bot.send_message(call.message.chat.id, text=answer,
                            parse_mode='Markdown', reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, text="📍 Комбинационных йог на текущий день не обнаружено",
                            parse_mode='Markdown', reply_markup=markup)

    elif call.data == '9':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        yoga_comb_tomorrow1 = list(yoga_comb[yoga_comb.yoga_date == tomorrow].yoga_name)
        yoga_comb_time_tomorrow_on1 = list(yoga_comb[yoga_comb.yoga_date == tomorrow].yoga_time_on)
        yoga_comb_time_tomorrow_off1 = list(yoga_comb[yoga_comb.yoga_date == tomorrow].yoga_time_off)
        
        answer = ""
        if len(yoga_comb_tomorrow1)>0:
            for i in range(len(yoga_comb_tomorrow1)):
                answer = answer + \
                    f"{list(yoga_comb_key[yoga_comb_key.yoga_name == yoga_comb_tomorrow1[i]].yoga_text_small)[0]} *{yoga_comb_tomorrow1[i]}* ({list(yoga_comb[yoga_comb.yoga_date == tomorrow].yoga_text)[i]}) начинается *{yoga_comb_time_tomorrow_on1[i]}* и длится до *{yoga_comb_time_tomorrow_off1[i]}*.\nПродолжительность - *{list(yoga_comb[yoga_comb.yoga_date == tomorrow].yoga_len)[i]}* час.\n\n{list(yoga_comb_key[yoga_comb_key.yoga_name == yoga_comb_tomorrow1[i]].yoga_text)[0]}\n\n"

            bot.send_message(call.message.chat.id, text=answer,
                            parse_mode='Markdown', reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, text="📍 Комбинационных йог на текущий день не обнаружено",
                            parse_mode='Markdown', reply_markup=markup)

    elif call.data == '10':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton(
            text='🔙 В начало', callback_data=7))

        yoga_comb_date1 = list(yoga_comb[yoga_comb.yoga_date == date].yoga_name)
        yoga_comb_time_date_on1 = list(yoga_comb[yoga_comb.yoga_date == date].yoga_time_on)
        yoga_comb_time_date_off1 = list(yoga_comb[yoga_comb.yoga_date == date].yoga_time_off)
        
        answer = ""
        if len(yoga_comb_date1)>0:
            for i in range(len(yoga_comb_date1)):
                answer = answer + \
                    f"{list(yoga_comb_key[yoga_comb_key.yoga_name == yoga_comb_date1[i]].yoga_text_small)[0]} *{yoga_comb_date1[i]}* ({list(yoga_comb[yoga_comb.yoga_date == date].yoga_text)[i]}) начинается *{yoga_comb_time_date_on1[i]}* и длится до *{yoga_comb_time_date_off1[i]}*.\nПродолжительность - *{list(yoga_comb[yoga_comb.yoga_date == date].yoga_len)[i]}* час.\n\n{list(yoga_comb_key[yoga_comb_key.yoga_name == yoga_comb_date1[i]].yoga_text)[0]}\n\n"

            bot.send_message(call.message.chat.id, text=answer,
                            parse_mode='Markdown', reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, text="📍 Комбинационных йог на текущий день не обнаружено",
                            parse_mode='Markdown', reply_markup=markup)

logging.info('START')
bot.infinity_polling()

