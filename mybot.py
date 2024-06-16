import telebot
import datetime as dt
import salonModel as m
from telebot import types
import re
with m.db as db:
        bot = telebot.TeleBot('7014214276:AAGt1g15BSNz7YYzXNWxGmf3R83VAXMiHSk')
        @bot.message_handler(commands=['start'])
        def hi(message):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                menua = types.KeyboardButton('Меню')
   #             menuadm = types.KeyboardButton('Меню администратора')
   #             menumaster = types.KeyboardButton('Меню мастера')
                markup.add(menua)
                bot.send_message(message.chat.id,'Привет это бот для записи в салон красоты', reply_markup=markup)
        @bot.message_handler(content_types=['contact'])
        def contact(message):
                if message.contact is not None:
                        global name
                        name = message.contact.first_name
                        global number
                        number = message.contact.phone_number
                        print(message.from_user.id)
                        a = m.Client(nomer = number, name = name)
                        a.save()
                        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        info = types.KeyboardButton('Список процедур📜')
                        info2 = types.KeyboardButton('Вернуться в меню')
                        menumaster = types.KeyboardButton('Меню мастера')
                        markup1.add(info,info2,menumaster)
                        bot.send_message(message.chat.id,'Выберите процедуру для записи',reply_markup=markup1)
try:
        @bot.message_handler(content_types=['text'])
        def menu(message):
                if message.text == 'Меню':
                        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Запись')
                        exitmenu = types.KeyboardButton('Выйти из меню')
                        info = types.KeyboardButton('Список процедур')
                        markup1.add(info,zapis,exitmenu)
                        bot.send_message(message.chat.id,'Вы зашли в меню',reply_markup=markup1)
                elif message.text == 'Выйти из меню':
                        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        menua = types.KeyboardButton('Меню')
       #                 menuadm = types.KeyboardButton('Меню администратора')
       #                 menumaster = types.KeyboardButton('Меню мастера')
                        markup2.add(menua)
                        bot.send_message(message.chat.id,'Вы вышли из меню',reply_markup=markup2)
                elif message.text == 'Назад':
                        markup2naz = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        menua = types.KeyboardButton('Меню')
                        markup2naz.add(menua)
                        bot.send_message(message.chat.id,'Вы вернулись',reply_markup=markup2naz)
                elif message.text == 'Список процедур':
                        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        info = types.KeyboardButton('Вернуться в меню')
                        brovi = types.KeyboardButton('Брови')
                        manikyr = types.KeyboardButton('Маникюр')
                        resnici = types.KeyboardButton('Ресницы')
                        pedikyr = types.KeyboardButton('Педикюр')
                        markup3.add(manikyr,pedikyr,resnici,brovi,info)
                        bot.send_message(message.chat.id,'Вы вошли в список процедур',reply_markup=markup3)
                elif message.text == 'Вернуться в меню':
                        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Запись')
                        exitmenu = types.KeyboardButton('Выйти из меню')
                        info = types.KeyboardButton('Список процедур')
                        markup4.add(info,zapis,exitmenu)
                        bot.send_message(message.chat.id,'Вы вернулись в меню',reply_markup=markup4)
                elif message.text == 'Запись':
                        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        kontakt = types.KeyboardButton(text='Дать телефонный номер', request_contact=True)
                        markup5.add(kontakt,zapis)
                        bot.send_message(message.chat.id,'Для продолжения работы боту необходимо предоставить номер телефона',reply_markup=markup5)
                elif message.text == 'Брови':
                        markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        brovikor = types.KeyboardButton('Коррекция бровей воском')
                        brovikras = types.KeyboardButton('Окрашивание бровей с использованием хны')
                        zapis = types.KeyboardButton('Вернуться в меню')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup6.add(brovikor,brovikras,nazad,zapis)
                        bot.send_message(message.chat.id,'Вы выбрали процедуру брови',reply_markup=markup6)
                elif message.text == 'Коррекция бровей воском':
                        markup6a = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        brovikor = types.KeyboardButton('Коррекция бровей воском')
                        brovikras = types.KeyboardButton('Окрашивание бровей с использованием хны')
                        zapis = types.KeyboardButton('Вернуться в меню')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup6a.add(brovikor,brovikras,nazad,zapis)
                        bot.send_message(message.chat.id,'Коррекция бровей воском — это процедура, которая позволяет удалить нежелательные волоски и придать бровям желаемую форму. Воск наносится на кожу, затем застывает и удаляется вместе с волосками. Эта процедура имеет ряд преимуществ: она безболезненная, эффективная и не вызывает раздражения кожи.',reply_markup=markup6a)
                        bot.send_message(message.chat.id,'Цена услуги: 500р')
                elif message.text == 'Окрашивание бровей с использованием хны':
                        markup6b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        brovikor = types.KeyboardButton('Коррекция бровей воском')
                        brovikras = types.KeyboardButton('Окрашивание бровей с использованием хны')
                        zapis = types.KeyboardButton('Вернуться в меню')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup6b.add(brovikor,brovikras,nazad,zapis)
                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hr.jpg")
                        bot.send_message(message.chat.id,'Окрашивание бровей с использованием хны — это натуральный и безопасный способ подчеркнуть красоту бровей. Хна — это природный краситель, который не только окрашивает, но и укрепляет волоски. Этот метод подходит для тех, кто хочет иметь густые и яркие брови.',reply_markup=markup6b)
                        bot.send_message(message.chat.id,'Цена услуги: 500р')
                elif message.text == 'Маникюр':
                        markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        manikyrbez = types.KeyboardButton('Маникюр без покрытия')
                        manikyrpok = types.KeyboardButton('Маникюр с покрытием')
                        snyatmanikyr = types.KeyboardButton('Снятие маникюра')
                        zapis = types.KeyboardButton('Вернуться в меню')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup7.add(manikyrbez,manikyrpok,snyatmanikyr,nazad,zapis)
                        bot.send_message(message.chat.id,'Вы выбрали процедуру маникюр',reply_markup=markup7)
                elif message.text == 'Маникюр без покрытия':
                        markup7a = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        manikyrbez = types.KeyboardButton('Маникюр без покрытия')
                        manikyrpok = types.KeyboardButton('Маникюр с покрытием')
                        snyatmanikyr = types.KeyboardButton('Снятие маникюра')
                        zapis = types.KeyboardButton('Вернуться в меню')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup7a.add(manikyrbez,manikyrpok,snyatmanikyr,nazad,zapis)
                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hn.jpg")
                        bot.send_message(message.chat.id,'Маникюр без покрытия — это стандартный гигиенический процесс, который включает обработку ногтей, удаление заусенцев, придание формы и обработку кутикулы. Такой маникюр подходит для тех, кто предпочитает естественный вид ногтей без использования гель-лака.',reply_markup=markup7a)
                        bot.send_message(message.chat.id,'Цена услуги: 800р')
                elif message.text == 'Маникюр с покрытием':
                        markup7b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        manikyrbez = types.KeyboardButton('Маникюр без покрытия')
                        manikyrpok = types.KeyboardButton('Маникюр с покрытием')
                        snyatmanikyr = types.KeyboardButton('Снятие маникюра')
                        zapis = types.KeyboardButton('Вернуться в меню')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup7b.add(manikyrbez,manikyrpok,snyatmanikyr,nazad,zapis)
                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hp.jpg")
                        bot.send_message(message.chat.id,'Маникюр с покрытием гель-лаком — это процедура, которая включает стандартную обработку ногтевой пластины, удаление ороговевшей кожи и использование гель-лака в качестве финишного покрытия. Гель-лак застывает под воздействием УФ-лампы и остаётся на ногтях в течение трёх-четырёх недель, сохраняя глянцевый блеск.',reply_markup=markup7b)
                        bot.send_message(message.chat.id,'Цена услуги: 1800р')
                elif message.text == 'Снятие маникюра':
                        markup7b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        manikyrbez = types.KeyboardButton('Маникюр без покрытия')
                        manikyrpok = types.KeyboardButton('Маникюр с покрытием')
                        snyatmanikyr = types.KeyboardButton('Снятие маникюра')
                        zapis = types.KeyboardButton('Вернуться в меню')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup7b.add(manikyrbez,manikyrpok,snyatmanikyr,nazad,zapis)
                        bot.send_message(message.chat.id,'Снятие маникюра у мастера — это процесс удаления гель-лака с ногтей. Мастер использует специальную машинку с фрезой или ацетон и фольгу для аккуратного и безопасного снятия покрытия.',reply_markup=markup7b)
                        bot.send_message(message.chat.id,'Цена услуги: 500р')
                elif message.text == 'Ресницы':
                        markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        narresnic = types.KeyboardButton('Классическое наращивание ресниц')
                        obresnic = types.KeyboardButton('Объёмное наращивание ресниц')
                        snyatresnic = types.KeyboardButton('Снятие ресниц')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup8.add(narresnic,obresnic,snyatresnic,nazad,zapis)
                        bot.send_message(message.chat.id,'Вы выбрали ресницы',reply_markup=markup8)
                elif message.text == 'Педикюр':
                        markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        pedikyrbez = types.KeyboardButton('Педикюр без покрытия')
                        pedikyrs = types.KeyboardButton('Педикюр с покрытием')
                        snyatpedikyr = types.KeyboardButton('Снятие педикюра')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup9.add(pedikyrbez,pedikyrs,snyatpedikyr,nazad,zapis)
                        bot.send_message(message.chat.id,'Вы выбрали процедуру педикюр',reply_markup=markup9)
                elif message.text == 'Педикюр без покрытия':
                        markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        pedikyrbez = types.KeyboardButton('Педикюр без покрытия')
                        pedikyrs = types.KeyboardButton('Педикюр с покрытием')
                        snyatpedikyr = types.KeyboardButton('Снятие педикюра')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup9.add(pedikyrbez,pedikyrs,snyatpedikyr,nazad,zapis)
                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96ho.jpg")
                        bot.send_message(message.chat.id,'Педикюр без покрытия — это комплекс процедур, направленных на уход за стопами, без использования лака или других декоративных средств. Процедура включает распаривание стоп, обработку ногтей, удаление огрубевшей кожи, пилинг и увлажнение. Педикюр без покрытия помогает предотвратить проблемы со стопами, делает их ухоженными и предотвращает появление вросших ногтей, мозолей и грибковых заболеваний.',reply_markup=markup9)
                        bot.send_message(message.chat.id,'Цена услуги: 1200р')
                elif message.text == 'Педикюр с покрытием':
                        markup9a = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        pedikyrbez = types.KeyboardButton('Педикюр без покрытия')
                        pedikyrs = types.KeyboardButton('Педикюр с покрытием')
                        snyatpedikyr = types.KeyboardButton('Снятие педикюра')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup9a.add(pedikyrbez,pedikyrs,snyatpedikyr,nazad,zapis)
                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hq.jpg")
                        bot.send_message(message.chat.id,'Педикюр с покрытием — это процедура, при которой ногти на ногах покрываются специальным защитным слоем, например, гель-лаком. Гель-лак образует прочное покрытие, которое держится на ногтях около месяца. Процесс педикюра с покрытием включает в себя распаривание ног, удаление натоптышей и мозолей, обработку ногтей, нанесение базового покрытия, цветного лака и закрепляющего покрытия.',reply_markup=markup9a)
                        bot.send_message(message.chat.id,'Цена услуги: 1800р')
                elif message.text == 'Снятие педикюра':
                        markup9b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        pedikyrbez = types.KeyboardButton('Педикюр без покрытия')
                        pedikyrs = types.KeyboardButton('Педикюр с покрытием')
                        snyatpedikyr = types.KeyboardButton('Снятие педикюра')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup9b.add(pedikyrbez,pedikyrs,snyatpedikyr,nazad,zapis)
                        bot.send_message(message.chat.id,'Снятие педикюра включает три основных этапа: размягчение покрытия, удаление гель-лака и обработка ногтевой пластины',reply_markup=markup9b)
                        bot.send_message(message.chat.id,'Цена услуги: 500р')
                elif message.text == 'Классическое наращивание ресниц':
                        markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        narresnic = types.KeyboardButton('Классическое наращивание ресниц')
                        obresnic = types.KeyboardButton('Объёмное наращивание ресниц')
                        snyatresnic = types.KeyboardButton('Снятие ресниц')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup10.add(narresnic,obresnic,snyatresnic,nazad,zapis)
                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hi.png")
                        bot.send_message(message.chat.id,'Классическое наращивание ресниц — это процедура, во время которой к каждой натуральной реснице приклеивают одну искусственную. Классическое наращивание бывает разной длины, толщины и изгиба, а также может выполняться в разных цветах.',reply_markup=markup10)
                        bot.send_message(message.chat.id,'Цена услуги: 1600р')
                elif message.text == 'Вернуться в список процедур':
                        markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        info = types.KeyboardButton('Вернуться в меню')
                        brovi = types.KeyboardButton('Брови')
                        manikyr = types.KeyboardButton('Маникюр')
                        resnici = types.KeyboardButton('Ресницы')
                        pedikyr = types.KeyboardButton('Педикюр')
                        markup11.add(manikyr,pedikyr,resnici,brovi,info)
                        bot.send_message(message.chat.id,'Вы вернулись в список процедур',reply_markup=markup11)
                elif message.text == 'Объёмное наращивание ресниц':
                        markup12 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        narresnic = types.KeyboardButton('Классическое наращивание ресниц')
                        obresnic = types.KeyboardButton('Объёмное наращивание ресниц')
                        snyatresnic = types.KeyboardButton('Снятие ресниц')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup12.add(narresnic,obresnic,snyatresnic,nazad,zapis)
                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hh.png")
                        bot.send_message(message.chat.id,'Объёмное наращивание ресниц — это техника, при которой на каждую натуральную ресницу крепится пучок из трёх искусственных. Объёмное наращивание создаёт яркий эффект, делая выбранную схему более выразительной. Оно подходит для клиентов с редкими или недостаточно густыми ресницами.',reply_markup=markup12)
                        bot.send_message(message.chat.id,'Цена услуги: 2500р')
                elif message.text == 'Снятие ресниц':
                        markup13 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        zapis = types.KeyboardButton('Вернуться в меню')
                        narresnic = types.KeyboardButton('Классическое наращивание ресниц')
                        obresnic = types.KeyboardButton('Объёмное наращивание ресниц')
                        snyatresnic = types.KeyboardButton('Снятие ресниц')
                        nazad = types.KeyboardButton('Вернуться в список процедур')
                        markup13.add(narresnic,obresnic,snyatresnic,nazad,zapis)
                        bot.send_message(message.chat.id,'Снятие наращенных ресниц должно проводиться аккуратно, чтобы не повредить натуральные.Мастер наносит ремувер на прикорневую зону наращенных ресниц, размягчая клей, затем аккуратно снимает искусственные реснички с помощью пинцета. После удаления всех ресниц мастер тщательно очищает волоски от остатков ремувера ватными дисками, смоченными в мицеллярной воде.',reply_markup=markup13)
                        bot.send_message(message.chat.id,'Цена услуги: 300р')
                elif name == message.from_user.first_name and message.text == 'Список процедур📜':
                                        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        info = types.KeyboardButton('Вернуться в меню')
                                        brovi = types.KeyboardButton('Брови✨')
                                        manikyr = types.KeyboardButton('Маникюр💅')
                                        resnici = types.KeyboardButton('Ресницы👁')
                                        pedikyr = types.KeyboardButton('Педикюр🦶')
                                        markup3.add(manikyr,pedikyr,resnici,brovi,info)
                                        bot.send_message(message.chat.id,'Вы вошли в список процедур',reply_markup=markup3)
                elif name == message.from_user.first_name and message.text == 'Брови✨':
                                        markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        brovikor = types.KeyboardButton('Коррекция бровей воском✨')
                                        brovikras = types.KeyboardButton('Окрашивание бровей с использованием хны✨')
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup6.add(brovikor,brovikras,nazad,zapis)
                                        bot.send_message(message.chat.id,'Вы выбрали процедуру брови',reply_markup=markup6)
                elif name == message.from_user.first_name and message.text == 'Коррекция бровей воском✨':
                                        markup6a = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        brovikor = types.KeyboardButton('Коррекция бровей воском✨')
                                        brovikras = types.KeyboardButton('Окрашивание бровей с использованием хны✨')
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup6a.add(brovikor,brovikras,nazad,zapis)
                                        bot.send_message(message.chat.id,'Коррекция бровей воском — это процедура, которая позволяет удалить нежелательные волоски и придать бровям желаемую форму. Воск наносится на кожу, затем застывает и удаляется вместе с волосками. Эта процедура имеет ряд преимуществ: она безболезненная, эффективная и не вызывает раздражения кожи.',reply_markup=markup6a)
                                        bot.send_message(message.chat.id,'Цена услуги: 500р')
                                        korbrov_inline = types.InlineKeyboardMarkup()
                                        korbrov_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes🖐🏿')
                                        korbrov_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        korbrov_inline.add(korbrov_yes,korbrov_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=korbrov_inline)   
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes🖐🏿")
                                        def callHandler1(korbrov):
                                                if korbrov.data == 'yes🖐🏿':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(korbrov.message.chat.id,'Выберите дату записи :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()     
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                
                                                elif korbrov.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Вернуться в список процедур📜':
                                        markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        info = types.KeyboardButton('Вернуться в меню')
                                        brovi = types.KeyboardButton('Брови✨')
                                        manikyr = types.KeyboardButton('Маникюр💅')
                                        resnici = types.KeyboardButton('Ресницы👁')
                                        pedikyr = types.KeyboardButton('Педикюр🦶')
                                        markup11.add(manikyr,pedikyr,resnici,brovi,info)
                                        bot.send_message(message.chat.id,'Вы вернулись в список процедур',reply_markup=markup11)
                elif name == message.from_user.first_name and message.text == 'Окрашивание бровей с использованием хны✨':
                                        markup6b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        brovikor = types.KeyboardButton('Коррекция бровей воском✨')
                                        brovikras = types.KeyboardButton('Окрашивание бровей с использованием хны✨')
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup6b.add(brovikor,brovikras,nazad,zapis)
                                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hr.jpg")
                                        bot.send_message(message.chat.id,'Окрашивание бровей с использованием хны — это натуральный и безопасный способ подчеркнуть красоту бровей. Хна — это природный краситель, который не только окрашивает, но и укрепляет волоски. Этот метод подходит для тех, кто хочет иметь густые и яркие брови.',reply_markup=markup6b)
                                        bot.send_message(message.chat.id,'Цена услуги: 500р')
                                        xny_inline = types.InlineKeyboardMarkup()
                                        xny_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes✨')
                                        xny_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        xny_inline.add(xny_yes,xny_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=xny_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes✨")
                                        def callHandler2(xny):
                                                if xny.data == 'yes✨':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(xny.message.chat.id,'Выберите дату записи :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                  
                                                elif xny.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Ресницы👁':
                                        markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        narresnic = types.KeyboardButton('Классическое наращивание ресниц👁')
                                        obresnic = types.KeyboardButton('Объёмное наращивание ресниц👁')
                                        snyatresnic = types.KeyboardButton('Снятие ресниц👁')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup8.add(narresnic,obresnic,snyatresnic,nazad,zapis)
                                        bot.send_message(message.chat.id,'Вы выбрали ресницы',reply_markup=markup8) 
                elif name == message.from_user.first_name and message.text == 'Классическое наращивание ресниц👁':
                                        markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        narresnic = types.KeyboardButton('Классическое наращивание ресниц👁')
                                        obresnic = types.KeyboardButton('Объёмное наращивание ресниц👁')
                                        snyatresnic = types.KeyboardButton('Снятие ресниц👁')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup10.add(narresnic,obresnic,snyatresnic,nazad,zapis)
                                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hi.png")
                                        bot.send_message(message.chat.id,'Классическое наращивание ресниц — это процедура, во время которой к каждой натуральной реснице приклеивают одну искусственную. Классическое наращивание бывает разной длины, толщины и изгиба, а также может выполняться в разных цветах.',reply_markup=markup10)
                                        bot.send_message(message.chat.id,'Цена услуги: 1600р')
                                        res_inline = types.InlineKeyboardMarkup()
                                        res_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes👌')
                                        res_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        res_inline.add(res_yes,res_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=res_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes👌")
                                        def callHandler3(res):
                                                if res.data == 'yes👌':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(res.message.chat.id,'Выберите дату записи :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()  
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')
                                                                                                                                                
                                                elif res.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Объёмное наращивание ресниц👁':
                                        markup12 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        narresnic = types.KeyboardButton('Классическое наращивание ресниц👁')
                                        obresnic = types.KeyboardButton('Объёмное наращивание ресниц👁')
                                        snyatresnic = types.KeyboardButton('Снятие ресниц👁')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup12.add(narresnic,obresnic,snyatresnic,nazad,zapis)
                                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hh.png")
                                        bot.send_message(message.chat.id,'Объёмное наращивание ресниц — это техника, при которой на каждую натуральную ресницу крепится пучок из трёх искусственных. Объёмное наращивание создаёт яркий эффект, делая выбранную схему более выразительной. Оно подходит для клиентов с редкими или недостаточно густыми ресницами.',reply_markup=markup12)
                                        bot.send_message(message.chat.id,'Цена услуги: 2500р')
                                        obres_inline = types.InlineKeyboardMarkup()
                                        obres_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes😮')
                                        obres_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        obres_inline.add(obres_yes,obres_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=obres_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes😮")
                                        def callHandler4(obres):
                                                if obres.data == 'yes😮':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(obres.message.chat.id,'Выберите дату записи :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d =  m.Session_date.delete().where(m.Session_date.date == call.data).execute()    
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                   
                                                elif obres.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Снятие ресниц👁':
                                        markup13 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        narresnic = types.KeyboardButton('Классическое наращивание ресниц👁')
                                        obresnic = types.KeyboardButton('Объёмное наращивание ресниц👁')
                                        snyatresnic = types.KeyboardButton('Снятие ресниц👁')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup13.add(narresnic,obresnic,snyatresnic,nazad,zapis)
                                        bot.send_message(message.chat.id,'Снятие наращенных ресниц должно проводиться аккуратно, чтобы не повредить натуральные.Мастер наносит ремувер на прикорневую зону наращенных ресниц, размягчая клей, затем аккуратно снимает искусственные реснички с помощью пинцета. После удаления всех ресниц мастер тщательно очищает волоски от остатков ремувера ватными дисками, смоченными в мицеллярной воде.',reply_markup=markup13)
                                        bot.send_message(message.chat.id,'Цена услуги: 300р')
                                        snres_inline = types.InlineKeyboardMarkup()
                                        snres_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes🙂')
                                        snres_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        snres_inline.add(snres_yes,snres_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=snres_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes🙂")
                                        def callHandler5(snres):
                                                if snres.data == 'yes🙂':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(snres.message.chat.id,'Выберите дату записи :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()   
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                  
                                                elif snres.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Педикюр🦶':
                                        markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        pedikyrbez = types.KeyboardButton('Педикюр без покрытия🦶')
                                        pedikyrs = types.KeyboardButton('Педикюр с покрытием🦶')
                                        snyatpedikyr = types.KeyboardButton('Снятие педикюра🦶')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup9.add(pedikyrbez,pedikyrs,snyatpedikyr,nazad,zapis)
                                        bot.send_message(message.chat.id,'Вы выбрали процедуру педикюр',reply_markup=markup9)
                elif name == message.from_user.first_name and message.text == 'Педикюр без покрытия🦶':
                                        markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        pedikyrbez = types.KeyboardButton('Педикюр без покрытия🦶')
                                        pedikyrs = types.KeyboardButton('Педикюр с покрытием🦶')
                                        snyatpedikyr = types.KeyboardButton('Снятие педикюра🦶')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup9.add(pedikyrbez,pedikyrs,snyatpedikyr,nazad,zapis)
                                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96ho.jpg")
                                        bot.send_message(message.chat.id,'Педикюр без покрытия — это комплекс процедур, направленных на уход за стопами, без использования лака или других декоративных средств. Процедура включает распаривание стоп, обработку ногтей, удаление огрубевшей кожи, пилинг и увлажнение. Педикюр без покрытия помогает предотвратить проблемы со стопами, делает их ухоженными и предотвращает появление вросших ногтей, мозолей и грибковых заболеваний.',reply_markup=markup9)
                                        bot.send_message(message.chat.id,'Цена услуги: 1200р')
                                        pedbez_inline = types.InlineKeyboardMarkup()
                                        pedbez_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes😕')
                                        pedbez_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        pedbez_inline.add(pedbez_yes,pedbez_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=pedbez_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes😕")
                                        def callHandler6(pedbez):
                                                if pedbez.data == 'yes😕':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(pedbez.message.chat.id,'Выберите дату записи  :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()  
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                   
                                                elif pedbez.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Педикюр с покрытием🦶':
                                        markup9a = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        pedikyrbez = types.KeyboardButton('Педикюр без покрытия🦶')
                                        pedikyrs = types.KeyboardButton('Педикюр с покрытием🦶')
                                        snyatpedikyr = types.KeyboardButton('Снятие педикюра🦶')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup9a.add(pedikyrbez,pedikyrs,snyatpedikyr,nazad,zapis)
                                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hq.jpg")
                                        bot.send_message(message.chat.id,'Педикюр с покрытием — это процедура, при которой ногти на ногах покрываются специальным защитным слоем, например, гель-лаком. Гель-лак образует прочное покрытие, которое держится на ногтях около месяца. Процесс педикюра с покрытием включает в себя распаривание ног, удаление натоптышей и мозолей, обработку ногтей, нанесение базового покрытия, цветного лака и закрепляющего покрытия.',reply_markup=markup9a)
                                        bot.send_message(message.chat.id,'Цена услуги: 1800р')
                                        peds_inline = types.InlineKeyboardMarkup()
                                        peds_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes🙃')
                                        peds_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        peds_inline.add(peds_yes,peds_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=peds_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes🙃")
                                        def callHandler7(peds):
                                                if peds.data == 'yes🙃':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(peds.message.chat.id,'Выберите дату записи  :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()   
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                  
                                                elif peds.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Снятие педикюра🦶':
                                        markup9b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        pedikyrbez = types.KeyboardButton('Педикюр без покрытия🦶')
                                        pedikyrs = types.KeyboardButton('Педикюр с покрытием🦶')
                                        snyatpedikyr = types.KeyboardButton('Снятие педикюра🦶')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup9b.add(pedikyrbez,pedikyrs,snyatpedikyr,nazad,zapis)
                                        bot.send_message(message.chat.id,'Снятие педикюра включает три основных этапа: размягчение покрытия, удаление гель-лака и обработка ногтевой пластины',reply_markup=markup9b)
                                        bot.send_message(message.chat.id,'Цена услуги: 500р')
                                        pedsn_inline = types.InlineKeyboardMarkup()
                                        pedsn_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes😖')
                                        pedsn_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        pedsn_inline.add(pedsn_yes,pedsn_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=pedsn_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes😖")
                                        def callHandler8(pedsn):
                                                if pedsn.data == 'yes😖':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(pedsn.message.chat.id,'Выберите дату записи  :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()   
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                  
                                                elif pedsn.data == 'no':
                                                        pass 
                elif '+79826614260' == number  and message.text == 'Меню мастера':
                                        markup2mas = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        naz = types.KeyboardButton('Назад')
                                        rab_vrem = types.KeyboardButton('Добавление рабочего времени')
                                        zapisi = types.KeyboardButton('Активные записи')
                                        markup2mas.add(naz,rab_vrem,zapisi)
                                        bot.send_message(message.chat.id,'Выберите нужную функцию',reply_markup=markup2mas)
                elif '+79826614260' == number and message.text == 'Активные записи':
                                        markup2mas = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        naz = types.KeyboardButton('Назад')
                                        rab_vrem = types.KeyboardButton('Добавление рабочего времени')
                                        vrem_inline = types.InlineKeyboardMarkup()
                                        vrem_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes👳🏽‍♂️')
                                        vrem_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        vrem_inline.add(vrem_yes,vrem_no)
                                        markup2mas.add(naz,rab_vrem)
                                        bot.send_message(message.chat.id,'Посмотреть записи',reply_markup=vrem_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes👳🏽‍♂️")
                                        def callHandler99(vrem):
                                                if vrem.data == 'yes👳🏽‍♂️':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Zapis.select(m.Zapis.Date_time).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                markupyes.add(types.InlineKeyboardButton(text= i['Date_time'].isoformat().split('T')[0]+' '+i['Date_time'].isoformat().split('T')[1],callback_data=i['Date_time'].isoformat().split('T')[0]+' '+i['Date_time'].isoformat().split('T')[1] ))  
                                                        bot.send_message(vrem.message.chat.id,'Активные записи на данный момент',reply_markup=markupyes)
                                                elif vrem.data == 'no':
                                                        pass                      
                elif '+79826614260' == number and message.text == 'Добавление рабочего времени':
                        markup2mas = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                        naz = types.KeyboardButton('Назад')
                        zapisi = types.KeyboardButton('Активные записи')
                        markup2mas.add(naz,zapisi)
                        bot.send_message(message.chat.id,'Введите дату и время записи в виде:"ГГГГ/ММ/ДД ЧЧ:ММ"',reply_markup=markup2mas)
                elif re.search(r"\d\d\d\d/\d\d?/\d\d? \d\d?:\d\d?", message.text) and '+79826614260' == number:
                        k = m.Session_date(date = message.text)
                        k.save()
                        bot.send_message(message.chat.id,'Запись добавлена')
                elif name == message.from_user.first_name and message.text == 'Маникюр💅':
                                        markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        manikyrbez = types.KeyboardButton('Маникюр без покрытия💅')
                                        manikyrpok = types.KeyboardButton('Маникюр с покрытием💅')
                                        snyatmanikyr = types.KeyboardButton('Снятие маникюра💅')
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup7.add(manikyrbez,manikyrpok,snyatmanikyr,nazad,zapis)
                                        bot.send_message(message.chat.id,'Вы выбрали процедуру маникюр',reply_markup=markup7)
                elif name == message.from_user.first_name and message.text == 'Маникюр без покрытия💅':
                                        markup7a = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        manikyrbez = types.KeyboardButton('Маникюр без покрытия💅')
                                        manikyrpok = types.KeyboardButton('Маникюр с покрытием💅')
                                        snyatmanikyr = types.KeyboardButton('Снятие маникюра💅')
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup7a.add(manikyrbez,manikyrpok,snyatmanikyr,nazad,zapis)
                                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hn.jpg")
                                        bot.send_message(message.chat.id,'Маникюр без покрытия — это стандартный гигиенический процесс, который включает обработку ногтей, удаление заусенцев, придание формы и обработку кутикулы. Такой маникюр подходит для тех, кто предпочитает естественный вид ногтей без использования гель-лака.',reply_markup=markup7a)
                                        bot.send_message(message.chat.id,'Цена услуги: 800р')
                                        manikbez_inline = types.InlineKeyboardMarkup()
                                        manikbez_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes👅')
                                        manikbez_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        manikbez_inline.add(manikbez_yes,manikbez_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=manikbez_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes👅")
                                        def callHandler9(manikbez):
                                                if manikbez.data == 'yes👅':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(manikbez.message.chat.id,'Выберите дату записи :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()  
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                   
                                                elif manikbez.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Маникюр с покрытием💅':
                                        markup7b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        manikyrbez = types.KeyboardButton('Маникюр без покрытия💅')
                                        manikyrpok = types.KeyboardButton('Маникюр с покрытием💅')
                                        snyatmanikyr = types.KeyboardButton('Снятие маникюра💅')
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup7b.add(manikyrbez,manikyrpok,snyatmanikyr,nazad,zapis)
                                        bot.send_photo(message.chat.id, "https://imgurhd.ru/i/96hp.jpg")
                                        bot.send_message(message.chat.id,'Маникюр с покрытием гель-лаком — это процедура, которая включает стандартную обработку ногтевой пластины, удаление ороговевшей кожи и использование гель-лака в качестве финишного покрытия. Гель-лак застывает под воздействием УФ-лампы и остаётся на ногтях в течение трёх-четырёх недель, сохраняя глянцевый блеск.',reply_markup=markup7b)
                                        bot.send_message(message.chat.id,'Цена услуги: 1800р')
                                        maniks_inline = types.InlineKeyboardMarkup()
                                        maniks_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes🦷')
                                        maniks_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        maniks_inline.add(maniks_yes,maniks_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=maniks_inline)
                                        @bot.callback_query_handler(func=lambda call: call.data == "yes🦷")
                                        def callHandler10(maniks):
                                                if maniks.data == 'yes🦷':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(maniks.message.chat.id,'Выберите дату записи :',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute() 
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                    
                                                elif maniks.data == 'no':
                                                        pass 
                elif name == message.from_user.first_name and message.text == 'Снятие маникюра💅':
                                        markup7b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
                                        manikyrbez = types.KeyboardButton('Маникюр без покрытия💅')
                                        manikyrpok = types.KeyboardButton('Маникюр с покрытием💅')
                                        snyatmanikyr = types.KeyboardButton('Снятие маникюра💅')
                                        zapis = types.KeyboardButton('Вернуться в меню')
                                        nazad = types.KeyboardButton('Вернуться в список процедур📜')
                                        markup7b.add(manikyrbez,manikyrpok,snyatmanikyr,nazad,zapis)
                                        bot.send_message(message.chat.id,'Снятие маникюра у мастера — это процесс удаления гель-лака с ногтей. Мастер использует специальную машинку с фрезой или ацетон и фольгу для аккуратного и безопасного снятия покрытия.',reply_markup=markup7b)
                                        bot.send_message(message.chat.id,'Цена услуги: 500р')
                                        maniksn_inline = types.InlineKeyboardMarkup()
                                        maniksn_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes🧠')
                                        maniksn_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')
                                        maniksn_inline.add(maniksn_yes,maniksn_no)
                                        bot.send_message(message.chat.id,'Вы хотите записаться на данную процедуру?', reply_markup=maniksn_inline)
                                        def callHandler11(maniksn):
                                                if maniksn.data == 'yes🧠':
                                                        markupyes = types.InlineKeyboardMarkup()
                                                        b = m.Session_date.select(m.Session_date.date).dicts().execute()
                                                        for i in b:
                                                                print(i)
                                                        for i in b:
                                                                     markupyes.add(types.InlineKeyboardButton(text= i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1],callback_data=i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1] ))  
                                                        bot.send_message(maniksn.message.chat.id,'Выберите дату записи  $',reply_markup=markupyes)
                                                        @bot.callback_query_handler(func=lambda call: True)
                                                        def date_to_zapis(call):
                                                                for i in b:
                                                                        if call.data == i['date'].isoformat().split('T')[0]+' '+i['date'].isoformat().split('T')[1]:
                                                                                k = m.Zapis(Date_time = call.data, procedures_id = '1', master_id = '1', client_id = call.from_user.id)
                                                                                k.save()
                                                                                d = m.Session_date.delete().where(m.Session_date.date == call.data).execute()  
                                                                                bot.send_message(call.message.chat.id,'Вы успешно записанны')                                                                   
                                                elif maniksn.data == 'no':
                                                        pass 
        bot.polling(none_stop=True)
except NameError:
    print("An error occured")