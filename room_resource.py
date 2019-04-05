DAYS = [
    "M",
    "T",
    "W",
    "Th",
    "F",
]


class AvailabeRooms:
    '''
    List of available room resources
    '''

    def __init__(self):
        self.rooms = {key: [] for key in DAYS}

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def add(self, room_resource):
        self.rooms[room_resource.day].append(room_resource)

    def pull_out_rooms(self, day, course):
        '''
        remove a number of rooms from the available slot on a given day
        '''

        def students_exceed_capacity(self):
            if self.room.capacity < course.num_students:
                # print(
                #     f'Capacity of {self.room.capacity} is too small for {course.num_students} that need the class.')
                return False
            else:
                # print(
                #     f'{self.room.capacity} is appropriate for {course.num_students} students.')
                return True

        filtered_rooms = list(
            filter(students_exceed_capacity, self.rooms[day]))
        if len(filtered_rooms) < 1:
            return []

        rooms = filtered_rooms[0:course.needed_time_slots()]
        return rooms


class RoomResource:
    '''
    A resource of a specific time slot in an associated room 
    '''

    def __init__(self, room, day, timeslot):
        self.code = f'{room.number}-{day}-{timeslot}'
        self.day = day
        self.room = room

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
