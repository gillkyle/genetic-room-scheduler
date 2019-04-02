from random import randint


class Solution:
    '''
    The composition of 93 unique course assignments all scheduled
    '''

    def __init__(self, course_assignments):
        self.course_assignments = course_assignments

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def get_fitness():
        '''
        returns a fitness value in the range 0-100
        '''
        # TODO determine individual fitness
        return randint(0, 100)
