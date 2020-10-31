user_name = "Alice"
def say_hello_world(name):
    print("Hello, World! and " + name)
say_hello_world(user_name)


def printAverage(a, b, c, d):
    total = a + b + c + d
    average = float("{0:.3f}".format(total/4))
    print(average)

printAverage(20.3, 5.87, 40.2, 2)



def getNumber():
    enteredNumber = float(input("Please enter a number: "))
    return enteredNumber

a = getNumber()
print(a)

def getAverage():
    num1 = getNumber()
    num2 = getNumber()
    num3 = getNumber()
    num4 = getNumber()
    printAverage(num1, num2, num3,num4)

getAverage()
