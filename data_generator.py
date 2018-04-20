import random
from config import count_tracks
from config import count_users
from random_words import RandomWords
from random_words import RandomNicknames
from models import User
from models import Track


rw = RandomWords()  # класс отвечающий за случайные слова
rn = RandomNicknames()  # класс отвечающий за случайный ник

tracks = [
    Track(' '.join(rw.random_words(count=random.randint(1, 5))),  # название из слов от 1 до 5
          random.randint(1, 8),  # размер в мб
          random.randint(50, 300)  # продолжительнос в с
          )
    for t in range(count_tracks)
]

users = [
    User(rn.random_nick(gender='u'),  # какой - то никнейм
         random.randint(12, 50),  # возраст
         [random.choice(tracks) for _ in range(random.randint(5, 20))]  # какие-то случайные песни от 5 до 20
         ) for _ in range(count_users)]
