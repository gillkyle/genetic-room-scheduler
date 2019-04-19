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

    def length(self, day):
        return len(self.rooms[day])

    def unused_rooms(self):
        total = 0
        for day in DAYS:
            for _ in self.rooms[day]:
                total += 1
        return total

    def pull_out_resources(self, course):
        rooms = []
        number_of_slots = course.needed_time_slots()
        # print(number_of_slots)

        # go through each day that the course needs
        day_index = 0
        for should_assign_day in course.days:
            if should_assign_day:
                # find the allotted time
                # print(f"-------{DAYS[day_index]}--------")
                avail = self.rooms[DAYS[day_index]]

                # stop looping the number of slots before to avoid index out of bounds
                for i in range(len(avail) - number_of_slots):
                    avail_resources = avail[i:number_of_slots]
                    # if there aren't enough slots available just skip
                    if number_of_slots > len(avail_resources):
                        break
                    # print(avail_resources)
                    # if all(resource.? == ? for resource in avail_resources)
                    if avail_resources[0].room.capacity > course.num_students:
                        rooms += avail_resources
                        # remove the rooms we're returning from the availability
                        for remove_index in range(i, i+number_of_slots):
                            self.rooms[DAYS[day_index]].pop(remove_index)
                        break
            day_index += 1

        return rooms


class RoomResource:
    '''
    A resource of a specific time slot in an associated room
    '''

    def __init__(self, room, day, timeslot):
        self.code = f'{room.number}-{day}-{timeslot}'
        self.day = day
        self.room = room
        self.timeslot = timeslot
        self.number = room.number

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
