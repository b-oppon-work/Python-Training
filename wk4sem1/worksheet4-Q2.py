# 2.Write a function that prompts students for how many credits they have.
# Print whether or not they have enough credits for graduation (At UoW 360 credits are needed for graduation).


def students_credit_checker(score):
    if (score >= 360 ):
        print("Congrats, you made it")
    else :
        print("Sorry you couldn't make the score to graduate ")

def main():
    student_input = float(input("Please enter credit: "))
    students_credit_checker(student_input)

main()
