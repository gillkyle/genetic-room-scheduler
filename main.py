import csv
from course import Course
from assignment import CourseAssignment
from room import Room
from room_resource import AvailabeRooms, RoomResource, DAYS
from solution import Solution
from generation import Generation
from random import shuffle
from collections import namedtuple
from statistics import mean


TOTAL_STUDENTS = 6277

run_opt = namedtuple(
    'run_opt', ('num_solutions', 'pct_elite', 'pct_cross', 'pct_mut'))

RUN_OPTIONS = [
    run_opt(200, 0.05, 0.8, 0.05),
    run_opt(200, 0.05, 0.4, 0.20),
    run_opt(200, 0.15, 0.4, 0.10),
    run_opt(200, 0.25, 0.8, 0.10),
    run_opt(200, 0.75, 0.8, 0.05),
    run_opt(1000, 0.05, 0.8, 0.05),
    run_opt(1000, 0.05, 0.4, 0.2),
    run_opt(1000, 0.15, 0.4, 0.1)
]


def main():
    ##############################
    # DATA LOADING
    ##############################
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

    ##############################
    # SOLUTION GENERATION
    ##############################
    def generate_solution():
        # Create 2880 room resources
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

    ##############################
    # MODEL TESTING
    ##############################
    run_number = 0
    for options in RUN_OPTIONS:
        run_number += 1
        print(f"------------RUN {run_number}--------------")
        print(
            f"-- Population: {options.num_solutions} - Elite: {options.pct_elite}")
        print(
            f"-- Crossover: {options.pct_cross} - Mutation: {options.pct_mut}")
        print("-------------------------------")
        solutions = []
        # generate a list of solutions to provide to the generation
        for i in range(options.num_solutions):
            solutions.append(generate_solution())

        # create generation with solutions and percentages from run options
        base_gen = Generation(solutions, options)

        # order solutions in the generation based on fitness
        base_gen.sort_solutions_fitness()

        ##############################
        # GENERATION IMPROVEMENT
        ##############################
        gen_avg = []
        gen_number = 1
        moving_avg = 999
        # loop until moving average stabilizes below 1.0 for last 10 items
        print(
            f"Generation, Mean Fitness, Max Fitness, Min Fitness")
        while moving_avg > 1:
            # create a new generation
            # keep elites
            new_gen = Generation(base_gen.get_elites(), options)
            gen_avg.append(new_gen.avg_fitness())
            print(
                f"{gen_number}, {new_gen.avg_fitness()}, {new_gen.max_fitness()}, {new_gen.min_fitness()}")

            # use crossover percentage from the solution set to fill in the rest of the new generation
            new_gen.crossover_solutions(base_gen)

            # mutate the % in the new generation
            new_gen.mutate_solutions()

            # calculate moving average
            avgs = gen_avg[-10:]
            avg_diffs = []
            if len(avgs) >= 10:
                for i in range(len(avgs)-1):
                    avg_diffs.append(abs(avgs[i] - avgs[i + 1]))
                moving_avg = mean(avg_diffs)

            # reset the base_gen to create another generation on next loop
            base_gen = new_gen
            gen_number += 1

        ##############################
        # OUTPUT RESULTS
        ##############################
        new_gen.sort_solutions_fitness()
        best_solution = new_gen.solutions[0]
        print()
        print("Best solution:")
        print("Course, Days, Room, Start Time, End Time")
        for ca in best_solution.course_assignments:
            print(
                f"{ca.course.name}, {ca.day}, {ca.room.number}, {ca.convert_to_time_range()}")
        # print(gen_avg)


### Main runner ###
if __name__ == '__main__':
    main()
