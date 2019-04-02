import csv
from course import Course
from room import Room


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


### Main runner ###
if __name__ == '__main__':
    main()
