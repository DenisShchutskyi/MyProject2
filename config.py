from pymongo import MongoClient


count_users = 50  # колиичество пользователей
count_tracks = 200  # количество треков создавать(это количество может не соответствовать количеству треков в базе т.к.
#  будут добавляться случайные треки в случайном количестве
str_connect_to_db = 'mongodb://localhost:27017'  # строка подключения к базе
try:
    client = MongoClient(str_connect_to_db)  # клиент для работы
    connect = client.univer  # указатель на базу univer
except:
    print('error in connect')
