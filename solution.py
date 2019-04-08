from random import randint


class Solution:
    '''
    The composition of 93 unique course assignments all scheduled
    '''

    def __init__(self, course_assignments, courses_outside_building):
        self.course_assignments = course_assignments
        self.courses_outside_building = courses_outside_building

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

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
        free_time_blocks = 0
        students_outside_tnrb = 0
        used_rooms = set()
        for ca in self.course_assignments:
            total_ind_fitness += ca.get_ind_fitness()
            used_rooms.add(ca.room.number)

        for course in self.courses_outside_building:
            students_outside_tnrb += course.num_students

        total_unused_room = abs(len(used_rooms) - 32)

        avg_fitness_score = total_ind_fitness / len(self.course_assignments)
        free_time_score = 100 * free_time_blocks / 2880
        outside_bldg_score = round(100 * students_outside_tnrb / 6277)
        unused_room_score = 100 * total_unused_room / 32
        print("---Avg fitness: ", avg_fitness_score)
        print()
        print("---Free time score: ", free_time_score)
        print("from ", free_time_blocks, " blocks of free time")
        print()
        print("---Outside building score: ", outside_bldg_score)
        print("from ", students_outside_tnrb, " students outside the building")
        print()
        print("---Unused Room Score: ", unused_room_score)
        print("from ", total_unused_room, " total unused rooms")
        print()
        return round((avg_fitness_score * 0.6) + (free_time_score * 0.2) - (outside_bldg_score * 0.2) + (unused_room_score * 0.2))

    def crossover(other):
        '''
        crosses with another solution and returns a new course assignemnt
        '''
        # TODO
        return None

    def mutate():
        '''
        mutates the solution in some way
        '''
        # TODO
        return None
