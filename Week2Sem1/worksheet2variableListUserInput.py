user_bill = float(input("please enter an amount in $ "))
tip_1 = user_bill * 10/100
tip_2 = user_bill * 15/100
tip_3 = user_bill * 20/100
#print(tip_1, tip_2, tip_3)

print("10, 15, and 20, percent tips as follows: ", [tip_1, tip_2, tip_3])

bill_1 = user_bill + tip_1
bill_2 = user_bill + tip_2
bill_3 = user_bill + tip_3
print("Total bills are in $ USD", [bill_1, bill_2, bill_3])





user_bill = int(input("please enter an amount in ?"))
tip_1 = user_bill * 10/100
tip_2 = user_bill * 15/100
tip_3 = user_bill * 20/100
print("percentages of tips:", [tip_1], [tip_2], [tip_3])

total_bill = [tip_1 + user_bill], [tip_2 + user_bill], [tip_3 + user_bill]
print("Bills in ?:", total_bill)


input_1 = input("Please enter your favourite food:" )
input_2 = input("Please enter your second favourite food:")
new_food = (input_1+ "-" +input_2)
print(new_food)
