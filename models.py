from bson.objectid import ObjectId


class User:
    def __init__(self, name, age, list_tracks):
        '''
        Инициализация класса пользователя
        :param name: имя
        :param age: возраст
        :param list_tracks: список его избранных
        '''
        self.id = ''
        self.name = name
        self.age = age
        self.list_tracks = list_tracks

    def insert_user_data(self, connect):
        '''
        добавление пользователя и его треков в базу
        :param connect: коннект к базе
        :return:
        '''
        self.insert_user_to_db(connect)
        for track in self.list_tracks:  # запись сго избранных треков
            track.insert_track_to_db(connect)
            connect.track_to_user.insert({'_id_user': self.id,
                                          '_id_track': track.id})

    def insert_user_to_db(self, connect):
        '''
        запись пользователя
        :param connect: коннект к базе
        :return:
        '''
        self.id = connect.users.insert({
            'name': self.name,
            'age': self.age
        })

    def remove_user(self, connect):
        '''
        удаление пользователя из базы и его избранного
        :param connect: коннект к базе
        :return:
        '''
        if self.id != '':
            connect.track_to_user.remove({'_id_user': self.id})
            connect.users.remove({'_id': ObjectId(self.id)})

    def __str__(self):
        '''
        принт пользователя
        :return:
        '''
        if self.id == '':
            return '<User(' \
                   'name: "{}" ' \
                   'age:  "{}" ' \
                   'len_tracks:{} ' \
                   'tracks:[{}])>'.format(self.name,
                                          self.age,
                                          len(self.list_tracks),
                                          ', '.join(map(str, self.list_tracks)))
        else:
            return '<User(' \
                   '_id: "{}" ' \
                   'name: "{}" ' \
                   'age:  "{}"  ' \
                   'len_tracks:{} ' \
                   'tracks:[{}])>'.format(self.id,
                                          self.name,
                                          self.age,
                                          len(self.list_tracks),
                                          ', '.join(map(str, self.list_tracks)))


class Track:
    def __init__(self, title, size, length):
        '''
        инициализация класса
        :param title: название трека
        :param size: размер
        :param length: длина
        '''
        self.id = ''
        self.title = title
        self.size = size
        self.length = length

    def insert_track_to_db(self, connect):
        '''
        запись трека в базу если такого нет (по названию)
        :param connect:
        :return:
        '''
        res = connect.track.find_one({'title': self.title})
        if res is None:
            self.id = connect.track.insert({
                'title': self.title,
                'size': self.size,
                'length': self.length
            })
        else:
            self.id = res['_id']

    def __str__(self):
        '''
        строки вывода
        :return:
        '''
        if self.id == '':
            return '<Track(' \
                   'title: "{}", ' \
                   'size: {}, ' \
                   'length: {})>'.format(self.title,
                                         self.length,
                                         self.size)
        else:
            return '<Track(' \
                   '_id: "{}" ' \
                   'title: "{}", ' \
                   'size: {}, ' \
                   'length: {})>'.format(self.id,
                                         self.title,
                                         self.length,
                                         self.size)
