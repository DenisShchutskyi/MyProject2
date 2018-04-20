import asyncio
from config import connect  # коннект к базе
from data_generator import users  # сгененриролванные пользователи
from main import Processing
from main import Statistic

count_thread_processing = 3  # количество потоков для обработки ввода
count_thread_statistic = 3  # количество потоков для подсчета

loop = asyncio.get_event_loop()

#
processing = Processing(users,  # инициализация
                        connect,
                        loop,
                        count_thread=count_thread_processing)

# добавление пользователей
print('добавление в базу пользователей')
processing.run_insert_data_to_mongo()
print("проверьте наличие данных \n(для продолжения enter)")
input()
statistic = Statistic(connect,  # инициализация
                      loop,
                      count_thread=count_thread_statistic)

print('1. подсчитывать количество лайков каждого трека (от всех пользователей)'
      '\n(для продолжения enter)')
input()
statistic.run_count_like_tracks()
print('ознакомьтесь с результатами '
      '\n(для продолжения enter)')
input()
print('2. количество лайков заданного трека(берется первый трек первого пользователя) '
      '\n(для продолжения enter)')
input()
statistic.run_count_like_track(users[0].list_tracks[0].title)
print('ознакомьтесь с результатами '
      '\n(для продолжения enter)')
input()
print('3. количество понравившихся треков конкретного пользователя (берется первый пользователь) '
      '\n(для продолжения enter)')
input()
statistic.run_count_like_from_user(users[0].name)
print('ознакомьтесь с результатами'
      '\n(для продолжения enter)')
input()
print('удаление пользователей и их данных'
      '\n(для продолжения enter)')
input()
processing.run_remove_data_user_from_mongo()
print('работа завершена')

loop.close()
