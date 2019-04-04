from random import randint


class CourseAssignment:
    '''
    A course assigned to a time slot in a room for a solution
    '''

    def __init__(self, room, course, time):
        self.room = room
        self.course = course
        self.time = time

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def get_ind_fitness(self):
        '''
        returns a fitness value in the range 0-100
        '''
        # TODO determine individual fitness
        return randint(0, 100)
