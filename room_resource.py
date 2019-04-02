class AvailabeRooms:
    '''
    List of available room resources
    '''

    def __init__(self):
        self.rooms = []

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def add(self, room_resource):
        self.rooms.append(room_resource)

    def get_len(self):
        return len(self.rooms)

    def get_free_slot(length, num_days):
        '''
        find the next free class to make an assignment to
        '''
        # TODO
        return None


class RoomResource:
    '''
    A resource of a specific time slot in an associated room 
    '''

    def __init__(self, room_number, day, timeslot):
        self.code = f'{room_number}-{day}-{timeslot}'

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
