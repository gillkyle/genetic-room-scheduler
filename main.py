import csv
from course import Course


def main():
    with open('classes.csv', mode="r") as csv_file:
        # read in the courses
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        courses = []
        for row in csv_reader:
            c = Course(row["Course"], row["Monday"], row["Tuesday"], row["Wednesday"], row["Thursday"], row["Friday"],
                       row["Sections"], row["Hours"], row["Preferred Time"], row["Preferred Room Type"], row["Students Per Section"])
            courses.append(c)

    print("Course list loaded")
    print(courses[0])


### Main runner ###
if __name__ == '__main__':
    main()
