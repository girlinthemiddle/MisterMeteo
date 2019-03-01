from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests, datetime, time, random, json
import logging


ListCold = ['https://www.youtube.com/watch?v=E1JplpqHkPw', 'https://www.youtube.com/watch?v=tC4lZAYDeBs',
             'https://www.youtube.com/watch?v=oy2x_kHCy4w', 'https://www.youtube.com/watch?v=WPw7nlluRdc',
             'https://www.youtube.com/watch?v=povMIUZGkQ8', 'https://www.youtube.com/watch?v=KGm1kz4E0Ws',
             'https://youtu.be/DaVKRLvN1tY', 'https://www.youtube.com/watch?v=zt_tyk3K1dY',
             'https://www.youtube.com/watch?v=94rl79_G9b8']

ListTechno = ['https://www.youtube.com/watch?v=ELVbJDAwI0E', 'https://www.youtube.com/watch?v=td6yY7_zdE8',
               'https://www.youtube.com/watch?v=iQLacVKFFx0', 'https://www.youtube.com/watch?v=TKyWthAUBt4']

ListMinimal = ['https://www.youtube.com/watch?v=APqnjoQ43_A', 'https://www.youtube.com/watch?v=O0N7TiUNd1k',
                'https://www.youtube.com/watch?v=Ft2wDN91S78', 'https://www.youtube.com/watch?v=8bOVEJk28pU',
                'https://www.youtube.com/watch?v=Aooy7iw-7cY', 'https://www.youtube.com/watch?v=0lBjcaMokvo',
                'https://www.youtube.com/watch?v=bQXIDmb99uY', 'https://www.youtube.com/watch?v=a4U7L99Ti44',
                'https://www.youtube.com/watch?v=ULSLloL7Zfg', 'https://www.youtube.com/watch?v=N55LdsouW08',
                'https://www.youtube.com/watch?v=NQzAvk7Leeg']

ListEpic = ['https://youtu.be/GZvxKhSl_c8', 'https://youtu.be/q7QppSWz00I', 'https://youtu.be/Uzrf9WrnwOU']

ListClassical = ['https://youtu.be/mmCnQDUSO4I', 'https://youtu.be/klPZIGQcrHA',
'https://youtu.be/YyknBTm_YyM', 'https://youtu.be/KpOtuoHL45Y', 'https://youtu.be/9E6b3swbnWg']


ListRandom = ListCold + ListTechno + ListMinimal + ListEpic + ListClassical
