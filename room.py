class Room:
    '''
    A class that represents a room
    '''

    def __init__(self, code, capacity, room_type):
        self.code = code
        self.capacity = int(capacity)
        self.room_type = room_type

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
