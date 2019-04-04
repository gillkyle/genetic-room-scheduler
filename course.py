from math import ceil


class Course:
    '''
    A class that holds a specific course
    '''

    def __init__(self, name, m, t, w, th, f, sections, hours, pref_time, pref_room_type, num_students):
        self.name = name
        self.m = m == "x"
        self.t = t == "x"
        self.w = w == "x"
        self.th = th == "x"
        self.f = f == "x"
        self.sections = sections
        self.hours = hours
        self.minutes = float(hours) * 60
        self.pref_time = pref_time
        self.pref_room_type = pref_room_type
        self.num_students = int(num_students)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def needed_time_slots(self):
        # account for 15 min break in classes and use 30 min blocks
        return ceil((self.minutes + 15) / 30)
