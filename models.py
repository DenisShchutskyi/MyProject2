from bson.objectid import ObjectId


class User:
    def __init__(self, name, age, list_tracks):
        self.id = ''
        self.name = name
        self.age = age
        self.list_tracks = list_tracks

    def insert_user_data(self, connect):
        self.insert_user_to_db(connect)
        for track in self.list_tracks:
            track.insert_track_to_db(connect)
            connect.track_to_user.insert({'_id_user': self.id,
                                          '_id_track': track.id})

    def insert_user_to_db(self, connect):
        # r = str(connect.users.find_one({'name':self.name})['_id'])
        self.id = connect.users.insert({
            'name': self.name,
            'age': self.age
        })

    def remove_user(self, connect):
        if self.id != '':
            connect.track_to_user.remove({'_id_user': self.id})
            connect.users.remove({'_id': ObjectId(self.id)})

    def __str__(self):
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
        self.id = ''
        self.title = title
        self.size = size
        self.length = length

    def insert_track_to_db(self, connect):
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
