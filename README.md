# Assignment: TNRB Classrooms

As the room scheduler for the Tanner building, you have been asked to schedule rooms and times for next semester's business management courses.  Your constraints are as follows:

* Two courses cannot be scheduled in the same room at the same time.
* Each course should be scheduled for its room at the same times each day it meets.
* Match the room size as close as possible to the number of students in each course.
* Rooms can only be used from 8am-5pm each day.
* Courses can only start on the hour or half-hour.
* When calculating free time, add 0.25 hours to the time of each course for students to move.
* Schedule courses during their preferred times of the day whenever possible.
* If you cannot find times for all courses in the building, minimize the total number of students who must leave the building for classrooms.
* Minimize the overall number of rooms used.
* Maximize blocks of free time for each room.

Write a genetic algorithm to find the best available overall fitness value that meets the constraints above.  Accept a solution when the successive generations plateau at a stable overall fitness value.

## Data Files

The classes are in `classes.csv` and the available rooms are in `rooms.csv`.

Note that many classes have more than one section.  The number of students is reported *per section*.  For example, BUS M 260 has 2 sections with 50 students each.  Consider the two sections as, essentially, two "courses" that need assigning.

* There are 6,277 total students that are taking the courses in the list.
* There are 93 courses that need to be assigned (93 courses times the number of sections in each).

The preferred time and room type apply to all sections of a course.  For example, both sections of BM 260 prefer morning slots on MW.

## Coding

Create a "solution" object to represent an assignment of a section of a class.  This object should have the following methods:

```
getFitness(): Calculates the fitness function for the current time slot.
crossover(other): Crosses with another solution and returns a new solution.
mutate(): Mutates the solution in some way.
```

As you create/crossover/mutate your solution objects, ensure that the following rules are met:

* Courses are in rooms with enough seats (capacity).
* Courses have the same time on days of the week they are assigned.
* Courses are assigned on the days specified in the csv file.  They cannot be moved to other days.
* Collisions (two courses in the same room) are not possible.
* Courses are assigned within business hours (8-5).  An assignment of a 2 hour class to 4pm is not allowed.
* Courses start on the hour/half hour.
* Internally, add 15 minutes to the time of every course.  This automatically adds the window for students to move between courses. Technically, we don't need a window at the end of the day, but we won't worry about that.  Even the last course of the day needs the window added to its time.

In other words, don't let your program ever create a solution that violates any of the above.

A few suggestions:

* It may help to convert your room resources into half-hour codes.  Each code represents a half-hour in a room on a specific day. This provides a set of overall resources that you can pull in creating a single solution.  Start with a big list of all possible codes.  When you make an assignment, remove the used codes from the availability set.  This prevents courses from clashing, and it makes calculating free time blocks and free rooms easier at the end.  For example, the following encodes room - day - time slot:
  * 110-M-1 = Monday at 8:00 in room 110
  * 110-M-2 = Monday at 8:30 in room 110
  * 110-W-6 = Wednesday at 10:30 in room 110.
* Encapsulate as much logic into your objects as possible. This simplifies your main loop logic.  For example:
  * The solution object should likely have the method `getFitness()` to calculate and return the fitness value of the given solution.
  * An `AvailableSlots` object might encapsulate the availability set and have the method `getFreeSlot(length, num_days)` to get the next free slot.
  * A `CourseAssignment` object might have the method `getFitness()` to calculate the fitness of a specific course+room+time assignment.
* Convert the input data where it makes sense.  For example, convert the hours a course takes (such as 1.25 or 2.0) to the number of time slots it needs (3 for 1.25 hours or 5 for 2.0 hours; the 2.0 hours goes to 5 time slots because of the 15 minute window that must be added to it).



## Run and Output

Run your program at least five times with different parameters.  Change the number of solutions in each generation, percentages of elite, crossover, and mutations each time.  Elite items are carried forward to the next generation and are not subject to mutations.

The first few runs must be according to the following values:

