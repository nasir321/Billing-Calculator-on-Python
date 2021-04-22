print("******************************************")
print("*** WELCOME TO CUSTOMER BILLING PORTAL ***")
print("******************************************\n")

a = int(input("Enter Total Numbers of Units : "))
print("Cost per unit is RS.15")
unit_cost = 15
discount = 0.9

b = a*unit_cost
c = b*discount

print("Your current bill is Rs.", b, "After 10% discount is Rs.", c)
print("Please Pay Rs.", c)
