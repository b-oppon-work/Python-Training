# 3. Write a program sign.py to ask the user for a number.
# Print out which category the number is in: 'positive', 'negative', or 'zero'.

def sign(number):
    if (number > 0):
        print("The number is Positive")
    elif (number == 0):
        print("The number is Zero")
    else:
        print("The number is Negative")
def main():
    user_input = int(input("Enter a number, please: "))
    sign(user_input)




main()
