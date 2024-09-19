# a = 12
# print(a > 10)

# print("Welcome to the rollercoaster!")
# height = int(input("What's your height in CM? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print(f"Please pay ${bill}.")
#   if age <= 18:
#     bill = 7
#     print(f"Please pay ${bill}.")
#   else:
#     bill = 12
#     print(f"Please pay ${bill}.")

#   wants_photo = input("Do you want a photo taken? Y or N ")
#   if wants_photo == "Y":
#     bill += 3
#     print(f"Your final bill is {bill}")
#   else:
#     print(f"Your final bill is {bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# #* Coding Challenge
# number = int(input())

# if (number % 2 == 0):
#   print(f"{number} is an even number")
# else:
#   print(f"{number} is an odd number")

# year = int(input())

# if (year % 4 == 0):
#   print("Leap Year")
# else:
#   print("Year")

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size do you want? ") #* S, M, or L
# add_pepperoni = input("Do you want to add pepperoni? ") #* Y or N
# extra_cheese = input("Do you want extra cheese? ") #* Y or N

# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1
# else:
#   bill = bill

# print(f"Your final bill is {bill}.")


# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# if size == "S":
#   print(f"you are ordering Small Pizza and your price is ${small_pizza}")
# elif size == "M":
#   medium_pizza
# else:
#   large_pizza

#! Logical Operators

# a = 12
# b = 16
# logic = a < b and b > 10
# print(logic)

your_name = input("What's your name? ")
their_name = input("Your partner's name? ")

combined_names = your_name + their_name
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e
