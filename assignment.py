from random import randint
from math import floor, modf


class CourseAssignment:
    '''
    A course assigned to a time slot in a room for a solution
    '''

    def __init__(self, room_resources, course):
        self.room = room_resources[0].room
        self.course = course
        self.number = room_resources[0].code.split("-")[0]
        self.day = room_resources[0].code.split("-")[1]
        self.time = int(room_resources[0].code.split("-")[2])
        self.timeslots = len(room_resources)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def set_new(self, resource):
        self.room = resource.room
        self.number = resource.number
        self.time = resource.timeslot

    def get_capacity_value(self):
        '''
        CapacityValue is assigned:
            50 if capacity of room minus students in course is 0-5.
            40 if capacity of room minus students in course is 6-10.
            30 if capacity of room minus students in course is 11-15.
            20 if capacity of room minus students in course is 16-20.
            10 if capacity of room minus students in course is 21-25.
            0 if capacity of room minus students in course is 26+.
            The number of students can never be greater than the capacity of the room (that would be an invalid assignment).
        '''
        disparity = self.room.capacity - self.course.num_students
        if 0 <= disparity <= 5:
            return 50
        elif 6 <= disparity <= 10:
            return 40
        elif 11 <= disparity <= 15:
            return 30
        elif 16 <= disparity <= 20:
            return 20
        elif 21 <= disparity <= 25:
            return 10
        else:
            return 0

    def get_pref_time_value(self):
        '''
        PrefTime is assigned:
            25 if the time slot is within the preferred time of the course (morning or afternoon).
            15 if the time slot crosses over the noon hour (thus partially matching the preferred time). This is time slot 8.
            0 if the time slot is not within the preferred time of the course.
        '''
        if (self.time < 8) and self.course.pref_time == 'Morning':
            return 25
        elif (self.time > 8) and self.course.pref_time == 'Afternoon':
            return 25
        elif (self.time == 8):
            return 15
        else:
            return 0

    def get_pref_type_value(self):
        '''
        PrefRoomType is assigned:
            25 if the preferred type of the room is met.
            0 if the preferred type of the room is not met.
        '''
        if self.room.room_type == self.course.pref_room_type:
            return 25
        else:
            return 0

    def get_ind_fitness(self):
        '''
        returns a fitness value in the range 0-100
        IndvFitness = CapacityValue + PrefTime + PrefRoomType
        '''
        return self.get_capacity_value() + self.get_pref_time_value() + self.get_pref_type_value()

    def convert_to_time_range(self):
        possible_hours = [8, 8.5, 9, 9.5, 10, 10.5, 11,
                          11.5, 12, 12.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
        start_hour = possible_hours[self.time]
        min_to_add = 0
        if floor(start_hour) % start_hour == 0:
            start_string = f"{start_hour}:00"
        else:
            start_string = f"{floor(start_hour)}:30"

        course_hours = float(self.course.hours)
        end_hour = start_hour + course_hours
        min_pct, end_hour_whole = modf(end_hour)
        end_minutes = min_pct * 60
        if end_minutes == 0:
            end_minutes_string = "00"
        else:
            end_minutes_string = str(int(end_minutes))
        end_string = f"{int(end_hour_whole)}:{end_minutes_string}"

        return f"{start_string}, {end_string}"
