from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bs4, requests, datetime, time, random, json
import logging

clock = datetime.datetime.now()
s = requests.get('https://sinoptik.com.ru/погода-усть-абакан')
b = bs4.BeautifulSoup(s.text, "html.parser")
# Утро
U = b.select(" .temperature .p3")[0].getText()
U += b.select(" .temperature .p4")[0].getText()
# День
D = b.select(" .temperature .p5")[0].getText()
D += b.select(" .temperature .p6")[0].getText()
# Вечер
V = b.select(' .temperature .p7')[0].getText()
V += b.select(' .temperature .p8')[0].getText()
# Ночь
N = b.select(" .temperature .p1")[0].getText()
N += b.select(" .temperature .p2")[0].getText()
# Общий
O = b.select(" .rSide .description")[0].getText()
# Ветер
Wu = b.select(" .gray .p4")[2].getText()
Wd = b.select(" .gray .p6")[2].getText()
Wv = b.select(" .gray .p8")[2].getText()
Wn = b.select(" .gray .p2")[2].getText()
#timeman
timeman = b.select(" .infoTimes .clock")[1].getText()
#Code contactation
xxx = ('Запускаем дрон в небо 🚀')
aaa = ('Прозваниваем данные 📞')
wwww = ('Связисты передают 📡')
zzz = ('-------------------------------------------------------'+'\nСистемное время: ' + clock.strftime('%H.%M') +'\n'+timeman +
          '\nТекущая дата: ' + clock.strftime('%d.%m.%Y') + '\n-' + '\nУтром: ' + U + '\nВетер: ' + Wu + 'мс' '\nДнём: ' + D + '\nВетер: ' + Wd + '\n-' +
          '\nВечером: ' + V + '\nВетер: ' + Wv + '\nНочью: ' + N + '\nВетер: ' + Wn + '\n-' + '\n' + O)
cherta = ('\n-------------------------------------------------------')
zzz = zzz + cherta

