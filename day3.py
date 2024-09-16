print("Welcome to the rollercoaster!")
height = int(input("What's your height in CM? "))

if height >= 120:
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
  print("You can ride the rollercoaster")
else:
  print("Sorry, you have to grow taller before you can ride.")

#* Coding Challenge
number = int(input())

if (number % 2 == 0):
  print(f"{number} is an even number")
else:
  print(f"{number} is an odd number")

year = int(input())

if (year % 4 == 0):
  print("Leap Year")
else:
  print("Year")

