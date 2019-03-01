from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bs4, requests, datetime, time, random, json
import logging

clock = datetime.datetime.now()
s = requests.get('https://sinoptik.com.ru/погода-красноярск')
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
    #
xxx = ('Смотрим в небо ☁')
aaa = ('Анализируем звезды ✨')
wwww = ('Шаманы установили следующие показатели 🌡')
zzz = ('-------------------------------------------------------'+'\nТекущие время: ' + clock.strftime('%H.%M') +
            '\nТекущая дата: ' + clock.strftime('%d.%m.%Y') + '\n-' + '\nУтром: ' + U + '\nДнём: ' + D + '\n-' +
            '\nВечером: ' + V + '\nНочью: ' + N + '\n-'+'\n' + O)
cherta = ('\n-------------------------------------------------------')
zzz = zzz + cherta

