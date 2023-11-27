from telebot.util import quick_markup
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from os import system
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
import io
import telebot;
import time
import random as r

init(autoreset=True)

system("title " + 'Running')

drops = io.open('drops.txt', encoding='utf-8') #редачить этот файл
drop = drops.read().split('\n')


cities = io.open('cities.txt', encoding='utf-8')
citylist = cities.read().split('\n')
cities_id = io.open('cities_id.txt', encoding='utf-8')
citylist_id = cities_id.read().split('\n')
#is_activeTicket = False

review1 = """🔸Показаны последние 20 отзывов
➖➖➖
👤F*******r
⭐️⭐️⭐️⭐️⭐️
🏠Город: Новосибирск
📨Текст отзыва: Все родной в касание
➖➖➖
👤Т*******и
⭐️⭐️⭐️⭐️⭐️
🏠Город: Новосибирск
📨Текст отзыва: по весам ровно 2 даже с бонусом ))) спасибо )))
➖➖➖
👤B****c
⭐️⭐️⭐️⭐️⭐️
🏠Город: Москва
📨Текст отзыва: На высшем , как всегда
➖➖➖
👤Z***a
⭐️⭐️⭐️⭐️⭐️
🏠Город: Екатеринбург
📨Текст отзыва: Братец съем кассио
➖➖➖
👤S******g
⭐️⭐️⭐️⭐️⭐️
🏠Город: Нижний Новгород
📨Текст отзыва: замаскированно хорошо, но место палевное, вокруг люди гуляют
➖➖➖
"""

review2 = """➖➖➖
👤T****p
⭐️⭐️⭐️⭐️⭐️
🏠Город: Омск
📨Текст отзыва: пиздец бошками воняют, липкий, вообще заебок
➖➖➖
👤А*****й
⭐️⭐️⭐️⭐️⭐️
🏠Город: Ульяновск
📨Текст отзыва: Поднял Бро Благодарю В темноте немного сложно На пенёк нашел и встал с нужного ракурса
➖➖➖
👤m**c
⭐️⭐️⭐️⭐️⭐️
🏠Город: Новосибирск
📨Текст отзыва: От души стафф годный
➖➖➖
👤M*****o
⭐️⭐️⭐️⭐️⭐️
🏠Город: Уфа
📨Текст отзыва: Забрал, всё 10 10 10 10 10 Ни одного промаха, за полгода
➖➖➖
👤F*******N
⭐️⭐️⭐️⭐️⭐️
🏠Город: Иркутск
📨Текст отзыва: В касание поднял, спасибо оператору за суету Курьер красавчик
➖➖➖
"""

review3 = """➖➖➖
👤y*******a
⭐️⭐️⭐️⭐️⭐️
🏠Город: Ульяновск
📨Текст отзыва: съем в касашу, но место ...
➖➖➖
👤X***********x
⭐️⭐️⭐️⭐️⭐️
🏠Город: Саратов
📨Текст отзыва: снято моментум кач что-то с чем-то)) 10.10.10 все десятки ваши
➖➖➖
👤А******z
⭐️⭐️⭐️⭐️⭐️
🏠Город: Санкт-Петерубрг
📨Текст отзыва: Все как обычно 
Все на месте все ровно 
Даже не сомневался))
➖➖➖
👤t******a
⭐️⭐️⭐️⭐️⭐️
🏠Город: Уфа
📨Текст отзыва: Прошу прощения за поздний отзыв, съем касание дольше искал. Еще не пробовал но уверен что тут как всегда все гуд) Отдельное спасибо оператору, выручил
➖➖➖
👤p*******s
⭐️⭐️⭐️⭐️⭐️
🏠Город: Красноярск
📨Текст отзыва: Возникла проблема но с оператором все быстро решили 10/9/10
➖➖➖
"""

review4 = """➖➖➖
👤d***2
⭐️⭐️⭐️⭐️⭐️
🏠Город: Красноярск
📨Текст отзыва: Когда на месте тогда на месте, все путем, магаз всегда идет на встречу, наход за находом!
➖➖➖
👤Y*******e
⭐️⭐️⭐️⭐️⭐️
🏠Город: Саратов
📨Текст отзыва: День добрый! Всё дома! Качество и вес на должном. Курьер просто молорик. Делает свою работу на 100%. Всем причастным респект за профессионализм. Берегите себя, до новых встреч
➖➖➖
👤a**********e
⭐️⭐️⭐️⭐️⭐️
🏠Город: Москва
📨Текст отзыва: И снова в касание! Курево хорошее) по весам все ровно)
➖➖➖
👤n***5
⭐️⭐️⭐️⭐️⭐️
🏠Город: Казань
📨Текст отзыва: в касашку, кач ровный как и съем
➖➖➖
👤i******h
⭐️⭐️⭐️⭐️⭐️
🏠Город: Красноярск
📨Текст отзыва: Исполнение 5, толя пробит 5, стафф 5)

🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
➖➖➖
"""

