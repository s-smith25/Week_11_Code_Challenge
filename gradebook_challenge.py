# CIS 105 - Code Challenge: Grade Book
# Name: Syeed Smith
# Section: CIS 105-01
#
# Complete the five functions below where you see # TODO.
# Do not change the test code at the bottom of the file.
#
# The grade book is a dictionary:
#   keys   = student names (strings)
#   values = lists of test scores (numbers)
# Example: {"Alex": [90, 85, 95], "Jordan": [70, 80]}


def add_student(book, name):
    if name in book:
        print(f"{name} is already in the grade book.")
    else:
        book[name] = ([])
    """Add a new student with an empty score list.
    If the student is already in the book, print a message and change nothing."""
    # TODO
    pass


def add_grade(book, name, grade):
    if name not in book:
        add_student(book, name)
    book[name].append(grade)
    """Add a score to a student's list.
    If the student is not in the book yet, add the student first, then the score."""
    # TODO
    pass


def student_average(book, name):
    scores = book.get(name)
    if scores is None:
        return None
    return sum(scores) / len(scores)
    """Return the average of a student's scores.
    Use .get() so this returns None instead of crashing
    if the student is not in the book."""
    # TODO
    pass


def top_student(book):
    return max(book, key=lambda name: student_average(book, name))
    """Return the name of the student with the highest average score."""
    # TODO
    pass


def print_report(book):
    for name, scores in book.items():
        avg = student_average(book,name)
        print(f"{name}: {scores} Average: {avg:.1f}")
    """Print every student, their scores, and their average,
    one student per line. Loop over the dictionary with .items()."""
    # TODO
    pass


# ---------------- TEST CODE - DO NOT CHANGE BELOW THIS LINE ----------------

gradebook = {}

add_student(gradebook, "Alex")
add_student(gradebook, "Jordan")
add_student(gradebook, "Taylor")

add_grade(gradebook, "Alex", 90)
add_grade(gradebook, "Alex", 85)
add_grade(gradebook, "Alex", 95)

add_grade(gradebook, "Jordan", 70)
add_grade(gradebook, "Jordan", 80)

add_grade(gradebook, "Taylor", 100)
add_grade(gradebook, "Taylor", 95)
add_grade(gradebook, "Taylor", 90)
add_grade(gradebook, "Taylor", 85)

print_report(gradebook)
print("Top student:", top_student(gradebook))

# Expected output:
# Alex: [90, 85, 95] Average: 90.0
# Jordan: [70, 80] Average: 75.0
# Taylor: [100, 95, 90, 85] Average: 92.5
# Top student: Taylor
