#The local delivery service has changed their pricing structure.
# Now, if your address is within 10 miles of the takeaway restaurant,
# and is over £20, you get free delivery.
# Otherwise, they add a delivery charge of 20% of the order total.
# Write a function which requires the user to enter a distance from the takeaway restaurant and the price of the order.
# This function will then output the total price of the order – including the delivery charge, if relevant.

def order_calculator(distance, amount):
    if (distance <= 10 and amount >= 20):
        print("Total price of your order is £: ", "{0:.2f}".format(amount))
    else :
        order_amount = (1.2 * amount)
        print("The total of your order is £:", "{0:.2f}".format(1.2 * amount), "Delivery Charged £:", "{0:.2f}".format(0.2 * amount))


def main():
    user_input1 = float(input("Please enter the distance to your house "))
    user_input2 = float(input("Please enter your order amount £: "))
    order_calculator( user_input1 , user_input2 )

main()