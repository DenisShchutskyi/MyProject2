import random
from config import count_tracks
from config import count_users
from random_words import RandomWords
from random_words import RandomNicknames
from models import User
from models import Track
from pymongo import MongoClient
from config import str_connect_to_db

rw = RandomWords()
rn = RandomNicknames()

client = MongoClient(str_connect_to_db)

db = client.univer

tracks = [
    Track(' '.join(rw.random_words(count=random.randint(1, 5))),
          random.randint(1, 8),
          random.randint(50, 300)
          )
    for t in range(count_tracks)
]

users = [
    User(rn.random_nick(gender='u'),
         random.randint(12, 50),
         [random.choice(tracks) for _ in range(2, random.randint(5, 20))]
         ) for _ in range(count_users)]
