#7.	A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Write a function which will ask the user for the number of units they require,
# and then prints the total cost of the order.

def discount(qty):
# Quantity = int(input("Enter Quantity "))

    Total_Cost = (100 * qty)
#Total_cost = 0

    if (Total_Cost > 1000):

        Total_cost = 0.9 * Total_Cost

        print(Total_cost)
    else:
        print(Total_Cost)

def main():
    Quantity = int(input("Enter Quantity "))
    discount(Quantity)

main()

