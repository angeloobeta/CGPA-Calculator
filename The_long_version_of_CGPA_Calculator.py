semester = int(input("How many semesters have you done? "))
count_semester = 0
A = 5
B = 4
C = 3
D = 2
E = 1
F = 0
grade_score = 0
credit = 0
while count_semester < semester:
    courses = int(input("How many courses except GST did you do? "))
    credit_unit = int(input("What is the total Units of the courses? "))
    count = 0
    while count < courses:
        new_courses = input("What is the name of the course? ")
        unit = int(input("What is the unit of this course: "))
        score = int(input("What did you score? "))
        if score >= 70 and score <= 100:
            score = A
            print("You had A in {}.".format(new_courses))
        elif (score < 70) and (score >= 60):
            score = B
            print("You had B in {}.".format(new_courses))
        elif score >= 50 and score < 60:
            score = C
            print("You had C in {}.".format(new_courses))
        elif score >= 45 and score < 50:
            score = D
            print("You had D in {}.".format(new_courses))
        elif score < 45 and score >= 40:
            score = E
            print("You had E in {}.".format(new_courses))
        else:
            score = F
            print("You had F in {}.".format(new_courses))
        new_score = (score * unit) + grade_score 
        grade_score = new_score
        count += 1
    new_credit_unit = credit_unit + credit
    credit = new_credit_unit
    count_semester += 1
total_score = new_score
print("Your Total Score is {}".format(total_score))
total_credit_unit = new_credit_unit
print("The required credit unit is {}".format(total_credit_unit))
def CGPA(calc = total_score):
    results = total_score / total_credit_unit
    print(results)
CGPA()