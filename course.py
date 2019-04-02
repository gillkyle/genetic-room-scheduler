class Course:
    '''
    A class that holds a specific course
    '''

    def __init__(self, name, m, t, w, th, f, sections, hours, pref_time, pref_room_type, num_students):
        self.name = name
        self.m = m
        self.t = t
        self.w = w
        self.th = th
        self.f = f
        self.sections = sections
        self.hours = hours
        self.pref_time = pref_time
        self.pref_room_type = pref_room_type
        self.num_students = num_students

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
