import csv
from course import Course
from assignment import CourseAssignment
from room import Room
from room_resource import AvailabeRooms, RoomResource, DAYS
from solution import Solution
from generation import Generation
from random import shuffle
from collections import namedtuple


TOTAL_STUDENTS = 6277

run_opt = namedtuple(
    'run_opt', ('num_solutions', 'pct_elite', 'pct_cross', 'pct_mut'))

RUN_OPTIONS = [
    run_opt(200, 0.05, 0.8, 0.05)
]


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

    with open('rooms.csv', mode="r") as room_csv:
        # read in the rooms
        room_reader = csv.DictReader(room_csv, delimiter=",")
        rooms = []
        for row in room_reader:
            r = Room(row["Room"], row["Capacity"], row["Type"])
            rooms.append(r)
    print("Room list loaded")
    # print(rooms[0])

    def generate_solution():
        # print("Create 2880 room resources")
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

        # randomize course order and create each section
        # print("Randomize courses")
        shuffle(courses)
        sections = []
        for course in courses:
            for i in range(course.sections):
                sections.append(course)

        # print(available.rooms["Th"][-1])
        # print("Add to Solution")
        cas = []
        outside_building = []

        for course in sections:
            # get enough room resources required for the course
            room_resources = available.pull_out_resources(course)

            if len(room_resources) == 0:
                outside_building.append(course)
            else:
                cas.append(CourseAssignment(room_resources, course))
        return Solution(cas, outside_building, available)

    for options in RUN_OPTIONS:
        solutions = []
        # generate a list of solutions to provide to the generation
        for i in range(options.num_solutions):
            solutions.append(generate_solution())

        # create generation with solutions and percentages from run options
        base_gen = Generation(solutions, options)

        # debug print values
        print(base_gen.solutions[0].get_fitness())
        print(base_gen.fitness_list())
        print(base_gen.avg_fitness())
        print(base_gen.min_fitness())
        print(base_gen.max_fitness())

        # order solutions in the generation based on fitness
        base_gen.sort_solutions_fitness()
        print(base_gen.fitness_list())

        gen_avg = []
        # loop until moving average stabilizes below 1.0 for last 10 items
        while len(gen_avg) < 10:
            new_gen = Generation(base_gen.get_elites(), options)
            print(new_gen.fitness_list())
            gen_avg.append(new_gen.avg_fitness())
            base_gen = new_gen

        # create a new generation

        # keep elites

        # use crossover percentage from the solution set to fill in the rest of the new generation

        # mutate the % in the new generation


### Main runner ###
if __name__ == '__main__':
    main()