1. 200 solutions, 5% Elite items, 80% crossover, 5% mutations.
1. 200 solutions, 5% Elite items, 40% crossover, 20% mutations.
1. 200 solutions, 15% Elite items, 40% crossover, 10% mutations.
1. 200 solutions, 25% Elite items, 80% crossover, 10% mutations.
1. 200 solutions, 75% Elite items, 80% crossover, 5% mutations.
1. 1000 solutions, 5% Elite items, 80% crossover, 5% mutations.
1. 1000 solutions, 5% Elite items, 40% crossover, 20% mutations.
1. 1000 solutions, 15% Elite items, 40% crossover, 10% mutations.

Once you finish the above required runs, add any additional runs you wish to try.  Try to use input values that get strong solutions within the fewest generations and smallest population numbers.

Stop a given run when the average fitness score across the solutions stabilizes.  More specifically, calculate a moving average and stop when the average stabilizes.  If the average population fitness scores for last ten runs are `50, 52, 54, 53, 55, 56, 55, 56, 55, 55`, the improvements are `2, 2, -1, 2, 1, -1, 1, -1, 0`.  The moving average of the improvements is `0.56`.  Stop the above runs when the moving average of the previous ten runs is less than 1.0.

For each run, print the following to a text file called `run01.txt`, `run02.txt`, etc.:

```
Population: 200
Elite: 5%
Crossover: 80%
Mutations: 5%

Generation, SolutionFitValue, Mean IndvFitness, Max IndvFitness, Min IndvFitness, Courses Scheduled, Courses Unscheduled
1, 50, 20, 80, 3, 93, 0
2, 55, 20, 82, 5, 93, 0
3, 59, 20, 84, 3, 93, 0
4, 66, 20, 82, 7, 93, 0
5, 67, 20, 86, 3, 90, 3
6, 51, 20, 87, 12, 93, 0
7, 54, 20, 89, 17, 93, 0
8, 65, 20, 95, 22, 93, 0

Best solution:
Course, Days, Section, Room, Start Time, End Time
BUS M 361, TTh, 1, 251, 9.0, 10.25
BUS M 361, TTh, 2, 251, 10:30, 11:45
BUS M 361, TTh, 3, 251, 12:00, 1:15
...

```

Do not include the 15 minute window at the end of course times in these output files.



## Crossovers

Crossovers should be done by combining the attributes (room assignments) of two solutions into a new solution.  When combining the assignments, try to do so in a way that improves its fitness value.

The specific algorithm you use to crossover two solutions is part of the final and should be created by you (without help).  One problem you need to figure out is how to combine the time slots of two solutions when course assignments clash on their time slot.  You'll have to make some changes to addresses this and other issues, but you'll be graded on how well you keep the attributes of *both* parent solutions in each child solution.



## Mutations

Mutations should be done by changing random assignments in a solution.  Mutations should generally be random, so try not to put too much logic here.  Mutations are done to the population *after* doing elitism and crossovers.

If the run specifies a 5% mutation rate and you have 1,000 solutions in your population, you should randomly change 50 solutions.  Mutating an individual solution could mean any of the following:

* Randomly change the assignment of one course within the solution.
* Randomly the assignment of five courses within the solution.
* Randomly swap the assignments of two courses within the solution.
* In any mutation, do not change more than five things about the solution.  Mutations should not be sweeping changes.

The specific algorithm you use to mutate a solution is part of the final and should be created by you (without help).


## Solution Fitness Function

**A "solution" is a finished schedule of courses with room assignments.**  For each generation, you'll create 1,000 solutions (or some number of solutions) and calculate the fitness value for each.  You'll crossover the top solutions to create the next generation of solutions.

One of the most important principles of data mining algorithms is summarization of each case into a single number. When cases turn into single numbers, it becomes much easier to evaluate, sort, analyze, and make decisions.

The official solution fitness function is as follows.  Each variable is in the range `0 - 100`, meaning that 100 is the maximum value.  Since we are weighting each variable, the final fitness value will also be in the range `0 - 100`.

```
SolutionFitValue = 0.6 * AvgIndvFitness  +  0.2 * FreeTimeBlocks  -  0.2 * StudentsOutsideTNRB  +  0.2 * UnusedRooms
```

### AvgIndFitness

