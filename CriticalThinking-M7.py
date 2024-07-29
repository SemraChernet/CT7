# The first thing I will do is defining a dictinaries based on the assignment specification
rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Here I will get the course number form the user
course_number = input("What is the course number (Note: course number is case sensetive): ")

# This will return the course detail 
if course_number in rooms and course_number in instructors and course_number in times:
    print(f"Course Number: {course_number}")
    print(f"Room Number: {rooms[course_number]}")
    print(f"Instructor: {instructors[course_number]}")
    print(f"Meeting Time: {times[course_number]}")
else:
    print("Sorry, invalid course number.")