bankPayMessage = f"""
            🧾Заказ №{str(r.randint(100000, 400000))}
💳Реквизиты для оплаты: {drop[0]}
➖➖➖
📌РЕКВИЗИТЫ ДЕЙСТВИТЕЛЬНЫ В ТЕЧЕНИИ 20 МИНУТ, если за это время совершить оплату не удалось, пожалуйста, создайте новый заказ.
📌Переводите ТОЧНО ТУ СУММУ, которая была указана при создании заявки.
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ]
            """
sbpPayMessage = f"""
            🧾Заказ №{str(r.randint(100000, 400000))}
💳Реквизиты для оплаты: {drop[1]}
➖➖➖
📌РЕКВИЗИТЫ ДЕЙСТВИТЕЛЬНЫ В ТЕЧЕНИИ 20 МИНУТ, если за это время совершить оплату не удалось, пожалуйста, создайте новый заказ.
📌Переводите ТОЧНО ТУ СУММУ, которая была указана при создании заявки.
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ]
            """
bitcoinPayMessage = f"""
            🧾Заказ №{str(r.randint(100000, 400000))}
💳Реквизиты для оплаты: bc1qu6ywhrjhu5ynf0xnnt5tjw6uxdcg63t2wujq5q
➖➖➖
📌РЕКВИЗИТЫ ДЕЙСТВИТЕЛЬНЫ В ТЕЧЕНИИ 20 МИНУТ, если за это время совершить оплату не удалось, пожалуйста, создайте новый заказ.
📌Переводите ТОЧНО ТУ СУММУ, которая была указана при создании заявки.
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ]
            """

bot = telebot.TeleBot('6399350277:AAH4GytGOkWrV37PiIF9BC3ox31PcXpuDgQ');

b_menu = 'https://i.ibb.co/YjtkVZv/b-menu.jpg'
b_shopwindow = 'https://i.ibb.co/nw5xhLn/b-shopwindow.jpg'
b_work = 'https://i.ibb.co/hcc1tT2/b-work.jpg'
b_op = 'https://i.ibb.co/0ZWJjfV/b-op.jpg'

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')

    if req[0] == 'shopwindow':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/shopwindow:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/shopwindow:{current_time}')
        markupShopwindow = InlineKeyboardMarkup(row_width=2)
        #print(citylist[0:])
        for x in range(len(citylist)):
            markupShopwindow.add(InlineKeyboardButton('🔶'+(citylist[x]), callback_data=citylist[x]))
                
        bot.send_photo(call.message.chat.id, photo=b_shopwindow, caption=("""
            🔹Выберите город:
➖➖➖
Чтобы вернуться в меню нажмите👉🏻/start"""), reply_markup = markupShopwindow)

    elif req[0] == 'buy1':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy1:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy1:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Архангельск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 2 шт (Магнит)
