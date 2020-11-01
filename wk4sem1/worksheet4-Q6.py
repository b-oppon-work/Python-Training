# 6.Write a function which takes in a student’s mark, and whether the work was submitted late from the user.
# The function will then output the grade depending on whether the work was submitted on time.
# If the work was submitted late, the student is capped at the pass mark of 40% (if the student hasn’t reached 40% and is late,
# they get the mark they received for the work).
# Otherwise, the following grade boundaries are used:
#
# Mark Range	Grade
# A*	        80+
# A	            70-79
# B	            60-69
# C	            50-59
# D	            40-49
# F  	        0-39

def students_grade(score, late):
    # user_input1 = int(input("score please "))
    # user_input2 = input("late or not ")
    if (late in ["yes", "Yes"]):
        if (score > 40):
            print("your grade is D")
        else:
            print("your Grade is F")
    else:
        if (score in [*range(80, 101, 1)]):
            print("your Grade is A*")
        elif (score in [*range(70, 80, 1)]):
            print("Your Garde is A")
        elif (score in [*range(60, 70, 1)]):
            print("Your Garde is B")
        elif (score in [*range(50, 60, 1)]):
            print("Your Garde is C")
        elif (score in [*range(40, 50, 1)]):
            print("Your Garde is D")
        else:
            print("Your Garde is F")
def main():
    user_input1 = int(input("score please "))
    user_input2 = input("late or not ")
    students_grade(user_input1, user_input2)

main()