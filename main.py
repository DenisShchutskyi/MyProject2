import asyncio
from bson.objectid import ObjectId


class Statistic:

    def __init__(self,
                 conn,
                 loop,
                 count_thread):
        self.conn = conn
        self.loop = loop
        self.count_thread = count_thread
        self.data_for_likes_tracks = {}  # json

    def all_data_to_empty(self):
        self.data_for_likes_tracks = {}  # json

    async def __count_like_tracks(self):
        #  1. подсчитывать количество лайков каждого трека (от всех пользователей)
        data = self.conn.track.find({})  #
        for d in data:
            if self.data_for_likes_tracks.get(d['_id'], False):  #
                pass
            else:
                self.data_for_likes_tracks[d['_id']] = {  #
                    'title': d['title'],
                    'count': self.conn.track_to_user.find({'_id_track': d['_id']}).count()  #
                }

    async def __count_like_track(self, title_track):
        # 2. количество лайков заданного трека
        data = self.conn.track_to_user.find({})  #
        for d in data:
            if self.conn.track.find_one({'_id': ObjectId(d['_id_track'])})['title'] == title_track:  #
                if self.data_for_likes_tracks.get(d['_id'], False):
                    pass
                else:
                    self.data_for_likes_tracks[d['_id']] = ''

    async def __count_like_user(self, name):
        # 3. количество понравившихся треков конкретного пользователя.
        data = self.conn.track_to_user.find({})  #
        for d in data:
            if self.conn.users.find_one({'_id': ObjectId(d['_id_user'])})['name'] == name:  #
                if self.data_for_likes_tracks.get(d['_id'], False):
                    pass
                else:
                    self.data_for_likes_tracks[d['_id']] = ' '

    def run_count_like_tracks(self):
        print('__START__')
        for _ in range(self.count_thread):  # создание указанное количества "потоков"
            self.loop.run_until_complete(self.__count_like_tracks())  # инициализация потока для функции
        print("__END__run")
        print('result count')
        count_in_program = 0
        for track in self.data_for_likes_tracks.keys():
            tmp = self.data_for_likes_tracks[track]
            print('track: "{}" count: {}'.format(tmp['title'], tmp['count']))
            count_in_program += tmp['count']
        count_id_db = self.conn.track_to_user.find({}).count()
        print('______________')
        print('count likes from program: {}\ncount likes in db: {}'.format(count_in_program, count_id_db))
        self.all_data_to_empty()

    def run_count_like_track(self, title_track):
        print('__START__')
        for _ in range(self.count_thread):
            self.loop.run_until_complete(self.__count_like_track(title_track))
        print("__END__run")
        print('result count')
        print('track: "{}" count: {}'.format(title_track, len(self.data_for_likes_tracks.keys())))
        self.all_data_to_empty()

    def run_count_like_from_user(self, name):
        print('__START__')
        for _ in range(self.count_thread):
            self.loop.run_until_complete(self.__count_like_user(name))
        print("__END__run")
        print('result count')
        print('user: "{}" count: {}'.format(name, len(self.data_for_likes_tracks.keys())))
        self.all_data_to_empty()


class Processing:
    def __init__(self, users,
                 conn,
                 loop,
                 count_thread=3):
        self.users = users
        self.conn = conn
        self.loop = loop
        self.count_thread = count_thread

    async def insert_to_db(self):
        for u in self.users:
            if u.id == '':
                u.insert_user_data(self.conn)

    async def remove_from_db(self):
        for u in self.users:
            if u.id != '':
                u.remove_user(self.conn)
                u.id = ''

    def run_insert_data_to_mongo(self):
        print('__START__')
        for _ in range(self.count_thread):
            self.loop.run_until_complete(self.insert_to_db())
        print('__END__')
        print('users inserted')

    def run_remove_data_user_from_mongo(self):
        print('__START__')
        for _ in range(self.count_thread):
            self.loop.run_until_complete(self.remove_from_db())
        print('__END__')
        print('users removed')