➖➖➖
‼️Запомните эту цену
Цена: {r.randint(2700, 2890)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy2':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy2:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy2:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Архангельск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 4 шт (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4200, 4550)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy3':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy3:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy3:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Архангельск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 1 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2200, 2430)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy4':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy4:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy4:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Архангельск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 3 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(6100, 6290)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy5':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy5:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy5:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Архангельск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 50 г (Надежность ААА+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(87500, 90000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy6':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy6:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy6:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Барнаул'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 2 шт (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2700, 2890)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy7':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy7:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy7:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Барнаул'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 4 шт (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4200, 4550)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy8':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy8:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy8:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Барнаул'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 1 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2500, 2750)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy9':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy9:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy9:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Барнаул'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4600, 4750)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy10':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy10:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy10:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Белгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "AK-47" 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3100, 3250)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy11':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy11:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy11:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Белгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "AK-47" 10 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(14900, 15250)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy12':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy12:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy12:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Белгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4100, 4250)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy13':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy13:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy13:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Белгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AFGHAN" 3 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(6000, 6100)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy14':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy14:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy14:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Белгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 1 г (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2700, 2900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy15':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy15:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy15:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Белгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 2 г (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3700, 3900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy16':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy16:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy16:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Белгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 10 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(18300, 18400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy17':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy17:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy17:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Владивосток'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "JIM BEAM" 1 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2300, 2400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy18':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy18:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy18:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Владивосток'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "JIM BEAM" 1 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2300, 2400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy19':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy19:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy19:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Владивосток'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "JIM BEAM" 10 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(16300, 16400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy20':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy20:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy20:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Владивосток'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 3 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(6600, 6700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy21':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy21:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy21:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Владивосток'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AFGHAN" 5 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(9800, 9900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy22':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy22:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy22:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Воронеж'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "JIM BEAM" 1 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2500, 2600)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy23':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy23:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy23:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Воронеж'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "JIM BEAM" 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3800, 3900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy24':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy24:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy24:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Воронеж'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "JIM BEAM" 5 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(9600, 9700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy25':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy25:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy25:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Воронеж'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3600, 3700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy26':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy26:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy26:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Воронеж'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 5 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(9600, 9720)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy27':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy27:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy27:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Воронеж'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 1000 г (Надежность ААА+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(1199000, 1200000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy28':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy28:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy28:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 1 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2200, 2300)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy29':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy29:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy29:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3800, 3900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy30':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy30:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy30:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 5 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3800, 3900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy31':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy31:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy31:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌈[VHQ] ЛСД 170мкг 2 шт (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3500, 3600)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy32':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy32:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy32:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌈[VHQ] ЛСД 170мкг 4 шт (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(5200, 5300)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy33':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy33:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy33:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌈[VHQ] ЛСД 170мкг 10 шт (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(12300, 12400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy34':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy34:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy34:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌈[VHQ] ЛСД 250мкг 2 шт (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4400, 4500)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy35':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy35:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy35:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌈[VHQ] ЛСД 250мкг 4 шт (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(7500, 7600)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy36':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy36:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy36:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 1 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2700, 2800)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy37':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy37:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy37:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Екатеринбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 3 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(6200, 6300)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy38':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy38:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy38:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Иркутск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "HONEY HAZE" 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4100, 4200)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy39':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy39:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy39:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Иркутск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "HONEY HAZE" 5 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(10500, 10600)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy40':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy40:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy40:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Иркутск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "HONEY HAZE" 10 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(19600, 19700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy41':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy41:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy41:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Иркутск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 50 шт (Прикоп ААА+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(52000, 52100)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy42':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy42:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy42:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Иркутск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 100 шт (Прикоп ААА+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(120500, 120600)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy43':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy43:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy43:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Казань'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "AK-47" 2 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4300, 4400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy44':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy44:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy44:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Казань'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "AK-47" 3 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(6200, 6300)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy45':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy45:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy45:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Казань'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "HONEY HAZE" 2 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4700, 4800)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy46':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy46:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy46:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Казань'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "HONEY HAZE" 5 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(11700, 11800)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy47':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy47:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy47:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Казань'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 4 шт (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(7900, 8000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy48':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy48:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy48:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Красноярск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 1 г (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2600, 2700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy49':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy49:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy49:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Красноярск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 3 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(7600, 7700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy50':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy50:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy50:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Красноярск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 200 г (Прикоп AAA+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(210000, 211400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy51':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy51:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy51:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Москва'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 2 г (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3100, 3200)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy52':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy52:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy52:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Москва'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 5 г (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(8300, 8400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy53':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy53:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy53:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Москва'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 15 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(23400, 23500)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy54':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy54:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy54:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Москва'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 30 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(41000, 41200)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy55':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy55:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy55:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Москва'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4600, 4700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy56':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy56:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy56:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Москва'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🦄[VHQ] Кодеин "ACTAVIS" 118 мл (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(9400, 9500)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy57':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy57:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy57:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Москва'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🦄[VHQ] Кодеин "ACTAVIS" 237 мл (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(14300, 14400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy58':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy58:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy58:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'НижнийНовгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4600, 4700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy59':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy59:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy59:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'НижнийНовгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AFGHAN" 10 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(13200, 13300)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy60':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy60:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy60:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'НижнийНовгород'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 20 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(34200, 34400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy61':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy61:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy61:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Новосибирск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 1 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2600, 2700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy62':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy62:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy62:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Новосибирск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 2 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3300, 3400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy63':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy63:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy63:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Новосибирск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 5 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(8900, 9000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy64':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy64:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy64:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Новосибирск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 15 г (Тайник ПРИГОРОД АА+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(29900, 30000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy71':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy71:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy71:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Омск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "GORILLA" 2 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4800, 4900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy72':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy72:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy72:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Омск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "GORILLA" 5 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(9400, 9500)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy73':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy73:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy73:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Омск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 2 шт (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3200, 3300)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy74':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy74:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy74:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Омск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Сердца 10 шт (Тайник ПРИГОРОД)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(15900, 16000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy75':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy75:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy75:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Оренбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "GORILLA" 2 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3700, 3800)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy76':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy76:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy76:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Оренбург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "GORILLA" 10 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(16700, 16800)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy77':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy77:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy77:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'СанктПетербург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "AK-47" 5 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(8600, 8700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy78':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy78:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy78:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'СанктПетербург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "AK-47" 10 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(14500, 14600)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy79':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy79:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy79:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'СанктПетербург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 3 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(5200, 5300)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy80':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy80:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy80:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'СанктПетербург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 5 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(8900, 9000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy81':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy81:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy81:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'СанктПетербург'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 10 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(15400, 15500)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy82':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy82:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy82:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Саратов'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌈[VHQ] ЛСД 250мкг 2 шт (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4700, 4800)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy83':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy83:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy83:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Саратов'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌈[VHQ] ЛСД 250мкг 4 шт (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(6900, 7000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy84':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy84:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy84:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Саратов'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌈[VHQ] ЛСД 250мкг 20 шт (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(31200, 31600)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy85':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy85:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy85:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Саратов'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4200, 4300)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy86':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy86:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy86:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Саратов'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 10 г (Прикоп АА+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(16800, 16900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy87':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy87:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy87:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Тольятти'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AFGHAN" 2 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(3600, 3700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy88':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy88:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy88:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Тольятти'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AFGHAN" 5 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(7800, 7900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy89':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy89:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy89:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Тольятти'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AFGHAN" 10 г (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(15300, 15400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy90':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy90:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy90:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Томск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 20 г (Тайник АА+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(33900, 34000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy91':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy91:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy91:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Томск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🤎[VHQ] Ice-o-Lator "AMNESIA" 100 г (Тайник ААА+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(126000, 126200)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy92':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy92:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy92:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Тюмень'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Черный Куб 2 шт (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(5600, 5700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy93':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy93:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy93:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Тюмень'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Черный Куб 4 шт (Тайник)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(8900, 9000)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy94':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy94:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy94:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Тюмень'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💊[VHQ] Экстази Черный Куб 10 шт (Тайник А+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(19600, 19700)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy95':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy95:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy95:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Тюмень'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "GORILLA" 1 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2300, 2400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy96':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy96:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy96:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Тюмень'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "GORILLA" 3 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(6400, 6500)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy97':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy97:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy97:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Ульяновск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 1 г (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(2800, 2900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy98':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy98:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy98:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Ульяновск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 2 г (Магнит)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(4100, 4200)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy99':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy99:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy99:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Ульяновск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 10 г (Прикоп ПРИГОРОД)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(17800, 17900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy100':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy100:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy100:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Ульяновск'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "GORILLA" 50 г (Прикоп ААА+ ПРИГОРОД)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(65000, 65100)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy101':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy101:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy101:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Уфа'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 2 г (Прикоп)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(5300, 5400)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy102':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy102:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy102:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Уфа'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            💎[VHQ] Меф Кристалл 10 г (Прикоп А+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(16400, 16500)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy103':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy103:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy103:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Уфа'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "AK-47" 10 г (Прикоп А+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(14800, 14900)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)
    elif req[0] == 'buy104':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/buy104:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/buy104:{current_time}')
        markupPay = quick_markup({
            '💳Банковская карта': {'callback_data': 'payBank'},
            '📳СБП': {'callback_data': 'paySBP'},
            '🪙Bitcoin-адрес': {'callback_data': 'payBitcoin'},
            '↩️ Назад': {'callback_data': 'Уфа'}
            }, row_width=1)
        bot.send_message(call.message.chat.id, f"""
            🌿[VHQ] Бошки "AK-47" 25 г (Прикоп А+)
➖➖➖
‼️Запомните эту цену 
Цена: {r.randint(34500, 34600)} руб.
Выберите способ оплаты
➖➖➖
            """, reply_markup=markupPay)

    ######################################################################################################
    elif req[0] == 'payBank':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.CYAN + f'@{call.message.chat.username}:/payBank:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.CYAN + f'{call.message.chat.username}:/payBank:{current_time}')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        time.sleep(r.randint(3, 5))
        #rand = str(r.randint(100000, 400000))
        markupBank = quick_markup({
        '🔄Проверить оплату': {'callback_data': 'checker'},
        '❌Отменить': {'callback_data': 'cancel'}
        }, row_width=1)
        bot.send_message(call.message.chat.id, bankPayMessage, reply_markup=markupBank)
    elif req[0] == 'paySBP':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.CYAN + f'@{call.message.chat.username}:/paySBP:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.CYAN + f'{call.message.chat.username}:/paySBP:{current_time}')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        time.sleep(r.randint(3, 5))
        #rand = str(r.randint(100000, 400000))
        markupBank = quick_markup({
        '🔄Проверить оплату': {'callback_data': 'checker'},
        '❌Отменить': {'callback_data': 'cancel'}
        }, row_width=1)
        bot.send_message(call.message.chat.id, sbpPayMessage, reply_markup=markupBank)
    elif req[0] == 'payBitcoin':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.CYAN + f'@{call.message.chat.username}:/payBitcoin:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.CYAN + f'{call.message.chat.username}:/payBitcoin:{current_time}')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        time.sleep(r.randint(3, 5))
        #rand = str(r.randint(100000, 400000))
        markupBank = quick_markup({
        '🔄Проверить оплату': {'callback_data': 'checker'},
        '❌Отменить': {'callback_data': 'cancel'}
        }, row_width=1)
        bot.send_message(call.message.chat.id, bitcoinPayMessage, reply_markup=markupBank)
    ######################################################################################################

    elif req[0] == 'checker':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Back.CYAN + Fore.BLACK + f'@{call.message.chat.username}:/checker:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Back.CYAN + Fore.BLACK +f'{call.message.chat.username}:/checker:{current_time}')
        time.sleep(r.randint(3, 10))
        bot.send_message(call.message.chat.id, '⚠️Нет информации о поступлении\nОбычно средства зачисляются в течении 10 минут')

    elif req[0] == 'cancel':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Back.RED + Fore.BLACK + f'@{call.message.chat.username}:/cancel:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.CYAN + Fore.BLACK + f'{call.message.chat.username}:/cancel:{current_time}')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        time.sleep(r.randint(3, 5))
        bot.send_message(call.message.chat.id, '✅Заявка на пополнение отменена')
    #cities

    elif req[0] == 'Архангельск':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Архангельск:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Архангельск:{current_time}')
        markupBuy = quick_markup({'💊[VHQ] Экстази Сердца 2 шт (Магнит)': {'callback_data': 'buy1'},
                                '💊[VHQ] Экстази Сердца 4 шт (Магнит)': {'callback_data': 'buy2'},
                                '💎[VHQ] Меф Кристалл 1 г (Прикоп)': {'callback_data': 'buy3'},
                                '💎[VHQ] Меф Кристалл 3 г (Прикоп)': {'callback_data': 'buy4'},
                                '💎[VHQ] Меф Кристалл 50 г (Надежность ААА+)': {'callback_data': 'buy5'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Архангельск
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)

    elif req[0] == 'Барнаул':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Барнаул:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Барнаул:{current_time}')
        markupBuy = quick_markup({'💊[VHQ] Экстази Сердца 2 шт (Прикоп)': {'callback_data': 'buy6'},
                                '💊[VHQ] Экстази Сердца 4 шт (Прикоп)': {'callback_data': 'buy7'},
                                '💎[VHQ] Меф Кристалл 1 г (Прикоп)': {'callback_data': 'buy8'},
                                '💎[VHQ] Меф Кристалл 2 г (Прикоп)': {'callback_data': 'buy9'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Барнаул
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Белгород':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Белгород:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Белгород:{current_time}')
        markupBuy = quick_markup({'🌿[VHQ] Бошки "AK-47" 2 г (Прикоп)': {'callback_data': 'buy10'},
                                '🌿[VHQ] Бошки "AK-47" 10 г (Прикоп)': {'callback_data': 'buy11'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Прикоп)': {'callback_data': 'buy12'},
                                '🤎[VHQ] Ice-o-Lator "AFGHAN" 3 г (Прикоп)': {'callback_data': 'buy13'},
                                '💎[VHQ] Меф Кристалл 1 г (Магнит)': {'callback_data': 'buy14'},
                                '💎[VHQ] Меф Кристалл 2 г (Магнит)': {'callback_data': 'buy15'},
                                '💎[VHQ] Меф Кристалл 10 г (Прикоп)': {'callback_data': 'buy16'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Белгород
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Владивосток':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Владивосток:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Владивосток:{current_time}')
        markupBuy = quick_markup({'🌿[VHQ] Бошки "JIM BEAM" 1 г (Прикоп)': {'callback_data': 'buy17'},
                                '🌿[VHQ] Бошки "JIM BEAM" 5 г (Прикоп)': {'callback_data': 'buy18'},
                                '🌿[VHQ] Бошки "JIM BEAM" 10 г (Прикоп)': {'callback_data': 'buy19'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 3 г (Прикоп)': {'callback_data': 'buy20'},
                                '🤎[VHQ] Ice-o-Lator "AFGHAN" 5 г (Прикоп)': {'callback_data': 'buy21'},
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Владивосток
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Воронеж':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Воронеж:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Воронеж:{current_time}')
        markupBuy = quick_markup({'🌿[VHQ] Бошки "JIM BEAM" 1 г (Прикоп)': {'callback_data': 'buy22'},
                                '🌿[VHQ] Бошки "JIM BEAM" 2 г (Прикоп)': {'callback_data': 'buy23'},
                                '🌿[VHQ] Бошки "JIM BEAM" 5 г (Тайник)': {'callback_data': 'buy24'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Тайник)': {'callback_data': 'buy25'},
                                '💎[VHQ] Меф Кристалл 5 г (Тайник)': {'callback_data': 'buy26'},
                                '💎[VHQ] Меф Кристалл 1000 г (Надежность ААА+)': {'callback_data': 'buy27'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Воронеж
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Екатеринбург':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Екатеринбург:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Екатеринбург:{current_time}')
        markupBuy = quick_markup({'🤎[VHQ] Ice-o-Lator "AMNESIA" 1 г (Прикоп)': {'callback_data': 'buy28'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Прикоп)': {'callback_data': 'buy29'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 5 г (Прикоп)': {'callback_data': 'buy30'},
                                '🌈[VHQ] ЛСД 170мкг 2 шт (Магнит)': {'callback_data': 'buy31'},
                                '🌈[VHQ] ЛСД 170мкг 4 шт (Магнит)': {'callback_data': 'buy32'},
                                '🌈[VHQ] ЛСД 170мкг 10 шт (Прикоп)': {'callback_data': 'buy33'},
                                '🌈[VHQ] ЛСД 250мкг 2 шт (Магнит)': {'callback_data': 'buy34'},
                                '🌈[VHQ] ЛСД 250мкг 4 шт (Магнит)': {'callback_data': 'buy35'},
                                '💎[VHQ] Меф Кристалл 1 г (Прикоп)': {'callback_data': 'buy36'},
                                '💎[VHQ] Меф Кристалл 3 г (Прикоп)': {'callback_data': 'buy37'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Екатеринбург
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Иркутск':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Иркутск:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Иркутск:{current_time}')
        markupBuy = quick_markup({'🤎[VHQ] Ice-o-Lator "HONEY HAZE" 2 г (Прикоп)': {'callback_data': 'buy38'},
                                '🤎[VHQ] Ice-o-Lator "HONEY HAZE" 5 г (Прикоп)': {'callback_data': 'buy39'},
                                '🤎[VHQ] Ice-o-Lator "HONEY HAZE" 10 г (Тайник)': {'callback_data': 'buy40'},
                                '💊[VHQ] Экстази Сердца 50 шт (Прикоп ААА+)': {'callback_data': 'buy41'},
                                '💊[VHQ] Экстази Сердца 100 шт г (Прикоп ААА+)': {'callback_data': 'buy42'},
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Иркутск
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Казань':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Казань:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Казань:{current_time}')
        markupBuy = quick_markup({'🌿[VHQ] Бошки "AK-47" 2 г (Тайник)': {'callback_data': 'buy43'},
                                '🌿[VHQ] Бошки "AK-47" 3 г (Тайник)': {'callback_data': 'buy44'},
                                '🤎[VHQ] Ice-o-Lator "HONEY HAZE" 2 г (Тайник)': {'callback_data': 'buy45'},
                                '🤎[VHQ] Ice-o-Lator "HONEY HAZE" 5 г (Тайник)': {'callback_data': 'buy46'},
                                '💊[VHQ] Экстази Сердца 4 шт (Прикоп)': {'callback_data': 'buy47'},
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Казань
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Красноярск':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Красноярск:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Красноярск:{current_time}')
        markupBuy = quick_markup({'💎[VHQ] Меф Кристалл 1 г (Магнит)': {'callback_data': 'buy48'},
                                '💎[VHQ] Меф Кристалл 3 г (Тайник)': {'callback_data': 'buy49'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 200 г (Прикоп AAA+)': {'callback_data': 'buy50'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Красноярск
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Москва':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Москва:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Москва:{current_time}')
        markupBuy = quick_markup({'💎[VHQ] Меф Кристалл 2 г (Магнит)': {'callback_data': 'buy51'},
                                '💎[VHQ] Меф Кристалл 5 г (Магнит)': {'callback_data': 'buy52'},
                                '💎[VHQ] Меф Кристалл 15 г (Прикоп)': {'callback_data': 'buy53'},
                                '💎[VHQ] Меф Кристалл 30 г (Прикоп)': {'callback_data': 'buy54'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Тайник)': {'callback_data': 'buy55'},
                                '🦄[VHQ] Кодеин "ACTAVIS" 118 мл (Прикоп)': {'callback_data': 'buy56'},
                                '🦄[VHQ] Кодеин "ACTAVIS" 237 мл (Прикоп)': {'callback_data': 'buy57'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Москва
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Нижний Новгород':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/НижнийНовгород:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/НижнийНовгород:{current_time}')
        markupBuy = quick_markup({'🤎[VHQ] Ice-o-Lator "AMNESIA" 2 г (Прикоп)': {'callback_data': 'buy58'},
                                '🤎[VHQ] Ice-o-Lator "AFGHAN" 10 г (Прикоп)': {'callback_data': 'buy59'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 20 г (Тайник AAA+)': {'callback_data': 'buy60'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Нижний Новгород
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Новосибирск':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Новосибирск:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Новосибирск:{current_time}')
        markupBuy = quick_markup({'💎[VHQ] Меф Кристалл 1 г (Тайник)': {'callback_data': 'buy61'},
                                '💎[VHQ] Меф Кристалл 2 г (Тайник)': {'callback_data': 'buy62'},
                                '💎[VHQ] Меф Кристалл 5 г (Тайник)': {'callback_data': 'buy63'},
                                '💎[VHQ] Меф Кристалл 15 г (Тайник ПРИГОРОД АА+)': {'callback_data': 'buy64'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Новосибирск
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Омск':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Омск:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Омск:{current_time}')
        markupBuy = quick_markup({'🌿[VHQ] Бошки "GORILLA" 2 г (Тайник)': {'callback_data': 'buy71'},
                                '🌿[VHQ] Бошки "GORILLA" 5 г (Тайник)': {'callback_data': 'buy72'},
                                '💊[VHQ] Экстази Сердца 2 шт (Тайник)': {'callback_data': 'buy73'},
                                '💊[VHQ] Экстази Сердца 10 шт (Тайник ПРИГОРОД)': {'callback_data': 'buy74'},
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Омск
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Оренбург':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Оренбург:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Оренбург:{current_time}')
        markupBuy = quick_markup({'🌿[VHQ] Бошки "GORILLA" 2 г (Тайник)': {'callback_data': 'buy75'},
                                '🌿[VHQ] Бошки "GORILLA" 10 г (Тайник)': {'callback_data': 'buy76'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Оренбург
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Пермь':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Пермь:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Пермь:{current_time}')
        #markupBuy = quick_markup({}, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Пермь
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """) #reply_markup = markupBuy)
        time.sleep(1.2)
        bot.send_message(call.message.chat.id, "❌Нет доступных позиций")
    elif req[0] == 'СанктПетербург':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/СанктПетербург:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/СанктПетербург:{current_time}')
        markupBuy = quick_markup({'🌿[VHQ] Бошки "AK-47" 5 г (Прикоп)': {'callback_data': 'buy77'},
                                '🌿[VHQ] Бошки "AK-47" 10 г (Прикоп)': {'callback_data': 'buy78'},
                                '💎[VHQ] Меф Кристалл 3 г (Тайник)': {'callback_data': 'buy79'},
                                '💎[VHQ] Меф Кристалл 5 г (Прикоп)': {'callback_data': 'buy80'},
                                '💎[VHQ] Меф Кристалл 10 г (Прикоп)': {'callback_data': 'buy81'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Санкт-Петербург
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Саратов':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Саратов:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Саратов:{current_time}')
        markupBuy = quick_markup({'🌈[VHQ] ЛСД 250мкг 2 шт (Магнит)': {'callback_data': 'buy82'},
                                '🌈[VHQ] ЛСД 250мкг 4 шт (Магнит)': {'callback_data': 'buy83'},
                                '🌈[VHQ] ЛСД 250мкг 20 шт (Прикоп)': {'callback_data': 'buy84'},
                                '💎[VHQ] Меф Кристалл 2 г (Прикоп)': {'callback_data': 'buy85'},
                                '💎[VHQ] Меф Кристалл 10 г (Прикоп АА+)': {'callback_data': 'buy86'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Саратов
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Сургут':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Сургут:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Сургут:{current_time}')
        #markupBuy = quick_markup({}, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Сургут
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """) #reply_markup = markupBuy)
        time.sleep(1.2)
        bot.send_message(call.message.chat.id, "❌Нет доступных позиций")
    elif req[0] == 'Тольятти':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Тольятти:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Тольятти:{current_time}')
        markupBuy = quick_markup({'🤎[VHQ] Ice-o-Lator "AFGHAN" 2 г (Тайник)': {'callback_data': 'buy87'},
                                '🤎[VHQ] Ice-o-Lator "AFGHAN" 5 г (Тайник)': {'callback_data': 'buy88'},
                                '🤎[VHQ] Ice-o-Lator "AFGHAN" 10 г (Тайник)': {'callback_data': 'buy89'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Тольятти
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Томск':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Томск:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Томск:{current_time}')
        markupBuy = quick_markup({'🤎[VHQ] Ice-o-Lator "AMNESIA" 20 г (Тайник АА+)': {'callback_data': 'buy90'},
                                '🤎[VHQ] Ice-o-Lator "AMNESIA" 100 г (Тайник ААА+)': {'callback_data': 'buy91'},
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Томск
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Тюмень':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Тюмень:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Тюмень:{current_time}')
        markupBuy = quick_markup({'💊[VHQ] Экстази Черный Куб 2 шт (Тайник)': {'callback_data': 'buy92'},
                                '💊[VHQ] Экстази Черный Куб 4 шт (Тайник)': {'callback_data': 'buy93'},
                                '💊[VHQ] Экстази Черный Куб 10 шт (Тайник А+)': {'callback_data': 'buy94'},
                                '🌿[VHQ] Бошки "GORILLA" 1 г (Прикоп)': {'callback_data': 'buy95'},
                                '🌿[VHQ] Бошки "GORILLA" 3 г (Прикоп)': {'callback_data': 'buy96'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Тюмень
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Ульяновск':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Ульяновск:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Ульяновск:{current_time}')
        markupBuy = quick_markup({'💎[VHQ] Меф Кристалл 1 г (Магнит)': {'callback_data': 'buy97'},
                                '💎[VHQ] Меф Кристалл 2 г (Магнит)': {'callback_data': 'buy98'},
                                '💎[VHQ] Меф Кристалл 10 г (Прикоп ПРИГОРОД)': {'callback_data': 'buy99'},
                                '🌿[VHQ] Бошки "GORILLA" 50 г (Прикоп ААА+ ПРИГОРОД)': {'callback_data': 'buy100'},
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Ульяновск
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Уфа':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Уфа:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Уфа:{current_time}')
        markupBuy = quick_markup({'💎[VHQ] Меф Кристалл 2 г (Прикоп)': {'callback_data': 'buy101'},
                                '💎[VHQ] Меф Кристалл 10 г (Прикоп А+)': {'callback_data': 'buy102'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Уфа
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Хабаровск':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Хабаровск:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Хабаровск:{current_time}')
        markupBuy = quick_markup({'🌿[VHQ] Бошки "AK-47" 10 г (Прикоп А+)': {'callback_data': 'buy103'},
                                '🌿[VHQ] Бошки "AK-47" 25 г (Прикоп А+)': {'callback_data': 'buy104'}
            }, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Хабаровск
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """, reply_markup = markupBuy)
    elif req[0] == 'Чита':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Чита:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Чита:{current_time}')
        #markupBuy = quick_markup({}, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Чита
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """) #reply_markup = markupBuy)
        time.sleep(1.2)
        bot.send_message(call.message.chat.id, "❌Нет доступных позиций")
    elif req[0] == 'Ярославль':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/Ярославль:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/Ярославль:{current_time}')
        #markupBuy = quick_markup({}, row_width=1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔸Витрина города: Ярославль
➖➖➖
Выберите товар:
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """) #reply_markup = markupBuy)
        time.sleep(1.2)
        bot.send_message(call.message.chat.id, "❌Нет доступных позиций")
    #############################################################################################
        
    elif req[0] == 'operator':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'@{call.message.chat.username}:/operator:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.GREEN + f'{call.message.chat.username}:/operator:{current_time}')
        bot.send_photo(call.message.chat.id, photo=b_op, caption=("Связь с оператором"))

    elif req[0] == 'work':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.RED + f'@{call.message.chat.username}:/work:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.RED + f'{call.message.chat.username}:/work:{current_time}')
        bot.send_photo(call.message.chat.id, photo=b_work, caption=("""
            🧑‍💻 Работа в вашем городе
➖➖➖
📌 Наличие вакансий узнавайте у @binshop24_work 
📌 Отправляйте заявку в формате: возраст (18+), город. Наш специалист отправит вам вакансии доступные в вашем городе
📌 Не спамьте, отвечаем всем по мере возможности
➖➖➖
Чтобы вернуться в меню нажмите👉🏻/start"""))

    elif req[0] == 'reviews':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(f'@{call.message.chat.username}:/reviews:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(f'{call.message.chat.username}:/reviews:{current_time}')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        time.sleep(1)
        bot.send_message(call.message.chat.id, review1)
        time.sleep(1)
        bot.send_message(call.message.chat.id, review2)
        time.sleep(1)
        bot.send_message(call.message.chat.id, review3)
        time.sleep(1)
        bot.send_message(call.message.chat.id, review4)


    elif req[0] == 'orders':
        if (call.message.chat.username) != None:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.BLUE + f'@{call.message.chat.username}:/orders:{current_time}')
        else:
            named_tuple = time.localtime() # get struct_time
            current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
            print(Fore.BLUE + f'{call.message.chat.username}:/orders:{current_time}')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, """
            🔹Ваши заказы:
➖➖➖
Нет заказов
➖➖➖
🧑‍💻 [ По любым вопросам касающихся заказа обращайтесь к ОПЕРАТОРУ: @binshop24_op ] (Проверяйте ссылку, оператор никогда не пишет первым!)

⚠️ [ В обращении не забудьте приложить ID заказа и чек об оплате ]

Чтобы вернуться в меню нажмите👉🏻/start
            """)
@bot.message_handler(content_types=['text'])
def start(m):
    if (m.from_user.username) != None:
        named_tuple = time.localtime() # get struct_time
        current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        print(f'@{m.from_user.username}:/start:{current_time}')
    else:
        named_tuple = time.localtime() # get struct_time
        current_time = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        print(f'{m.from_user.username}:/start:{current_time}')
    markup = quick_markup({
    '🛍Витрина': {'callback_data': 'shopwindow'},
    '💻Работа': {'callback_data': 'work'},
    '📃Отзывы': {'callback_data': 'reviews'},
    '🧑‍💻Оператор': {'url': 'https://t.me/binshop24_op'},
    '📍Мои заказы': {'callback_data': 'orders'}
    }, row_width=2)
    bot.send_photo(m.from_user.id, photo=b_menu, caption=("""🔸Добро пожаловать в Binance Shop — ваш источник наслаждения
➖➖➖
🛒 Всего заказов: 0
💰 На сумму: 0.00 руб.
➖➖➖
        """), reply_markup = markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)