from random import randint
from room_resource import DAYS
import more_itertools as mit


class Solution:
    '''
    The composition of up to 93 unique course assignments all scheduled
    '''

    def __init__(self, course_assignments, courses_outside_building, remaining_available):
        self.course_assignments = course_assignments
        self.courses_outside_building = courses_outside_building
        self.remaining_available = remaining_available

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def num_of_assignments(self):
        return len(self.course_assignments)

    def get_fitness(self):
        '''
        returns a fitness value in the range 0-100
        SolutionFitValue = 
            0.6 * AvgIndvFitness  +  
            0.2 * FreeTimeBlocks  -  
            0.2 * StudentsOutsideTNRB  +  
            0.2 * UnusedRooms
        '''
        total_ind_fitness = 0
        # TODO work out free time calculations
        students_outside_tnrb = 0
        used_rooms = set()
        for ca in self.course_assignments:
            total_ind_fitness += ca.get_ind_fitness()
            used_rooms.add(ca.room.number)

        for course in self.courses_outside_building:
            students_outside_tnrb += course.num_students

        free_days_score = []
        all_timeslots = []
        for day in DAYS:
            code = 0
            last_timeslot = 0
            timeslots = []
            curr_times = []
            for avail in self.remaining_available.rooms[day]:
                # build an array of all unused room codes
                if code > int(avail.code.split("-")[2]):
                    timeslots.append(curr_times)
                    curr_times = []
                code = int(avail.code.split("-")[2])
                curr_times.append(code)
            all_timeslots.append(timeslots)
        free_time_block_sum = 0
        for day_timeslot in all_timeslots:
            for course_timeslot in day_timeslot:
                # group blocks of numbers in each availability list eg [[1,2,3], [5,6]]
                contiguous_groups = [
                    list(group) for group in mit.consecutive_groups(course_timeslot)]
                len_contiguous_groups = list(
                    map(lambda x: len(x), contiguous_groups))
                free_time_block_sum += max(len_contiguous_groups)

        total_unused_room = abs(len(used_rooms) - 32)

        avg_fitness_score = total_ind_fitness / len(self.course_assignments)
        free_time_score = 100 * free_time_block_sum / 2880
        outside_bldg_score = round(100 * students_outside_tnrb / 6277)
        unused_room_score = 100 * total_unused_room / 32
        # print("---Avg fitness: ", avg_fitness_score)
        # print()
        # print("---Free time score: ", free_time_score)
        # print("from ", free_time_block_sum, " score for blocks of free time")
        # print()
        # print("---Outside building score: ", outside_bldg_score)
        # print("from ", students_outside_tnrb, " students outside the building")
        # print()
        # print("---Unused Room Score: ", unused_room_score)
        # print("from ", total_unused_room, " total unused rooms")
        # print()
        return round((avg_fitness_score * 0.6) + (free_time_score * 0.2) - (outside_bldg_score * 0.2) + (unused_room_score * 0.2))

    def crossover(other):
        '''
        crosses with another solution and returns a new and improved solution combines solutions A and B and returns a solution C that's better than either A or B
        '''
        # TODO
        return None

    def mutate():
        '''
        mutates the solution in a randomized way
        '''
        # TODO
        return None
