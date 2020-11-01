# Take two int values from user and print greatest among them.

# we will collect the data from the user

def greatest_number(input1, input2):
    if (input1 > input2 ):
        print("this greatest number is " , input1 )
    else :
        print("this greatest number is ", input2 )

def main():
    user_input1 = int(input("Please enter first number: "))
    user_input2 = int(input("Please enter second number: "))
    greatest_number( user_input1 , user_input2 )

main()
