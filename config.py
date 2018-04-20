from pymongo import MongoClient


count_users = 50
count_tracks = 200
str_connect_to_db = 'mongodb://localhost:27017'
try:
    client = MongoClient(str_connect_to_db)
    connect = client.univer
except:
    print('error in connect')