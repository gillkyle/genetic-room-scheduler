import csv
from course import Course
from assignment import CourseAssignment
from room import Room
from room_resource import AvailabeRooms, RoomResource, DAYS
from solution import Solution

TOTAL_STUDENTS = 6277


def main():
    with open('classes.csv', mode="r") as class_csv:
        # read in the courses
        class_reader = csv.DictReader(class_csv, delimiter=",")
        courses = []
        for row in class_reader:
            c = Course(row["Course"], [row["Monday"] == "x", row["Tuesday"] == "x", row["Wednesday"] == "x", row["Thursday"] == "x", row["Friday"] == "x"],
                       row["Sections"], row["Hours"], row["Preferred Time"], row["Preferred Room Type"], row["Students Per Section"])
            courses.append(c)

    print("Course list loaded")
    print(courses[0])
    sections = []
    for course in courses:
        for i in range(course.sections):
            sections.append(course)

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

    print(available.rooms["Th"][-1])

    print("Add to Solution")
    solution = Solution(None)
    cas = []
    outside_building = []

    # go through all sections
        # extract room resources 
        # if resources is empty
            # add course to outside_building
        # else
            # add course assignment to cas

    for course in sections:
        index = 0
        for schedule_on_this_day in course.days:
            if schedule_on_this_day:
                # get enough room resources required for the course
                room_resources = available.pull_out_rooms(DAYS[index], course)
                if len(room_resources) == 0:
                    outside_building.append(course)
                else:
                    cas.append(CourseAssignment(room_resources, course))
            index += 1

    print(cas[5].course.name)
    print("course", cas[5].course)
    print("room", cas[5].room)
    print(cas[5].get_capacity_value())
    print(cas[5].get_pref_time_value())
    print(cas[5].get_pref_type_value())
    print(cas[5])
    print(len(cas))
    print(outside_building)


### Main runner ###
if __name__ == '__main__':
    main()
