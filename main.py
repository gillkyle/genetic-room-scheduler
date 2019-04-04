import csv
from course import Course
from assignment import CourseAssignment
from room import Room
from room_resource import AvailabeRooms, RoomResource, DAYS
from solution import Solution


def main():
    with open('classes.csv', mode="r") as class_csv:
        # read in the courses
        class_reader = csv.DictReader(class_csv, delimiter=",")
        courses = []
        for row in class_reader:
            c = Course(row["Course"], row["Monday"], row["Tuesday"], row["Wednesday"], row["Thursday"], row["Friday"],
                       row["Sections"], row["Hours"], row["Preferred Time"], row["Preferred Room Type"], row["Students Per Section"])
            courses.append(c)

    print("Course list loaded")
    print(courses[0])

    with open('rooms.csv', mode="r") as room_csv:
        # read in the rooms
        room_reader = csv.DictReader(room_csv, delimiter=",")
        rooms = []
        for row in room_reader:
            r = Room(row["Room"], row["Capacity"], row["Type"])
            rooms.append(r)

    print("Room list loaded")
    print(rooms[0])

    print("Create 2880 room resources")
    available = AvailabeRooms()
    # loop through all the days
    for day in DAYS:
        # add availability for every room
        for room in rooms:
            # 8:00 (0), 8:30 (1), 9:00 (2), 9:30 (3),
            # 10:00 (4), 10:30 (5), 11:00 (6), 11:30 (7),
            # 12:00 (8), 12:30 (9), 1:00 (10), 1:30 (11),
            # 2:00 (12), 2:30 (13), 3:00 (14), 3:30 (15),
            # 4:00 (16), 4:30 (17)
            for i in range(0, 18):
                available.add(RoomResource(room, day, i))

    print(available.rooms["M"][-1])

    print("Add to Solution")
    solution = Solution(None)
    cas = []
    for course in courses:
        if course.m:
            for room_resource in available.pull_out_rooms("M", course.needed_time_slots()):
                cas.append(CourseAssignment(room_resource.room,
                                            course, room_resource.code.split("-")[2]))
        if course.t:
            for room_resource in available.pull_out_rooms("T", course.needed_time_slots()):
                cas.append(CourseAssignment(room_resource.room,
                                            course, room_resource.code.split("-")[2]))
        if course.w:
            for room_resource in available.pull_out_rooms("W", course.needed_time_slots()):
                cas.append(CourseAssignment(room_resource.room,
                                            course, room_resource.code.split("-")[2]))
        if course.th:
            for room_resource in available.pull_out_rooms("Th", course.needed_time_slots()):
                cas.append(CourseAssignment(room_resource.room,
                                            course, room_resource.code.split("-")[2]))
        if course.f:
            for room_resource in available.pull_out_rooms("F", course.needed_time_slots()):
                cas.append(CourseAssignment(room_resource.room,
                                            course, room_resource.code.split("-")[2]))
    print(len(cas))
    for ca in cas:
        print(ca.get_ind_fitness())


### Main runner ###
if __name__ == '__main__':
    main()