AvgIndFitness is the average individual fitness value across all course assignments.  This average will be in the range `0 - 100` since each individual course fitness value is in this range.  Since there are 93 classes to assign, this would calculate as `AvgIndvFitness = sum(IndvFitness values) / 93`.

The `IndvFitness` value is the fitness of a specific course assigned to a time slot and room.  An example is BM 331 assigned to TNRB 408 from 1:00-2:15pm on Mondays and Wednesdays.  The `IndvFitness` number for this assignment will be some number in the range `0 - 100`.

The calculation is as follows:

```
IndvFitness = CapacityValue + PrefTime + PrefRoomType

CapacityValue is assigned:
    50 if capacity of room minus students in course is 0-5.
    40 if capacity of room minus students in course is 6-10.
    30 if capacity of room minus students in course is 11-15.
    20 if capacity of room minus students in course is 16-20.
    10 if capacity of room minus students in course is 21-25.
    0 if capacity of room minus students in course is 26+.
    The number of students can never be greater than the capacity of the room (that would be an invalid assignment).

PrefTime is assigned:
    25 if the time slot is within the preferred time of the course (morning or afternoon).
    15 if the time slot crosses over the noon hour (thus partially matching the preferred time).
    0 if the time slot is not within the preferred time of the course.

PrefRoomType is assigned:
    25 if the preferred type of the room is met.
    0 if the preferred type of the room is not met.
```



### FreeTimeBlocks

FreeTimeBlocks is a score of half hour blocks free across all rooms in the building, weighted to 100.

We have 32 rooms in the building.  Each room has 18 half-hour time blocks per day (8, 8:30, 9, 9:30, 10, 10:30, 11, 11:30, 12, 12:30, 1, 1:30, 2, 2:30, 3, 3:30, 4, 4:30).  Each room has 5 days.  Therefore, we have `32 * 18 * 5 = 2,880` half hour blocks that could be free each week (if we assigned no classes at all).

To calculate `FreeTimeBlocks`, iterate across the rooms and iterate the 5 days of the week for each room.  For example, suppose on Monday, TNRB 110 has free times: 9:00 - 11:00 (four half-hour blocks) and 2:00 - 5:00 (six half-hour blocks).  This gets a score of 6 because the 2:00 - 5:00 slot is the *longest* contiguous free time.  On Tuesday, TNRB has free times 8:00 - 12:00, 1:00 - 2:00, and 3:00 - 5:00.  This gets a score of 8 because 8:00 - 12:00 is the longest time for the room on that day (8 half-hour blocks).  Suppose the scores for TNRB 110 for the days of the week were, respectively: 6, 8, 4, 3, 18.  TNRB 110 gets a score of 39.

*Note that you can only record one time block per room per day.  Always record the longest block as the score for a room on a day.*

Continue to iterate the rooms and tally a sum of all scores for all rooms.  Suppose the total score across all 32 rooms is 998.  Calculate the percentage of blocks that were free and weight to the `0-100` range: `100 * 998 / 2880 = 35` (rounded to a whole number).  Put this score into the overall fitness function: `FreeTimeBlocks = 35`.


### StudentsOutsideTNRB

StudentsOutsideTNRB is the number of students that must meet somewhere else on campus, weighted to 100.  There are a total of 6,277 students in the course list for the semester.

Suppose BUS M 170 and BUS M 180 cannot be assigned in the building.  There are 640 students in these two courses.
`StudentsOutsideTNRB` is calculated as `100 * 640 / 6277 = 10` (rounded to whole number).  Put this score into the overall fitness function: `StudentsOutsideTNRB = 10`.


### UnusedRooms

UnusedRooms is the number of rooms that are not used at all during the week, weighted to 100.  There are 32 usable rooms in the building (the ones in `rooms.csv`).

Suppose a given solution uses 27 rooms, leaving 5 rooms free.  `UnusedRooms` is calculated as `100 * 5 / 32 = 16` (rounded to whole number).  Put this score into the overall fitness function: `UnusedRooms = 16`.




## Submitting the Assignment

Zip your code and output files and submit on Learning Suite.